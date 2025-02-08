import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

save_files = open("gesafety-al-data.csv", 'a', encoding='utf-8')

with open("C:/Users/PK/Desktop/Web-Scrapping/August-2023/gesafety.com/url/gesafety-url.csv", 'r') as file:
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
        for k in soup.find('div', {"class": "col-xs-12 nav-breadcrumb"}).find_all('a'):
            l3_name.append(k.text.strip())
        print('l3_name...', l3_name)
    except AttributeError:
        l3_name = ''
        print('Not Found')

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        Product_title = soup.find('span', {"class": "desc"}).text.strip()
        print('title...', Product_title)
    except:
        Product_title = ''
        pass

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        mpn = soup.find('span', {"class": "model"}).text.strip()
        print("Model-number...", mpn)
    except:
        mpn = ''
        pass

    #   ---------------------------------------------------------------------------------------------------------------

    try:
        img = soup.find('div', {"id": "prod_right"}).find('img')
        images = 'http://www.gesafety.com'+img.get('src').strip()
        print("Images...", images)
    except:
        images = ''
        print('Not Found Images')

    #   ---------------------------------------------------------------------------------------------------------------

    try:
        des = []
        for desc in soup.find('div', {"id": "copy_area"}).find_all('p'):
            dec = desc.text
            des.append(dec)
        print("descriptions...", des)
    except:
        des = ''
        print("Not Found")


    try:
        ft = []
        for fet in soup.find('div', {"id": "copy_area"}).find_all('ul'):
            feature = fet.text.replace('\n', '>>')
            ft.append(feature)
        print("features...", ft)
    except:
        ft = ''
        print("Not Found")

    #   ---------------------------------------------------------------------------------------------------------------

    try:
        datasheet = []
        for pdf in soup.find('div', {"id": "prod_right"}).find_all('a'):
            pdf_d = 'http://www.gesafety.com'+pdf.get("href")
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
        # "L3_Name": l3_name,
        "Product_title": Product_title,
        "Image_URL_1": images,
        # "Image_URL_2": imgs2,
        # "Image_URL_3": imgs3,
        # "Image_URL_4": imgs4,
        # "Image_URL_5": imgs5,
        "Product_Detail": des,
        "Features": ft,
        "Datasheet": datasheet,
        # "item_ID": item,
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
    for csv_link in range(5, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        get_data(url, soup)



main()
