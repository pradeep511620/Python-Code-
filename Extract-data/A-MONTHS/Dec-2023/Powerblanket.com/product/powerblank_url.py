import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

url = 'https://www.powerblanket.com/products/'
driver.get(url)
time.sleep(2)

for url_link in driver.find_elements(By.XPATH, "//ul[@class='products columns-3']//a"):
    product_url = url_link.get_attribute('href')
    print(product_url)
