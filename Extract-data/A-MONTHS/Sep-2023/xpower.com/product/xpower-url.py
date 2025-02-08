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
    'https://xpower.com/',
]
for url in mylist:
    browser.get(url)
    print("Product_urls", url)
    time.sleep(1)
    for product in browser.find_elements(By.XPATH, "//li[@class='dropdown_menu']//a"):
        print(product.get_attribute('href'))
