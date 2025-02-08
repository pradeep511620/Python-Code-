import csv
import time

from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


# url = 'https://www.aquorwatersystems.com/collections/shop-all'
#
# driver.get(url)
# time.sleep(4)
#
# url_link = driver.find_element(By.ID, "product-grid")
# ur = url_link.find_elements(By.TAG_NAME, "a")
# for product_u in ur:
#     url_links = product_u.get_attribute('href')
#     save = open('aquor-water-system-urls-step3.txt', 'a+', encoding='utf-8')
#     save.write('\n' + "'" + url_links + "',")
with open('aquor-water-system-urls.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

for csv_link in range(15, csv_length):
    url = csv_list[csv_link][0]
    print("Product-Length...", csv_link)
    print("Product-Urls......", url)

    driver.get(url)
    time.sleep(1)
    try:
        option = driver.find_element(By.ID, "Option-template--16680690974970__main-0").find_elements(By.TAG_NAME, "option")
        for op in option:
            op.click()
            time.sleep(1)
            opt = op.text
            print(opt)
            get_url = driver.current_url
            print('current..', get_url)
            save = open('urlss.txt', 'a+', encoding='utf-8')
            save.write("\n" + get_url)
    except NoSuchElementException:
        print("Unable to locate element")
