import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
# driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver = uc.Chrome()

driver.maximize_window()

L = 0
Result = [
    'https://www.applied.com/brands/timken-company/lovejoy/c/Brand-985',
]
for url in Result:
    L = L + 1
    r = requests.get(url, headers=headers)
    # print(soup.prettify())?page=
    driver.get(url)
    time.sleep(2)
    print("Products Urls", L, url)

    links = driver.find_element(By.XPATH, "//div[@class='product-list']").find_elements(By.TAG_NAME, 'a')
    print("Lenght", len(links))
    for x in links:
        url_links = (x.get_attribute('href'))
        data_urls = ("'" + url_links + "',")
        print(data_urls)

    #

    l = driver.find_element(By.CLASS_NAME, "total-results")
    c = l.text.replace(',', '').split()[-1]
    print("count = ", c)
    length = round(int(c) / 20 + 1)
    print(length)
    for i in range(1, length):
        driver.get(url + "?page=" + str(i) + '&q=:&override=true&isLevelUp=false&usePlp=')
        time.sleep(5)
        links = driver.find_element(By.XPATH, "//div[@class='product-list']").find_elements(By.TAG_NAME, 'a')
        print("Lenght", len(links))
        for x in links:
            url_links = (x.get_attribute('href'))
            data_urls = ("'" + url_links + "',")
            print(data_urls)
        print(i)

