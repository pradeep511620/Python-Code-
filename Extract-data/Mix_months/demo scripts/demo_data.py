import time
from typing import TextIO

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

# url = 'https://www.championbuilt.com/store/p11/Drawer_Cabinet_NW600-0201ILC.html'
# url = "https://www.championbuilt.com/cht3056.html"
url = "https://taylorpneumatic.com/collections/new-tools/products/t-8867rn-hd-rivnut-tool"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())
opts = Options()
opts.headless = True
driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
time.sleep(3)
driver.get(url)
de = driver.find_element(By.ID, "overview-tab-1").text.strip()
# print(de)



"""
links = []
# =================================================== Find breadcrumb =================================================
bread_crumb = soup.find('ul', id='wsite-com-breadcrumbs').find_all("span")
list = []
# print(bread_crumb)
for bread in bread_crumb:
    bread_list = bread.text.strip()
    list.append(bread_list)
# print(list)

# ================================================ find title =========================================================
title = soup.find("h2", itemprop="name")
title_details = title.text.strip()
# print("title = ", title_details)

# =============================================== Find price ==========================================================
price = soup.find('span', class_='wsite-com-product-price-amount')
price_details = price.text.strip()
# print("price = ", price_details)

sku = soup.find('span', id="wsite-com-product-sku-value").find("sku")
sku_details = sku
# print(sku_details)

# ============================================ Description ============================================================
x = []
product = soup.find_all("div", id="wsite-com-product-short-description")
for para_details in product:
    x.append(para_details.text.strip().replace("\n", " ").replace('',''))
    # print("Description = ", x)


product = soup.find("div", id="wsite-com-product-short-description")
j = product.text.strip().replace("\n", "")
# print(j)

# =============================================== image all urls  =====================================================
all_img = []
images = soup.find("div", id="wsite-com-product-images").find_all("img")
for image_details in images:
    all_img = image_details['src']
    # print(all_img)
# print(len(all_img))
# print("Image urls = ", all_img)

# =============================================== image single urls  ==================================================
# image = soup.find('a', id="zoom1")
# image_details = image.get("href")
# # print(image_details)


# =============================================== Features ============================================================
feature = soup.find("div", id="wsite-com-product-tab").find("div", class_="paragraph").find_all("span")
a = ""
for feature_details in feature:
    a = a+feature_details.text.strip()
# print("feature = ", a)

# ================================================ Tables =============================================================
attr_name = soup.find_all('td', class_='cell')
attr_value = soup.find_all('td', class_='cell')
i = 0
while i < len(attr_name):
    j = 0
    while j < len(attr_value):
        x = attr_name[i].text
        # print(x)
        i = i + 1
        y = attr_value[j].text
        # print(y)
        j = j + 1

# ================================================ DRAWER COMPARTMENTS ================================================
try:
    draw_detail = ""
    draw = soup.find("tr", class_="wsite-multicol-tr").find_all("strong")
    draw1 = soup.find("tr", class_="wsite-multicol-tr").find_all("span")
    draw_details = []
    for drawer, dra in zip(draw, draw1):
        draw_details = drawer.text
        print(draw_details)
        draw_detail = dra.text
        print(draw_detail)

        images = soup.find_all("img", alt="Picture")
        for draw_image in images:
            draw_image1 = draw_image['src']
            print(draw_image1)
            save_details: TextIO = open("data.txt", "a+", encoding="utf-8")
            save_details.write("\n" + draw_details + "\t" + draw_detail + "\t" + draw_image1)
            print("End")
            save_details.close()
            print("\n ***** Record stored into Table Specifications . *****")
            print()
except:
    draw_image1 = "not found"
"""