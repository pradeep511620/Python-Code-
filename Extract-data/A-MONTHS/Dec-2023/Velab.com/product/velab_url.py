import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
#
# driver.maximize_window()


url_list = [
    'https://www.velab.net/collections/all?page=1',
    'https://www.velab.net/collections/all?page=2',
    'https://www.velab.net/collections/all?page=3',
    'https://www.velab.net/collections/all?page=4',
    'https://www.velab.net/collections/all?page=5',
    'https://www.velab.net/collections/all?page=6',
    'https://www.velab.net/collections/all?page=7',
]
for url in url_list:
    # driver.get(url)
    # time.sleep(2)
    # print("Product - url : -----", url)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")

    for relat in soup.find_all('figure', {"class": "product-card_image"}):
        related_href = relat.find_all('a')
        for url_related in related_href:
            href_tag = url_related.get('href')
            print("https://www.velab.net"+href_tag)
