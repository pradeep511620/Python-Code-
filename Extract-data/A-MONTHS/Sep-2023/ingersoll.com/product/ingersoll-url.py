import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()

mylist = [
    'https://www.ingersoll-imc.com/product/category/indexable-mills',
    'https://www.ingersoll-imc.com/product/category/solid-carbide-mills',
    'https://www.ingersoll-imc.com/product/category/boring-and-reaming',
    'https://www.ingersoll-imc.com/product/category/holemaking',
    'https://www.ingersoll-imc.com/product/category/parting-grooving',
    'https://www.ingersoll-imc.com/product/category/threading',
    'https://www.ingersoll-imc.com/product/category/tool-holding',
    'https://www.ingersoll-imc.com/product/category/turning',
]
for url in mylist:

    browser.get(url)
    print("Product_urls", url)
    time.sleep(9)
    print(len(browser.find_elements(By.XPATH, "//div[@id='productcatalogcontainer']//a")))
    with open('product_url_for1.txt', 'a+', encoding='utf-8') as save_file:
        for url_link in browser.find_elements(By.XPATH, "//div[@id='productcatalogcontainer']//a"):
            product_url = url_link.get_attribute('href')
            save_file.write('\n' + product_url)
