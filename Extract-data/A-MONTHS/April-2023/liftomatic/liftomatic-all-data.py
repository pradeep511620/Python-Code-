import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

save_files = open("liftomatic_all_data.csv", 'a', encoding='utf-8')

with open('liftomatic-urls.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def get_data(url, soup):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    l3_Name = []
    l3_Name = soup.find("nav", {"id": "plp-bread-crumb"}).text.strip().split('All CategoriesAll Categories')[0]
    print("Breadcrumb...", l3_Name)
    #
    Product_title = soup.find('nav', {"id": "plp-product-title"}).find('h1').text.strip()
    print('product_title...', Product_title)
    #
    try:
        desc = soup.find('div', {"itemprop": "description"}).text.strip().replace('\n', "")
        print('description...', desc)
    except:
        print('Not Found')

    image = soup.find('div', {"id": "imageCarousel"}).find('img')
    images = "https://drum-handlers.liftomatic.com"+image.get('src')
    print('images...', images)

    try:
        option = soup.find('p').text.strip().replace('\n', "")
        print('option...', option)
    except:
        print("Not Found")

    try:
        pdf_d = []
        for pdf in soup.find('div', {"class": "plp-promo-item"}).find_all('a'):
            pdf_d.append("https://drum-handlers.liftomatic.com"+pdf.get("href"))
        print("pdf...", pdf_d)
    except:
        print('Not Found')

    # names = []
    # values = []
    # h2 = soup.find_all('td', itemprop="name")
    # td = soup.find_all('span', class_="plp-spec-value")
    # for span in td:
    #     names.append(span.text.strip().replace('\n', '').replace('N/A ', ''))
    # for th in h2:
    #     values.append(th.text.strip())
    # # print(values)
    # # print(names)
    # for a, b in zip(values, names):
    #     # print(a, ".....", b
    #     pass
    #     save = open('liftomatic-table.txt', "a+", encoding="utf-8")
    #     save.write('\n' + url + ' \t' + Product_title + '\t' + a + '\t' + b)
    # print('save data into table')

    pdfs = soup.find('a', {"id": "plpdownloadpdflink"})
    download_pdf = "https://drum-handlers.liftomatic.com"+pdfs.get('data-url')
    save = open('liftomatic-pdf.txt', "a+", encoding="utf-8")
    save.write('\n' + url + ' \t' + Product_title + '\t' + download_pdf)
    print('save data into table')

    #
    # mylist = [
    #     "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
    #     "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
    #     "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
    #     "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
    #     "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
    #     "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    # ]

    # row = []
    # #
    # row.append({
    #     # "Mpn": mpn,
    #     "L3_Name": l3_Name,
    #     "Product_title": Product_title,
    #     "Image_URL_1": images,
    #     # "Image_URL_2": imgs2,
    #     # "Image_URL_3": imgs3,
    #     # "Image_URL_4": imgs4,
    #     # "Image_URL_5": imgs5,
    #     "Product_Detail": desc,
    #     "Features": option,
    #     "Datasheet": pdf_d,
    #     # "item_ID": item,
    #     # "Price(usd)": price,
    #     "Url": url,
    #
    # })

    # data_save(row, mylist)


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def main():
    for csv_link in range(1, 4):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        get_data(url, soup)


main()
