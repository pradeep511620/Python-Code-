import os
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc




def ReadChromeDriver(product_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = uc.Chrome()
    # driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(15)
    return driver




def ReadSoupUrl(product_url):
    r = requests.get(product_url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup





def FetchProductUrl(driver):
    for product in driver.find_elements(By.XPATH, "(//div[@class='image'])//a"):
        product_url_main = product.get_attribute('href')
        print(product_url_main)
        with open("product_url.txt", 'a+', encoding="utf-8") as file_save:
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

        'https://www.govets.com/isaac/brands/result/b/benchpro?&page=57',
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
