import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://new.abb.com/search/en/results#query=TY%20RAP#lang=en'
driver.get(url)
time.sleep(4)

try:
    driver.find_element(By.CSS_SELECTOR, ".seeall_link.all_btnseeallproducts").click()
    time.sleep(2)
except NoSuchElementException:
    print("click not found1")

try:
    shadow_host = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#PublicWrapper > main > section > div.search_maincontent > div:nth-child(4) > div.search_tabcontent.Products.search_active > div > pis-products-instance > pis-products-loading-indicator > pis-products-search-view > div > div.col-9.product_col_9 > pis-products-search-toolbar")))
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
    select_element = shadow_root.find_element(By.CSS_SELECTOR, "div > div > div.d-flex.justify-content-between.my-2.mx-2.w-100.order-1 > label.d-flex.align-items-center.ms-2 > select")
    driver.execute_script("arguments[0].value = '72'; arguments[0].dispatchEvent(new Event('change'));", select_element)
    time.sleep(8)
    print("Option with value 72 selected successfully.")
except Exception as e:
    print("Error occurred:", e)
def extract_url():
    while True:
        try:
            next_button = driver.execute_script("""
            return document.querySelector('#PublicWrapper > main > section > div.search_maincontent > div:nth-child(4) > div.search_tabcontent.Products.search_active > div > pis-products-instance > pis-products-loading-indicator > pis-products-search-view > div > div.col-9.product_col_9 > pis-products-search-pagination')
            .shadowRoot.querySelector('nav > div > ul > li > a[title=\"Next\"]')""")
            next_button.click()
            time.sleep(5)
            print('click')

            for href_model in range(1, 72 + 1):
                try:
                    model_title = driver.execute_script(f''' return document.querySelector("#PublicWrapper > main > section > div.search_maincontent > div:nth-child(4) > div.search_tabcontent.Products.search_active > div > pis-products-instance > pis-products-loading-indicator > pis-products-search-view > div > div.col-9.product_col_9 > pis-products-list-view > pis-products-search-list")
                    .shadowRoot.querySelector("div > div > div:nth-child({href_model}) > div > div:nth-child(4) > a > strong")''').text.strip()
                    # print(model_title)
                except AttributeError:
                    model_title = None
                    print("not found")

                try:
                    model_number = driver.execute_script(f''' return document.querySelector("#PublicWrapper > main > section > div.search_maincontent > div:nth-child(4) > div.search_tabcontent.Products.search_active > div > pis-products-instance > pis-products-loading-indicator > pis-products-search-view > div > div.col-9.product_col_9 > pis-products-list-view > pis-products-search-list")
                    .shadowRoot.querySelector("div > div > div:nth-child({href_model}) > div > div:nth-child(4) > div.small.text-muted.fw-bold")''').text.strip()
                    # print(model_number)
                except AttributeError:
                    model_number = None
                    print("not found")

                if model_title and model_number:
                    add_string1 = f"https://new.abb.com/products/{model_title}/{model_number}"
                    print(add_string1)
                    with open('abb_urls.txt', 'a+', encoding='utf') as url_save1:
                        url_save1.write(f"{add_string1}\n")


        except Exception as e:
            print(f"An error occurred: {e}")
            break


# extract_url()
