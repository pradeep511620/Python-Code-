import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

product_urls = []


def get_url(url):
    driver.get(url)
    time.sleep(5)

    # Collect URLs from the initial page
    for href_tag in driver.find_elements(By.CSS_SELECTOR, "#parametricSearchResult div.row a"):
        product_url = href_tag.get_attribute('href')
        if '.html' in product_url:
            product_urls.append(product_url)

    while True:
        try:
            click_to_pagination = driver.find_element(By.CSS_SELECTOR, "li.next-page a")
            click_to_pagination.click()
            time.sleep(2)

            # Collect URLs from the paginated pages
            for href_tag in driver.find_elements(By.CSS_SELECTOR, "#parametricSearchResult div.row a"):
                product_url = href_tag.get_attribute('href')
                if '.html' in product_url:
                    product_urls.append(product_url)
        except:
            print('click not found')
            break
    # Create DataFrame with collected URLs
    df = pd.DataFrame(product_urls, columns=['URL'])
    print(df)
    df.to_csv('product_url.csv', mode='a+', index=False)


# get_url('https://www.onlinecomponents.com/en/productsearch/taxonomy/circuit-protection/overcurrent-protection/circuit-breakers/?manf=eaton+emobility+transportation+%2f+powerstor+%2f+bussmann')



file_path = r"P:\Web-scrapings\A-MONTH-2024\Sep\Onlinecomponents-Brand-Eaton.com\product\product_u.csv"
read_file = pd.read_csv(file_path)['URL']
start_url = 0
for url_count, url in enumerate(read_file[start_url:], start=start_url):
    print(f'Processing URL: {url}')
    get_url(url)
