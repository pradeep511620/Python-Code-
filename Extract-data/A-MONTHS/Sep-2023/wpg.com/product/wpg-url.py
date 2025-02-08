import time
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()
"""
mylist = [
    'https://www.wpg.com/catalog/hand-held-vacuum-cups',
    'https://www.wpg.com/catalog/vacuum-lifters',
    'https://www.wpg.com/catalog/vacuum-mounting-cups',
    'https://www.wpg.com/catalog/parts',
    'https://www.wpg.com/catalog/other-products',
]
for url in mylist:
    browser.get(url)
    # print("Product_urls", url)
    time.sleep(1)

    count = browser.find_element(By.XPATH, "//div[@class='filter-total']").text.strip().split(' ')[0]
    length = round(int(count) / 24)
    # print(length)
    for i in range(1, length + 1):
        Result = [
            f"{url}/{'page'}/{i}"
        ]
        for jj in Result:
            print("'" + jj + "',")
"""

mylists = [
    'https://www.wpg.com/catalog/hand-held-vacuum-cups/page/1',
    'https://www.wpg.com/catalog/hand-held-vacuum-cups/page/2',
    'https://www.wpg.com/catalog/vacuum-lifters/page/1',
    'https://www.wpg.com/catalog/vacuum-mounting-cups/page/1',
    'https://www.wpg.com/catalog/parts/page/1',
    'https://www.wpg.com/catalog/parts/page/2',
    'https://www.wpg.com/catalog/parts/page/3',
    'https://www.wpg.com/catalog/parts/page/4',
    'https://www.wpg.com/catalog/parts/page/5',
    'https://www.wpg.com/catalog/parts/page/6',
    'https://www.wpg.com/catalog/parts/page/7',
    'https://www.wpg.com/catalog/parts/page/8',
    'https://www.wpg.com/catalog/parts/page/9',
    'https://www.wpg.com/catalog/parts/page/10',
    'https://www.wpg.com/catalog/parts/page/11',
    'https://www.wpg.com/catalog/parts/page/12',
    'https://www.wpg.com/catalog/parts/page/13',
    'https://www.wpg.com/catalog/parts/page/14',
    'https://www.wpg.com/catalog/parts/page/15',
    'https://www.wpg.com/catalog/parts/page/16',
    'https://www.wpg.com/catalog/parts/page/17',
    'https://www.wpg.com/catalog/parts/page/18',
    'https://www.wpg.com/catalog/parts/page/19',
    'https://www.wpg.com/catalog/parts/page/20',
    'https://www.wpg.com/catalog/parts/page/21',
    'https://www.wpg.com/catalog/parts/page/22',
    'https://www.wpg.com/catalog/parts/page/23',
    'https://www.wpg.com/catalog/parts/page/24',
    'https://www.wpg.com/catalog/parts/page/25',
    'https://www.wpg.com/catalog/parts/page/26',
    'https://www.wpg.com/catalog/parts/page/27',
    'https://www.wpg.com/catalog/other-products/page/1',
    'https://www.wpg.com/catalog/other-products/page/2',
    'https://www.wpg.com/catalog/other-products/page/3',
    'https://www.wpg.com/catalog/other-products/page/4',
    'https://www.wpg.com/catalog/other-products/page/5',
]

for url in mylists:
    browser.get(url)
    print(url)
    for main_url in browser.find_elements(By.XPATH, "//div[@class='products-grid grid-3']//a"):
        product_url = main_url.get_attribute('href')
        print(product_url)
        save = open("specs.txt", 'a+', encoding='utf-8')
        save.write('\n' + product_url)
