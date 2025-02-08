# import mysql.connector
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import re

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/whitmancontrols.com/data/whitman-all-data.csv", 'a',
                  encoding='utf-8')


def Get_Soup_Url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def Get_Driver_Urls(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(options=opts)
    # driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    return driver


def product_detail(url, soup):
    print('soup')

    """    l3_name = []
    bread = soup.find('div', {"class": "breadcrumbs"}).find_all('li')
    for l3 in bread:
        cleaned_text = ' '.join(l3.text.strip().split('/'))
        l3_name.append(cleaned_text)
    print('l3_name.....', l3_name)

    try:
        product_title = soup.find('h1', {"class": "page-title"}).text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute ... product_title')
    #
    try:
        sku = soup.find('div', {"class": "simpleSku"}).text.strip()
        print('sku.....', sku)
    except AttributeError:
        sku = ''
        print('nnnnnnnnnnnnnnnnnnnn')

    try:
        price = soup.find("span", {"class": "price"}).text.strip()
        print(price)
    except AttributeError:
        price = ''
        print('nnnnnnnnnnnnnnn')


    try:
        des_1 = soup.find(class_='tabs-block').findChild('p').text.strip()
        des_2 = soup.find(class_='tabs-block').findChild('ul').text.strip().replace('\n', '')
        other_description = des_1+des_2
        print('others descriptions.....', other_description)
    except AttributeError:
        other_description = ''
        print('nnnnnnnnnnnnnnnnnnnnnnnnn')

    try:
        description = soup.find('div', {"class": "product attribute description"}).find('p').text.strip()
        print('description.....', description)
    except AttributeError:
        description = ''
        print('nnnnnnnnnnnnnnnnnnnnnnnn')
    try:
        data = []
        Features = soup.find('div', {"class": "product attribute description"}).find_all('ul')
        for f in Features:
            data.append(f.text.split('\n'))
    except AttributeError:
        data = ''
    try:
        feature = data[0]
        print('feature.....', feature)
    except IndexError:
        feature = ''
        print('list index out of range')

    try:
        specification = data[1]
        print('specification.....', specification)
    except IndexError:
        specification = ''
        print('list index out of range')
"""


    datasheet = []
    for pdf in soup.find("div", {"id": "product.info.specs"}).find_all('a'):
        datasheet.append("https://www.whitmancontrols.com"+pdf.get('href'))
    print('datasheet....', datasheet)




    # --------------------------------------- Images------------------------------------------------
    try:
        image = []
        imgs = soup.find('div', {"class": "product-media product media"}).find_all('img')
        for img in imgs:
            image.append(img.get('src'))
        print("Images....", image)
    except AttributeError:
        image = ''
        print('object has no attribute ... image')
    # #
    # try:
    #     imgs = image[0]
    #     print('imgs...', imgs)
    # except IndexError:
    #     imgs = ''
    #     print('List out of index')
    # try:
    #     imgs1 = image[1]
    #     print('imgs1...', imgs1)
    # except IndexError:
    #     imgs1 = ''
    #     print('List out of index')
    # try:
    #     imgs2 = image[2]
    #     print('imgs2...', imgs2)
    # except IndexError:
    #     imgs2 = ''
    #     print('List out of index')
    # try:
    #     imgs3 = image[3]
    #     print('imgs3...', imgs3)
    # except IndexError:
    #     imgs3 = ''
    #     print('List out of index')
    # try:
    #     imgs4 = image[4]
    #     print('imgs4...', imgs4)
    # except IndexError:
    #     imgs4 = ''
    #     print('List out of index')

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
        # "Product_title": product_title,
        # "Image_URL_1": imgs,
        # "Image_URL_2": imgs1,
        # "Image_URL_3": imgs2,
        # "Image_URL_4": imgs3,
        # "Image_URL_5": imgs4,
        # "Image_Name": image,
        # "Product_Detail": other_description,
        # "Features": feature,
        # "Accessories": description,
        # "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video_d,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Cross_Reference": specification,
        # "Url": url,

    }]  # save data here

    # data_save(row, mylist)
    # return sku


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Table_Specs(url, soup, sku):
    print('table.......')
    """    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test",
        port=3306
    )
    print('local database connected')
    cursor = conn.cursor()
            # cursor.execute("INSERT INTO scrape_files (url, name, value) VALUES (%s, %s, %s)", (url, a, b))
    conn.commit()
    conn.close()
    """  # save data into database using python
    # driver.execute_script(f"window.scrollBy(0, {700});")



    attr_name = []
    attr_value = []
    table = soup.find('table', {"id": "product-attribute-specs-table"})
    for th in table.find_all('th'):
        attr_name.append(th.text.strip())
    for th in table.find_all('td'):
        attr_value.append(th.text.strip())
    for a, b in zip(attr_name, attr_value):
        pass
        # print(a, ".......", b)
        save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/whitmancontrols.com/data/whitman_specs1.txt", 'a+', encoding='utf-8')
        save.write('\n' + url + " \t" + sku + "\t" + a + "\t" + b)
    print('save data into table files ................1')




def main():
    url_link_count = 0
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/whitmancontrols.com/url/whitman_product_url.csv")['url']
    for url in url_link[:2]:
        url_link_count += 1
        print("Product-Length...", url_link_count)
        print("Product-Urls......", url)
        soup = Get_Soup_Url(url)
        product_detail(url, soup)
        # Get_Table_Specs(url, soup, sku)

        # selenium calling here
        # driver = Get_Driver_Urls(url)
        # product_detail(url, driver)
        # get_specs(url, driver)
    print('loop End')


if __name__ == "__main__":
    main()
