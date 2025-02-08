import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

driver = webdriver.Chrome()
driver.maximize_window()

for pagination in range(200, 300):
    url = f'https://superiormachinetools.com/shop-all/?limit=96&page={pagination}'
    driver.get(url)
    time.sleep(2)
    print(".....", driver.current_url)
    for url_tag in driver.find_elements(By.CSS_SELECTOR, "h4.card-title a"):
        product_url = url_tag.get_attribute('href')
        print(product_url)
        with open('superiormachinetools1.csv', 'a+', encoding='utf') as url_save:
            url_save.write(f"{product_url}\n")
