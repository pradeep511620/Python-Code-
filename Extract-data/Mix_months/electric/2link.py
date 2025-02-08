import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver.maximize_window()
l = 0
Result = [
    'https://www.se.com/in/en/product-category/1600-electrical-protection-and-control/',
    'https://www.se.com/in/en/product-category/5600-light-switches-and-electrical-sockets/',
    'https://www.se.com/in/en/product-category/4200-circuit-breakers-and-switches/',
    'https://www.se.com/in/en/product-category/4800-push-buttons-switches-pilot-lights-and-joysticks/',
    'https://www.se.com/in/en/product-category/87897-medium-voltage-switchgear/',
    'https://www.se.com/in/en/product-category/8000-uninterruptible-power-supply-ups/',
    'https://www.se.com/in/en/product-category/2900-variable-speed-drives-and-frequency-drives/',
    'https://www.se.com/in/en/product-category/3000-motor-starters-and-protection-components/',
    'https://www.se.com/in/en/product-category/1500-contactors-and-protection-relays/',


]
for url in Result:
    l = l + 1
    # r = requests.get(url, headers=headers)
    # soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup)
    driver.get(url)
    time.sleep(10)
    print("Url_link", l, url)
    link = driver.find_element(by=By.XPATH, value="//div[@class='content-width-limiter subcats-wrapper js-category-ranges-list']")
    url_link = link.find_elements(by=By.TAG_NAME, value="a")
    print(len(url_link))
    for x in url_link:
        u = x.get_attribute('href')
        print(u)


