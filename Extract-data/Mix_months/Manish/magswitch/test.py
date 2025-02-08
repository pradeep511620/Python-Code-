"""Logic testing for recursive function for getting nested urls using selenium"""

import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common import exceptions


base_url = 'https://magswitch.com/collections'
test_url = 'https://magswitch.com/collections/welding-fabrication'


def request_func(url):
    driver = Chrome()
    driver.get(url)
    time.sleep(5)
    # print(driver.current_url)
    try:
        item_container = driver.find_element(By.CLASS_NAME, 'page-width').find_elements(By.XPATH, '//*[@id="shopify-section-list-collections-template"]/div/ul/li/div/a')
        if len(item_container) < 1:
            raise exceptions.StaleElementReferenceException
        print(driver.current_url)
        for item_link in item_container:
            driver.get(item_link.get_attribute('href'))

    except exceptions.StaleElementReferenceException:
        try:
            print("i'm in exception")
            item_container = driver.find_element(By.CLASS_NAME, 'page-width').find_elements(By.XPATH, '//*[@id="Collection"]/ul[1]/li/div/a')
            for item_link in item_container:
                print(item_link.get_attribute('href'))

            button = driver.find_element(By.XPATH, '//*[@id="Collection"]/ul[2]/li[3]/a').get_attribute('href')
            if button:
                request_func(button)
        except exceptions.NoSuchElementException:
            time.sleep(5)
            driver.back()

    driver.back()
    time.sleep(5)


request_func(base_url)

