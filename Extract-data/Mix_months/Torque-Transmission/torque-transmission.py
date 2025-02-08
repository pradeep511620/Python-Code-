import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup
save_files = open("torque.csv", 'a', encoding='utf-8')

with open('tor-que-url1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def extract_data(soup, url):
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
    print(l3_name)

    title = soup.find('h1').text.strip()
    print('Title...', title)

    mpn = soup.find('span', {"name": "cds-product-number"}).text.strip()
    print('MPN...', mpn)

    for img in soup.find('div', {"id": "cds-product-image-container"}).find_all('img'):
        images = img.get('src')
        print(images)

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

    # data_save(row, cols)


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(file, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def table_data(soup, url):
    mpns = soup.find('span', {"name": "cds-product-number"}).text.strip()
    mpn = "rp_"+mpns
    print('MPN...', mpn)
    j = 0
    name = []
    value = []
    table = soup.find('table', {"id": "cds-product-attribute-table"}).find_all('td')
    # print(table)
    for td in table:
        j += 1
        tab = td.text.strip()
        if j % 2 != 0:
            name.append(tab.replace('\n', ''))
        else:
            value.append(tab.replace('\n', ''))
    #   Add a "rp_" all float number and integer number
    for i in range(len(value)):
        if isinstance(value[i], (int, float)):
            value[i] = 'rp_' + str(value[i])
        elif isinstance(value[i], str) and value[i][0].isdigit():
            value[i] = 'rp_' + value[i]
    for a, b in zip(name, value):
        print(a, "..........", b)
    #     # pass
        save = open('tableqq.txt', 'a+', encoding="utf-8")
        save.write('\n' + url + "\t" + mpn + "\t" + a + "\t" + b)
    print("save into table")


def main():
    for url_Links in range(0, 2):
        urls = csv_list[url_Links]
        url = urls[0]
        soup = get_url(url)
        print("Product-Length...", url_Links)
        print("Product-Urls......", url)
        table_data(soup, url)   # calling table function here
        # extract_data(soup, url)      # calling function extract_data()


main()
