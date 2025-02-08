import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.maximize_window()

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['pageLoadStrategy'] = 'none'


url = 'https://s5.raptorsupplies.com.au/login'

driver.get(url)

time.sleep(2)


driver.find_element(By.CSS_SELECTOR, "[name='login[username]']").send_keys('tusharsharma@raptorsupplies.com')
time.sleep(1)
print('input')

driver.find_element(By.CSS_SELECTOR, "[name='login[password]']").send_keys('Test!234')
time.sleep(2)
print('pass')

sign_click = driver.find_element(By.XPATH, "(//*[@id='send2'])[1]")
sign_click.click()
time.sleep(3)
print('click to sign button')

driver.find_element(By.XPATH, "//*[@class='header_changePassword']").click()
time.sleep(3)
print('click to change password')

driver.find_element(By.XPATH, "(//*[@class='fieldset password']//input)[2]").send_keys('Test!234')
time.sleep(1)
print('Current password')
driver.find_element(By.XPATH, "(//*[@class='fieldset password']//input)[3]").send_keys('Test!234')
time.sleep(1)
print('New password')
driver.find_element(By.XPATH, "(//*[@class='fieldset password']//input)[4]").send_keys('Test!234')
time.sleep(1)
print('confirm password')

save = driver.find_element(By.XPATH, "//*[@class='action save save-address']")
save.click()
driver.set_page_load_timeout(5)

try:
    page_source = driver.page_source
    with open('tusar.txt', 'a+', encoding='utf-8') as file_save:
        file_save.write(f"{page_source}\n")
except TimeoutException:
    page_source = driver.page_source
    with open('tusar.txt', 'a+', encoding='utf-8') as file_save:
        file_save.write(f"{page_source}\n")

print(page_source)


