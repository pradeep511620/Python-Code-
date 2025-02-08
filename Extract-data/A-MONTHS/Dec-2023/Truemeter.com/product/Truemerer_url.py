import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()


url_list = [
    'https://www.trumeter.com/products/apm/volt-frequency-current/',
    'https://www.trumeter.com/products/apm/power-meters',
    'https://www.trumeter.com/products/apm/process/',
    'https://www.trumeter.com/products/apm/flow-indicators',
    'https://www.trumeter.com/products/apm/multipurpose/',
    'https://www.trumeter.com/products/iot/',
    'https://www.trumeter.com/products/vista-touch/',
    'https://www.trumeter.com/product/apm-vista-touch-flow/',
    'https://www.trumeter.com/product/vista-touch-power/',
    'https://www.trumeter.com/products/counters/die/',
    'https://www.trumeter.com/products/counters/predetermining/',
    'https://www.trumeter.com/products/counters/rotary/',
    'https://www.trumeter.com/products/counters/stroke/',
    'https://www.trumeter.com/products/counters/totalizing/',
    'https://www.trumeter.com/products/timers/day-timers/',
    'https://www.trumeter.com/products/timers/hour-meters/',
    'https://www.trumeter.com/products/timers/time-relays/',
    'https://www.trumeter.com/products/length/cable-wire-rope/',
    'https://www.trumeter.com/products/length/fabric-carpet/',
    'https://www.trumeter.com/products/distance/rail-measuring-wheels/',
    'https://www.trumeter.com/products/distance/road-measuring-wheels/',
    'https://www.trumeter.com/products/distance/land-measuring-wheels/',
    'https://www.trumeter.com/products/other/encoders/',
    'https://www.trumeter.com/products/other/panel-meters/',
    'https://www.trumeter.com/products/other/tachometers/',
    'https://www.trumeter.com/products/other/thermometers/',
]
for url in url_list:
    driver.get(url)
    time.sleep(2)
    # print("Product - url : -----", url)
    # res = requests.get(url)
    # soup = BeautifulSoup(res.content, "html.parser")
    for product_url in driver.find_elements(By.XPATH, "//div[@class='elementor-jet-woo-products jet-woo-builder']//a"):
        product_url_links = product_url.get_attribute('href')
        print(product_url_links)

