import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
save_files = open("world-wide.csv", 'a', encoding='utf-8')

with open('Product-Urls.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def get_data(url, soup):
    try:
        l3_name = []
        for k in soup.find('div', {"id": "breadcrumbs"}).find_all('a'):
            l3_name.append(k.text.strip())
        print('l3_name...', l3_name)
    except:
        pass

    Product_title = soup.find('h1', {"class": "entry-title"}).text.strip()
    print('title...', Product_title)

    mpn = soup.find('ul', {"class": "product-attibutes"}).text
    print("Model-number...", mpn)
    try:
        img = soup.find('div', {"class": "header__image"}).find('img')
        images = img.get('src')
        print("Images...", images)
    except:
        images = ''
        print('Not Found Images')

    try:
        desc = soup.find('section', {"class": "entry-content"}).find('p').text.strip().replace('• ', '').replace('\n', '')
        print("description...", desc)
    except:
        desc = ''
        print("Not Found")

    try:
        pdf_d = []
        for pdf in soup.find('ul', {"class": "woocommerce-product-downloads"}).find_all('a'):
            pdf_d.append(pdf.get("href"))
    except:
        pdf_d = ''
        pass

    try:
        name = []
        value = []
        table = soup.find('div', class_="woocommerce-product-attributes shop_attributes")
        td = table.find_all('div', class_="woocommerce-product-attributes-item__label")
        td1 = table.find_all('div', class_="woocommerce-product-attributes-item__value")
        for tab in td:
            name.append(tab.text.strip())
        for tab1 in td1:
            value.append(tab1.text.strip())
        for i in range(len(value)):
            if isinstance(value[i], (int, float)):
                value[i] = 'rp_' + str(value[i])
            elif isinstance(value[i], str) and value[i][0].isdigit():
                value[i] = 'rp_' + value[i]

        for a, b in zip(name, value):
            print(a, "......", b)
            save = open('world-wide-table1.txt', 'a+', encoding='utf-8')
            save.write("\n" + url + "\t" + mpn + "\t" + a + "\t" + b)
        print('save data into tables files')
    except:
        print('Not Found')


    #
    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]

    row = []

    row.append({
        "Mpn": mpn,
        "L3_Name": l3_name,
        "Product_title": Product_title,
        "Image_URL_1": images,
        # "Image_URL_2": imgs2,
        # "Image_URL_3": imgs3,
        # "Image_URL_4": imgs4,
        # "Image_URL_5": imgs5,
        "Product_Detail": desc,
        # "Features": features,
        # "item_ID": item,
        # "Price(usd)": price,
        "Url": url,

    })

    # data_save(row, mylist)


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def main():
    for csv_link in range(1, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        get_data(url, soup)


main()
