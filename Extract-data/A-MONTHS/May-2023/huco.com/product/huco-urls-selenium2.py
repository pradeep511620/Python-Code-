import csv
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(8)

with open('product-url-huco.csv', 'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

for csv_link in range(1, csv_length):
    url = csv_list[csv_link][0]
    driver.get(url)
    time.sleep(3)
    print("Product-Length...", csv_link)
    print("Product-Urls......", url)

    try:
        driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
    except NoSuchElementException:
        print(' Unable to locate element')

    time.sleep(4)
    for product in driver.find_elements(By.XPATH, "//div[@class='product-list']//li//a"):
        url_links = product.get_attribute('href')
        print(url_links)
        save = open('product-url-huco-main.txt', 'a+', encoding='utf-8')
        save.write('\n' + url_links)
    print('save data into files')


