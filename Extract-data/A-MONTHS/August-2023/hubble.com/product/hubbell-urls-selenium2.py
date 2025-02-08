import csv
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)

with open("C:/Users/PK/Desktop/Web-Scrapping/August-2023/hubble.com/urls/hubbell-url.csv", 'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

for csv_link in range(680, csv_length):
    url = csv_list[csv_link][0]
    driver.get(url)
    time.sleep(1)
    print("Product-Length...", csv_link)
    print("Product-Urls......", url)
    try:
        try:
            driver.find_element(By.ID, "onetrust-close-btn-container").click()
        except NoSuchElementException:
            print(' Unable to locate element')


        for product in driver.find_elements(By.XPATH, "//div[@class='grid']//a"):
            url_links = product.get_attribute('href')
            if url_links is not None:
                print(url_links)
                save = open('product-url-hubbell.txt', 'a+', encoding='utf-8')
                save.write('\n' + url_links)

        try:
            le = driver.find_element(By.XPATH, "//div[contains(@class,'utilities-grid-left clearfix')]")
            c = le.text.replace(',', '').split()[0]
            print("count....", c)
            length = round(int(c) / 30+1)
            print("loop.... ", length)
            for i in range(1, length + 1):
                driver.find_element(By.XPATH, "//div[@class='utilities-pagination hidden-xs']//a[@class='icon icon-right-arrow']").click()
                time.sleep(2)
                print(i)

                length = driver.find_elements(By.XPATH, "//div[@class='grid']//a")
                print(len(length))
                for product in driver.find_elements(By.XPATH, "//div[@class='grid']//a"):
                    url_links = product.get_attribute('href')
                    if url_links is not None:
                        print(url_links)
                        save = open('product-url-hubbell.txt', 'a+', encoding='utf-8')
                        save.write('\n' + url_links)
                        # print('save data into files')
        except NoSuchElementException:
            print('unable to locate the elements')
    except Exception as e:
        print('nnn')





