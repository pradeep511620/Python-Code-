import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup

files = open("torque-transmission-data.csv", 'a', encoding='utf-8')

# reading the CSV file
with open('tor-que-url1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

# displaying the contents of the CSV file
for url_Links in range(2581, csv_length):
    urls = csv_list[url_Links]
    url = urls[0]
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    print("Product-Length...", url_Links)
    print("Product-Urls......", url)
#
    cols = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]
    row = []

    l3_name = []
    bread = soup.find("ul", {"class": "cds-crumbs"}).find_all('li')
    for b in bread:
        l3_name.append(b.text.strip().replace("\n", ""))
    print("Breadcrumb...", l3_name)

    title = soup.find('h1').text.strip()
    print('Title...', title)

    mpn = soup.find('span', {"name": "cds-product-number"}).text.strip()
    print('MPN...', "rp_"+mpn)

    for img in soup.find('div', {"id": "cds-product-image-container"}).find_all('img'):
        images = img.get('src')
        print("Images...", images)

        # save data from here to csv
    row.append({
        "Mpn": mpn,
        "L3_Name": l3_name,
        "Product_title": title,
        "Image_URL_1": images,
        # "Image_URL_2": imgs2,
        # "Image_URL_3": imgs3,
        # "Image_URL_4": imgs4,
        # "Image_URL_5": imgs5,
        # "Features": features,
        # "item_ID": item,
        # "Price(usd)": price,
        "Url": url,

    })
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')

# Here is the Tables data
    mpn = soup.find('span', {"name": "cds-product-number"}).text.strip()
    print('MPN...', mpn)
    i = 0
    name = []
    value = []
    table = soup.find('table', {"id": "cds-product-attribute-table"}).find_all('td')
    # print(table)
    for td in table:
        i += 1
        tab = td.text.strip()
        if i % 2 != 0:
            name.append(tab.replace('\n', ''))
        else:
            value.append(tab.replace('\n', ''))
    # print(name)
    for a, b in zip(name, value):
        print(a, "..........", b)
        save = open('tor-que-transmission-table.txt', 'a+', encoding="utf-8")
        save.write('\n' + url + "\t" + "rp_"+mpn + "\t" + a + "\t" + b)
    print("save into table")

