import time
from selenium import webdriver
import pandas as pd
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

base_url = 'https://www.fabory.com/en/'


product_urls = []


def get_url(url):
    driver.get(url)
    time.sleep(3)
    # try:
    #     click_to_accept = driver.find_element(By.CSS_SELECTOR,"button#onetrust-accept-btn-handler")
    #     click_to_accept.click()
    #     time.sleep(3)
    # except NoSuchElementException:
    #     print("elements not found to accept")
    #
    # try:
    #     click_cross = driver.find_element(By.CSS_SELECTOR, "label.switch")
    #     click_cross.click()
    #     time.sleep(3)
    # except Exception as e:
    #     print(f"{e}")


    for href_tag in driver.find_elements(By.CSS_SELECTOR, "a.subcatcelltextlink"):
        product_url = href_tag.get_attribute('href')
        if product_url:
            product_urls.append(product_url)

    for url in product_urls:
        print(url)
    print(f"Total URLs extracted: {len(product_urls)}")






    df = pd.DataFrame(product_urls, columns=['URL'])
    print(df)
    df.to_csv('smc1.csv', mode='w', index=False)



# get_url('https://www.allvalves.co.uk/products/solenoid-valve.aspx')



file_path = r"P:\Web-scrapings\A-MONTH-2024\Sep\allvalves-Brand-smc-valves\product\smc.csv"
read_file = pd.read_csv(file_path)['URL']
start_url = 0
for url_count, url in enumerate(read_file[start_url:], start=start_url):
    print(f'Processing URL: {url} url count: {url_count}')
    get_url(url)
