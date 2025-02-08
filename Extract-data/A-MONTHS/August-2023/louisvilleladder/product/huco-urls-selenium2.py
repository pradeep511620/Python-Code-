import csv
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

url = 'https://louisvilleladder.com/ladders'

driver.get(url)
time.sleep(1)

for product_url in driver.find_elements(By.XPATH, "//div[@id='foundLadders']//a"):
    data = product_url.get_attribute('href')
    save = open('urls.txt', 'a+', encoding='utf-8')
    save.write('\n' + data)


