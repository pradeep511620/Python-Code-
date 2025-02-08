import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver.maximize_window()

l = [
    'https://www.panduit.com/en/products.html',
]
for url_list in l:
    r = requests.get(url_list, headers=headers)
    driver.get(url_list)

    # soup = BeautifulSoup(r.content, 'html.parser')
    # link = soup.find('div', {"class": "col col-products"}).find_all('a')
    # for links in link:
    #     print(links.get("href"))
    # link = soup.find_all('a')
    # for x in link:
    #     print(x.get('href'))

    links = driver.find_element(By.XPATH, "//div[@id='container-l1-l3']").find_elements(By.TAG_NAME, 'a')
    for x in links:
        url_links = (x.get_attribute('href'))
        print("''"+url_links+"',")
