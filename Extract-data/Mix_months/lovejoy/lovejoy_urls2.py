import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from typing.io import TextIO
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
# driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver = uc.Chrome()

driver.maximize_window()

L = 0
for inc in range(1, 6169+1):
    Result = [
        f'https://www.applied.com/brands/timken-company/lovejoy/c/Brand-985?q=:&override=true&isLevelUp=false&usePlp=&page={inc}',
    ]
    for url in Result:
        L = L + 1
        r = requests.get(url, headers=headers)
        # print(soup.prettify())?page=
        driver.get(url)
        print("Products Urls", L, url)
        save_details: TextIO = open("lovejoy.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + "'"+url+"',")
        save_details.close()
        print("\n ***** Record stored into watts  files. *****")
