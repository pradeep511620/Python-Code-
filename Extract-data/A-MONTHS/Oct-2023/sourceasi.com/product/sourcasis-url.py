import time

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
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

"""
mylist = [
    'https://www.sourceasi.com/shop',

]

for url in mylist:
    browser.get(url)
    print("Product_urls", url)
    # time.sleep(2)
    count = browser.find_elements(By.XPATH, "//ul[@class=' pagination m-0 ']//li")
    length = len(count)

    for i in range(604, 658 + 1):
        browser.find_element(By.XPATH, "//a[normalize-space()='Next']").click()
        Result = [
            f"{url}/{'page'}/{i}"
        ]
        for pagination_link in Result:
            print("'" + pagination_link + "',")
"""



url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/sourceasi.com/url/bakergauges_product_url - Copy.csv")['URL']
url_length = 602
for url_count, url in enumerate(url_link[url_length:], start=url_length):
    browser.get(url)
    time.sleep(1)
    print("Product-Urls......", url)

    for product in browser.find_elements(By.XPATH, "//div[@id='products_grid']//tr//td//a"):
        product_link = product.get_attribute('href')
        print(product_link)
        save = open('url.txt', 'a+', encoding='utf-8')
        save.write(f"{product_link}\n")









