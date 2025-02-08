import csv
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

sess = requests.Session()

data = {
    "categoryIndex": 17
}

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

save_files = open("grainger-plumbing-all-data1.csv", 'a', encoding='utf-8')

with open("C:/Users/PK/Desktop/Web-Scrapping/Grainger_urls/Grainger_Plumbing/urls/granger_plumbing_urls_31952.csv", 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    # time.sleep(1)
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def product_detail(url, soup):
    try:
        Product_title = soup.h1.text
        print('Product_title....', Product_title)
    except AttributeError:
        Product_title = ''
        print('Not Found')


    l3_name = []
    bread = soup.find(class_='Gcu9yB').findAll('a')
    for txt in bread:
        l3_name.append(txt.text.strip().replace('\n', '>'))
    print('l3_name..', l3_name)

    item_number = soup.findAll(class_='vDgTDH')
    mpn = item_number[0].text
    print("item...", mpn)

    sku = item_number[1].text
    print("mfr...", sku)

    try:
        price = soup.find(class_="rZErC5").find('span').text.strip()
        print('price....', price)
    except AttributeError:
        price = ''
        print("Not Found")

    try:
        moq = soup.find(class_="rZErC5").find(class_="G32gdF").text.strip()
        print('Moq....', moq)
    except AttributeError:
        moq = ''
        print('Not Found')

    image = []
    for img in soup.find(class_="vJXKUW").find_all('img'):
        image.append(img.get('src'))
    # print("Images...", image)
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
        desc = soup.find(class_="doFS6-").find(class_="W7BBCC").text.strip().replace('\n', '')
        print('Description...', desc)
    except AttributeError:
        desc = ''
        print('Not Found')

    try:
        discontinued = soup.find(class_="TAmQLj").text.strip()
        print('discontinued ....', discontinued)
    except AttributeError:
        discontinued = ''
        print("Not found")

    # ------------------------------------------------------------------------------------------------------------------
    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]   # save data list

    row = [{
        "Mpn": mpn,
        "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": Product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": desc,
        # "Features": features,
        # "Accessories": related_url,
        # "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": price,
        "Quantity": moq,
        "Price(usd)": price,
        "Cross_Reference": discontinued,
        "Url": url,

    }]  # save data

    data_save(row, mylist)
    return mpn


def data_save(row, cols):
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')
    # using save data into dataframe


#   -------------------------------------------------------------------------------------------------------------------


def data_table(url, mpn, soup):
    name = []
    value = []
    table = soup.find(class_="P9I57X")
    # print(table)
    dl = table.find_all('dt')
    dd = table.find_all('dd')
    for td in dl:
        name.append(td.text.strip())
    for td1 in dd:
        value.append(td1.text.strip())

    for a, b in zip(name, value):
        # print(a, ".....", b)
        save = open('grainger-table1.txt', 'a+', encoding='utf-8')
        save.write('\n' + url + "\t" + mpn + "\t" + a + "\t" + b)
    print('save data into files')


def main():
    for csv_link in range(15499, 15500):  # start point 25000
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        mpn = product_detail(url, soup)
        data_table(url, mpn, soup)


main()
