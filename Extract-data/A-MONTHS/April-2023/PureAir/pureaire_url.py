import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

for i in range(1, 3 + 1):
    myurl = [f"https://www.pureairemonitoring.com/monitors-by-gas-detected/page/{i}/",
             ]
    for url in myurl:
        driver.get(url)
        time.sleep(2)
        print("Product-urls", url)

        url_link = driver.find_element(by=By.XPATH, value="//ul[@class='products columns-3']")
        url_links = url_link.find_elements(By.TAG_NAME, "a")
        for urls in url_links:
            url_lnk = urls.get_attribute('href')
            print(url_lnk)
            save = open('url_pureaire.txt', 'a+', encoding="utf-8")
            save.write("\n" + "'"+url_lnk+"',")
        print("save url in text files")
