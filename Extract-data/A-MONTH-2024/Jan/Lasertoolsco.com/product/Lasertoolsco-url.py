import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()


url_list = [
    "https://lasertoolsco.com/product-category/function/",
    "https://lasertoolsco.com/product-category/construction-laser-products/",
    "https://lasertoolsco.com/product-category/laser-products/",
    "https://lasertoolsco.com/product-category/mining-laser-products/",
    "https://lasertoolsco.com/product-category/accessories/",
    "https://lasertoolsco.com/product-category/custom-solutions/",
    "https://lasertoolsco.com/product-category/industrial-laser-products/",
    "https://lasertoolsco.com/product-category/marineunderwater-laser-products/",
]
for url in url_list:
    driver.get(url)
    time.sleep(4)
    print("Product - url : -----", url)
    save = open('url.txt', "a+", encoding='utf-8')



    for product_cate in driver.find_elements(By.XPATH, "//ul[@class='products columns-4 list']//a"):
        product_tag = product_cate.get_attribute("href")
        if "#" not in product_tag and "=" not in product_tag:
            print(product_tag)
            save.write(f"{product_tag}\n")


