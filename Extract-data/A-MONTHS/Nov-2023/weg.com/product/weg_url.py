import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
browser = webdriver.Chrome()
browser.maximize_window()

website_url = 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/General-Purpose-/TEAO-TEFC-Rolled-Steel/Steel-Motor/General-0-25-HP-2P-B56C-1Ph-115-208-230-V-60-Hz-IC411---TEFC---Foot-mounted/p/10566830'

browser.get(website_url)
time.sleep(3)
print("Product_urls", website_url)

url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Nov-2023/weg.com/url/weg-mpn-url.csv")['URL']
print(len(url_link))
i = 7104
for url_count, url in enumerate(url_link[i:], start=i):
    # browser.get(url)
    # time.sleep(4)
    print("Product-Length...", url_count)
    print("Product-Urls......", url)

    try:
        browser.find_element(By.XPATH, "//input[@class='form-control input-sm']").send_keys(url)
        time.sleep(2)
        browser.find_element(By.XPATH, "//i[@class='fa-solid fa-magnifying-glass']").click()
        time.sleep(3)

        get_url = browser.current_url
        print("current.....", get_url)
        with open('product_url_weg.txt', 'a+', encoding='utf-8') as save:
            save.write('\n' + get_url)
        print('save 1')
    except Exception as e:
        with open('remain_product_url_weg.txt', 'a+', encoding='utf-8') as save:
            save.write('\n' + url)
        print('remaining')

