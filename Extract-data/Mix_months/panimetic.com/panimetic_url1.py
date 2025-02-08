from typing import TextIO

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome()
driver.maximize_window()
# time.sleep(5)

mylst = [
    'https://www.panimatic.com/water-chiller_677_83.html',
    'https://www.panimatic.com/intermediate-provers_677_71.html',
    'https://www.panimatic.com/moulders_677_69.html',
    'https://www.panimatic.com/proofers_677_65.html',
    'https://www.panimatic.com/retarder-proofers-for-filets_677_60.html',
    'https://www.panimatic.com/retarder-proofers-for-automatic-couches_677_56.html',
    'https://www.panimatic.com/retarder-proofers-for-400x600-trays_677_64.html',
    'https://www.panimatic.com/retarder-proofers-for-grids-and-couches_677_62.html',
    'https://www.panimatic.com/retarder-proofers-for-dough-trays_677_52.html',
    'https://www.panimatic.com/panel-boards_677_66.html',
    'https://www.panimatic.com/fridges_677_80.html',
    'https://www.panimatic.com/for-dough-trays_677_78.html',
    'https://www.panimatic.com/chocolate_677_79.html',
    'https://www.panimatic.com/freezers_677_50.html',
    'https://www.panimatic.com/blast-freezers_677_54.html',
    'https://www.panimatic.com/freezers-and-blast-freezers_677_58.html',
    'https://www.panimatic.com/automatic-couches_677_76.html',
    'https://www.panimatic.com/racks-trolleys-and-resting-cabinets_677_75.html',
    'https://www.panimatic.com/furniture_677_77.html',
    'https://www.panimatic.com/accessories_677_74.html',
    'https://www.panimatic.com/ventilated-ovens_677_24.html',
    'https://www.panimatic.com/deck-ovens_677_82.html',
    'https://www.panimatic.com/accessories_677_81.html',
]


def extract_url(url):
    driver.get(url)
    print("Products Urls", url)
    urls = driver.find_element(By.XPATH, "//div[@class='contenu']").find_elements(By.TAG_NAME, "a")
    print(len(urls))
    url_link = ''
    for j in urls:

        # print(type(url_link))
        if url_link != j.get_attribute('href'):
            url_link = j.get_attribute('href')
            print(url_link)
        # if '#' not in url_link:
        #     print(url_link)
        # save_url: TextIO = open('url2.txt', 'a+', encoding='utf-8')
        # save_url.write('\n' + "'"+url_link+"',")


for url in mylst:
    extract_url(url)
