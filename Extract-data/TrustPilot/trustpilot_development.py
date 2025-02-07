import time
import mysql.connector
from mysql.connector import Error
from itertools import zip_longest
# import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


last_saved_time = ''
try:
    connection = mysql.connector.connect(
        host='dcom',
        user='',
        password='', database='trustpilot')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        cursor.execute('SELECT Review_last_time FROM trust_pilot_data')
        last_saved_time = cursor.fetchone()[0]
        print("Last saved time:", last_saved_time)
except (TypeError, Error) as e:
    print(f"Found..{last_saved_time}")
    print(f"Error while connecting to MySQL {e}")

def Extract_all_reviews(driver, url):


    # Find elements using CSS selectors
    Review_name_elements = driver.find_elements(By.CSS_SELECTOR, "span[data-consumer-name-typography]")
    Review_Title_elements = driver.find_elements(By.CSS_SELECTOR, "h2[data-service-review-title-typography]")
    Review_text_elements = driver.find_elements(By.CSS_SELECTOR, "p[data-service-review-text-typography]")
    Review_stars_elements = [sr.get_attribute('src') for sr in driver.find_elements(By.CSS_SELECTOR, "div[data-service-review-rating] img")]
    cus_review_elements = driver.find_elements(By.CSS_SELECTOR, 'span[data-consumer-reviews-count-typography]')
    Country_elements = driver.find_elements(By.CSS_SELECTOR, "div[data-consumer-country-typography] span")
    Last_time_elements = driver.find_elements(By.CSS_SELECTOR, "time[data-service-review-date-time-ago]")

    values_list = []

    # Using zip_longest to ensure all lists are the same length
    for name, title, texts, star, cus_review, country, times in zip_longest(
            Review_name_elements, Review_Title_elements, Review_text_elements,
            Review_stars_elements, cus_review_elements, Country_elements, Last_time_elements, fillvalue=None):

        # Extract text or set as empty string if element is None
        Review_name = name.text if name else ''
        Review_Title = title.text if title else ''
        Review_text = texts.text.replace("\n", ">>") if texts else ''
        Review_stars = star if star else ''
        Review_cus = cus_review.text.replace(" review", "").replace("s", "") if cus_review else ''
        Review_country = country.text if country else ''
        Review_last_time = times.text if times else ''

        # Print extracted data for debugging
        # print(f"Extracted data - Name: {Review_name}, Title: {Review_Title}, Text: {Review_text}, Stars: {Review_stars}, Reviews: {Review_cus}, Country: {Review_country},Time: {Review_last_time}")

        # # Break the loop if the last saved time matches the current scraped time
        if Review_last_time == last_saved_time:
            print(f"first date is {Review_last_time} second - date is {last_saved_time}")
            print("Match found. Breaking the loop.")
            break

        # Create a list of the extracted values
        lis = [Review_name, Review_Title, Review_text, Review_stars, Review_cus, Review_country,
               Review_last_time]
        values_list.append(lis)

    print(values_list)

    # If there are new values, insert them into the database
    if values_list:

        try:
            connection = mysql.connector.connect(
                host='develws.com',
                user='',
                password='', database='trustpilot')
            cursor = connection.cursor()

            cursor.executemany('''
            INSERT INTO trust_pilot_data (Review_name, Review_title, Review_text, Review_stars, Review_cus, Review_country, Review_last_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', values_list)
            connection.commit()
            print("Data Inserted into database")
        except mysql.connector.Error as ee:
            print(f"Database error: {ee}")
        finally:
            connection.close()
            print("MySQL connection is closed")
    else:
        print('Empty list data')



def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        for i in range(39, 40):
            # url = 'https://www.trustpilot.com/review/raptorsupplies.com?languages=all&sort=recency'
            url = f'https://www.trustpilot.com/review/raptorsupplies.com?languages=all&page={i}&sort=recency'
            driver.get(url)
            time.sleep(6)
            Extract_all_reviews(driver, url)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
