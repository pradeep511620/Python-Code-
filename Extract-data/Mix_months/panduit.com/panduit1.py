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

Result = [
    'https://www.panduit.com/en/products/fiber-optic-systems/industrial-fiber-optic-systems/outdoor-fiber-closures-and-accessories.html'
    # 'https://www.panduit.com/en/products/audio-video-systems/above-floor-raceway-and-fittings/above-floor-raceway-fittings.html',
    # 'https://www.panduit.com/en/products/wire-termination/terminals-terminal-kits/fork-terminals.html',

    ]
for url in Result:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    driver.get(url)
    time.sleep(8)
    # print("Products Urls", url)

    links = driver.find_element(By.XPATH, "//div[@id='coveo-full-results']").find_elements(By.TAG_NAME, 'a')
    for x in links:
        url_links = (x.get_attribute('href'))
        print("''" + url_links + "',")

# ================================= sub url print for BeautifulSoup ==================================================
#     links = soup.find_all('a', class_="js-range-thumb-link")
#     for x in links:
#         product_link = x.get('href')
#         print("''"+product_link+"',")



