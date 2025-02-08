import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver.maximize_window()

Result = [
    'https://www.se.com/in/en/all-products',


]
for url in Result:
    driver.get(url)
    time.sleep(10)

    links = driver.find_element(by=By.XPATH, value="//ul[@class='all-products-slider js-slider-main']")
    urls_link = links.find_elements(by=By.TAG_NAME, value="a")
    for urs in urls_link:
        u = urs.get_attribute('href')
        print(u)

