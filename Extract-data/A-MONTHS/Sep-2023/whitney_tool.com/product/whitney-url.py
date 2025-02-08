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
    # 'https://www.whitneytool.com/Products.aspx?ID=846',
    # 'https://www.whitneytool.com/Products.aspx?ID=849',
    # 'https://www.whitneytool.com/Products.aspx?ID=850',
    # 'https://www.whitneytool.com/Category.aspx?ID=10',
    # 'https://www.whitneytool.com/Products.aspx?ID=30',
    # 'https://www.whitneytool.com/Products.aspx?ID=22',
    # 'https://www.whitneytool.com/Products.aspx?ID=2',
    # 'https://www.whitneytool.com/Products.aspx?ID=20',
    # 'https://www.whitneytool.com/Products.aspx?ID=21',
    # 'https://www.whitneytool.com/Products.aspx?ID=24',
    # 'https://www.whitneytool.com/Products.aspx?ID=25',
    # 'https://www.whitneytool.com/Products.aspx?ID=23',
    # 'https://www.whitneytool.com/Products.aspx?ID=43',
    # 'https://www.whitneytool.com/Products.aspx?ID=45',
    # 'https://www.whitneytool.com/Products.aspx?ID=44',
    # 'https://www.whitneytool.com/Products.aspx?ID=46',
    # 'https://www.whitneytool.com/Products.aspx?ID=47',
    # 'https://www.whitneytool.com/Products.aspx?ID=64',
    # 'https://www.whitneytool.com/Products.aspx?ID=36',
    # 'https://www.whitneytool.com/Products.aspx?ID=37',
    # 'https://www.whitneytool.com/Products.aspx?ID=41',
    # 'https://www.whitneytool.com/Products.aspx?ID=40',
    # 'https://www.whitneytool.com/Products.aspx?ID=38',
    # 'https://www.whitneytool.com/Products.aspx?ID=39',
    # 'https://www.whitneytool.com/Products.aspx?ID=42',
    # 'https://www.whitneytool.com/Products.aspx?ID=69',
    # 'https://www.whitneytool.com/Products.aspx?ID=26',
    # 'https://www.whitneytool.com/Products.aspx?ID=27',
    # 'https://www.whitneytool.com/Products.aspx?ID=31',
    # 'https://www.whitneytool.com/Products.aspx?ID=32',
    # 'https://www.whitneytool.com/Products.aspx?ID=847',
    # 'https://www.whitneytool.com/Products.aspx?ID=66',
    # 'https://www.whitneytool.com/Products.aspx?ID=67',
    # 'https://www.whitneytool.com/Products.aspx?ID=58',
    # 'https://www.whitneytool.com/Products.aspx?ID=57',
    # 'https://www.whitneytool.com/Products.aspx?ID=35',
    # 'https://www.whitneytool.com/Products.aspx?ID=34',
    # 'https://www.whitneytool.com/Products.aspx?ID=33',

]

# //div[@class='dir-row ng-star-inserted']//a

for url in mylists:
    browser.get(url)
    time.sleep(3)
    # print('Product-urls...', url)

    for option in browser.find_elements(By.XPATH, "//select[@id='Content_PageSize']//option"):
        print('option', option.text)
        if 'All Items' in option.text:
            print('ok')
            option.click()
            time.sleep(2)
        else:
            pass
            # print('no')

    for main_url in browser.find_elements(By.XPATH, "//div[@class='left products']//a"):
        product_url = main_url.get_attribute('href')
        # print("'" + product_url + "',")
        # print(product_url)
        save = open("urls.txt", 'a+', encoding='utf-8')
        save.write('\n' + product_url)
    print('save')
