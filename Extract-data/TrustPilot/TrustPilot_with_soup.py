import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import mysql.connector

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


def trustpilot_reviews(URL):
    ress = requests.get(URL, headers=headers)
    pk = BeautifulSoup(ress.content, 'lxml')

    """Fetches and extracts reviews data from the given Trustpilot URL."""
    re_name = [names.text.strip() for names in pk.select("article [data-consumer-name-typography]")]
    re_count = [names.text.strip() for names in pk.select("article [data-consumer-reviews-count-typography]")]
    re_country = [countrys.text.strip() for countrys in pk.select("article [data-consumer-country-typography]")]
    re_star = [stars.get('src').strip() for stars in pk.select("article [data-service-review-rating] img")]
    re_times = [times.text.strip().replace('Updated ', '') for times in pk.select("article time[data-service-review-date-time-ago]")]
    current_time = datetime.now().strftime('%H:%M:%S')
    re_time = [datetime.strptime(date.replace('Sept', 'Sep') + f' {current_time}', '%d %b %Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')for date in re_times]
    re_title = [titles.text.strip() for titles in pk.select("div.styles_reviewContent__0Q2Tg a[data-review-title-typography]")]
    # re_des = [desc.get_text(strip=True, separator='>>').split('>>')[1:-3] for desc in pk.select("article section .styles_reviewContent__0Q2Tg")]
    re_des = [' '.join(desc.get_text(strip=True, separator='>>').split('>>')[1:-3]) for desc in pk.select("article section .styles_reviewContent__0Q2Tg")]

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

    # df.to_csv('review_data_stars1.csv', mode='a+', index=False)
    print("Data saved to csv file successfully.")


    connection = mysql.connector.connect(
        host='development-uk.c5tedj3txtxy.eu-west-1.rds.amazonaws.com',
        user='raptoradmin',
        password='Raptorpwa2020', database='trustpilot')


    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        # Convert DataFrame to list of tuples
        data_tuples = list(df.itertuples(index=False, name=None))

        # Correct column names with backticks due to spaces
        cursor.executemany('''
            INSERT INTO trust_pilot_data (`Review Name`, `Review Count`, `Review Country`, `Review Star Rating`, `Review Time`, `Review Title`, `Review Text`)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', data_tuples)

        # connection.commit()
        print("Data inserted into database successfully")

        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



# trustpilot_reviews('https://uk.trustpilot.com/review/raptorsupplies.com?languages=all&sort=recency&stars=1&stars=2&stars=3&stars=4&stars=5')



for i in range(1, 3 + 1):
    url = f'https://uk.trustpilot.com/review/raptorsupplies.com?languages=all&page={i}&sort=recency&stars=1&stars=2&stars=3&stars=4&stars=5'
    trustpilot_reviews(url)
