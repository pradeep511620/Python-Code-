import os
import time

import pandas as pd
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def ReadChromeDriver(product_url):
    headless_mode = True
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    if headless_mode:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(3)

    return driver


def ReadSoupUrl(product_url):
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    ress = requests.get(product_url, headers=header)
    soup = BeautifulSoup(ress.content, "html.parser")
    return soup







def FetchProductUrl(driver):
    """
    try:
        for product_tag in soup.find(class_="views-table cols-10 table table-hover table-striped").find_all("a"):
            product_url_main = product_tag.get('href')
            product_tag_url = "https://www.knapeandvogt.com/" + product_url_main
            print("'" + product_tag_url + "',")
            with open("prods.txt", 'a+', encoding="utf-8") as file_save:
                    file_save.write(f"{product_tag_url}\n")
        print('')
    except AttributeError:
        print("NN")
    """


    # try:
    #     option = driver.find_element(By.CLASS_NAME, "plp-pageRange").find_elements(By.TAG_NAME, "option")
    # except NoSuchElementException:
    #     option = ''
    # for opn in option:
    #     clk = opn.text.strip()
    #     if clk == "200":
    #         opn.click()
    #         time.sleep(4)
    #         break


    for product in driver.find_elements(By.XPATH, "//div[@id='product-dynamicID-367984']//a"):
        product_url_main = product.get_attribute('href')
        if "#" not in product_url_main:
            print("'"+product_url_main+"',")
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
    # file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Knapeandvogt.com/url/Product-url.csv"
    # url_lists = pd.read_csv(file_path)["URL"]

    url_list = [

        'https://www.kwikool.com/overviewaircoolediceberg-series/',
        'https://www.kwikool.com/o-ac-kbio-series/',
        'https://www.kwikool.com/overview-aircooled-kpacii-series/',
        'https://www.kwikool.com/overview-aircooled-kpo-series/',
        'https://www.kwikool.com/overview-aircooled-php-portable-heat-pump/',
        'https://www.kwikool.com/o-ac-kbio-series/',
        'https://www.kwikool.com/overviewwatercoolediceberg-series/',
        'https://www.kwikool.com/o-ap-bioair/',
        'https://www.kwikool.com/115v-60hz-air-cooled/',
        'https://www.kwikool.com/bpr-115v-60hz-water-cooled/',
        'https://www.kwikool.com/bpr-115v-60hz-heat-pump/',
        'https://www.kwikool.com/bpr-115v-60hz-air-purifier/',
        'https://www.kwikool.com/bpr-460v-60-hz-3o-air-cooled/',
        'https://www.kwikool.com/bpr-460v-60-hz-3o-water-cooled/',
        'https://www.kwikool.com/bt-portable-bioair-series/',
        'https://www.kwikool.com/o-ac-kbio-series/',
        'https://www.kwikool.com/bt-portable-kib-series/',
        'https://www.kwikool.com/bt-portable-kpacii-series/',
        'https://www.kwikool.com/bt-portable-kwib-series-2/',
        'https://www.kwikool.com/bt-heat-pump-php/',
        'https://www.kwikool.com/bt-high-static-kpo-series/',
        'https://www.kwikool.com/bt-high-static-atticmaster/',
        # "https://www.kwikool.com/product-details/kam14/"
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

        # soup = ReadSoupUrl(product_url)
        # FetchProductUrl(soup)

        driver = ReadChromeDriver(product_url)
        try:
            FetchProductUrl(driver)
        except Exception as e:
            print(f"Error processing {product_url}: {e}")
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

        # driver.quit()
    print('Saved Url')


def main():
    ReadFromListUrl()


if __name__ == "__main__":
    main()
