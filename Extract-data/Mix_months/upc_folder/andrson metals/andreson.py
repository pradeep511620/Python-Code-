import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()
browser.maximize_window()

url = 'https://www.acnc.gov.au/'

browser.get(url)
print("Product_urls", url)
time.sleep(3)
with open('abn.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

for csv_link in range(163, 300):
    url = csv_list[csv_link][0]
    print("Product-Length...", csv_link)
    print("Urls......", url)

    browser.find_element(By.XPATH, "//input[@placeholder='Site search']").send_keys(url)
    time.sleep(3)

    try:
        browser.find_element(By.XPATH, "//button[@class='position-absolute top-50 end-0 translate-middle-y me-lg-2 btn btn-outline-secondary border-0 rounded-circle']//*[name()='svg']").click()
        time.sleep(2)
    except:
        pass
    #
    try:
        browser.find_element(By.XPATH, "//input[@placeholder='Site search']").clear()
        time.sleep(2)
    except:
        pass

    data = browser.find_element(By.XPATH, "//div[@role='alert']").text
    print("something..", data)
