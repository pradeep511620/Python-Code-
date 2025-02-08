import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

save_files = open("jomarvalve-all-data.csv", 'a', encoding='utf-8')

with open("C:/Users/PK\Desktop/Web-Scrapping/August-2023/jomarvalve/url/jomarvalve-urls.csv", 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


#   -------------------------------------------------------------------------------------------------------------------


def get_data(url, soup):
    try:
        l3_name = []
        for k in soup.find('ol', {"class": "awb-breadcrumb-list"}).find_all('a'):
            l3_name.append(k.text.strip())
        print('l3_name...', l3_name)
    except AttributeError:
        l3_name = ''
        print('Not Found')

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        Product_title = soup.find('div', {"class": "fusion-title"}).text.strip()
        print('title...', Product_title)
    except:
        Product_title = ''
        pass

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        mpn = soup.find('div', {"class": "product-details"}).find('h1').text.strip()
        print("Model-number...", mpn)
    except:
        mpn = ''
        pass

    #   ---------------------------------------------------------------------------------------------------------------

    try:
        img = soup.find('div', {"class": "woocommerce-product-gallery__wrapper"}).find('img')
        images = img.get('src').strip()
        print("Images...", images)
    except:
        images = ''
        print('Not Found Images')

    #   ---------------------------------------------------------------------------------------------------------------

    try:
        feature = soup.find('div', {"class": "woocommerce-product-details__short-description"}).find('p').text.strip().replace('\n', '>>')
        print("feature...", feature)
    except:
        feature = ''
        print("Not Found")

    try:
        description = soup.find('div', {"class": "post-content"}).find('p').text.strip()
        print("description...", description)
    except:
        description = ''
        print("Not Found")

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        for pdf in soup.find('div', {"class": "woocommerce-product-details__short-description"}).find_all('a'):
            pdf_d = pdf.get("href")
            datasheet.append(pdf_d)
        print(datasheet)
    except AttributeError:
        datasheet = ''
        print("Not Found")

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
        "Mpn": mpn,
        "L3_Name": l3_name,
        "Product_title": Product_title,
        "Image_URL_1": images,
        # "Image_URL_2": imgs2,
        # "Image_URL_3": imgs3,
        # "Image_URL_4": imgs4,
        # "Image_URL_5": imgs5,
        "Product_Detail": description,
        "Features": feature,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Price(usd)": price,
        "Url": url,

    }]

    data_save(row, mylist)
    return mpn


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(soup, url, mpn):
    table = soup.find('table').find_all('tr')
    for tr in table:
        data_table = tr.text.strip().replace('\n', '>').split('>')
        save = open('jomarvalve.txt', 'a+', encoding='utf-8')
        save.write("\n" + url + "\t" + mpn + "\t".join(data_table))



def main():
    for csv_link in range(1, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        mpn = get_data(url, soup)
        get_specs(soup, url, mpn)


main()
