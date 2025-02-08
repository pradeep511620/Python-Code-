from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()

mylist = [
    # 'https://thomasprod.com/flow-switches/',
    # 'https://thomasprod.com/level-switches/',
    # 'https://thomasprod.com/pump-controls/',
    # 'https://thomasprod.com/indicators/',
    'https://thomasprod.com/accessories/'
]

for url in mylist:
    browser.get(url)
    time.sleep(2)

    urls = []
    print('enter first')
    try:
        for category_url in browser.find_elements(By.XPATH, "//*[@class='show-on-mousehover']//a"):
            href_tag = category_url.get_attribute('href')
            urls.append(href_tag)
    except:
        print('enter second')
    #
    try:
        for category_url in browser.find_elements(By.XPATH, "//*[@class='product-title']//a"):
            href_tag = category_url.get_attribute('href')
            urls.append(href_tag)
    except:
        print('enter third')

    print('enter third')
    try:
        for category_url in browser.find_elements(By.XPATH, "//*[@class='product-title']//a"):
            href_tag = category_url.get_attribute('href')
            urls.append(href_tag)
    except:
        print('NNNN3')

    for tick in urls:
        print(tick)
        with open('Fast.txt', "a+", encoding='utf-8') as save_file:
            save_file.write(f"{tick}\n")
    print('data save')
