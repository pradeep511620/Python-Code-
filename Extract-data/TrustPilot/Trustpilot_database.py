import time
import mysql.connector
from datetime import datetime
from itertools import zip_longest
from selenium import webdriver
from selenium.webdriver.common.by import By

# login_url = "https://businessapp.b2b.trustpilot.com/reviews?date=2024-07-01,2024-07-23"
login_url = "https://businessapp.b2b.trustpilot.com/reviews"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(login_url)
time.sleep(5)

conn = ''
try:
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )
    cursor = conn.cursor()
    print("connection create successfully")

    # Fetch the minimum date from the database
    cursor.execute('SELECT Last_time FROM trust_pilot_data1')
    last_saved_time = cursor.fetchone()[0]
    print("Last saved time:", last_saved_time)
except mysql.connector.Error as err:
    print(f"Database error: {err}")
    last_saved_time = None
finally:
    if conn:
        conn.close()



def login_details():
    username = 'raptorsupplies@gmail.com'
    password = 'Raptor2014@#'
    driver.find_element(By.CSS_SELECTOR, "input#email").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "input#password[name='password']").send_keys(password)
    time.sleep(1)
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='login']")
    submit_button.click()
    time.sleep(20)


# Function to scroll the page and reload the script
def scroll_and_reload():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


# Function to get all detail  the page
def get_all_details():
    scroll_and_reload()

    # Find elements using CSS selectors
    Review_Title_elements = driver.find_elements(By.CSS_SELECTOR, "a.review__title")
    Review_text_elements = driver.find_elements(By.CSS_SELECTOR, "div.review__text p")
    Review_name_elements = driver.find_elements(By.CSS_SELECTOR, 'div.review__consumer div.review__consumer__name')
    Review_source_elements = driver.find_elements(By.CSS_SELECTOR, "div.review__details div[title='Organic']")
    cus_review_elements = driver.find_elements(By.CLASS_NAME, 'review__consumer__reviews')
    Review_stars_elements = [sr.get_attribute('src') for sr in driver.find_elements(By.CSS_SELECTOR, 'div.review__stars img')]
    Last_time_elements = driver.find_elements(By.CSS_SELECTOR, "div.review__stars p span")

    values_list = []

    # Using zip_longest to ensure all lists are the same length
    for title, texts, name, source, star, cus_review, times in zip_longest(
            Review_Title_elements, Review_text_elements, Review_name_elements, Review_source_elements,
            Review_stars_elements, cus_review_elements, Last_time_elements, fillvalue=None):

        # Extract text or set as empty string if element is None
        Review_Title = title.text if title else ''
        Review_text = texts.text if texts else ''
        Review_name = name.text if name else ''
        Review_source = source.text if source else ''
        Review_stars = star if star else ''
        Last_time = times.text if times else ''
        cus_review = cus_review.text if cus_review else ''

        # Print extracted data for debugging
        # print(f"Extracted data - Title: {Review_Title}, Text: {Review_text}, Name: {Review_name}, Source: {Review_source}, Stars: {Review_stars}, Reviews: {cus_review}, Time: {Last_time}")

        # # Break the loop if the last saved time matches the current scraped time
        if Last_time == last_saved_time:
            print("Match found. Breaking the loop.")
            break
        print('break')

        # Create a list of the extracted values
        lis = [Review_Title, Review_text, Review_name, Review_source, Review_stars, cus_review, Last_time]
        values_list.append(lis)

    # If there are new values, insert them into the database
    if values_list:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test"
            )
            cursor = conn.cursor()
            cursor.executemany('''
            INSERT INTO trust_pilot_data1 (Review_Title, Review_text, Review_name, Review_source, Review_stars, cus_review, Last_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', values_list)
            conn.commit()
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()

    time.sleep(5)


def main():

    login_details()
    get_all_details()
    driver.quit()


if __name__ == "__main__":
    main()
