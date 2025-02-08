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
# website_url = 'https://hosewarehouse.com/products/250-dc-al-dixon-2-1-2-356t6-aluminum-type-dc-dust-cap?variant=11766839476260'
# browser.get(website_url)
# time.sleep(3)
# print("Product_urls", website_url)

url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Nov-2023/dixon.com/url/dixon-mpn-url.csv")['URL']
print(len(url_link))
i = 7107
for url_count, url in enumerate(url_link[i:], start=i):
    browser.get(url)
    time.sleep(2)
    print("Product-Urls......", url_count, url)

    try:
        product_url = browser.find_element(By.XPATH, "//div[@id='snize-search-results-grid-mode']//ul//li[1]//a")
        product_href = product_url.get_attribute('href')
        print('product_href.....', product_href)
        with open('product_url_weg.txt', 'a+', encoding='utf-8') as save:
            save.write('\n' + product_href)
        print('save 1')
    except Exception as e:
        with open('product_url_weg.txt', 'a+', encoding='utf-8') as save:
            save.write('\n' + url)
        print('save 1')
        print(e)
