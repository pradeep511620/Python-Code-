import csv
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options

opts = Options()
# Set headless mode
opts.headless = True

save_files = open("huco-all-data.csv", 'a', encoding='utf-8')

with open('product-url-huco-main.csv', 'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def getDriveUrls(url):
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    time.sleep(4)
    return driver


def product_detail(url, driver):
    part_n = []
    price_d = []

    driver.execute_script('return document.querySelector("#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")').click()
    time.sleep(2)

    try:
        l3_Name = driver.find_element(By.XPATH, "(//div[@class='component-content'])//nav//ol").text.strip().replace('\n', '')
        print('l3_Name....', l3_Name)
    except AttributeError:
        l3_Name = ''
        print('Not')

    try:
        product_title = driver.find_element(By.XPATH, "//div[@class='product-name']").text.strip()
        print('Product_title...',product_title)
    except AttributeError:
        product_title = ''
        print("Not")

    price = driver.find_element(By.XPATH, "//div[@class='price-only']").text.strip()
    price_d.append(price)
    print('Price....', price_d)

    try:
        part = driver.find_element(By.ID, "fullProductIdWithBoreConfig").text.strip()
        part_n.append(part)
        print('Part....', part_n)
    except NoSuchElementException:
        print('Not')

    image = []
    for img in driver.find_elements(By.XPATH, "//div[@class='product-images']//a"):
        image.append(img.get_attribute('href'))
    print("Images....", image)
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
        for pdf in driver.find_elements(By.XPATH, "//div[@class='product-literature component-content']//a"):
            datasheet.append(pdf.get_attribute('href'))
        print("Pdf....", datasheet)
    except AttributeError:
        datasheet = ''
        print("Not")

    try:

        option = driver.find_element(By.ID, "boreCode1Select").find_elements(By.TAG_NAME, "option")
        print("option1", len(option))
        for opt in option:
            opt.click()
            time.sleep(3)
            options = opt.text

            option2 = driver.find_element(By.ID, "boreCode2Select").find_elements(By.TAG_NAME, "option")
            for opt2 in option2:
                opt2.click()
                time.sleep(2)
                options2 = opt2.text

                price = driver.find_element(By.XPATH, "//div[@class='price-only']").text.strip()
                price_d.append(price)

                try:
                    part = driver.find_element(By.ID, "fullProductIdWithBoreConfig").text.strip()
                    part_n.append(part)
                except NoSuchElementException:
                    print("Unable to locate element")
    except:
        pass

    print('Price....', price_d)
    print('Part....', part_n)
    #

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
        "Price(usd)": price_d,
        # "Cross_Reference": Cross_Reference,
        "Url": url,

    }]
    print(row)

    data_save(row, mylist)
    return product_title


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(url, soup, product_title):
    try:
        i = 0
        name = []
        value = []
        table = soup.findAll(class_='product-techspecs component-content')
        for td in table:
            tds = td.text.strip().replace('\n', ':').replace(':::', '\n').split('\n')
            tabs = tds
            for t in tabs:
                alldata = t.split(':')
                td1 = alldata[0]
                td2 = alldata[1]
                name.append(td1.strip())
                value.append(td2.strip())
        for a, b in zip(name, value):
            pass
            # print(a, "......", b)
            save = open('huco-all-table.txt', 'a+', encoding='utf-8')
            save.write('\n' + url + "\t" + a + "\t" + b + "\t" + product_title)
    except AttributeError:
        print('Not Found')


def main():
    for csv_link in range(7353, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        driver = getDriveUrls(url)
        product_title = product_detail(url, driver)
        get_specs(url, soup, product_title)


main()
