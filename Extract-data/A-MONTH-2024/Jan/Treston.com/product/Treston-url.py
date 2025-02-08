import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.maximize_window()


url_list = [

#
# # 'https://www.treston.us/chairs/treston-ergo',
# # 'https://www.treston.us/chairs/treston-plus',
# # 'https://www.treston.us/chairs/neon',
# # 'https://www.treston.us/chairs/flex-sit-stand-chair',
# # 'https://www.treston.us/chairs/work-stools',
# # 'https://www.treston.us/chairs/saddle-chairs',
# # 'https://www.treston.us/chairs/accessories-chairs',
# # 'https://www.treston.us/lighting/treston-dual-led-lighting',
# # 'https://www.treston.us/lighting/lighting-accessories',
# # 'https://www.treston.us/drawers/lmc-light-steel-cabinet',
# # 'https://www.treston.us/drawers/drawer-units-30-and-35',
# 'https://www.treston.us/drawers/drawer-unit-45',
# 'https://www.treston.us/drawers/drawer-unit-55',
# 'https://www.treston.us/drawers/drawer-unit-71',
# 'https://www.treston.us/drawers/drawer-unit-70',
# 'https://www.treston.us/drawers/drawer-unit-90',
# 'https://www.treston.us/drawers/drawer-unit-130',
# 'https://www.treston.us/drawers/accessories-drawers',
# 'https://www.treston.us/storage-systems/bins-and-bin-cabinets',
# 'https://www.treston.us/storage/shelves-and-cabinets',
# 'https://www.treston.us/storage-systems/fifo-flow-rack',
# 'https://www.treston.us/storage-systems/perforated-panels',
# 'https://www.treston.us/storage-systems/industrial-screens',
# 'https://www.treston.us/storage-systems/roll-stands',
# 'https://www.treston.us/storage-systems/tool-storage-systems',
# 'https://www.treston.us/storage-systems/accessories-storage',
# 'https://www.treston.us/workbenches/concept-workbench',
# 'https://www.treston.us/workbenches/cornerstone-workbenches',
# 'https://www.treston.us/workbenches/treston-electric-desk-ted',
# 'https://www.treston.us/workbenches/treston-quick-edge-workstation',
# 'https://www.treston.us/workbenches/tpb-packing-bench',
# 'https://www.treston.us/workbenches/tp-workbench',
# 'https://www.treston.us/workbenches/basic-upright-frame',
# "https://www.treston.us/carts/accessories-carts",
# 'https://www.treston.us/carts/bin-and-cabinet-carts/stacking-bin-carts',
# 'https://www.treston.us/carts/bin-and-cabinet-carts/cabinet-carts',
# 'https://www.treston.us/carts/additional-mobile-work-surface/concept-cart',
# 'https://www.treston.us/trolleys/additional-mobile-work-surface/sap-trolley',
# 'https://www.treston.us/carts/additional-mobile-work-surface/mlc-mobile-workstation',
# 'https://www.treston.us/carts/additional-mobile-work-surface/mobile-height-adjustable-work-surface-mlct',
# 'https://www.treston.us/carts/packing-carts/carton-carts',
# 'https://www.treston.us/carts/packing-carts/prmt-recycling-material-cart',
# 'https://www.treston.us/carts/picking-and-storage-carts/trta-adjustable-cart',
# 'https://www.treston.us/carts/picking-and-storage-carts/treston-industrial-multi-cart',
# 'https://www.treston.us/carts/picking-and-storage-carts/storage-cart',
# 'https://www.treston.us/carts/workshop-carts/fitters-cart',
# 'https://www.treston.us/carts/workshop-carts/treston-industrial-multi-cart',
# 'https://www.treston.us/carts/workshop-carts/heavy-duty-cart',
# 'https://www.treston.us/trolleys/workshop-trolleys/service-trolley',
# 'https://www.treston.us/carts/workshop-carts/tool-cart',
# 'https://www.treston.us/carts/rrt-reel-holder-cart',

]
for url in url_list:
    driver.get(url)
    time.sleep(3)
    print("Product - url : -----", url)
    # res = requests.get(url)
    # soup = BeautifulSoup(res.content, "html.parser")
    save = open('url.txt', "a+", encoding='utf-8')

    try:
        driver.find_element(By.XPATH,"//div[@class='button-container']//span").click()
        time.sleep(2)
    except ElementNotInteractableException:
        print('Not interact')




    url_lists = []

    try:
        first_link = driver.find_element(By.XPATH, "//div[@class='links']//a[1]")
        first_link.click()
        time.sleep(1)
        try:
            driver.find_element(By.XPATH, "(//a[normalize-space()='Display all'])[1]").click()
            time.sleep(4)
        except NoSuchElementException:
            print('nn')
        for product_url in driver.find_elements(By.XPATH, "(//div[@class='view-content'])[1]//table//td//a"):
            product_url_links = product_url.get_attribute('href')
            if all(keyword not in product_url_links for keyword in [".jpg", "news", "-team", "lab", "pdf"]):
                # print("'" + product_url_links + "',")
                url_lists.append(product_url_links)
        # print(url_lists)
    except NoSuchElementException:
        print("unable to click.")


    try:
        try:
            second_link = driver.find_element(By.XPATH, "//div[@class='links']//a[2]")
            second_link.click()
            time.sleep(1)
            print('second click')
        except ElementClickInterceptedException:
            print('Noo')
        max_attempts = 5
        attempts = 1
        while attempts < max_attempts:

            try:
                driver.find_element(By.XPATH, "//ul[@class='js-pager__items pager']//li//a").click()
                time.sleep(4)
            except ElementNotInteractableException:
                try:
                    driver.find_element(By.XPATH, "(//ul[@class='js-pager__items pager'])[2]//li//a").click()
                    time.sleep(4)
                except ElementNotInteractableException:
                    attempts += 1
                    print(f"Attempt {attempts}: Element not found. Retrying...")

                    for product_url in driver.find_elements(By.XPATH,
                                                            "(//div[@class='view-content'])[2]//table//td//a"):
                        product_url_links = product_url.get_attribute('href')
                        if all(keyword not in product_url_links for keyword in [".jpg", "news", "-team", "lab", "pdf"]):
                            # print("'" + product_url_links + "',")
                            url_lists.append(product_url_links)

        for product_url in driver.find_elements(By.XPATH, "(//div[@class='view-content'])[2]//table//td//a"):
            product_url_links = product_url.get_attribute('href')
            if all(keyword not in product_url_links for keyword in [".jpg", "news", "-team", "lab", "pdf"]):
                # print("'" + product_url_links + "',")
                url_lists.append(product_url_links)
        # print(url_lists)
    except NoSuchElementException:
        print("unable to click.")
    for product_url_href in url_lists:
        print(product_url_href)
        save.write(f"{product_url_href}\n")

driver.quit()
