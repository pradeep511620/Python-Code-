import time

import pandas as pd
from selenium import webdriver
from selenium.common import ElementNotInteractableException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()
#

# mylist = [
#     'https://medifyair.com/products/ma-40-replacement-filter-set',
#
#     # 'https://medifyair.com/products/16-x-25-x-4-hvac-filters',
#
#
#     #
#
# ]
#
# for url in mylist:
#     browser.get(url)
#     time.sleep(4)
#     print("Product_urls", url)

# url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/modifyair.com/url/modifyair-product-url.csv")['URL']
# i = 0
# for url_count, url in enumerate(url_link[i:], start=i):
#     browser.get(url)
#     time.sleep(4)
#     print("Product-Length...", url_count)
#     print("Product-Urls......", url)


try:
    dropdown = browser.find_element(By.XPATH, "//div[@class='select position-relative js-dropdown js-select'][1]")
    rating_options = dropdown.find_elements(By.TAG_NAME, "option")
    for option in rating_options:
        option.click()
        time.sleep(2)
        print('click value ...', option.text.strip())
        get_current_url = browser.current_url
        print('get_current_url.....', get_current_url)
        with open('product_url.txt', 'a+', encoding='utf-8') as save:
            save.write('\n' + get_current_url)
        print('save 1')

        dropdown_1 = browser.find_element(By.XPATH, "(//div[@class='select position-relative js-dropdown js-select'])[2]")
        rating_options_1 = dropdown_1.find_elements(By.TAG_NAME, "option")
        for option_1 in rating_options_1:
            option_1.click()
            time.sleep(2)
            print('click value ...', option_1.text.strip())
            get_current_url_1 = browser.current_url
            print('get_current_url_1.....', get_current_url_1)
            with open('product_url.txt', 'a+', encoding='utf-8') as save:
                save.write('\n' + get_current_url_1)
            print('save 2')

except Exception as e:
    print('Not Click 2')
    print(e)


