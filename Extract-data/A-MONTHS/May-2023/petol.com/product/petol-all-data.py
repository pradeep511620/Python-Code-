import csv
import time
from typing import TextIO

from selenium import webdriver
from selenium .webdriver.common.by import By
import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

save_files = open("petol-all-data.csv", 'a', encoding='utf-8')

with open('petol-urls.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_soup_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def get_driver_url(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver


#   -------------------------------------------------------------------------------------------------------------------
def extract_product_detail(url, soup):
    l3_name = []
    try:
        for k in soup.find('ol', {"class": "breadcrumb"}).find_all('li'):
            l3_name.append(k.text.strip())
        print('l3_name...', l3_name)
    except AttributeError:
        l3_name = ''
        print('Not Found')

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        Product_title = soup.find('div', {"id": "prodDesc"}).find('h1').text.strip()
        print('title...', Product_title)
    except AttributeError:
        Product_title = ''
        print('Not Found')

    #   ---------------------------------------------------------------------------------------------------------------
    image = []
    imgage_url = []
    for img in soup.find('div', {"id": "mainImgBlock"}).find_all('img'):
        images = img.get('src')
        image.append(images)

    img_main = soup.find('div', {"id": "thmImages"}).find_all('img')
    for x in img_main:
        s = (x['src'])
        imgage_url.append(s.replace('thumbs', 'products'))
    print("Main-Images....", imgage_url)
    # print("images...", image)
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

    #  ---------------------------------------------------------------------------------------------------------------
    try:
        description = []
        for desc in soup.find('div', {"id": "prodDesc"}).find_all('p'):
            description.append(desc.text.strip().replace('\n', ''))
        print("Description...", description)
    except:
        description = ''
        print("Not Found")

    #  ---------------------------------------------------------------------------------------------------------------
    try:
        related_d = []
        for related in soup.find('div', {"id": "prodDesc"}).find('ul').find_all('a'):
            related_d.append("https://petol.com/"+related.get("href"))
        print("Related..", related_d)
    except AttributeError:
        related_d = ''
        print('NoneType')

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        for pdf in soup.find('div', id="pan-2").find_all('a'):
            datasheet.append(pdf.get("href"))
        print('datasheet...', datasheet)
    except AttributeError:
        datasheet = ''
        print("Not Found")

    #  ---------------------------------------------------------------------------------------------------------------
    Cross_Reference = []
    for video in soup.find('div', id="pan-4").find_all('source'):
        Cross_Reference.append("https://petol.com/"+video.get('src'))
    print("Cross_Reference...", Cross_Reference)

    #   ---------------------------------------------------------------------------------------------------------------
    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]

    row = [{
        # "Mpn": mpn,
        # "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": Product_title,
        "Image_Name": imgage_url,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": description,
        # "Features": feature,
        "Accessories": related_d,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Quantity": stock,
        # "Price(usd)": price,
        "Cross_Reference": Cross_Reference,
        "Url": url,

    }]
#
    # data_save(row, mylist)
    return Product_title


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(soup, url):
    try:
        table = soup.find('div', class_='table-responsive').find('tbody')
        td = table.find_all('tr')
        # print(td)
        for dd in td:
            ss = dd.find_all('th')
            if len(ss) > 1:
                print(ss)
                save_details: TextIO = open("hh1.txt", "a+", encoding="utf-8")
                save_details.write('\n' + url)
                print("\n ***** Record stored into urls files. *****")
                for f1 in ss:
                    save_details.write('\t' + f1.text)
                    continue
            s = dd.find_all('td')
            if not s:
                continue
            save_details: TextIO = open("hh1.txt", "a+", encoding="utf-8")
            save_details.write('\n' + url)
            for f in s:
                save_details.write('\t' + f.text)
                print("\n ***** Record stored into  tables  files. *****")
    except AttributeError:
        print('non type')


def main():
    for csv_link in range(1, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_soup_url(url)
        extract_product_detail(url, soup)
        get_specs(soup, url)


main()
