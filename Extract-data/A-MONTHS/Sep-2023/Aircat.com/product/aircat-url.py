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

    'https://aircat.com/aircat/impact-wrenches',
    'https://aircat.com/aircat/ratchets',
    'https://aircat.com/aircat/grinders',
    'https://aircat.com/aircat/cut-off-tools',
    'https://aircat.com/aircat/drills',
    'https://aircat.com/aircat/hammers',
    'https://aircat.com/aircat/sanders',
    'https://aircat.com/aircat/specialty-tools',
    'https://aircat.com/aircat/tire-buffers',
    'https://aircat.com/aircat/new-products',
]
for url in mylist:
    browser.get(url)
    print("Product_urls", url)
    time.sleep(1)
    browser.find_element(By.XPATH, "//button[normalize-space()='View All']").click()
    time.sleep(2)
    for product in browser.find_elements(By.XPATH, "//div[@class='row products-grid']//a"):
        product_url = product.get_attribute('href')
        if "product_compare/" not in product_url:
            print(product_url)
            save = open("url.txt", "a+", encoding="utf-8")
            save.write(f"\n {product_url}")
