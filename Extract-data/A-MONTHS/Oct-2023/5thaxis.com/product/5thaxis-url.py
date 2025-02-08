import time
from selenium import webdriver
from selenium.common import NoSuchElementException
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

    # 'https://www.reelcraft.com/catalog/interactive-catalog/air-hose-reels/general-air-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/air-hose-reels/enclosed-air-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/air-hose-reels/stainless-steel-air-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/air-hose-reels/air-vend-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/air-hose-reels/high-temperature-air-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/air-hose-reels/reelsafe-air-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/air-hose-reels/cabinet-style-air-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/air-hose-reels/storage-hose-reels-air-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/fuel-gas-reels/def-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/fuel-gas-reels/diesel-and-gas-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/general-water-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/enclosed-water-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/pressure-wash-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/pre-rinse-potable-water/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/stainless-steel-water-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/garden-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/ss-fluid-path-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/reelsafe-water-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/cabinet-style-water-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/water-hose-reels/storage-hose-reels-water-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/oil-hose-reels/general-oil-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/oil-hose-reels/stainless-steel-oil-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/oil-hose-reels/reelsafe-oil-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/welding-reels/single-line-welding/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/welding-reels/twin-line-welding-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/welding-reels/welding-cable-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/grease-hose-reels/general-grease-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/grease-hose-reels/reelsafe-grease-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/cord-cable-reels/power-cord-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/cord-cable-reels/light-cord-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/cord-cable-reels/nema-4-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/cord-cable-reels/reverse-plug-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/cord-cable-reels/light-cord-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/twin-hydraulic-hose-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/welding-reels/welding-cable-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/tool-balancers/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/grounding-reels/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/inlet-hose-assemblies/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/reel-covers/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/roller-guide-assemblies/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/motor-accessories/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/swing-brackets-bases/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/garden-accessories/',
    'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/hose-assemblies/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/adjustable-bumper-stops/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/rewind-motors/',
    # 'https://www.reelcraft.com/catalog/interactive-catalog/reel-accessories/swivel-assemblies/',
]

for url in mylist:
    browser.get(url)
    print("Product_urls", url)
    time.sleep(2)

    for product in browser.find_elements(By.XPATH, "//ul[@class='products columns-5']//li//a"):
        product_url = product.get_attribute('href')
        print(product_url)
        save = open("url1.txt", "a+", encoding="utf-8")
        save.write(f"\n {product_url}")
    print('save url ...........1')

    count_of_total_url_number = browser.find_element(By.XPATH, "//p[@class='woocommerce-result-count']").text.strip().split(' ')[-2]
    print('count_of_total_url_number.....', count_of_total_url_number)
    length = round(int(count_of_total_url_number) / 80 + 1)
    print(length)
    for i in range(1, length):
        try:
            browser.find_element(By.XPATH, "//a[contains(text(),'→')]").click()
            time.sleep(3)
            print(i)
        except NoSuchElementException:
            print('Unable to locate element')

        for product in browser.find_elements(By.XPATH, "//ul[@class='products columns-5']//li//a"):
            product_url = product.get_attribute('href')
            print(product_url)
            save = open("url1.txt", "a+", encoding="utf-8")
            save.write(f"\n {product_url}")
    print('save url ...........2')
