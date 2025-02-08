# import time
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
browser = webdriver.Chrome()
browser.maximize_window()
#
website_url = 'https://www.regalrexnord.com/products/1082593'
browser.get(website_url)
time.sleep(2)
print("Product_urls", website_url)

url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Nov-2023/Browning.com/url/browning-mpn-url.csv")['mpn']
print(len(url_link))
i = 0
for url_count, url in enumerate(url_link[i:3], start=i):
    # browser.get(url)
    # time.sleep(2)
    print("Product-Urls......", url_count, url)

    browser.find_element(By.XPATH, "//input[@id='txtSearchGlobal']").send_keys(url)
    time.sleep(1)
    print('send_keys')

    browser.find_element(By.XPATH, "//button[@id='btnSearch']").click()
    time.sleep(30)
    print('click')

    browser.find_element(By.XPATH, "//input[@id='txtSearchGlobal']").clear()
    time.sleep(2)
    print('clear')

    # try:
    #     product_url = browser.find_element(By.XPATH, "//div[@id='snize-search-results-grid-mode']//ul//li[1]//a")
    #     product_href = product_url.get_attribute('href')
    #     print('product_href.....', product_href)
    #     with open('product_url_browning.txt', 'a+', encoding='utf-8') as save:
    #         save.write('\n' + product_href)
    #     print('save 1')
    # except Exception as e:
    #     with open('remaining-product_url_browning.txt', 'a+', encoding='utf-8') as save:
    #         save.write('\n' + url)
    #     print('save 1')
    #     print(e)
