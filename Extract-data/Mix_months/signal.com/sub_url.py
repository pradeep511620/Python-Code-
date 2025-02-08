import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
Result = [
    'https://signaling.fedsig.com/category/signaling',
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

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(99)
    links = driver.find_element(by=By.ID, value='product-grid')
    linkss = links.find_elements(by=By.TAG_NAME, value='a')
    for x in linkss:
        data = (x.get_attribute('href'))
        print("''"+data+"',")

