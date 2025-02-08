import os
import time

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
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
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(2)

    return driver



def FetchProductUrl(driver):
    # try:
    #     driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
    #     time.sleep(1)
    # except NoSuchElementException:
    #     print('not interact elements')
    #
    # try:
    #     option = driver.find_element(By.ID, "available-variants__size").find_elements(By.TAG_NAME, "option")
    # except NoSuchElementException:
    #     option = ''
    # for opn in option:
    #     clk = opn.text.strip()
    #     if clk == "ALL":
    #         opn.click()
    #         time.sleep(4)
    #         break


    for product in driver.find_elements(By.XPATH, "//div[@class='fusion-fullwidth fullwidth-box fusion-builder-row-2 nonhundred-percent-fullwidth non-hundred-percent-height-scrolling']//div[@class='fusion-builder-row fusion-row']//a"):
        product_url_main = product.get_attribute('href')
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

    # url_lists = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/kennametal.csv")["URL"]

    url_list = [

        'https://kalamazooind.com/products/abrasive-saws/',
        # 'https://kalamazooind.com/products/belt-grinders/',
        # 'https://kalamazooind.com/products/belt-sanders/',
        # 'https://kalamazooind.com/products/combination-disc-sanders/',
        # 'https://kalamazooind.com/products/disc-sanders/',
        # 'https://kalamazooind.com/products/dust-collectors/',
        # 'https://kalamazooind.com/products/abrasive-mitre-chop-saws/',
        # 'https://kalamazooind.com/products/non-ferrous-saws/',
        # 'https://kalamazooind.com/products/5c-collet-fixtures/',
        # 'https://kalamazooind.com/products/vibratory-finisher/',
        # 'https://kalamazooind.com/specialty-equipment-custom-made-for-your-application/',
        'https://kalamazooind.com/products/accessories/',

    ]

    # Read url from file to compare url
    try:
        compare_product_url = ReadUrlFromFile()
    except FileNotFoundError:
        compare_product_url = ''
        print('file not found')

    # Read url one by one using list
    i = 0
    for N0, product_url in enumerate(url_list[i:], start=i):
        print("Product --", N0, product_url)


        # compare url in already exist file
        if product_url in compare_product_url:
            print(f"Skipped this {product_url} Url Because It Is Already Done")
            continue

        # colling function
        # FetchProductUrl()
        driver = ReadChromeDriver(product_url)
        FetchProductUrl(driver)

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
