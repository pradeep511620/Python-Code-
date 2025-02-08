import csv
import time

from selenium import webdriver
from selenium .webdriver.common.by import By
import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

save_files = open("med-source-labs-all-data.csv", 'a', encoding='utf-8')

with open('med-source-labs-urls.csv', 'r') as file:
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
        for k in soup.find('div', {"class": "p2-category-wrapper"}).find_all('span'):
            l3_name.append(k.text.strip())
        print('l3_name...', l3_name)
    except AttributeError:
        l3_name = ''
        print('Not Found')

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        Product_title = soup.find('div', {"class": "p2-header-slider-left"}).find('h1').text.strip()
        print('title...', Product_title)
    except AttributeError:
        Product_title = ''
        print('Not Found')

    #   ---------------------------------------------------------------------------------------------------------------
    # try:
    #     price = soup.find('div', {"class": "flex flex-row items-center justify-start"}).find('label').text.strip()
    #     print("price...", price)
    # except:
    #     price = ''
    #
    # try:
    #     stock = soup.find('span', class_="text-green-600").text.strip()
    #     print('stock...', stock)
    # except:
    #     stock = ''
    #     pass

    #   ---------------------------------------------------------------------------------------------------------------

    image = []
    for img in soup.find('div', {"id": "p2-header-slider"}).find_all('img'):
        images = img.get('src')
        image.append(images)
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
        desc = soup.find('div', {"class": "main-highlight-desc"}).text.strip().replace('\n', '')
        print("Description...", desc)
    except:
        desc = ''
        print("Not Found")

    #  ---------------------------------------------------------------------------------------------------------------
    try:
        feature = soup.find('div', {"class": "p-highlight-desc"}).text.strip().replace('\n', '')
        print("Features...", feature)
    except:
        feature = ''
        print("Not Found")

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        for pdf in soup.find('div', class_="p2-product-enquiry").find_all('a'):
            datasheet.append(pdf.get("href"))
        print('datasheet...', datasheet)
    except AttributeError:
        datasheet = ''
        print("Not Found")

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
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": desc,
        "Features": feature,
        # "Accessories": related_url,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Cross_Reference": Cross_Reference,
        "Url": url,

    }]

    data_save(row, mylist)
    return Product_title


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(soup, url, Product_title):
    try:
        name = []
        value = []
        i = 0
        table = soup.find('div', class_='p2-specification-left').find_all('td')
        for td in table:
            i += 1
            tab = td.text.strip()
            if i % 2 != 0:
                name.append(tab)
            else:
                value.append(tab)
        for a, b in zip(name, value):
            print(a, "......", b)
            save = open('med-source-labs-urls-table.txt', 'a+', encoding='utf-8')
            save.write("\n" + url + "\t" + Product_title + "\t" + a + "\t" + b)
        print('save data into tables files')
    except IndexError:
        print('string index out of range')
    except AttributeError:
        print('Attribute error')

    # po = []
    # for t in soup.find_all('div', class_='fusion-row w-100'):
    #     for r in t.find_all('table'):
    #         po.append(r.find('td').text)
    # tdd = po
    # print(tdd)
    try:
        ii = 0
        name1 = []
        value1 = []
        for table1 in soup.find('div', class_="p2-variations-section-wrapper").find_all('tr'):
            td = table1.find_all('td')
            for tds in td:
                ii += 1

                tab1 = tds.text.strip()
                if ii % 2 != 0:
                    name1.append(tab1)
                else:
                    value1.append(tab1)
        for a1, b1 in zip(name1, value1):
            print(a1, "......", b1)
            save = open('med-source-labs-urls-table1.txt', 'a+', encoding='utf-8')
            save.write("\n" + url + "\t" + Product_title + "\t" + a1 + "\t" + b1)
        print('save data into tables files')

    except IndexError:
        print('Attribute error')


def main():
    for csv_link in range(10, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_soup_url(url)
        Product_title = extract_product_detail(url, soup)
        get_specs(soup, url, Product_title)


main()
