import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

# Initialize the Chrome driver
driver = uc.Chrome()
driver.maximize_window()
url = 'https://www.supplyhouse.com/Johnson-Controls'
driver.get(url)
time.sleep(5)
print('current_url.............................', driver.current_url)
while True:
    try:
        load_more_button = driver.find_element(By.CSS_SELECTOR, ".Box-sc-1z9git-0.juIpOK.ProductListingPage__LoadMoreButton-sc-1r2bxzk-6.eyZQUc")
        load_more_button.click()
        time.sleep(10)
    except NoSuchElementException:
        print("No more 'Load More' button found, exiting loop.")
        break
for product_url in driver.find_elements(By.CSS_SELECTOR, ".Box-sc-1z9git-0.lhPYbe.ProductTileName__ProductTileNameLink-sc-1fe0vqu-0.kaGDGU"):
    product_url_href_link = product_url.get_attribute('href')
    print(product_url_href_link)
    with open('jo.txt', 'a+', encoding='utf-8') as file_save:
        file_save.write(f"{product_url_href_link}\n")

driver.quit()

