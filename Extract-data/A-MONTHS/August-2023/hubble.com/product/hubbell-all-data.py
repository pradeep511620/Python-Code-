import csv
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

save_files = open("C:/Users/PK/Desktop/Web-Scrapping/August-2023/hubble.com/data/Hubbell-all-data.csv", 'a', encoding='utf-8')

with open("C:/Users/PK/Desktop/Web-Scrapping/August-2023/hubble.com/urls/product-hubbell-url.csv", 'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def getDriveUrls(url):
    driver = webdriver.Chrome(options=opts)
    # driver = webdriver.Chrome()
    # driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    return driver


def product_detail(url, driver):
    part_n = []

    try:
        driver.find_element(By.ID, "onetrust-close-btn-container").click()
    except NoSuchElementException:
        print(' Unable to locate element')


    try:
        l3_Name = driver.find_element(By.XPATH, "//ol[@class='breadcrumb']").text.strip().replace('\n', '')
        print('l3_Name....', l3_Name)
    except AttributeError:
        l3_Name = ''
        print('Not')

    try:
        product_title = driver.find_element(By.XPATH, "//div[@class='h1 product-name hidden-xs']").text.strip()
        print('Product_title...',product_title)
    except AttributeError:
        product_title = ''
        print("Not")
    except NoSuchElementException:
        product_title = ''
        pass


    try:
        part = driver.find_element(By.XPATH, "//div[@class='product-collection-catalog clearfix']//span[2]").text.strip()
        part_n.append("rp_"+part)
        print('Part....', part_n)
    except NoSuchElementException:
        print('Not')

    image = []
    for img in driver.find_elements(By.XPATH, "//div[@id='pdp-image-panel']//img"):
        image.append(img.get_attribute('src'))
    # print("Images....", image)
    try:
        imgs = image[0]
        print(imgs)
    except IndexError:
        imgs = ''
        print('List out of index')
    try:
        imgs1 = image[1]
        print(imgs1)
    except IndexError:
        imgs1 = ''
        print('List out of index')
    try:
        imgs2 = image[2]
        print(imgs2)
    except IndexError:
        imgs2 = ''
        print('List out of index')
    try:
        imgs3 = image[3]
        print(imgs3)
    except IndexError:
        imgs3 = ''
        print('List out of index')
    try:
        imgs4 = image[4]
        print(imgs4)
    except IndexError:
        imgs4 = ''
        print('List out of index')

    try:
        des = driver.find_element(By.XPATH, "//div[@class='product-description']").text.strip().replace('\n', '')
        print("description....", des)
    except AttributeError:
        des = ''
        print("Not")

    try:
        datasheet = []
        for pdf in driver.find_elements(By.XPATH, "//div[@id='resource-item-groups']//a"):
            datasheet.append(pdf.get_attribute('href'))
        print("Pdf....", datasheet)
    except AttributeError:
        datasheet = ''
        print("Not")




    # ------------------------------------------------------------------------------------------------------------------
    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]

    row = [{
        "Mpn": part_n,
        # "Grainger_Sku": sku,
        "L3_Name": l3_Name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": des,
        # "Features": features,
        # "Accessories": related_url,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price_d,
        # "Cross_Reference": Cross_Reference,
        "Url": url,

    }]

    data_save(row, mylist)
    return product_title


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(url, driver, product_title):

    try:
        driver.execute_script('return document.querySelector("#prod-detail-section > a")').click()
        time.sleep(1)
    except ElementClickInterceptedException:
        print('nnn')
    except AttributeError:
        print('nn')

    try:
        i = 0
        name = []
        value = []
        for table in driver.find_elements(By.XPATH, "//table[@class='table']//tr//td"):
            i = i + 1
            tab = table.text.strip()
            # print(tab)
            # print(i)
            if i % 2 != 0:
                name.append(tab.replace('\n', ""))
            else:
                value.append("rp_"+tab.replace('\n', ''))
        for a, b in zip(name, value):
            print(a, "..........", b)
            save = open("C:/Users/PK/Desktop/Web-Scrapping/August-2023/hubble.com/data/hubbell-all-table.txt", 'a+', encoding='utf-8')
            save.write('\n' + url + "\t" + a + "\t" + b + "\t" + product_title)
    except AttributeError:
        print('Not Found')


def main():
    for csv_link in range(4561, 5000):    # start from 1 to 5000
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        # soup = get_url(url)
        driver = getDriveUrls(url)
        product_title = product_detail(url, driver)
        get_specs(url, driver, product_title)


main()
