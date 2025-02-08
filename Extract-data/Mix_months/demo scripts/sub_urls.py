import time
from typing import TextIO

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
mlist = [
    'https://www.abilityone.com/all-products/category/all-products',
    'https://www.abilityone.com/quick-order',
    'https://www.abilityone.com/absorbents/category/1029',
    'https://www.abilityone.com/cleaners-amp-detergents/category/301',
    'https://www.abilityone.com/buckets-wringers/category/302',
    'https://www.abilityone.com/restroom-cleaners-amp-accessories/category/303',
    'https://www.abilityone.com/waste-receptacles-amp-accessories/category/304',
    'https://www.abilityone.com/air-cleaner-machines/category/305',
    'https://www.abilityone.com/air-fresheners-amp-dispensers/category/306',
    'https://www.abilityone.com/caddy-bags/category/307',
    'https://www.abilityone.com/cleaning-brushes/category/308',
    'https://www.abilityone.com/fans/category/309',
    'https://www.abilityone.com/cleaning-supplies/category/3',
    'https://www.abilityone.com/inks-toners/category/4',
    'https://www.abilityone.com/first-aid-amp-health-supplies/category/200',
    'https://www.abilityone.com/personal-care/category/201',
    'https://www.abilityone.com/ambulance-kits/category/202',
    'https://www.abilityone.com/gloves/category/205',
    'https://www.abilityone.com/medical-supplies/category/2',
    'https://www.abilityone.com/batteries-amp-electrical-supplies/category/101',
    'https://www.abilityone.com/binders-amp-binding-supplies/category/102',
    'https://www.abilityone.com/calendars-planners-amp-organizers/category/103',
    'https://www.abilityone.com/bags-carrying-cases-amp-briefcases/category/104',
    'https://www.abilityone.com/money-handling/category/105',
    'https://www.abilityone.com/classroom-learning-materials/category/106',
    'https://www.abilityone.com/crafts-amp-recreation-room/category/107',
    'https://www.abilityone.com/desk-amp-workspace-organizers/category/109',
    'https://www.abilityone.com/file-folders-amp-storage-box-files/category/110',
    'https://www.abilityone.com/forms-recordkeeping-amp-ref-materials/category/113',
    'https://www.abilityone.com/office-supplies/category/1',
    'https://www.abilityone.com/all-products/category/all-products',
    'https://www.abilityone.com/cleaning-supplies/category/3',
    'https://www.abilityone.com/absorbents/category/1029',
    'https://www.abilityone.com/cleaners-amp-detergents/category/301',
    'https://www.abilityone.com/buckets-wringers/category/302',
    'https://www.abilityone.com/restroom-cleaners-amp-accessories/category/303',
    'https://www.abilityone.com/waste-receptacles-amp-accessories/category/304',
    'https://www.abilityone.com/air-cleaner-machines/category/305',
    'https://www.abilityone.com/air-fresheners-amp-dispensers/category/306',
    'https://www.abilityone.com/caddy-bags/category/307',
    'https://www.abilityone.com/cleaning-brushes/category/308',
    'https://www.abilityone.com/fans/category/309',
    'https://www.abilityone.com/cleaning-supplies/category/3',
    'https://www.abilityone.com/inks-toners/category/4',
    'https://www.abilityone.com/medical-supplies/category/2',
    'https://www.abilityone.com/first-aid-amp-health-supplies/category/200',
    'https://www.abilityone.com/personal-care/category/201',
    'https://www.abilityone.com/ambulance-kits/category/202',
    'https://www.abilityone.com/gloves/category/205',
    'https://www.abilityone.com/medical-supplies/category/2',
    'https://www.abilityone.com/office-supplies/category/1',
    'https://www.abilityone.com/batteries-amp-electrical-supplies/category/101',
    'https://www.abilityone.com/binders-amp-binding-supplies/category/102',
    'https://www.abilityone.com/calendars-planners-amp-organizers/category/103',
    'https://www.abilityone.com/bags-carrying-cases-amp-briefcases/category/104',
    'https://www.abilityone.com/money-handling/category/105',
    'https://www.abilityone.com/classroom-learning-materials/category/106',
    'https://www.abilityone.com/crafts-amp-recreation-room/category/107',
    'https://www.abilityone.com/desk-amp-workspace-organizers/category/109',
    'https://www.abilityone.com/file-folders-amp-storage-box-files/category/110',
    'https://www.abilityone.com/forms-recordkeeping-amp-ref-materials/category/113',
    'https://www.abilityone.com/office-supplies/category/1',

]

for data in mlist:
    urls = data

    r = requests.get(urls, headers=headers)
    # print(r)
    soup = BeautifulSoup(r.content, 'html.parser')

    # print(r)
    opts = Options()
    opts.headless = True
    opts.add_argument(
        "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
    driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
    driver.get(urls)
    time.sleep(5)
    urls = ""
    tags = driver.find_elements(By.TAG_NAME, "a")
    print("Total urls: ", len(tags))
    for i in tags:
        urls = (i.get_attribute('href'))
        print(urls)
        save_details: TextIO = open("abilityone.txt", "a+", encoding="utf-8")
        save_details.write("\n" + str(urls))
        print("End")
        save_details.close()
        print("\n ***** Record stored into Table Specifications . *****")
        print()



