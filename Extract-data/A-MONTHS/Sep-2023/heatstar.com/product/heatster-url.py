import csv
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()


with open("C:/Users/PK/Desktop/web-scrapping/Sep-2023/heatstar.com/url/heatstar-url.csv", 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)
    print(csv_length)

for csv_link in range(0, csv_length):
    url = csv_list[csv_link][0]
    print("Product-Length...", csv_link)
    print("Urls......", url)
    browser.get(url)
    time.sleep(1)


    try:
        browser.execute_script('return document.querySelector("#btn-cookie-allow")').click()
    except ElementNotInteractableException:
        print('Message: element not interactable')

    for product in browser.find_elements(By.XPATH, "//div[@class='column main']//div[1]//a"):
        product_url = product.get_attribute('href')
        if '#' not in product_url:
            print(product_url)
            save = open('product-url-heatstar.txt', 'a+', encoding='utf-8')
            save.write('\n' + product_url)
    print('save url in file 1')
    try:
        browser.find_element(By.XPATH, '(//*[@class="action  next"])[2]').click()
        time.sleep(1)
    except NoSuchElementException:
        print('not next to go')

    for product in browser.find_elements(By.XPATH, "//div[@class='column main']//div[1]//a"):
        product_url = product.get_attribute('href')
        if '#' not in product_url:
            print(product_url)
            save = open('product-url-heatstar.txt', 'a+', encoding='utf-8')
            save.write('\n' + product_url)
    print('save url in file 2')


#
#     try:
#         browser.execute_script('return document.querySelector("#regionDropdownModal > div > div.modal-body > div > div:nth-child(1) > div.col.col-sm-4.pointer")').click()
#         print('click')
#     except AttributeError:
#         print('Not click pop up')
#
#     browser.find_element(By.XPATH, "//input[@id='theSearch']").send_keys(url)
#     time.sleep(1)
#
#     browser.find_element(By.XPATH, "//button[@jason='desktop']//*[name()='svg']").click()
#     time.sleep(1)
#     get_current_url = browser.current_url
#     print('get_current_url.....1', get_current_url)
#     save = open('enerpac_product_url.txt', 'a+', encoding='utf-8')
#     save.write('\n' + get_current_url)
#
#     try:    # click product page
#         browser.find_element(By.XPATH, "//div[@class='row EnerpacDynamicProductList__Table EnerpacDynamicProductList__Table--Desktop ']//img[1]").click()
#         time.sleep(1)
#         get_current_url = browser.current_url
#         print('get_current_url.....2', get_current_url)
#         save = open('enerpac_product_url.txt', 'a+', encoding='utf-8')
#         save.write('\n' + get_current_url)
#     except:
#         print("not click product page")
