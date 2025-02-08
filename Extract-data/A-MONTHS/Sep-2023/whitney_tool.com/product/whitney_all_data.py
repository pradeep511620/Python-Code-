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

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/whitney_tool.com/data/whitney-all-data.csv", 'a',
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

    l3_name = []
    bread = soup.find_all('span', {"class": "breadcrumb"})
    for l3 in bread:
        cleaned_text = ' '.join(l3.text.strip().split('/'))
        l3_name.append(cleaned_text)
    print('l3_name.....', l3_name)

    try:
        product_title = soup.find('table', {"class": "data"}).find('h2').text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute ... product_title')
    #

    cleaned_text = []
    mixed_data = soup.find('table', {"class": "data"}).find_all('td')
    for mixed in mixed_data:
        cleaned_text.append(re.sub(r'\s+', ' ', mixed.text.strip()))
    modols_details = cleaned_text[1].split('No.')

    try:
        model = modols_details[-2]
        print('model.....', model)
    except IndexError:
        model = ''
        print('Index out of range')

    try:
        sku = modols_details[-1]
        print('sku.....', sku)
    except IndexError:
        sku = ''
        print('Index out of range')

    Cross_Reference = soup.find(class_='techSpec').findChild('div').text.strip().replace('\n', '').replace('\r', '')
    print('Cross_Reference.....', Cross_Reference)


    # --------------------------------------- Images------------------------------------------------
    try:
        image = []
        imgs = soup.find('table', {"class": "data"}).find_all('a')
        for img in imgs:
            img_1 = img.find('img')
            if img_1 is not None:
                image.append("https://www.whitneytool.com/" + img_1.get('src'))
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
        "Mpn": model,
        "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": product_title,
        # "Image_URL_1": imgs,
        # "Image_URL_2": imgs1,
        # "Image_URL_3": imgs2,
        # "Image_URL_4": imgs3,
        # "Image_URL_5": imgs4,
        "Image_Name": image,
        # "Product_Detail": description,
        # "Features": feature,
        # "Accessories": href_type_exe,
        # "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video_d,
        # "Quantity": stock,
        # "Price(usd)": price,
        "Cross_Reference": Cross_Reference,
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


def Get_Table_Specs(url, soup, product_title):
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

    count_number = 0
    attr_name = []
    attr_value = []
    table = soup.find('div', {"class": "techSpec"}).find_all('td')
    for td in table:
        count_number += 1
        tab = td.text.strip()
        if count_number % 2 != 0:
            attr_name.append(tab)
        else:
            attr_value.append("rp_"+tab.replace('\n', '').replace('\r', '').replace("                           ", ''))
    for a, b in zip(attr_name, attr_value):
        print(a, ".......", b)
        save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/whitney_tool.com/data/whitney_specs1.txt", 'a+', encoding='utf-8')
        save.write('\n' + url + " \t" + product_title + "\t" + a + "\t" + b)
    print('save data into table files ................1')


def main():
    url_link_count = 3468
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/whitney_tool.com/url/whitney_product_url.csv")['url']
    for url in url_link[:]:
        url_link_count += 1
        print("Product-Length...", url_link_count)
        print("Product-Urls......", url)
        soup = Get_Soup_Url(url)
        product_title = product_detail(url, soup)
        Get_Table_Specs(url, soup, product_title)

        # selenium calling here
        # driver = Get_Driver_Urls(url)
        # product_detail(url, driver)
        # get_specs(url, driver)
    print('loop End')


if __name__ == "__main__":
    main()
