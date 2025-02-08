import time
from selenium import webdriver
import pandas as pd
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

base_url = 'https://www.fabory.com/en/'


product_urls = []


def get_url(url):
    driver.get(url)
    time.sleep(1)
    try:
        click_to_accept = driver.find_element(By.CSS_SELECTOR,"button#onetrust-accept-btn-handler")
        click_to_accept.click()
        time.sleep(3)
    except NoSuchElementException:
        print("elements not found to accept")

    try:
        click_cross = driver.find_elements(By.CSS_SELECTOR, "button.close")[-1]
        click_cross.click()
        time.sleep(1)
    except Exception as e:
        print(f"{e}")

    try:
        click_to_all_variant = driver.find_element(By.CSS_SELECTOR, "div.product-box.product-variant a")
        click_to_all_variant.click()
        time.sleep(2)
    except Exception as e:
        print(f"{e}")

    for href_tag in driver.find_elements(By.CSS_SELECTOR, "a.js-google-analytics-product-click-event"):
        product_url = href_tag.get_attribute('href')
        print(product_url)
        if 'com/group' not in product_url:
            product_urls.append(product_url)

    while True:
        try:
            click_pagination = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Next'] span")
            click_pagination.click()
            time.sleep(2)

            for href_tag in driver.find_elements(By.CSS_SELECTOR, "a.js-google-analytics-product-click-event"):
                product_url = href_tag.get_attribute('href')
                print(product_url)
                if 'com/group' not in product_url:
                    product_urls.append(product_url)

        except NoSuchElementException:
            print("No more pages to paginate.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break




    df = pd.DataFrame(product_urls, columns=['URL'])
    print(df)
    df.to_csv('fabory_url.csv', mode='w', index=False)



# get_url('https://www.fabory.com/en/spacer%2c-internal-and-external-thread-free-cutting-steel-zinc-plated/p/11398?q=%3Amost-popular')



file_path = r"P:\Web-scrapings\A-MONTH-2024\Sep\Fabory-products\product\read_url.csv"
read_file = pd.read_csv(file_path)['URL']
start_url = 1500
for url_count, url in enumerate(read_file[start_url:], start=start_url):
    print(f'Processing URL: {url} url count: {url_count}')
    get_url(url)
