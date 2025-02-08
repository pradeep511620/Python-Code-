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

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/hardinge/data/hardinge-all-data.csv", 'a', encoding='utf-8')
with open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/hardinge/url/hardinge-product-url.csv", 'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_soup_url(url):
    r = requests.get(url, headers=headers)
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
    # global feature_options
    global feature_options, abouts, software, excerpt
    print('soup')
    status = requests.get(url)
    print(status.status_code)

    product_title = soup.find('h1').text.strip()
    print('product_title....', product_title)

    try:
        excerpt = soup.find('div', {"class": "excerpt"}).text.strip()
        print('excerpt.....', excerpt)
    except AttributeError:
        expert = ''
        print()


    try:
        abouts = []
        mix_data = []
        feature_options = []
        about = soup.find('div', {"class": "tab-content"})
        if about:
            paragraphs = about.find_all('p')
            lists = about.find_all('ul')

            for p in paragraphs:
                abouts.append(p.text.replace('\n', ''))
            print('abouts....', abouts)

            for ul in lists:
                mix_data.append(ul.text)
            # print('mix_data.....', mix_data)
            software = mix_data[-1].replace('\n', '<<<<')
            print('software.....', software)

            feature_options = mix_data[0:2]
            print('feature_options....', feature_options)
        else:
            print("No 'tab-content' div found.")
    except:

        print()

    try:
        description = soup.find('div', {"class": "desc"}).find('p').text.strip().replace('\n', '')
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
        img = soup.find('div', {"class": "outer"}).find_all('a')
        for images_s in img:
            image.append(images_s.get('href'))
        # print("Images....", image)      #
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
        # "Mpn": model,
        # "Grainger_Sku": sku,
        # "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": description,
        "Features": feature_options,
        "Accessories": abouts,
        # "Datasheet": datasheet,
        # "item_ID": item,
        "Uses": software,
        # "Video_Url": video_d,
        # "Quantity": stock,
        # "Price(usd)": price,
        "Cross_Reference": excerpt,
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


def Get_Specs_Table(url, soup, product_title):
    print('Tables')

    table = soup.find("table", {"class": "table"})
    if table:
        rows = table.find_all('tr')
        for row in rows:
            td_elements = row.find_all('td')
            row_text = ">>".join(td.get_text(strip=True) for td in td_elements)
            th = row_text.split('>>')
            save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/hardinge/data/hardinge_specs.txt", 'a+',encoding='utf-8')
            save.write('\n' + url + "\t" + "\t".join(th))
        print('save into files')
    else:
        print("Table not found.")




def main():
    for csv_link in range(0, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_soup_url(url)
        product_title = product_detail(url, soup)
        Get_Specs_Table(url, soup, product_title)

        # selenium calling here
        # driver = GetDriverUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)


main()
