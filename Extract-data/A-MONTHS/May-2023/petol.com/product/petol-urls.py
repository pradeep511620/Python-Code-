import time

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://petol.com/prodindex.aspx'


driver.get(url)
time.sleep(1)
length = driver.find_elements(By.XPATH, "//div[@id='Pcontent']//a")
print(len(length))
for ur in driver.find_elements(By.XPATH, "//div[@id='Pcontent']//a"):
    product_urls = ur.get_attribute('href')
    if product_urls is not None:
        print(product_urls)


