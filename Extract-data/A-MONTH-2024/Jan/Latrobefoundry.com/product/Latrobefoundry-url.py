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
    use_headless = True
    chrome_options = Options()
    if use_headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(3)

    return driver



def FetchProductUrl(driver):
    for product in driver.find_elements(By.XPATH, "//table[@id='plp-table-filter']//tr//a"):
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

    url_lists = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Globescientific.com/url/Globescientific-product-url.csv")["URL"]

    url_list = [
        "https://fittings.latrobefoundry.com/viewitems/all-categories/all-categories-butt-weld-fittings",
        "https://fittings.latrobefoundry.com/viewitems/all-categories/nipples",
        "https://fittings.latrobefoundry.com/viewitems/flanged-pipe-fittings/flanged-pipe-elbow-45-",
        "https://fittings.latrobefoundry.com/viewitems/flanged-pipe-fittings/flanged-pipe-elbow-90-",
        "https://fittings.latrobefoundry.com/viewitems/flanged-pipe-fittings/flanged-pipe-reducer",
        "https://fittings.latrobefoundry.com/viewitems/flanged-pipe-fittings/flanged-pipe-tee-reducing",
        "https://fittings.latrobefoundry.com/viewitems/flanged-pipe-fittings/flanged-pipe-tee",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/bushings",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/cap",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/cross",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/plug-countersunk-square-head",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/locknut",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/lateral-45-",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/plug-square-head",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/return-bend-180-",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/tee",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/tee-reducing",
        "https://fittings.latrobefoundry.com/viewitems/threaded-pipe-fittings/union",
        "https://fittings.latrobefoundry.com/viewitems/elbows/elbow-45-",
        "https://fittings.latrobefoundry.com/viewitems/elbows/elbow-45-street",
        "https://fittings.latrobefoundry.com/viewitems/elbows/elbow-90-",
        "https://fittings.latrobefoundry.com/viewitems/elbows/elbow-90-reducing",
        "https://fittings.latrobefoundry.com/viewitems/elbows/elbow-90-street",
        "https://fittings.latrobefoundry.com/viewitems/couplings-2/coupling-full",
        "https://fittings.latrobefoundry.com/viewitems/couplings-2/coupling-half",
        "https://fittings.latrobefoundry.com/viewitems/couplings-2/coupling-full-2-x-standard-wall",
        "https://fittings.latrobefoundry.com/viewitems/couplings-2/coupling-reducing-bell",
        "https://fittings.latrobefoundry.com/viewitems/couplings-2/coupling-half-1-1-2-x-standard-wall",
        "https://fittings.latrobefoundry.com/viewitems/couplings-2/coupling-full-1-1-2-x-standard-wall",
        "https://fittings.latrobefoundry.com/viewitems/couplings-2/coupling-reducing-bell",
        "https://fittings.latrobefoundry.com/viewitems/flanges/flange-blind",
        "https://fittings.latrobefoundry.com/viewitems/flanges/flange-floor",
        "https://fittings.latrobefoundry.com/viewitems/flanges/flange-reducing",
        "https://fittings.latrobefoundry.com/viewitems/flanges/flange-slip-on",
        "https://fittings.latrobefoundry.com/viewitems/flanges/flange-weld-neck",
        "https://fittings.latrobefoundry.com/viewitems/flanges/flange-threaded",

    ]

    # Read url from file to compare url
    try:
        compare_product_url = ReadUrlFromFile()
    except FileNotFoundError:
        compare_product_url = ''
        print('file not found')

    # Read url one by one using list
    i = 1
    for N0, product_url in enumerate(url_list[i:], start=i):
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
