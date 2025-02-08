import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.maximize_window()

file_path = "C:/Users/PK/Desktop/web-scrapping/Test-Purpose-Work/dixon.csv"
url_list = pd.read_csv(file_path)['URL']
save_file = open('dixonhh.txt', "a+", encoding='utf-8')


def scrape_url(url):
    try:
        driver.get(url)
        time.sleep(2)
        print("Product - url : -----", url)
        for product_url in driver.find_elements(By.XPATH, "//div[@id='snize-search-results-grid-mode']//li//a"):
            product_url_links = product_url.get_attribute('href')
            save_file.write(f'{product_url_links}\n')
    except Exception as e:
        print(f"Error occurred while processing {url}: {e}")


with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(scrape_url, url_list)

save_file.close()
