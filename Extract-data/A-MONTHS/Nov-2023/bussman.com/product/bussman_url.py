# import time
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

# browser = webdriver.Chrome()
browser = uc.Chrome()
browser.maximize_window()
#

website_url = 'https://www.eaton.com/us/en-us/skuPage.170M4396.html'
browser.get(website_url)
time.sleep(6)
print("Product_urls", website_url)

url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Nov-2023/bussman.com/url/bussman_mpn.csv")['MPN']
print(len(url_link))
i = 3
for url_count, url in enumerate(url_link[i:5], start=i):
    # browser.get(url)
    # time.sleep(2)
    print("Product-Urls......", url_count, url)
    try:
        browser.find_element(By.XPATH, "//textarea[@id='site-search-box'][1]").send_keys(url)
        time.sleep(2)
        browser.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
        time.sleep(3)
        browser.find_element(By.XPATH, "//textarea[@id='site-search-box'][1]").clear()
        time.sleep(1)
    except Exception as e:
        print('click is running')
        print(e)


    # product_url = browser.find_element(By.XPATH, "//div[@id='snize-search-results-grid-mode']//ul//li[1]//a")
    # product_href = product_url.get_attribute('href')
    # print('product_href.....', product_href)
    # with open('product_url_weg.txt', 'a+', encoding='utf-8') as save:
    #     save.write('\n' + product_href)
    # print('save 1')
