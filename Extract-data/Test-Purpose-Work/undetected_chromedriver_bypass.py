import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()


driver = uc.Chrome()
driver.maximize_window()
def Get_url():
    for i in range(1, 10):
        url = f'https://www.webstaurantstore.com/search/t%26s.html?page={i}'
        driver.get(url)
        time.sleep(10)

        for href_tag in driver.find_elements(By.CSS_SELECTOR, "#product_listing a.block"):
            product_url = href_tag.get_attribute('href')
            print(product_url)
            with open('ts_brass.txt', 'a+', encoding='utf-8') as url_save:
                url_save.write(f"{product_url}\n")

    driver.quit()



Get_url()




