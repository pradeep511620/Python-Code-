import time

import pandas as pd
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome(options=opts)
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()

url_cout = 804
mylist = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/webshop.toolflo.com/url/sub_url_webshop.csv")['url']
for url in mylist[804:]:  # 930
    browser.get(url)
    print("Product_urls", url_cout, url)
    time.sleep(3)

    total_height = browser.execute_script(
        "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    scroll_position = browser.execute_script(
        "return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")
    for i in range(scroll_position, total_height - 500, 450):
        browser.execute_script("window.scrollBy(0, 100000)", "")
        time.sleep(1)

        product_urls = []
        for product in browser.find_elements(By.XPATH,
                                             "//table[@class='product_list uk-margin-small-top uk-margin-small-bottom']//a"):
            product_url = product.get_attribute('href')
            if product_url is not None and 'signin' not in product_url:
                product_urls.append(product_url)
        for urls in product_urls:
            print(urls)
            save = open('urlsss.txt', 'a+', encoding='utf-8')
            save.write('\n' + urls)
    url_cout += 1
