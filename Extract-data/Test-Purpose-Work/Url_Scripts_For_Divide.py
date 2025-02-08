import time
# import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.maximize_window()
# file_path = "C:/Users/PK/Desktop/web-scrapping/Test-Purpose-Work/urlsafe.csv"
# url_list = pd.read_csv(file_path)['URL']

url_list = [
    'https://www.dillonsupply.com/Brands/anvil/Catalog/All'

]

counter = 0
for index, url in enumerate(url_list[counter:], start=counter):
    driver.get(url)
    time.sleep(3)
    print('current_url..........', driver.current_url)

    # driver.find_element(By.CSS_SELECTOR, "").click()
    # time.sleep(2)

    try:
        product_url = [href_tag.get_attribute('href') for href_tag in driver.find_elements(By.CSS_SELECTOR, "#parametricSearchResult .browse-results-wrap .result-product a")]
        for url_link in product_url:
            if ".html" in url_link:
                product_url_link = url_link
                print(product_url_link)
                with open('onlinecomponents.txt', 'a+', encoding='utf-8') as url_save:
                    url_save.write(f'\n{product_url_link}')
    except (NoSuchElementException, ValueError, IndexError, Exception) as e:
        print(f"Error{e}")

    try:
        length = round(int(driver.find_element(By.CSS_SELECTOR, ".d-flex.align-items-center.mb-15 b").text.strip()) / 10) + 1
        print(length)
        for i in range(1, length + 1):
            driver.find_element(By.CSS_SELECTOR, 'li.next-page').click()
            time.sleep(2)

            try:
                product_url = [href_tag.get_attribute('href') for href_tag in driver.find_elements(By.CSS_SELECTOR,"#parametricSearchResult .browse-results-wrap .result-product a")]
                for url_link in product_url:
                    if ".html" in url_link:
                        product_url_link = url_link
                        print(product_url_link)
                        with open('onlinecomponents.txt', 'a+', encoding='utf-8') as url_save:
                            url_save.write(f'\n{product_url_link}')
            except (NoSuchElementException, ValueError, IndexError, Exception) as e:
                print(f"Error{e}")

    except (NoSuchElementException, ValueError, IndexError, Exception):
        print('click not found next page')
