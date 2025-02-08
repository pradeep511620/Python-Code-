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
    'https://www.watts.com/product-directory',
]
for url_list in l:
    r = requests.get(url_list, headers=headers)
    driver.get(url_list)

    links = driver.find_element(By.XPATH, "//div[@role='main']").find_elements(By.TAG_NAME, 'a')
    for x in links:
        url_links = (x.get_attribute('href'))
        ur = ("'"+url_links+"',")
        print(ur)

        save_details: url_links = open("watts_urls_main_links.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + ur)
        print("End")
        save_details.close()
        print("\n ***** Record stored into urls  files. *****")
