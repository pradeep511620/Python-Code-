import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-plugins")
chrome_options.add_argument("--headless")
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
driver = webdriver.Chrome()

driver.maximize_window()

mylist = [
    'https://www.powerbuilt.com/collections/air-compressors-and-accessories-1',
    'https://www.powerbuilt.com/collections/brake-tools-2',
    'https://www.powerbuilt.com/collections/diagnostic-tools-1',
    'https://www.powerbuilt.com/collections/engine-drivetrain-tools-2',
    'https://www.powerbuilt.com/collections/fuel-ignition-tools-1',
    'https://www.powerbuilt.com/collections/installer-kits-2',
    'https://www.powerbuilt.com/collections/lubrication-tools-2',
    'https://www.powerbuilt.com/collections/steering-suspension-tools-1',
    'https://www.powerbuilt.com/collections/garage-wall-storage-system-2',
    'https://www.powerbuilt.com/collections/cutting-tools-2',
    'https://www.powerbuilt.com/collections/hex-torx-keys-and-sockets-1',
    'https://www.powerbuilt.com/collections/pliers-2',
    'https://www.powerbuilt.com/collections/ratchets-2',
    'https://www.powerbuilt.com/collections/screwdrivers-1',
    'https://www.powerbuilt.com/collections/sockets-1',
    'https://www.powerbuilt.com/collections/wrenches-1',
    'https://www.powerbuilt.com/collections/tool-sets-1',
    'https://www.powerbuilt.com/collections/striking-tools-1',
    'https://www.powerbuilt.com/collections/jacks-and-lift-equipment-2',
    'https://www.powerbuilt.com/collections/seating-equipment',
    'https://www.powerbuilt.com/collections/lighting-2',
    'https://www.powerbuilt.com/collections/pro-tech-pliers-2',
    'https://www.powerbuilt.com/collections/pro-tech-ratchets-accessories-2',
    'https://www.powerbuilt.com/collections/pro-tech-screwdrivers-2',
    'https://www.powerbuilt.com/collections/pro-tech-tool-sets-2',
    'https://www.powerbuilt.com/collections/pro-tech-wrenches-2',
    'https://www.powerbuilt.com/collections/power-tools-2',
    'https://www.powerbuilt.com/collections/tool-storage-1',
    'https://www.powerbuilt.com/collections/powerbuilt-gear-1',
    'https://www.powerbuilt.com/collections/zeon-tools-for-damaged-nuts-and-bolts',
    'https://www.powerbuilt.com/collections/all-new-vde-tools',
]

for url in mylist:
    driver.get(url)
    time.sleep(2)
    # print(url)
    save = open('Sealmaster_urls.txt', "a+", encoding='utf-8')
    for product_cate in driver.find_elements(By.XPATH, "//*[@class='product-item-meta']//a"):
        product_tag = product_cate.get_attribute("href")
        if "#" not in product_tag and "pages" not in product_tag:
            print("'" + product_tag + "',")
            save.write(f"{product_tag}\n")

    s_num = driver.find_element(By.XPATH, "//span[@role='status']").text.strip().split(" ")[0]
    length = round(int(s_num) / 24 + 1)
    for i in range(1, length + 1):
        try:
            driver.find_element(By.XPATH, "//a[@aria-label='Next']").click()
            time.sleep(2)
        except NoSuchElementException:
            print("don't get next button")

    for product_cate in driver.find_elements(By.XPATH, "//*[@class='product-item-meta']//a"):
        product_tag = product_cate.get_attribute("href")
        if "#" not in product_tag and "pages" not in product_tag:
            print("'" + product_tag + "',")
            save.write(f"{product_tag}\n")
driver.quit()
