import csv
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome(options=opts)
browser.maximize_window()

save_files = open("C:/Users/PK/Desktop/Python_project/scrape/Web-Scrapping/August-2023/kleintools.com/data/kleinttools-all-data.csv", 'a', encoding='utf-8')

with open(
        "C:/Users/PK/Desktop/Python_project/scrape/Web-Scrapping/August-2023/kleintools.com/url/klientools_product_url.csv",
        'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_soup_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def getDriveUrls(url):
    # driver = webdriver.Chrome()
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    time.sleep(4)
    return driver


def product_detail(url, soup):

    try:
        l3_name = []
        breadcrumb = soup.find('div', {"id": "block-klein-basic-breadcrumbs"}).find_all('a')
        for l3 in breadcrumb:
            l3_name.append(l3.text.strip())
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = ''
        print('object has no attribute')

    try:
        title = soup.find('div', {"class": "product-name-sticky-wrapper"}).h1
        product_title = title.text.strip()
        print("product_title.....", product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute')

    try:
        mpn = f"{'rp_'}" + soup.find('h2', {"class": "pdp-catalog-nbr"}).text.strip()
        print('mpn.....', mpn)
    except AttributeError:
        mpn = ''
        print('object has no attribute')

    try:
        video = soup.find('div', {"class": "pdp-videos"}).find('iframe')
        video_d = video.get('src').replace('//', '')
        print('video.....', video_d)
    except AttributeError:
        video_d = ''
        print('object has no attribute')

    try:
        description = []
        desc = soup.find('div', {"class": "features-wrapper"}).find_all('li')
        for des in desc:
            description.append(des.text)
        print('description.....', description)
    except AttributeError:
        description = ''
        print('object has no attribute')


    try:
        image = []
        for img in soup.find('div', {"class": "mp-gallery"}).find_all('img'):
            image.append("https://www.kleintools.com"+img.get('src'))
        print("Images....", image)
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
    ]   # save data here

    row = [{
        "Mpn": mpn,
        # "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": description,
        # "Features": features,
        # "Accessories": related_url,
        # "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        "Video_Url": video_d,
        # "Quantity": stock,
        # "Price(usd)": price_d,
        # "Cross_Reference": Cross_Reference,
        "Url": url,

    }]  # save data here

    data_save(row, mylist)
    return mpn


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(url, soup, mpn):
    try:
        i_count = 0
        attr_name = []
        attr_value = []
        table = soup.find('div', {"class": "specs-wrapper"}).find_all('span')
        for td in table:
            i_count += 1
            # print(i_count)
            tab = td.text.strip()
            # print(tab)
            if i_count % 2 != 0:
                attr_name.append(tab)
            else:
                attr_value.append("rp_" + tab)
        for a, b in zip(attr_name, attr_value):
            # print(a, ".......", b)
            save = open("C:/Users/PK/Desktop/Python_project/scrape/Web-Scrapping/August-2023/kleintools.com/data/kleinttools_specs.txt", 'a+', encoding='utf-8')
            save.write('\n' + url + "\t" + a + "\t" + b + "\t" + mpn)
        print('save data into table files')
    except AttributeError:
        print('object has no attribute')


def main():
    for csv_link in range(1698, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_soup_url(url)
        mpn = product_detail(url, soup)
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        get_specs(url, soup, mpn)


main()
