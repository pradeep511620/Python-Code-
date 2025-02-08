import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()


url_list = [

'https://metroled.com/product-category/indoor-lighting/',
'https://metroled.com/product-category/indoor-lighting/led-high-bay-lights/',
'https://metroled.com/product-category/indoor-lighting/led-panel-lights/',
'https://metroled.com/product-category/outdoor-lighting/',
'https://metroled.com/product-category/outdoor-lighting/led-canopy-fixture/',
'https://metroled.com/product-category/emergency-exit-signs/',
'https://metroled.com/product-category/indoor-lighting/linear-fixture/',
'https://metroled.com/product-category/highbay-fixtures/',
'https://metroled.com/product-category/outdoor-lighting/corn-bulbs/',
'https://metroled.com/product-category/indoor-lighting/linear-tubes/',
'https://metroled.com/product-category/panel-fixtures/',
'https://metroled.com/product-category/street-lights/',
'https://metroled.com/product-category/outdoor-lighting/led-wall-packs/',

]
for url in url_list:
    driver.get(url)
    time.sleep(2)
    print("Product - url : -----", url)
    # res = requests.get(url)
    # soup = BeautifulSoup(res.content, "html.parser")
    save = open('url.txt', "a+", encoding='utf-8')

    for product_url in driver.find_elements(By.XPATH, "//ul[@class='products columns-3']//a"):
        product_url_links = product_url.get_attribute('href')
        if "#" not in product_url_links and "category" not in product_url_links:
            print(product_url_links)
            save.write(f"{product_url_links}\n")

    s_num = driver.find_element(By.XPATH, "//p[@class='woocommerce-result-count']").text.strip().split(" ")[-2]
    length = round(int(s_num) / 12 + 1)
    print(length)
    for i in range(1, length + 1):
        try:
            driver.find_element(By.XPATH, "//a[@class='next page-numbers']").click()
            time.sleep(2)
        except NoSuchElementException:
            print("don't get next button")

        for product_url in driver.find_elements(By.XPATH, "//ul[@class='products columns-3']//a"):
            product_url_links = product_url.get_attribute('href')
            if "#" not in product_url_links and "category" not in product_url_links:
                print(product_url_links)
                save.write(f"{product_url_links}\n")

