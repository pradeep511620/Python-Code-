import time
from typing import TextIO
from bs4 import BeautifulSoup
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# url = 'https://www.championbuilt.com/modular-series.html'
# url = 'https://www.abilityone.com/first-aid-amp-health-supplies/category/200#'
url = 'https://www.3m.com/3M/en_US/p/c/abrasives/brushes/'

r = requests.get(url, headers=headers)
opts = Options()
opts.headless = True
soup = BeautifulSoup(r.content, 'html.parser')
opts.add_argument("--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
driver.get(url)
time.sleep(5)
urls = ""
tags = driver.find_elements(By.TAG_NAME, "a")
print("Total urls: ", len(tags))
for i in tags:
    urls = (i.get_attribute('href'))
    print(urls)

# save_details: TextIO = open("main ulrs.xlsx", "a+", encoding="utf-8")
# save_details.write("\n" + str(urls))
# print("End")
# save_details.close()
# print("\n ***** Record stored into Table Specifications . *****")
# print()
#