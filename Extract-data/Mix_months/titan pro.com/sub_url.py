import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
for i in range(0, 16):
    Result = [
        f'https://www.packardonline.com/search/?brand=Titan%20Pro&pg={i}',
        # 'https://www.packardonline.com/search/?brand=Titan%20Pro',
        # 'https://www.packardonline.com/search/?brand=Titan%20Pro&pg=2',
        # 'https://www.packardonline.com/search/?brand=Titan%20Pro&mpp=24',
        # 'https://www.packardonline.com/search/?brand=Titan%20Pro&mpp=36',
        # 'https://www.packardonline.com/search/?brand=Titan%20Pro&mpp=72',

    ]
    for url in Result:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        # print(soup.prettify())
        opts = Options()
        opts.headless = True
        driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver")
        driver.get(url)
        time.sleep(3)
        print("Products Urls", url)



        u1 = driver.find_element(by=By.XPATH, value='//*[@id="hawktoppager"]/div[2]').click()
        urlss = driver.find_element(by=By.ID, value='main-content')
        u = urlss.find_elements(by=By.TAG_NAME, value='a')
        for i in u:
            print(i.get_attribute('href'))
