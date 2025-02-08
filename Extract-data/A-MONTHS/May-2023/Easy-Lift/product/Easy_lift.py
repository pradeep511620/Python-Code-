import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

import csv
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

save_files = open("easy-lift-all-data.csv", 'a', encoding='utf-8')

with open('easy-lift.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def getDriveUrls(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(4)
    return driver
#   -------------------------------------------------------------------------------------------------------------------


def product_detail(url,  driver):
    # try:
    #     l3_Name = driver.find_element(By.XPATH, "//body/div[@class='topbg']/div[@id='container']/div[@id='mainContent']/div[@class='leftpan cf']/div[@class='contentbg']/div[1]").text
    #     print('l3_Name...', l3_Name)
    # except NoSuchElementException:
    #     l3_Name = ''
    #     print()

    try:
        Product_Title = driver.find_element(By.XPATH, "//span[@itemprop='description']//h2").text
        print("Product_Title...", Product_Title)
    except NoSuchElementException:
        Product_Title = ''
#
#     try:
#         description = driver.find_element(By.XPATH, "//span[@itemprop='description']//p[1]").text.strip()
#         print('description...', description)
#     except NoSuchElementException:
#         description = ''
#
#     image = []
#     for img in driver.find_elements(By.XPATH, "//div[@class='products-details-thumb']//a"):
#         image.append(img.get_attribute('href'))
#     print('Images..', image)
#     try:
#         imgs = image[0]
#         print(imgs)
#     except IndexError:
#         imgs = ''
#         print('List out of index')
#     try:
#         imgs1 = image[1]
#         print(imgs1)
#     except IndexError:
#         imgs1 = ''
#         print('List out of index')
#     try:
#         imgs2 = image[2]
#         print(imgs2)
#     except IndexError:
#         imgs2 = ''
#         print('List out of index')
#     try:
#         imgs3 = image[3]
#         print(imgs3)
#     except IndexError:
#         imgs3 = ''
#         print('List out of index')
#     try:
#         imgs4 = image[4]
#         print(imgs4)
#     except IndexError:
#         imgs4 = ''
#         print('List out of index')
#
#     video = []
#     try:
#         driver.find_element(By.XPATH, "//ul[@class='TabbedPanelsTabGroup']//li[3]").click()
#     except NoSuchElementException:
#         pass
#     for vdo in driver.find_elements(By.XPATH, "//div[@class='TabbedPanelsContent TabbedPanelsContentVisible']//a"):
#         # print(vdo.get_attribute('href'))
#         video.append(vdo.get_attribute('href'))
#     print('Video..', video)
#
#     try:
#         driver.find_element(By.XPATH, "//ul[@class='TabbedPanelsTabGroup']//li[1]").click()
#     except NoSuchElementException:
#         pass
#     time.sleep(1)
#     features = []
#     for feature in driver.find_elements(By.XPATH, "//div[@class='TabbedPanelsContent TabbedPanelsContentVisible']//p"):
#         features.append(feature.text.strip())
#     print('feature...', features)
#
#     datasheet = []
#     for data in driver.find_elements(By.XPATH, "//div[@class='download-brochurebox']//a"):
#         datasheet.append(data.get_attribute('href'))
#     print('datasheet...', datasheet)
#
#
#
#
#
# #
#
#     # ------------------------------------------------------------------------------------------------------------------
#     mylist = [
#         "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
#         "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
#         "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
#         "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
#         "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
#         "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
#     ]
#
#     row = [{
#         # "Mpn": mpn,
#         # "Grainger_Sku": sku,
#         "L3_Name": l3_Name,
#         "Product_title": Product_Title,
#         "Image_URL_1": imgs,
#         "Image_URL_2": imgs1,
#         "Image_URL_3": imgs2,
#         "Image_URL_4": imgs3,
#         "Image_URL_5": imgs4,
#         "Product_Detail": description,
#         "Features": features,
#         # "Accessories": related_url,
#         "Datasheet": datasheet,
#         # "item_ID": item,
#         # "Uses": uses_d,
#         "Video_Url": video,
#         # "Quantity": stock,
#         # "Price(usd)": price,
#         # "Cross_Reference": Cross_Reference,
#         "Url": url,
#
#     }]
#
#     # data_save(row, mylist)
    return Product_Title
#
#
# def data_save(row, cols):
#     # using save data into dataframe
#     df = pd.DataFrame(row, columns=cols)
#     print(df)
#     df.to_csv(save_files, header=False, index=False, lineterminator='\n')
#     print('save data into csv files')


def get_specs(url, driver, Product_Title):
    try:
        fu = []
        driver.find_element(By.XPATH, "//ul[@class='TabbedPanelsTabGroup']//li[2]").click()
        f = len(
            driver.find_elements(By.XPATH, "//div[@class='TabbedPanelsContent TabbedPanelsContentVisible']//table//tr"))
        for table in driver.find_elements(By.XPATH, "//div[@class='TabbedPanelsContent TabbedPanelsContentVisible']//table//tr")[3:f]:
            su = []
            for tata in table.find_elements(By.TAG_NAME, 'td'):
                su.append(tata.text)
            fu.append(su)
        print(fu)
        for j in fu:
            save = open('tab.txt', 'a+', encoding="utf-8")
            save.write('\n' + url + "\t" + Product_Title + "\t".join(j))
        print('save data')
    except AttributeError:
        print('Attribute error')
        print('table Not Found')
    table_data = driver.find_elements(By.XPATH, "//div[@class='TabbedPanelsContent TabbedPanelsContentVisible']//p")
    for d in table_data:
        print(d.text)


def main():
    for csv_link in range(8, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        # driver = get_url(url)
        driver = getDriveUrls(url)
        Product_Title = product_detail(url, driver)
        get_specs(url, driver, Product_Title)


main()
