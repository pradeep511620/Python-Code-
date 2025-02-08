
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

mylist = [
    'https://www.newstripe.com/product/aerosol-can-recycling-box/'
]

for url in mylist:
    driver.get(url)
    time.sleep(4)
    print(url)

    select_option = driver.find_elements(By.CSS_SELECTOR, ".value select option")
    select_option_list = []
    for li in select_option:
        option_get_unique_value = li.get_attribute('value')  # get value to unique id
        select_option_list.append(option_get_unique_value)
    del select_option_list[0]
    select_option_list_del = select_option_list
    for unique_value in select_option_list_del:
        click_select_item = driver.find_element(By.XPATH, f"//option[@value='{unique_value}']")    # here is click one by one
        click_select_item.click()
        time.sleep(2)
