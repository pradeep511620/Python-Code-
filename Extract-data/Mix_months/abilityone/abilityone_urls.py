import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.support.select import Select

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver.maximize_window()
# time.sleep(8)
# first options to get urls
# for change in range(1000, 1047):
#     Result = [
#         f'https://www.abilityone.com/all-products/category/all-products/{change}',
#     ]
#     for url in Result:
#         try:
#             r = requests.get(url, headers=headers)
#             driver.get(url)
#             time.sleep(5)
#             print("Products Urls", url)
#             links = driver.find_element(By.XPATH, "//div[@class='col-lg-9 col-md-9 col-sm-12 col-xs-12']").find_elements(By.TAG_NAME, 'a')
#             print(len(links))
#             for x in links:
#                 url_links = (x.get_attribute('href'))
#                 data_urls = url_links
#                 print(data_urls)
#                 save_details: url_links = open("abilityone_full_urls.xlsx", "a+", encoding="utf-8")
#                 save_details.write("\n" + "'"+data_urls+"',")
#                 save_details.close()
#             print("\n ***** Record stored into urls  files. *****")
#         except:
#             print("Not Found")


#

# Seconds options to get urls
# Result = [
#     'https://www.abilityone.com/all-products/category/all-products/',
# ]
# for url in Result:
#     try:
#         l = l + 1
#         r = requests.get(url, headers=headers)
#         driver.get(url)
#         time.sleep(5)
#         print("Products Urls", l, url)
#         le = driver.find_element(By.XPATH, "//p[@class='results_filter-description-showing']")
#         c = le.text.replace(',', '').split()[-1]
#         print("count....", c)
#         length = round(int(c) / 12 + 1)
#         print("loop.... ", length)
#         for i in range(105, length):
#             driver.find_element(By.XPATH, "//span[@aria-label='Next']").click()
#             time.sleep(3)
#             print(i)
#             links = driver.find_element(By.XPATH, "//div[@class='col-lg-9 col-md-9 col-sm-12 col-xs-12']").find_elements(By.TAG_NAME, 'a')
#             for x in links:
#                 url_links = (x.get_attribute('href'))
#                 data_urls = url_links
#                 print(data_urls)
#             #     save_details: url_links = open("abilityone_full_urls.xlsx", "a+", encoding="utf-8")
#             #     save_details.write("\n" + "'"+data_urls+"',")
#             #     save_details.close()
#             # print("\n ***** Record stored into urls  files. *****")
#     except Exception as e:
#         print(e)


# for change in range(1, 1047):
#     Result = [
#         f'https://www.abilityone.com/all-products/category/all-products/{change}',
#     ]

#

# Simple urls
l = 0
myurls = [
    # 'https://www.abilityone.com/all-products/category/all-products/189',
    # 'https://www.abilityone.com/all-products/category/all-products/282',
    # 'https://www.abilityone.com/all-products/category/all-products/283',
    # 'https://www.abilityone.com/all-products/category/all-products/506',
    # 'https://www.abilityone.com/all-products/category/all-products/387',
    # 'https://www.abilityone.com/all-products/category/all-products/416',
    # 'https://www.abilityone.com/all-products/category/all-products/491',
    # 'https://www.abilityone.com/all-products/category/all-products/532',
    # 'https://www.abilityone.com/all-products/category/all-products/671',
    # 'https://www.abilityone.com/all-products/category/all-products/672',
    # 'https://www.abilityone.com/all-products/category/all-products/728',
    # 'https://www.abilityone.com/all-products/category/all-products/739',
    # 'https://www.abilityone.com/all-products/category/all-products/759',
    # 'https://www.abilityone.com/all-products/category/all-products/805',
    # 'https://www.abilityone.com/all-products/category/all-products/906',
    # 'https://www.abilityone.com/all-products/category/all-products/906',
    'https://www.abilityone.com/all-products/category/all-products/1001',
]
for url in myurls:
    driver.get(url)
    time.sleep(8)
    print("Products Urls", url)
    links = driver.find_element(By.XPATH, "//div[@class='col-lg-9 col-md-9 col-sm-12 col-xs-12']").find_elements(By.TAG_NAME, 'a')
    for x in links:
        url_links = (x.get_attribute('href'))
        data_urls = url_links
        print(data_urls)
        save_details: url_links = open("abilityone_full_urls1.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + "'"+data_urls+"',")
        save_details.close()
    print("\n ***** Record stored into urls  files. *****")