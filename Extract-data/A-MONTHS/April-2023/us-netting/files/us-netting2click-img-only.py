import time
from typing import TextIO

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome()
driver.maximize_window()

mylst = [

    # 'https://www.usnetting.com/all-purpose-netting/knotless-netting/sbn-5100/',
    # 'https://www.usnetting.com/all-purpose-netting/knotless-netting/sbn-14/',
    # 'https://www.usnetting.com/all-purpose-netting/knotless-netting/sbn-2020/',
    'https://www.usnetting.com/all-purpose-netting/knotless-netting/sbn-5045/',
]
l = 0

for url in mylst:
    l += 1
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    driver.get(url)
    time.sleep(2)
    print("Product-url...", l, url)
    description = ''

    meta_title = driver.find_element(By.XPATH, '/html/head/title').get_attribute("innerHTML")
    print("meta_title...", meta_title)
    #
    print("********** Breadcrumb : **********")
    bread = driver.find_element(By.CLASS_NAME, "breadcrumbs").text.replace('\n', '>>')
    print('bread...', bread)
    #
    print("********** Title : **********")
    title = driver.find_element(By.TAG_NAME, 'h1').text.strip()
    print('Title...', title)
# Double click options  =============================== fist Option
    #   Length of First option

    count = driver.find_element(By.XPATH, "//div[@class='option-description js-active radio-img-container border-style']").find_elements(By.TAG_NAME, "img")
    length = len(count)
    l=0
    for ln in count:
        l += 1
        time.sleep(10)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div['+str(l)+']').click()
        time.sleep(2)
    #     # Length of Second option
        color = (driver.find_element(By.XPATH, "//div[@class='option-description js-active radio-img-container colors']").find_elements(By.TAG_NAME, "img"))
        for cl in color:
            cl.click()
            time.sleep(2)



            #   Get Price Here
            # print("********** Price : **********")
            # price = driver.find_element(By.XPATH, "//div[@class=' cargo-netting-product-price']").text.strip()
            # print("Price...", price)
            # #
            # # #   Get Images Here
            # for img in driver.find_element(By.XPATH, "//div[@class='product-photos col-xs-12 col-sm-5']").find_elements(By.TAG_NAME, "img"):
            #     images = img.get_attribute('src')
            #     print("Images...", images)
            #     save_d: TextIO = open("2click-img-only.txt", "a+", encoding="utf-8")
            #     save_d.write("\n" + url + "\t" + meta_title + "\t" + bread + "\t" + title + "\t" + price + "\t" + images)
            # print('data save into images')

    print("********** Description : **********")
    try:
        description = driver.find_element(By.ID, "desc").find_element(By.TAG_NAME, 'p').text.strip()
        print('description...', description)
    except:
        print("Not Found")

#
    print("********** Table : **********")
    name = []
    value = []
    i = 0
    table = soup.find('div', {'id': "specs"}).find("ul").find_all('li')
    for j in table:
        all_data = j.text.split(":")
        name.append(all_data[0].strip())
        value.append(all_data[1].strip())
    for a, b in zip(name, value):
        print(a, "....", b)
    #     save_d: TextIO = open("2click-img-only.txt", "a+", encoding="utf-8")
    #     save_d.write("\n" + url + "\t" + meta_title + "\t" + bread + "\t" + title + "\t" + price + "\t" + images + "\t" + description + "\t" + a + "\t" + b)
    # print('data save into table')




