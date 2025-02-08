import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver.maximize_window()
L = 0
Result = [
    'https://www.watts.com/products/drainage-solutions',
]
for url in Result:
    L = L + 1
    r = requests.get(url, headers=headers)
    # print(soup.prettify())
    driver.get(url)
    time.sleep(5)
    print("Products Urls", L,  url)

    clk = driver.find_element(By.ID, "SelectResultCount").find_elements(By.TAG_NAME, 'option')
    for s in clk:
        # print(s.text)
        if "50" or "49" or "29" in s.text:
            s.click()
            time.sleep(3)
        else:
            pass
            # print("!!!!!!")

#
    l = driver.find_element(By.XPATH, "//div[@class='js-pagination-showing-results__container pagination-showing-results__container']")
    c = l.text.replace(',', '').split()[-2]
    # print("count = ", c)
    length = round(int(c) / 50 + 1)
    # print(length)
    for i in range(1, length):
        driver.find_element(By.XPATH, "//a[normalize-space()='>']").click()
        time.sleep(5)
        links = driver.find_element(By.XPATH, "//div[@class='js-results-target results-target']").find_elements(By.TAG_NAME, 'a')
        print("Lenght", len(links))
        for x in links:
            url_links = (x.get_attribute('href'))
            data_urls = ("'" + url_links + "',")
            print(data_urls)
        print(i)

