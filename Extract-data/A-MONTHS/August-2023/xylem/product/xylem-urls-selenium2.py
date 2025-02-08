import csv
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

mylst = [
 'https://www.xylem.com/en-us/brands/mcdonnell--miller/products/?currentpageid=104695&categoryid=1127&page=1&isbrandproductsearch=true&pagesize=24'
 # 'https://www.xylem.com/en-us/brands/mcdonnell--miller/products/?currentpageid=104695&categoryid=1127&page=2&isbrandproductsearch=true&pagesize=24'
 # 'https://www.xylem.com/en-us/brands/mcdonnell--miller/products/?currentpageid=104695&categoryid=1127&page=3&isbrandproductsearch=true&pagesize=24'
]
for url in mylst:
    driver.get(url)
    time.sleep(4)
    le = driver.find_element(By.XPATH, "//div[@class='sp-bottom hidden-on-no-results']//div[@class='filters-summary']")
    c = le.text.replace(',', '').split()[-1]
    print("count....", c)
    length = round(int(c) / 24 + 1)
    print("loop.... ", length)
    for i in range(1, length+1):
        driver.find_element(By.XPATH, f"(//div[@class='item item__pager']//a)[{i}]").click()
        time.sleep(3)
        print(i)
        #
        for product_url in driver.find_elements(By.XPATH, "//div[@class='search-results hidden-on-no-results grid-view pure-g guttered hide-compare']//a"):
            prod_url = product_url.get_attribute('href')
            print(prod_url)


