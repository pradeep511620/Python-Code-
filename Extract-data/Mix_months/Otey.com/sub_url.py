import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

Result = [
    # 'https://www.oatey.com/products/cements-primers-cleaners',
    # 'https://www.oatey.com/products/thread-sealants',
    # 'https://www.oatey.com/products/copper-installation',
    # 'https://www.oatey.com/products/putty-caulks-water-barriers',
    # 'https://www.oatey.com/products/oils-lubricants-hand-cleaners',
    # 'https://www.oatey.com/products/drain-waste-system-cleaners',
    # 'https://www.oatey.com/products/heating-chemicals-antifreeze',
    # 'https://www.oatey.com/products/gaskets-bolts',
    # 'https://www.oatey.com/products/drains-closet-flanges',
    # 'https://www.oatey.com/products/shower-systems',
    # 'https://www.oatey.com/products/supply-boxes',
    # 'https://www.oatey.com/products/flashings',
    # 'https://www.oatey.com/products/air-admittance-valves-aav',
    # 'https://www.oatey.com/products/pipe-support',
    # 'https://www.oatey.com/products/brass-plastic-commercial-tubulargrab-bars',
    # 'https://www.oatey.com/products/bath-waste-overflow',
    # 'https://www.oatey.com/products/baskets-sink-strainers',
    # 'https://www.oatey.com/products/pneumatic-test-balls',
    # 'https://www.oatey.com/products/mechanical-test-plugs',
    # 'https://www.oatey.com/products/testing-equipment-tools-accessories',
    # 'https://www.oatey.com/products/pans-stands',
    # 'https://www.oatey.com/products/commercial-drains',
    # 'https://www.oatey.com/products/rough-products',

]
for url in Result:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
    driver.get(url)
    time.sleep(3)
    print("Products Urls", url)
    urlss = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[2]/div/div[5]/div[1]/div/div/div[3]')
    u = urlss.find_elements(by=By.TAG_NAME, value='a')
    for i in u:
        print(i.get_attribute('href'))
