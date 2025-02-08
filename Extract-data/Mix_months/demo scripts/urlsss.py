import time
from typing import TextIO

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

myresults = [
    'https://www.jbind.com/product-category/access-valves/copper-tube-extension-single-step/',

]

for fetch in myresults:
    try:
        url = fetch
        print("Product_urls", url)
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        opts = Options()
        opts.headless = True
        opts.add_argument(
            "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
        driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
        driver.get(url)
        time.sleep(3)
        tag = driver.find_element(By.XPATH, '//*[@id="Accessories__Parts"]/div/div/div').find_elements(By.TAG_NAME, 'a')
        for i in tag:
            i.send_keys(Keys.PAGE_DOWN)
            # time.sleep(3)
            urls = i.get_attribute('href')
            print(urls)
            # save_details: TextIO = open("sub urls.xlsx", "a+", encoding="utf-8")
            # save_details.write("\n" + i)
            # print("End")
            # save_details.close()
            # print("\n ***** Record stored into Table Specifications . *****")
        print(" next urls ------")
    except:
        print("Not Found Urls")

    # ================================== sub urls find ===============================================
    # tag = driver.find_elements(By.TAG_NAME, "a")
    # product_links = ""
    # for product_link in tag:
    #     product_links = product_link.get_attribute("href")
    #     dict = ({'urls': [product_links]})
    #     print(dict)
    # save_details: TextIO = open("sub urls.xlsx", "a+", encoding="utf-8")
    # save_details.write("\n" + product_links)
    # print("End")
    # save_details.close()
    # print("\n ***** Record stored into Table Specifications . *****")
    # print()
    # print("------")
