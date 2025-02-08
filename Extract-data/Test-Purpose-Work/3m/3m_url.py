import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

my_url_list = [
    'https://www.3m.com/3M/en_US/p/c/abrasives/',
    'https://www.3m.com/3M/en_US/p/c/adhesives/',
    'https://www.3m.com/3M/en_US/p/c/advanced-materials/',
    'https://www.3m.com/3M/en_US/p/c/automotive-parts-hardware/',
    'https://www.3m.com/3M/en_US/p/c/building-materials/',
    'https://www.3m.com/3M/en_US/p/c/cleaning-supplies/',
    'https://www.3m.com/3M/en_US/p/c/coatings/',
    'https://www.3m.com/3M/en_US/p/c/communications/',
    'https://www.3m.com/3M/en_US/p/c/compounds-polishes/',
    'https://www.3m.com/3M/en_US/p/c/dental-orthodontics/',
    'https://www.3m.com/3M/en_US/p/c/electrical/',
    'https://www.3m.com/3M/en_US/p/c/electronics-components/',
    'https://www.3m.com/3M/en_US/p/c/filtration-separation/',
    'https://www.3m.com/3M/en_US/p/c/home/',
    'https://www.3m.com/3M/en_US/p/c/insulation/',
    'https://www.3m.com/3M/en_US/p/c/lab-supplies-testing/',
    'https://www.3m.com/3M/en_US/p/c/labels/',
    'https://www.3m.com/3M/en_US/p/c/lubricants/',
    'https://www.3m.com/3M/en_US/p/c/medical/',
    'https://www.3m.com/3M/en_US/p/c/office-supplies/',
    'https://www.3m.com/3M/en_US/p/c/ppe/',
    'https://www.3m.com/3M/en_US/p/c/signage-marking/',
    'https://www.3m.com/3M/en_US/p/c/tapes/',
    'https://www.3m.com/3M/en_US/p/c/tools-equipment/',
    'https://www.3m.com/3M/en_US/p/c/films-sheeting/graphic/',
]


def Extract_product_url():
    product_urls = []
    start_url = 20
    for i, url in enumerate(my_url_list[start_url:21], start=start_url):
        driver.get(url)
        time.sleep(2)
        print(f"Scraping URL {i}: {url}")

        # Extract product URLs
        for href_tag in driver.find_elements(By.CSS_SELECTOR, "a.mds-link"):
            product_url = href_tag.get_attribute('href')
            print(product_url)
            product_urls.append(product_url)

        try:
            click_to_check_box = driver.find_element(By.CSS_SELECTOR, "[aria-label='dismiss cookie message']")
            click_to_check_box.click()
            time.sleep(3)
        except (ElementNotInteractableException, NoSuchElementException, TimeoutException):
            print('No cookie message to dismiss')

        while True:
            try:
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                time.sleep(1)
                driver.execute_script("window.scrollBy(0, -200);")
                time.sleep(2)
                driver.find_element(By.CSS_SELECTOR, "div.sps2-gallery_showMore button").click()
                time.sleep(2)

                # Extract product URLs
                for href_tag in driver.find_elements(By.CSS_SELECTOR, "a.mds-link"):
                    product_url = href_tag.get_attribute('href')
                    product_urls.append(product_url)
                    print(product_url)
            except NoSuchElementException:
                break

        df = pd.DataFrame(product_urls, columns=['URL'])
        df.to_csv('3m_url_list.csv', mode='a+', index=False)


Extract_product_url()
