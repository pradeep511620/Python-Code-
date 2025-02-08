import os
import time

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


def ReadChromeDriver(product_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(6)

    return driver



def FetchProductUrl(driver):

    driver.execute_script('return document.querySelector("path")').click()
    time.sleep(3)
    print('click...')
    # try:
    #     driver.find_element(By.XPATH, "(//*[name()='circle'])[1]").click()
    #     time.sleep(4)
    # except NoSuchElementException:
    #     print('nn')

    try:
        driver.find_element(By.XPATH, "//button[@id='close']").click()
        time.sleep(2)
        print('click 1')
    except NoSuchElementException:
        print('not interact elements')

    try:
        driver.find_element(By.XPATH, "(//header[@class='modal-header'])[3]//button").click()
        time.sleep(2)
        print('click 2')
    except NoSuchElementException:
        print('not interact elements')



    try:
        option = driver.find_element(By.ID, "limiter-top").find_elements(By.TAG_NAME, "option")
    except NoSuchElementException:
        option = ''
    for opn in option:
        clk = opn.text.strip()
        print(clk)
        if clk == "All Items":
            opn.click()
            time.sleep(2)
            break


    for product in driver.find_elements(By.XPATH, "//ol[@class='products list items product-items']//a"):
        product_url_main = product.get_attribute('href')
        if "psku=" in product_url_main:
            print(product_url_main)
            with open("prod.txt", 'a+', encoding="utf-8") as file_save:
                file_save.write(f"{product_url_main}\n")
    print('')





def ReadUrlFromFile():
    compare_product_url = []
    compare_url = pd.read_csv('already-scrape-url.csv')['URL']
    for compare_urls in compare_url:
        compare_product_url.append(compare_urls.strip())
    return compare_product_url





def ReadFromListUrl():

    url_lists = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Globescientific.com/url/Globescientific-product-url.csv")["URL"]

    url_list = [

        "https://www.globescientific.com/gs-products/glassware.html",
        # "https://www.kennametal.com/us/en/products/fam.kencut-hm-hpfdm-square-end-5-flutes-plain-shank-inch.100003586.html",

    ]

    # Read url from file to compare url
    try:
        compare_product_url = ReadUrlFromFile()
    except FileNotFoundError:
        compare_product_url = ''
        print('file not found')

    # Read url one by one using list
    i = 1
    for N0, product_url in enumerate(url_lists[i:], start=i):
        print("Product --", N0, product_url)


        # compare url in already exist file
        if product_url in compare_product_url:
            print(f"Skipped this {product_url} Url Because It Is Already Done")
            continue

        # colling function
        # FetchProductUrl()

        driver = ReadChromeDriver(product_url)
        try:
            FetchProductUrl(driver)
        finally:
            driver.quit()

        # save running url
        last_product_url = product_url
        file_path = 'already-scrape-url.csv'
        header = 'URL'
        file_exists = os.path.exists(file_path)
        with open(file_path, 'a', newline='', encoding='utf-8') as save:
            if not file_exists:
                save.write(f"{header}\n")
            save.write(f"{last_product_url}\n")
    print('Saved Url')


def main():
    ReadFromListUrl()


if __name__ == "__main__":
    main()
