import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from tabulate import tabulate

save_files = open("C:/Users/PK\Desktop/web-scrapping/A-MONTHS/Sep-2023/ingersoll.com/data/ingersoll-all-data.csv", 'a', encoding='utf-8')

with open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/ingersoll.com/url/ingersoll_product_url.csv", 'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)
    print(csv_length)


def get_soup_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def getDriveUrls(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(options=opts)
    # driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    # time.sleep(3)
    return driver


def product_detail(url, soup):
    print('Soup')


    l3_name = []
    bread = soup.find_all('span', {"class": "breadcrumbs"})
    for i in bread:
        cleaned_text = ' '.join(i.text.strip().split())
        l3_name.append(cleaned_text)
    print('l3_name.....', l3_name)

    try:
        product_title = soup.find('h2', class_="underlined").text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('Not Found')


    features_1 = []
    for features in soup.find('div', class_="productfeaturebox").find_all('li'):
        features_1.append(features.text)
    print('features_1.....', features_1)


    pdf_links_pdf = []
    for pdf in soup.find('table', {"id": "productmodelsdatatable_SeriesItems_ProductTable"}).find_all('td'):
        pdf_link = pdf.find_all('a')
        for pdf_links in pdf_link:
            pdf_links_pdf.append("https://www.ingersoll-imc.com"+pdf_links.get('href'))
    pdf_links_pdf = [url for url in pdf_links_pdf if 'ProductId' not in url]
    print('pdf_links_pdf.....', pdf_links_pdf)


    #
    try:
        image = []
        img_3 = soup.find('img', class_="productimage")
        image.append(img_3.get('src'))

        img_2 = soup.find('div', class_="productdiagrambox").find('img')
        image.append(img_2.get('src'))

        for img_1 in soup.find('div', class_="applicationthumbs").find_all('img'):
            image.append(img_1.get('src'))
        # print("Images....", image)
    except AttributeError:
        image = ''
        print('object has no attribute')
    #
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

    # ------------------------------------------------------------------------------------------------------------------
    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]  # save data here

    row = [{
        # "Mpn": mpn,
        # # "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        # "Product_Detail": description,
        "Features": features_1,
        # "Accessories": related_url,
        "Datasheet": pdf_links_pdf,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video_d,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Cross_Reference": Cross_Reference,
        "Url": url,

    }]  # save data here

    data_save(row, mylist)
    return product_title


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(url, soup):
    print('Tables')

    table = soup.find('table', {"id": "productmodelsdatatable_SeriesItems_ProductTable"}).find_all('tr')
    for td in table:
        td_d = td.find_all('td')
        table_td = [ts.text for ts in td_d if ts.text.strip()]
        if table_td:
            table_save = '\t'.join(table_td)
            # print(url, product_title, table_save)
    #         save = open("C:/Users/PK\Desktop/web-scrapping/A-MONTHS/Sep-2023/ingersoll.com/data/ingersoll_specs.txt", 'a+', encoding='utf-8')
    #         save.write('\n' + url + "\t" + product_title + "\t" + table_save)
    # print('save table into files..')


    table = soup.find('table', {"id": "productmodelsdatatable_SeriesItems_ProductTable"})
    rows = table.find_all('tr')
    table_data = []
    for row in rows:
        cells = row.find_all('td')
        cell_texts = [cell.text.strip() for cell in cells if cell.text.strip()]
        if cell_texts:
            table_data.append(cell_texts)
    if table_data:
        table_headers = []
        print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


def main():
    for csv_link in range(1, 3):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_soup_url(url)
        # product_title = product_detail(url, soup)
        # get_specs(url, soup, product_title)
        get_specs(url, soup)

        # selenium calling here
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)


main()
