import time
import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
ress = requests.session()
base_url = 'https://catalog.taperline.com/'
mylist = [




    'https://www.klingspor.com/Product-Catalog/Specialty-Abrasives-Accessory/Unitized-Disc-Wheel/Depressed-Center-Unitized-Disc-3100532162',

]
url_links = []
for url in mylist:
    driver.get(url)
    time.sleep(2)
    print(url)

    try:
        for product in driver.find_elements(By.XPATH, "//div[@class='category-image-wrapper']//a"):
            get_href_tag = product.get_attribute('href')
            url_link = "'" + get_href_tag + "',"
            print(url_link)
            with open('Klingspor_catalog.txt', 'a+', encoding='utf-8') as file_save:
                file_save.write(f"{url_link}\n")
        print("save all data in file")

    except:
        pass

    try:
        option = driver.find_element(By.XPATH, "(//div[@id='dvMain']//select)[1]").find_elements(By.TAG_NAME, "option")
    except NoSuchElementException:
        option = ''
    for opn in option:
        clk = opn.text.strip()
        if clk == "50":
            opn.click()
            time.sleep(2)
            break
    try:
        for product in driver.find_elements(By.XPATH, "//*[@id='product-image-container']//a"):
            get_href_tag = product.get_attribute('href')
            with open('save_url1.txt', 'a+', encoding='utf-8') as file_save:
                file_save.write(f"{get_href_tag}\n")
            print(get_href_tag)
            url_links.append(get_href_tag)
    except NoSuchElementException:
        print("nn")

    try:
        length = driver.find_elements(By.XPATH, "//*[@id='dvpagerTopH']//a")[-1].text.strip()
    except IndexError:
        length = ''
    try:
        for i in range(2, int(length) + 1):
            print(i)
            driver.find_element(By.XPATH, f"(//div[@id='dvpagerTopH']//a)[{i}]").click()
            time.sleep(5)

            for product in driver.find_elements(By.XPATH, "//*[@id='product-image-container']//a"):
                get_href_tag = product.get_attribute('href')
                with open('save_url1.txt', 'a+', encoding='utf-8') as file_save:
                    file_save.write(f"{get_href_tag}\n")
                url_links.append(get_href_tag)
        # print(url_links)
    except:
        pass

for save_url in url_links:
    with open('save_url.txt', 'a+', encoding='utf-8') as file_save:
        file_save.write(f"{save_url}\n")
print('save url')
