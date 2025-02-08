import undetected_chromedriver as uc
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import os
import csv

df = pd.read_csv('D:/Web-Scrapping/A-MONTH-2024/May/Lovejoy/url/Product-url.csv')
urls = df['URL']
with uc.Chrome() as driver:
    for i, url in enumerate(urls[0:1]):
        print(url)
        driver.get(url)
        if i == 0:
            time.sleep(6)
        else:
            time.sleep(2)
        res = driver.page_source
        soup = bs(res, 'lxml')
