import pandas as pd
import requests
from bs4 import BeautifulSoup
import mysql.connector
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


def send_email(msg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = ["pradeep@raptorsupplies.co.uk", "raptorsupplyuk@gmail.com", ]
    # sender_email = ["nkmishra@nextgenesolutions.com", "nirbhay@raptorsupplies.com", "tajender@raptorsupplies.com"]
    smtp_username = "raptorsupplyuk@gmail.com"
    smtp_password = "unwkbryielvgwiuk"
    message = MIMEMultipart()
    message["From"] = smtp_username
    message["To"] = ','.join(sender_email)
    message["Subject"] = "Script Execution Status"

    body = msg
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, sender_email, message.as_string())
    print("Email sent successfully")


mgs = "Your web scraping script has been started"
send_email(mgs)
print(mgs)



def open_db_connection():
    """Opens a MySQL database connection and returns the connection and cursor."""
    try:
        connection = mysql.connector.connect(
            host='development-uk.c5tedj3txtxy.eu-west-1.rds.amazonaws.com',
            user='raptoradmin',
            password='Raptorpwa2020',
            database='trustpilot'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

            # Fetch the minimum date from the database
            cursor.execute('SELECT `Review Time` FROM trust_pilot_data_copy ORDER BY `Review Time` DESC LIMIT 1')
            last_review_time = cursor.fetchone()
            compare_last_time = ''
            if last_review_time:
                compare_last_time = last_review_time[0].strftime('%Y-%m-%d')
                print('compare_last_time ----- :', compare_last_time)
            return connection, cursor, compare_last_time
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None, None

def close_db_connection(connection, cursor):
    """Closes the database connection and cursor."""
    if connection and connection.is_connected():
        try:
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")
        except mysql.connector.Error as err:
            print(f"Error closing the MySQL connection: {err}")
    else:
        print("No open connection to close.")


def trustpilot_reviews(URL, connection, cursor, compare_last_time):
    ress = requests.get(URL, headers=headers)
    pk = BeautifulSoup(ress.content, 'lxml')

    """Fetches and extracts reviews data from the given Trustpilot URL."""
    try:
        re_name = [names.text.strip() for names in pk.select("article [data-consumer-name-typography]")]
        re_count = [names.text.strip() for names in pk.select("article [data-consumer-reviews-count-typography]")]
        re_country = [countrys.text.strip() for countrys in pk.select("article [data-consumer-country-typography]")]
        re_star = [stars.get('src').strip() for stars in pk.select("article [data-service-review-rating] img")]
        re_times = [times.text.strip().replace('Updated ', '') for times in pk.select("article time[data-service-review-date-time-ago]")]
        re_time = [datetime.strptime(date.replace('Sept', 'Sep') + f' 00:00:00', '%d %b %Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')for date in re_times]
        re_title = [titles.text.strip() for titles in pk.select("div.styles_reviewContent__0Q2Tg a[data-review-title-typography]")]
        re_des = [' '.join(desc.get_text(strip=True, separator='>>').split('>>')[1:-3]) for desc in pk.select("article section .styles_reviewContent__0Q2Tg")]
    except Exception as e:
        mgs_1 = f"Error extracting review data: {e}"
        send_email(mgs_1)
        print(mgs_1)
        return None

    """ Create a DataFrame with review data """
    df = pd.DataFrame({
        'Review Name': re_name,
        'Review Count': re_count,
        'Review Country': re_country,
        'Review Star Rating': re_star,
        'Review Time': re_time,
        'Review Title': re_title,
        'Review Text': re_des
    })

    """ Save the DataFrame to a CSV file, appending if the file already exists else Create a new csv files """
    # df.to_csv('review_data_stars.csv', mode='a+', index=False)
    # print("Data saved to csv file successfully.")


    """ Check if the review time matches the last review date """
    for review_time in re_time:
        review_date = review_time.split()[0]
        if review_date == compare_last_time:
            print(f"compare_last_time ----- {compare_last_time} -- review_date ----- {review_date}")
            print(f"Match found: {review_date}. Terminating program.")
            mgs_2 = "program terminating because of data already exist"
            send_email(mgs_2)
            print(mgs_2)
            sys.exit()

    else:
        print("No match found. Inserting new reviews into the database.")


    """ Convert DataFrame to list of tuples to save the into database """
    data_tuples = list(df.itertuples(index=False, name=None))

    """ Correct column names with backticks due to spaces """
    cursor.executemany('''
        INSERT INTO trust_pilot_data_copy (`Review Name`, `Review Count`, `Review Country`, `Review Star Rating`, `Review Time`, `Review Title`, `Review Text`)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', data_tuples)

    connection.commit()
    print("Data inserted into database successfully")

    mgs_3 = "Data inserted into database successfully"
    send_email(mgs_3)
    print(mgs_3)




""" Function to scrape reviews from single pages """
def single_page():
    connection, cursor, compare_last_time = open_db_connection()
    if connection and cursor:
        url = 'https://uk.trustpilot.com/review/raptorsupplies.com?sort=recency'
        # url = 'https://uk.trustpilot.com/review/raptorsupplies.com?languages=all&page=3'
        trustpilot_reviews(url, connection, cursor, compare_last_time)
        close_db_connection(connection, cursor)

    mgs_4 = "execution completed"
    send_email(mgs_4)
    print(mgs_4)


single_page()



""" Function to scrape reviews from multiple pages """
def main():
    connection, cursor, compare_last_time = open_db_connection()
    if connection and cursor:
        for i in range(1, 39 + 1):
            url = f'https://uk.trustpilot.com/review/raptorsupplies.com?languages=all&page={i}&sort=recency&stars=1&stars=2&stars=3&stars=4&stars=5'
            trustpilot_reviews(url, connection, cursor, compare_last_time)
        close_db_connection(connection, cursor)

    mgs_5 = "execution completed"
    send_email(mgs_5)
    print(mgs_5)

# if __name__ == "__main__":
#     main()
