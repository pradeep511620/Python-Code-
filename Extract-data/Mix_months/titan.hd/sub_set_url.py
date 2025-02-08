import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
#
Result = [
    'https://www.packardonline.com/search/?brand=Titan%20HD',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=2',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=3',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=4',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=5',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=6',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=7',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=8',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=10',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=11',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=12',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=13',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=14',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=15',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=16',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=17',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=18',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=19',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=20',
    'https://www.packardonline.com/search/?brand=Titan%20HD&pg=21',


    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=2',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=3',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=4',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=5',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=6',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=7',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=8',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=9',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=10',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=24&pg=11',


    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=36',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=36&pg=2',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=36&pg=3',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=36&pg=4',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=36&pg=5',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=36&pg=6',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=36&pg=7',


    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=72',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=72&pg=2',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=72&pg=3',
    'https://www.packardonline.com/search/?brand=Titan%20HD&mpp=72&pg=4',

    ]
for url in Result:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
    driver.get(url)
    # time.sleep(3)
    print("Products Urls", url)
    urlss = driver.find_element(by=By.ID, value='main-content')
    u = urlss.find_elements(by=By.TAG_NAME, value='a')
    for i in u:
        url_link = i.get_attribute('href')
        print("''"+url_link+"',")


