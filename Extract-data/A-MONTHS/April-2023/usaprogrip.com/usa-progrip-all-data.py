import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

with open('usa-progrip-url.csv', 'r', encoding='utf-8') as file_url:
    csv_reader = csv.reader(file_url)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

save_files = open("usa-progrip-data.csv", 'a', encoding='utf-8')


def get_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def extract_data(soup, url):
    # time.sleep(2)
    Product_title = soup.find(class_="av-special-heading").text.strip()
    print('Product_title...', Product_title)

    sku = soup.find('section', class_="av_textblock_section").text.strip().split('\n')[0]
    print('Sku...', sku)

    images = soup.find('div', {"class": "entry-content-wrapper clearfix"}).find('img').get('src')
    print('Images..', images)

    try:
        Product = soup.find('div', {"itemprop": "text"}).find('ul')
        Product_details = Product.text.strip().split('\n')[0:-1]
        print('Product_details...', Product_details)
    except AttributeError:
        Product_details = ''
        print("Non Type")

    try:
        quantity = soup.find('div', {"itemprop": "text"}).find('ul')
        quantity_details = quantity.text.strip().split('\n')[-1]
        print('Quantity_details...', quantity_details)
    except AttributeError:
        quantity_details = ''
        print("Non Type")
    try:
        feature = soup.find('div', {"itemprop": "text"}).find('p')
        feature_details = feature.text.strip()
        print('Feature_details...', feature_details)
    except AttributeError:
        feature_details = ''
        print('object has no attribute')
    print('---------------------------------------------------------------------------')

    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]

    row = [{
        # "Mpn": product_number,
        # "L3_Name": l3_Name,
        "Grainger_Sku": sku,
        "Product_title": Product_title,
        "Image_URL_1": images,
        # "Image_URL_2": img2,
        # "Image_URL_3": imgs3,
        # "Image_URL_4": imgs4,
        # "Image_URL_5": imgs5,
        "Product_Detail": Product_details,
        "Features": feature_details,
        # "item_ID": item,
        # "Datasheet": Datasheet,
        "Quantity": quantity_details,
        # "Price(usd)": price,
        "Url": url,

    }]

    data_save(row, mylist)


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
        extract_data(soup, url)


main()
