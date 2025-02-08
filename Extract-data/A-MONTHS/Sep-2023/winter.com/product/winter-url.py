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

    # 'https://winters.com/products-and-services/products-by-industry/fire-equipment/d6e1b08d-8427-4c6b-d86b-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/food--beverage/7a18c165-1418-4e85-d86c-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/hvac/344768ee-4023-4f15-d86d-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/hydraulic--pneumatic/206055b1-a136-4dae-d86e-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/manufacturing/6f4fb930-b85a-4735-d86f-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/metals--mining/eeb62e04-56c5-41fa-d870-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/oil--gas/7bad4b36-1f01-4000-d871-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/petrochemical/3fcdccff-f7ef-4561-d872-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/pharmaceutical--biotechnology/2b79bfb9-c39f-42e6-d873-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/pipe-valve--fitting/b2a2c0bb-45e5-4371-d874-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/plumbing/2a766e45-7ed6-4eca-d875-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/power-generation/0df7942e-d7fb-42ad-d876-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/pulp--paper/63dddb02-a7b7-40d9-d877-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/refrigeration/e433d74c-d701-4907-d878-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/transportation/797f395c-5116-4ffe-d879-08dad8c12b04',
    # 'https://winters.com/products-and-services/products-by-industry/waterwaste-water/b0a3159c-9eab-4fa3-d87a-08dad8c12b04',
    # 'https://winters.com/products-and-services/pressure/pressure-gauges/d72b26de-874c-4c12-a534-cb6739361203',
    # 'https://winters.com/products-and-services/pressure/pressure-transmitters/e8fdd1af-0e60-4d8b-95e8-fd28ec8eb860',
    # 'https://winters.com/products-and-services/pressure/pressure-switches/1ded80e8-7d37-41b0-9675-be3eda18b103',
    # 'https://winters.com/products-and-services/pressure/diaphragm-seals/6d88c2ae-abed-4f92-bc20-f6b390ec9600',
    # 'https://winters.com/products-and-services/accessories/valves/126cbee9-18cf-4cd8-8a39-79025a63b590',
    # 'https://winters.com/products-and-services/accessories/manifolds/6324f131-1567-4b15-923d-7cfd50a36b3e',
    # 'https://winters.com/products-and-services/accessories/additional-accessories/33e19c84-523c-477f-814d-e5905f17cc74',
    # 'https://winters.com/products-and-services/temperature/9ca34bd5-b3c1-4d4f-96f9-0622f6d1b1cb',
    # 'https://winters.com/products-and-services/temperature/rtds-and-thermocouples/9ecfa825-5779-42f5-aefa-b83d6ae4c455',
    # 'https://winters.com/products-and-services/temperature/thermowells/4979c698-5c8a-4300-9b95-95d66af59b90',

    'https://winters.com/products-and-services/temperature/thermometers/e6734e31-ebf2-425a-a945-970567585671',
    'https://winters.com/products-and-services/temperature/rtds-and-thermocouples/9ecfa825-5779-42f5-aefa-b83d6ae4c455',
    'https://winters.com/products-and-services/temperature/thermowells/4979c698-5c8a-4300-9b95-95d66af59b90',
    'https://winters.com/products-and-services/accessories/valves/126cbee9-18cf-4cd8-8a39-79025a63b590',
    'https://winters.com/products-and-services/accessories/manifolds/6324f131-1567-4b15-923d-7cfd50a36b3e',
    'https://winters.com/products-and-services/accessories/additional-accessories/33e19c84-523c-477f-814d-e5905f17cc74',
    'https://winters.com/products-and-services/pressure/pressure-gauges/d72b26de-874c-4c12-a534-cb6739361203',
    'https://winters.com/products-and-services/pressure/pressure-transmitters/e8fdd1af-0e60-4d8b-95e8-fd28ec8eb860',
    'https://winters.com/products-and-services/pressure/pressure-switches/1ded80e8-7d37-41b0-9675-be3eda18b103',
    'https://winters.com/products-and-services/pressure/diaphragm-seals/6d88c2ae-abed-4f92-bc20-f6b390ec9600',
]

# //div[@class='dir-row ng-star-inserted']//a

for url in mylists:
    browser.get(url)
    time.sleep(8)
    print('Product-urls...', url)
    for main_url in browser.find_elements(By.XPATH, "//div[@class='dir-row ng-star-inserted']//a"):
        product_url = main_url.get_attribute('href')
        # print("'" + product_url + "',")
        print(product_url)
        save = open("urls.txt", 'a+', encoding='utf-8')
        save.write('\n' + product_url)
