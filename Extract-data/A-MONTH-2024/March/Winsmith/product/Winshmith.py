import time
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
ress = requests.session()

url_list = [


    'https://www.mrosupply.com/brands/winsmith/?per_page=120&sort_by=-popularity&page=142',
]
for url in url_list:
    driver.get(url)
    time.sleep(3)
    print(url)

    for product_href in driver.find_elements(By.XPATH, "//*[@class='m-catalogue-product--section']//a"):
        product_url = product_href.get_attribute('href')
        print(product_url)
        with open('urls.txt', 'a+', encoding='utf-8') as file_save:
            file_save.write(f"{product_url}\n")
