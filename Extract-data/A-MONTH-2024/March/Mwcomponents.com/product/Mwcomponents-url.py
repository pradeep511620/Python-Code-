import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
ress = requests.session()

url_list = [
    'https://www.mwcomponents.com/shop/spacers-swage-smooth-shank-standard-asm?page=220',
    'https://www.mwcomponents.com/shop/spacers-swage-smooth-shank-standard-asm?page=221',
    'https://www.mwcomponents.com/shop/spacers-swage-smooth-shank-standard-asm?page=222',

]
for url in url_list:
    driver.get(url)
    time.sleep(3)
    print(url)

    for product_href in driver.find_elements(By.XPATH, "//*[@class='text-14']//a"):
        product_url = product_href.get_attribute('href')
        # print("'" + product_url + "',")
        with open('urlss1.txt', 'a+', encoding='utf-8') as file_save:
            file_save.write(f"{product_url}\n")


    # s_num = driver.find_element(By.XPATH, "//span[@class='text-sm']").text.strip().split(" ")[-1].replace(",", "")
    # print(s_num)
    # length = round(int(s_num) / 500 + 1)
    # print(length)
    # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    # time.sleep(2)
    # driver.execute_script(f"window.scrollBy(0, {-800});")
    # time.sleep(2)
    #
    # for i in range(1, length):
    #     print(i)
    #     try:
    #         driver.find_element(By.XPATH, "//*[@aria-label='Next page']").click()
    #         time.sleep(4)
    #         driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    #         time.sleep(1)
    #         driver.execute_script(f"window.scrollBy(0, {-800});")
    #         time.sleep(1)
    #     except NoSuchElementException:
    #         print("No click Found")
    #     #
    #     for product_href in driver.find_elements(By.XPATH, "//*[@class='text-14']//a"):
    #         product_url = product_href.get_attribute('href')
    #         # print("'" + product_url + "',")
    #         with open('urlss1.txt', 'a+', encoding='utf-8') as file_save:
    #             file_save.write(f"{product_url}\n")
