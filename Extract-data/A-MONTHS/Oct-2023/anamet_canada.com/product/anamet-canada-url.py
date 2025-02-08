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

mylist = [
    'https://www.anametcanada.com/products/anaconda-flexible-conduits-and-fittings/sealtite-metallic-liquid-tight/',
    'https://www.anametcanada.com/products/anaconda-flexible-conduits-and-fittings/fittings-for-sealtite-metallic-liquid-tight/',
    'https://www.anametcanada.com/products/anaconda-flexible-conduits-and-fittings/sealtite-non-metallic-conduit/',
    'https://www.anametcanada.com/products/anaconda-flexible-conduits-and-fittings/fittings-for-sealtite-non-metallic-conduit/',
    'https://www.anametcanada.com/products/anaconda-flexible-conduits-and-fittings/non-jacketed-conduit/',
    'https://www.anametcanada.com/products/anaconda-flexible-conduits-and-fittings/fittings-for-non-jacketed-conduit/',
    'https://www.anametcanada.com/products/anaconda-flexible-conduits-and-fittings/anaquick-nylon/',
    'https://www.anametcanada.com/products/anaconda-flexible-conduits-and-fittings/fittings-for-anaquick-nylon/',
    'https://www.anametcanada.com/products/fittings/metallic-conduit-fittings/',
    'https://www.anametcanada.com/products/fittings/non-metallic-conduit-fittings/',
    'https://www.anametcanada.com/products/fittings/specialty-fittings/',
    'https://www.anametcanada.com/products/nylon/anaquick-conduit/',
    'https://www.anametcanada.com/products/nylon/fittings-for-anaquick-conduit/',
    'https://www.anametcanada.com/products/firetech/firetech-protection/',
    'https://www.anametcanada.com/products/firetech/accessories-for-firetech-protection/',
    'https://www.anametcanada.com/products/cable-glands/',
    'https://www.anametcanada.com/markets/train-infrastructure/',
    'https://www.anametcanada.com/markets/power-energy/',
    'https://www.anametcanada.com/markets/food-pharma/',
    'https://www.anametcanada.com/markets/oem-machinebuilding/',
    'https://www.anametcanada.com/markets/factory-automation/',
    'https://www.anametcanada.com/markets/steel-foundry/',
    'https://www.anametcanada.com/markets/marine-defence/',
    'https://www.anametcanada.com/markets/oil-gas/',

]
for url in mylist:
    browser.get(url)
    print("Product_urls", url)
    time.sleep(1)
    for product in browser.find_elements(By.XPATH, "//div[@class='uk-margin-medium uk-margin-remove-top']//a"):
        product_url = product.get_attribute('href')
        print(product_url)
        save = open("url1.txt", "a+", encoding="utf-8")
        save.write(f"\n {product_url}")
    print('save url ...........1')

    # count = browser.find_element(By.XPATH, "(//td[@align='left'])[4]").text.strip().split(' ')[-2]
    # length = round(int(count) / 12 + 1)
    # print(count)
    # for i in range(1, length):
    #     try:
    #         browser.find_element(By.XPATH, "(//a[contains(text(),'Next >>')])[1]").click()
    #         time.sleep(3)
    #         print(i)
    #     except NoSuchElementException:
    #         print('Unable to locate element')

    #     Result = [
    #         f"{url}/{'page'}/{i}"
    #     ]
    #     for jj in Result:
    #         print("'" + jj + "',")

    # for product in browser.find_elements(By.XPATH, "//table[@id='partNumList']//a"):
    #     product_url = product.get_attribute('href')
    #     print(product_url)
    #     save = open("url1.txt", "a+", encoding="utf-8")
    #     save.write(f"\n {product_url}")
    # print('save url ...........2')
