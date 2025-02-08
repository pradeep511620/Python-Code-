import csv
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

save_files = open("weg-data.csv", 'a', encoding='utf-8')

with open('Product_url_weg.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def get_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def get_data(soup, url):
    try:
        l3_Name = []
        for l3 in soup.find('div', {"id": "breadcrumb"}).find_all('span'):
            l3_Name.append(l3.text.strip())
        print("Breadcrumb...", l3_Name)
    except AttributeError:
        l3_Name = ''
        print('Non Type')

    try:
        product_title = soup.find('h1', {"class": "product-card-title page-header xtt-nbb"}).text
        print('Product-title...', product_title)
    except AttributeError:
        product_title = ''
        print("Non Type")

    #

    try:
        sku_all = soup.find('small', {"class": "product-card-info"}).text
        catalog_number = sku_all.strip().split('|')[0]
        print('catalog_number...', catalog_number)
    except IndexError:
        catalog_number = ''
        print('list index out of range')

    #
    try:
        product_number = sku_all.strip().split('|')[1]
        print('product_number...', product_number)
    except IndexError:
        product_number = ''
        print('list index out of range')

    #
    try:
        images1 = driver.find_element(By.XPATH, "//div[@class='xtt-product-thumbnails hidden-xs hidden-sm col-md-2']//img")
        img1 = images1.get_attribute('src')
        print('Images1...', img1)
    except NoSuchElementException:
        img1 = ''
        print(' Unable to locate element')

    try:
        images = driver.find_element(By.XPATH, "//div[@class='carousel slide col-xs-12 col-md-10']//a")
        img2 = images.get_attribute('href')
        print('Images2...', img2)
    except NoSuchElementException:
        img2 = ''
        print(' Unable to locate element')
    #
    try:
        price = driver.find_element(By.XPATH, "//span[@class='price']").text
        print('price..', price)
    except:
        price = ''
        print("Not Found Price")

    try:
        product_desc = driver.find_element(By.XPATH, "//div[@class='xtt-product-description']").text
        print('product_description...', product_desc)
    except AttributeError:
        print('')

    try:
        Datasheet = []
        for pdf in driver.find_elements(By.XPATH, "//div[@class='tabs-left product-download-central-tabs']//a"):
            pdf_d = pdf.get_attribute('href')
            if ".pdf" in pdf_d:
                Datasheet.append(pdf_d)
        print('pdf...', Datasheet)
    except:
        pass
    #
    # try:
    #     print("********** table 1 **********")
    #     name = []
    #     value = []
    #     table = driver.find_element(By.XPATH, "//div[@class='row product-info-specs']")
    #     th = table.find_elements(By.TAG_NAME, "th")
    #     td = table.find_elements(By.TAG_NAME, "td")
    #     for t in th:
    #         name.append(t.text.strip())
    #     for tds in td:
    #         value.append(tds.text.strip())
    #     for i in range(len(value)):
    #         if isinstance(value[i], (int, float)):
    #             value[i] = 'rp_' + str(value[i])
    #         elif isinstance(value[i], str) and value[i][0].isdigit():
    #             value[i] = 'rp_' + value[i]
    #     for a, b in zip(name, value):
    #         print(a, ".....", b)
    #         save = open("weg-data-table.txt", "a+", encoding="utf-8")
    #         save.write('\n' + url + "\t" + product_number + "\t" + catalog_number + "\t" + a + "\t" + b)
    #     print('sava list into table1 files')
    # except:
    #     print("Not Found")
    # #
    # try:
    #     print("********** table 2 **********")
    #     name1 = []
    #     value1 = []
    #     table1 = driver.find_element(By.XPATH, "//div[@id='datasheet-0']")
    #     th1 = table1.find_elements(By.TAG_NAME, "th")
    #     td1 = table1.find_elements(By.TAG_NAME, "td")
    #     for t1 in th1:
    #         name1.append(t1.text.strip())
    #     for tds1 in td1:
    #         value1.append(tds1.text.strip())
    #     for i in range(len(value1)):
    #         if isinstance(value1[i], (int, float)):
    #             value1[i] = 'rp_' + str(value1[i])
    #         elif isinstance(value1[i], str) and value1[i][:0].isdigit():
    #             value1[i] = 'rp_' + value1[i]
    #     for a1, b1 in zip(name1, value1):
    #         print(a1, ".....", b1)
    #         save = open("weg-data-table1.txt", "a+", encoding="utf-8")
    #         save.write('\n' + url + "\t" + product_number + "\t" + catalog_number + "\t" + a1 + "\t" + b1)
    #     print('sava list into table2 files')
    # except:
    #     print()
    # #
    # try:
    #     print("********** table 3 **********")
    #     name2 = []
    #     value2 = []
    #     table2 = driver.find_element(By.XPATH, "//table[@class='table table-striped table-hover']")
    #     th2 = table2.find_elements(By.TAG_NAME, "th")
    #     td2 = table2.find_elements(By.TAG_NAME, "td")
    #     for t2 in th2:
    #         name2.append(t2.text.strip())
    #     for tds2 in td2:
    #         value2.append(tds2.text.strip())
    #     for i in range(len(value2)):
    #         if isinstance(value2[i], (int, float)):
    #             value2[i] = 'rp_' + str(value2[i])
    #         elif isinstance(value2[i], str) and value2[i][0].isdigit():
    #             value2[i] = 'rp_' + value2[i]
    #     for a2, b2 in zip(name2, value2):
    #         print(a2, ".....", b2)
    #         save = open("weg-data-table2.txt", "a+", encoding="utf-8")
    #         save.write('\n' + url + "\t" + product_number + "\t" + catalog_number + "\t" + a2 + "\t" + b2)
    #     print('sava list into table3 files')
    # except:
    #     print('Not Found')

    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]

    row = [{
        "Mpn": product_number,
        "L3_Name": l3_Name,
        "Grainger_Sku": catalog_number,
        "Product_title": product_title,
        "Image_URL_1": img1,
        "Image_URL_2": img2,
        # "Image_URL_3": imgs3,
        # "Image_URL_4": imgs4,
        # "Image_URL_5": imgs5,
        "Product_Detail": product_desc,
        # "Features": feature,
        # "item_ID": item,
        "Datasheet": Datasheet,
        # "Quantity": pack1,
        "Price(usd)": price,
        "Url": url,

    }]

    #

    # data_save(row, mylist)


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def main():
    for csv_link in range(1080, 3400):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        driver.get(url)
        time.sleep(1)
        get_data(soup, url)  # calling table function here


main()
