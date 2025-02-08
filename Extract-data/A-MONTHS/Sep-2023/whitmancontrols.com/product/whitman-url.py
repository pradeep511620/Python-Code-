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
    'https://www.whitmancontrols.com/pressure-switches.html',
    'https://www.whitmancontrols.com/pressure-transmitters.html',
    'https://www.whitmancontrols.com/vacuum-switches.html',
    'https://www.whitmancontrols.com/liquid-level-switches.html',
    'https://www.whitmancontrols.com/liquid-level-switches/level-switches.html',
    'https://www.whitmancontrols.com/liquid-level-switches/vibrating-forks-rods.html',
    'https://www.whitmancontrols.com/level-transmitters.html',
    'https://www.whitmancontrols.com/temperature-products.html',
    'https://www.whitmancontrols.com/p845-differential-pressure-switches.html',
    'https://www.whitmancontrols.com/pressure-switches/compound-switches.html',
    'https://www.whitmancontrols.com/oem-replacement-parts.html',

]

# //div[@class='dir-row ng-star-inserted']//a

for url in mylists:
    browser.get(url)
    time.sleep(3)
    # print('Product-urls...', url)
    for main_url in browser.find_elements(By.XPATH,"//div[@class='products wrapper list products-list category-product-list']//a"):
        product_url = main_url.get_attribute('href')
        save = open("urls.txt", 'a+', encoding='utf-8')
        save.write('\n' + product_url)
    print('save1')
    try:
        count = browser.find_element(By.XPATH, "//div[@class='toolbar-top']//p[@id='toolbar-amount']").text.strip().split(' ')[-1]
        length = round(int(count) / 25)
        print(length)
        for i in range(1, length + 1):
            browser.find_element(By.XPATH, "//div[contains(@class,'toolbar-bottom toolbar-view-list')]//span[contains(text(),'NEXT')]").click()
            time.sleep(2)

            for main_url in browser.find_elements(By.XPATH,
                                                  "//div[@class='products wrapper list products-list category-product-list']//a"):
                product_url = main_url.get_attribute('href')
                print("'" + product_url + "',")

                # print(product_url)
                save = open("urls.txt", 'a+', encoding='utf-8')
                save.write('\n' + product_url)
            print('save2')
    except:
        print('noooo')
        for main_url in browser.find_elements(By.XPATH,"//div[@class='products wrapper list products-list category-product-list']//a"):
            product_url = main_url.get_attribute('href')
            print("'" + product_url + "',")

        # print(product_url)
            save = open("urls.txt", 'a+', encoding='utf-8')
            save.write('\n' + product_url)
        print('save2')
