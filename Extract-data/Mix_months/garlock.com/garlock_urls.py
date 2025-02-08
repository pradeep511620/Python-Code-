import time
from typing import TextIO

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

mylst = [
    'https://garlockequipment.com/powered-deck-equipment.html?product_list_limit=24',
    'https://garlockequipment.com/on-deck-equipment.html?product_list_limit=36',
    'https://garlockequipment.com/water-proofing.html',
    'https://garlockequipment.com/cold-processing.html',
    'https://garlockequipment.com/roof-top-safety.html?product_list_limit=36',
    'https://garlockequipment.com/roof-top-safety.html?p=2&product_list_limit=36',


]
for url in mylst:
    driver.get(url)
    time.sleep(3)
    link = driver.find_element(By.XPATH, "//ol[@class='products list items product-items']")
    u_links = link.find_elements(By.TAG_NAME, "a")
    for links in u_links:
        url_link = links.get_attribute('href')
        if '#' not in url_link:
            print(url_link)
            save_u: TextIO = open('url.txt', 'a+', encoding='utf-8')
            save_u.write('\n' + "'" + url_link + "',")
print('urls save into files')
