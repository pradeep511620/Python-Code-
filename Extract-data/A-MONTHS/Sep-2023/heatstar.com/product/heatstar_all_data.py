import csv
import json

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

save_files = open("C:/Users/PK/Desktop/web-scrapping/Sep-2023/heatstar.com/data/heatstar-all-data.csv", 'a',
                  encoding='utf-8')

with open("C:/Users/PK/Desktop/web-scrapping/Sep-2023/heatstar.com/url/enerpac_product_url.csv", 'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_soup_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def GetDriverUrls(url):
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

    product_title = soup.find('h1', {"class": "ppbd-product-name"}).text.strip()
    print('product_title....', product_title)

    l3_name = f'home > {product_title}'
    print('l3_name.....', l3_name)

    try:
        model = soup.find('div', {"class": "ppbd-product-attribute"}).text.strip().replace('\n', '')
        print('model....', model)
    except AttributeError:
        model = ''

    try:
        sku = soup.find('div', {"class": "product attribute sku"}).text.strip().replace('\n', '')
        print('sku....', sku)
    except AttributeError:
        sku = ''
        print('sku.... object has no attribute')

    try:
        features1 = soup.findAll('div', {"class": "ppbd-product-attribute"})[1].text.strip().replace('\n', '')
    except IndexError:
        features1 = ''
    try:
        features2 = soup.find('div', {"class": "ppbd-product-short-description"}).text.strip().replace('\n', '')
        features = features2 + ".." + features1
        print('features....', features)
    except AttributeError:
        features = ''
        print('object has no attribute')

    try:
        description = soup.find('div', {"class": "ppbd-product-description"}).text.strip().replace('\n', '')
        print('description....', description)
    except AttributeError:
        description = ''
        print('object has no attribute')

    try:
        datasheet = []
        for pdf in soup.find('div', {"class": "product-attachment-container"}).find_all('a'):
            datasheet.append(pdf.get('href'))
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = ''

    try:
        image = []
        mmg = soup.find('div', class_="product media").findAll('script')
        img = json.loads(mmg[1].text)['[data-gallery-role=gallery-placeholder]']['mage/gallery/gallery']['data']
        for i in img:
            image.append(i['full'])
        # print("Images....", image)
    except AttributeError:
        image = ''
        print('object has no attribute')

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
        "Mpn": model,
        "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": description,
        "Features": features,
        # "Accessories": related_url,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video_d,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Cross_Reference": Cross_Reference,
        "Url": url,

    }]  # save data here

    data_save(row, mylist)
    return model


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, model):
    print('Tables')
    try:
        count_i = 0
        attr_name = []
        attr_value = []
        table = soup.find_all('table', {"id": "super-product-table"})
        for th in table:
            row = th.find_all('td')
            for td in row:
                tab = td.text.strip()
                count_i += 1
                if count_i % 2 != 0:
                    attr_name.append(tab)
                else:
                    attr_value.append(tab)
        for a, b in zip(attr_name, attr_value):
            print(a, "..............", b)
            save = open("C:/Users/PK/Desktop/web-scrapping/Sep-2023/heatstar.com//data/heatstar_specs.txt", 'a+', encoding='utf-8')
            save.write('\n' + url + "\t" + a + "\t" + b + "\t" + model)
        print('save data into table files...1')
    except:
        print('')
    try:
        attr_name1 = []
        attr_value1 = []
        table1 = soup.find('table', {"id": "product-attribute-specs-table"})
        th1 = table1.find_all('th')
        td1 = table1.find_all('td')
        for th_1 in th1:
            attr_name1.append(th_1.text)
        for td_1 in td1:
            attr_value1.append(td_1.text)
        for a1, b1 in zip(attr_name1, attr_value1):
            print(a1, "...........", b1)
            save = open("C:/Users/PK/Desktop/web-scrapping/Sep-2023/heatstar.com//data/heatstar_specs.txt", 'a+', encoding='utf-8')
            save.write('\n' + url + "\t" + a1 + "\t" + b1 + "\t" + model)
        print('save data into table files...2')
    except:
        print('')


def main():
    for csv_link in range(54, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_soup_url(url)
        model = product_detail(url, soup)
        Get_Specs_Table(url, soup, model)

        # selenium calling here
        # driver = GetDriverUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)


main()
