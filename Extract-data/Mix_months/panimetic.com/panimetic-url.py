from typing import TextIO

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome()
driver.maximize_window()
# time.sleep(5)

mylst = [
    'https://www.panimatic.com/',
]


def extract_url(url):
    driver.get(url)
    print("Products Urls", url)
    urls = driver.find_element(By.CLASS_NAME, "menu-haut").find_elements(By.TAG_NAME, "a")
    for j in urls:
        url_link = j.get_attribute('href')
        if '#' not in url_link:
            print(url_link)
            save_url: TextIO = open('url1.txt', 'a+', encoding='utf-8')
            save_url.write('\n' + "'"+url_link+"',")


for url in mylst:
    extract_url(url)
