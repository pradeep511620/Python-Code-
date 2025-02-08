import time

import pandas as pd
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()
#

mylist = [
    'https://www.shoplinco.com/casters-by-brand/linco/?page=1',
    'https://www.shoplinco.com/casters-by-brand/linco/?page=2',
]

for url in mylist:
    browser.get(url)
    time.sleep(10)
    print("Product_urls", url)

    save = open('urlsafe.txt', 'a+', encoding='utf-8')
    for product in browser.find_elements(By.XPATH, "//div[@class='product-grid grid-l-3 grid-m-2']//a"):
        product_link = product.get_attribute('href')
        print(product_link)
    #     print("'" + product_link + "',")
        save.write(f"{product_link}\n")


# count = browser.find_element(By.XPATH, "//div[@class='col-md-4']").text.strip().split(' ')[-2]
# lengths_count = len(count)
# print('lengths', lengths_count)
# length_c = round(int(lengths_count) / 20 + 1)
# print('length', length_c)
#
# time.sleep(1)
# print('time')
# for i in range(1, 3 + 1):
#     browser.find_element(By.XPATH, "//a[@class='next js-search-link']").click()
#     time.sleep(5)
#     get_current_urls = browser.current_url
#     # print(get_current_urls)
#     print("Product_urls", url)
#     save = open('url.txt', 'a+', encoding='utf-8')
#     save .write(f"{get_current_urls}\n")
#     print(i)
#     Result = [
#         f"{url}/{'page'}/{i}"
#     ]
#     for pagination_link in Result:
#         print("'" + pagination_link + "',")

    # total_height =browser.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    # scroll_position = browser.execute_script("return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")
    # print("Total height of scrollable area:", total_height)
    # for i in range(scroll_position, total_height - 900, 900):
    #     browser.execute_script("window.scrollBy(0, 900)", "")
    #     time.sleep(3)
    #     print(i)

    # for product in browser.find_elements(By.XPATH, "//div[@class='products wrapper grid products-grid']//a"):
    #     product_link = product.get_attribute('href')
    #     if product_link is not None:
    #         print(product_link)
        #     save = open('url.txt', 'a+', encoding='utf-8')
        #     save.write(f"{product_link}\n")

