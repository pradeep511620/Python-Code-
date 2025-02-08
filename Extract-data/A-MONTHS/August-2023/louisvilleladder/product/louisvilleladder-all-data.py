import csv
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

opts = Options()
# Set headless mode
opts.headless = True

save_files = open("huco-all-data.csv", 'a', encoding='utf-8')

with open("C:/Users/PK/Desktop/Web-Scrapping/August-2023/louisvilleladder/urls/louisvillerladder-urls.csv", 'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def getDriveUrls(url):
    driver = webdriver.Chrome(options=opts)
    # driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    time.sleep(1)
    return driver


def product_detail(url, driver):

    driver.execute_script('return document.querySelector("#bs-gdpr-cookies-modal > div > div > div.modal-footer")').click()

    # try:
    #     l3_Name = driver.find_element(By.XPATH, "//div[@class='component-content'])//nav//ol").text.strip().replace('\n', '')
    #     print('l3_Name....', l3_Name)
    # except AttributeError:
    #     l3_Name = ''
    #     print('Not')

    try:
        product_title = driver.find_element(By.XPATH, "//p[@class='text-uppercase text-bold text-orange']").text.strip()
        print('Product_title...', product_title)
    except AttributeError:
        product_title = ''
        print("Not")
    #
    try:
        part = driver.find_element(By.XPATH, "//div[@class='product-detail-description']//p[4]").text.strip()
        print('Part....', part)
    except NoSuchElementException:
        part = ''
        print('Part Not..')

    try:
        series = driver.find_element(By.XPATH, "//div[@class='product-detail-description']//p[1]").text.strip()
        print('series....', series)
    except NoSuchElementException:
        series = ''
        print('Part Not..')

    image = []
    for img in driver.find_elements(By.XPATH, "//div[@id='product-detail-carousel']//img"):
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
        descriptions = driver.find_element(By.XPATH, "(//div[@class='product-detail-description'])//p[6]").text.strip().replace('\n', '')
        print("description....", descriptions)
    except AttributeError:
        descriptions = ''
        print("Not")


    element = driver.find_element(By.XPATH, "//*[@class='product-detail-description']//ul[1]//li")
    # Scroll to the element using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", element)

    try:
        feature_d = []
        for feature in driver.find_elements(By.XPATH, "//*[@class='product-detail-description']//ul[1]//li"):
            feature_d.append(feature.text.replace('\n', ''))
        print("feature....", feature_d)
    except AttributeError:
        feature_d = ''
        print("Not")

    try:
        datasheet = []
        for pdf in driver.find_elements(By.XPATH, "//li[@class='resources']//a"):
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
        "Mpn": part,
        # "Grainger_Sku": sku,
        # "L3_Name": l3_Name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": descriptions,
        "Features": feature_d,
        # "Accessories": related_url,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price_d,
        "Cross_Reference": series,
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


def get_specs(url, soup, product_title):
    pass
    # name = []
    # value = []
    # table = soup.find('div', {"id": "productSpecs"}).find_all('li')
    # for td in table:
    #     spl = td.text
    #     spls = spl.split(': ')
    #     name.append(spls[0])
    #     value.append(spls[1:])
    # for a, b in zip(name, value):
    #     print(a, "......", b)
    #     save = open('lousivilleladder-all-table.txt', 'a+', encoding='utf-8')
    #     save.write('\n' + url + "\t" + str(a) + "\t" + str(b) + "\t" + product_title)



def main():
    for csv_link in range(335, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        driver = getDriveUrls(url)
        product_title = product_detail(url, driver)
        get_specs(url, soup, product_title)


main()
