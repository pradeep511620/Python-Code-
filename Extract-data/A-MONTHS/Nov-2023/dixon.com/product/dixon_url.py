
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import undetected_chromedriver as uc


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
# driver = uc.Chrome()

driver.maximize_window()


website_url = 'https://shop.tipcotech.com/5523/manufacturer/dixon'
driver.get(website_url)
time.sleep(1)
print("Product_urls", website_url)

url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Nov-2023/dixon.com/url/dixon-mpn-url.csv")['URL']
print(len(url_link))



save = open('product_url_weg.txt', 'a+', encoding='utf-8')



def Get_Url_Details():
    i = 433
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Urls......", url_count, url)


        driver.find_element(By.XPATH, "//input[@id='txtSearch']").send_keys(url)
        time.sleep(3)


        driver.find_element(By.XPATH, "//button[@id='performSearchBtn']").click()
        time.sleep(2)


        driver.find_element(By.XPATH, "//input[@id='txtSearch']").clear()
        time.sleep(1)

        get_current_url = driver.current_url
        print('get_current_url......', get_current_url)
        save.write(f"{get_current_url}\n")



Get_Url_Details()



