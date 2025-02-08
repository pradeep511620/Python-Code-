import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

product_urls = []


def get_url(url):
    driver.get(url)
    time.sleep(2)

    # Collect URLs from the initial page
    for href_tag in driver.find_elements(By.CSS_SELECTOR, "a.plp-itemlink"):
        product_url = href_tag.get_attribute('href')
        print(product_url)
        # if '.html' in product_url:
        product_urls.append(product_url)


    df = pd.DataFrame(product_urls, columns=['URL'])
    print(df)
    df.to_csv('jamco_url.csv', mode='a', header=not pd.io.common.file_exists('jamco_url.csv'), index=False)


# get_url('https://industrialcarts.jamcoproducts.com/')
file_path = r"P:\Web-scrapings\A-MONTH-2024\Aug\Jamco-products.com\product\jamco2.csv"
read_file = pd.read_csv(file_path)['URL']

# Process each URL one by one
start_url = 2
for url_count, url in enumerate(read_file[start_url:], start=start_url):
    print(f'Processing URL: {url} url count: {url_count}')
    get_url(url)
