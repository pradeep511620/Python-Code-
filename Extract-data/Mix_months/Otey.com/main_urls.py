from select import select
import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

Result = [
    # 'https://www.oatey.com/products/oatey-liquilock-water-absorbing-crystals--1792398291',
    'https://www.oatey.com/all-products'

]
for url in Result:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(r"C:\Users\PK\Downloads\chromedriver_win32/chromedriver", options=opts)
    driver.get(url)
    time.sleep(3)
    print("Products Urls", url)
    urlss = driver.find_element(by=By.XPATH, value='//*[@id="block-views-block-all-products-block-1"]/div/div/div')
    u = urlss.find_elements(by=By.TAG_NAME, value='a')
    for i in u:
        print(i.get_attribute('href'))