import time
from selenium import webdriver
from selenium.common import JavascriptException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://www.weg.net/catalog/weg/US/en/search?text=weg'
driver.get(url)
time.sleep(2)
for i in range(0, 10):
    driver.find_element(By.CSS_SELECTOR, ".next").click()
    time.sleep(3)
    print('click')
    print(".....", driver.current_url)

    for product_cate in driver.find_elements(By.CSS_SELECTOR, ".table.xtt-table.tablesaw.table-row-height  tbody tr a"):
        product_url = product_cate.get_attribute('href')
        print(product_url)
        with open('weg_url.txt', 'a+', encoding='utf-8') as file_save:
            file_save.write(f"{product_url}\n")
