import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

url_list = [
    "https://hoto-instruments.com/product-category/stroboscopes/",
    "https://hoto-instruments.com/product-category/tachometer-lengthmeter/",
    'https://hoto-instruments.com/product-category/durometers/handheld-durometer/',
    'https://hoto-instruments.com/product-category/durometers/constant-load-stand-durometer/',
    'https://hoto-instruments.com/product-category/durometers/auto-load-durometer/',
    'https://hoto-instruments.com/product-category/durometers/auto-foam-hardness-tester/',
    'https://hoto-instruments.com/product-category/durometers/temperature-controlled-durometer/',
    'https://hoto-instruments.com/product-category/torque-measurement/digital-torque-screwdrivers/',
    'https://hoto-instruments.com/product-category/torque-measurement/digital-torque-wrenches/',
    'https://hoto-instruments.com/product-category/torque-measurement/digital-torque-calibrators/',
    'https://hoto-instruments.com/product-category/torque-measurement/breakaway-torque-tester/',
    'https://hoto-instruments.com/product-category/torque-measurement/rotating-torque-tester/',
    'https://hoto-instruments.com/product-category/torque-measurement/torque-data-acquisition/',
    'https://hoto-instruments.com/product/di-3-1p-digital-torque-tester/',
    'https://hoto-instruments.com/product/di-3n-1p-digital-torque-tester/',
    'https://hoto-instruments.com/product/di-5-rl-digital-torque-screwdriver/',
    'https://hoto-instruments.com/product/di-5-tw20-digital-torque-wrench/',
    'https://hoto-instruments.com/product/di-5n-rl-digital-torque-screwdriver/',
    'https://hoto-instruments.com/product/di-5n-tw20-digital-torque-wrench/',
    'https://hoto-instruments.com/product/dis-tw20-digital-torque-wrench/',
    'https://hoto-instruments.com/product/dsd-4-digital-torque-screwdriver/',
    'https://hoto-instruments.com/product/dsw-digital-torque-wrench/',
    'https://hoto-instruments.com/product/dw-digital-torque-wrench/',
    'https://hoto-instruments.com/product/esl-10-led-stroboscope/',
    'https://hoto-instruments.com/product/esl-100-led-stroboscope/',
    'https://hoto-instruments.com/product/esl-20-led-stroboscope/',
    'https://hoto-instruments.com/product/ex-durometer/',




# "https://hoto-instruments.com/product/plastic-or-glass-encoder-discs-for-oem/",
]
for url in url_list:
    driver.get(url)
    time.sleep(2)
    # print("Product - url : -----", url)
    # res = requests.get(url)
    # soup = BeautifulSoup(res.content, "html.parser")
    for product_url in driver.find_elements(By.XPATH, "//ul[@class='products columns-4']//a"):
        product_url_links = product_url.get_attribute('href')
        print(product_url_links)
