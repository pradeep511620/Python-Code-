import time
import csv
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
with open('urls-world-wide.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)
    print("url-length...", csv_length)

for url_Linkss in range(3, csv_length):
    url_links = csv_list[url_Linkss]
    url = url_links[0]
    print("Product-Length...", url_Linkss)
    print("Product-Urls......", url)
    driver.get(url)
    time.sleep(2)

    # Get First url without pagination
    try:
        for urls in driver.find_element(By.ID, "product-table").find_elements(By.TAG_NAME, "a"):
            link = urls.get_attribute('href')
            print(link)
            save_data = open("Product-Urls.txt", "a+", encoding="utf-8")
            save_data.write('\n' + link)
        print('save url in files without pagination')
    except NoSuchElementException:
        print('Unable to locate element:')

    try:
        # Get First url with pagination
        le = driver.find_element(By.XPATH, "//div[@id='product-table_info']")
        c = le.text.split(' ')[-2]
        print("count....", c)
        length = round(int(c) / 25 + 1)
        print('click...', length)
        for i in range(1, length + 1):
            try:
                driver.find_element(By.ID, "product-table_next").click()
                time.sleep(1)
            except ElementClickInterceptedException:
                print('element click intercepted:')
    except NoSuchElementException:
        print()

        try:
            for urls in driver.find_element(By.ID, "product-table").find_elements(By.TAG_NAME, "a"):
                link = urls.get_attribute('href')
                print(link)
                save_data = open("Product-Urls.txt", "a+", encoding="utf-8")
                save_data.write('\n' + link)
            print('save url in files')
        except NoSuchElementException:
            print('Unable to locate element:')
