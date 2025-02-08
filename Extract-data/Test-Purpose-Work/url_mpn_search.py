
import time
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
# import undetected_chromedriver as la
driver = webdriver.Chrome()
driver.maximize_window()


url_1 = 'https://www.grainger.com/'
file_path = r"C:\Users\prade\Downloads\Grainger (18-07-2024).xlsx"
url_links = pd.read_excel(file_path)['MPN']
start_url = 2
for url_count, url in enumerate(url_links[start_url:], start=start_url):
    send_url = url.replace("rp_", '')
    print('product_url.....', url_count, send_url)
    # try:
    if url_count == 0:
        driver.get(url_1)
        time.sleep(2)
    else:
        driver.get(url_1)
        time.sleep(2)



    try:
        search_box = driver.find_element(By.CSS_SELECTOR, "div.gcom__typeahead-query-field-container input")
        search_box.send_keys(send_url)
        time.sleep(2)
    except NoSuchElementException:
        print("Input box Not found")

    try:
        click_to_search_button = driver.find_element(By.CSS_SELECTOR, "button.gcom__typeahead-submit-button")
        click_to_search_button.click()
        time.sleep(3)
    except NoSuchElementException:
        print("Input box click Not found")

    current_url = driver.current_url
    with open('grainger_current.txt', 'a+', encoding='utf') as url_save:
        url_save.write(f"{current_url}\t{send_url}\n")

    brand = ''
    try:
        brand = driver.find_elements(By.CSS_SELECTOR, "div.search-results__product-brand-name")[0].text.strip()
        print(f"Brand---{brand}---mpn---{send_url}")
    except IndexError:
        try:
            brand = driver.find_elements(By.CSS_SELECTOR, "dd.rOM8HV._2DmSH.IuSbF.N5ad3")[3].text.strip()
            print(f"Brand---{brand}")
        except IndexError:
            print('Not found')


    product_url = ''
    try:
        product_url = driver.find_elements(By.CSS_SELECTOR, "div.search-results__product-description a")[0].get_attribute('href')
        print(product_url)
    except IndexError:
        try:
            product_url = current_url = driver.current_url
            print(product_url)
        except IndexError:
            print('NOt found')

    sku = ''
    try:
        sku = driver.find_elements(By.CSS_SELECTOR, "[data-automated-test='sku']")[0].text.strip()
        print(sku)
    except IndexError:
        try:
            sku = driver.find_elements(By.CSS_SELECTOR, "dd.rOM8HV._2DmSH.IuSbF.N5ad3")[0].text.strip()
            print(sku)
        except IndexError:
            print('NOt found')

    model = ''
    try:
        model = driver.find_elements(By.CSS_SELECTOR, "[data-automated-test='manufacturerModelNumber']")[0].text.strip()
        print(model)
    except IndexError:
        try:
            model = driver.find_elements(By.CSS_SELECTOR, "dd.rOM8HV._2DmSH.IuSbF.N5ad3")[1].text.strip()
            print(model)
        except IndexError:
            print('NOt found')

    price = ''
    try:
        price = driver.find_elements(By.CSS_SELECTOR, "div.pricing__leftSide.pricing__regular span.pricing__price")[0].text.strip()
        print(price)
    except IndexError:
        try:
            price = driver.find_elements(By.CSS_SELECTOR, ".XCqnjh span.HANkB.IuSbF.N5ad3.xqCG3.a0SF-._4TUUj")[
                0].text.strip()
            print(price)
        except IndexError:
            print('NOt found')

    with open('grainger_data_1.txt', 'a+', encoding='utf') as url_save:
        url_save.write(f"{brand}\t{send_url}\t{product_url}\t{sku}\t{model}\t{price}\n")
