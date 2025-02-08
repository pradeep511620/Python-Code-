import csv
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
# save_files = open("world-wide.csv", 'a', encoding='utf-8')

with open('hilti-urls.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):

    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def get_data(url, soup):

    l3_name = soup.find(id="main").find(class_="m-breadcrumbs-col").text.replace('\n', '')
    print("breadcrumb", l3_name)

    Product_title = soup.find('h1').text.strip()
    print('title...', Product_title)

    images = []
    for img in soup.find('div', {"class": "m-product-pictures m-product-pictures--gallery"}).find_all('img'):
        images.append(img.get('src'))
    print("Images...", images)
    imgs = images[1]
    # print("images..."imgs)

    #
    sku = driver.find_element(By.XPATH, "//div[@class='col-24']//div[2]//span").text.strip()
    print("product-number...", sku)

    package = driver.find_element(By.XPATH, "//main[@class='hdms-main-mixed']//section[2]").text.strip().replace('\n', '')
    print('package...', package)

    pack1 = driver.find_element(By.XPATH, "//span[@class='m-property-group-single-product ng-binding ng-scope']").text.strip()
    print("pack-size...", pack1)

    price = driver.find_element(By.XPATH, "//div[@class='a-price']").text
    print("Price...", price)

    try:
        # feature = driver.find_element(By.XPATH, "//div[contains(@class,'m-columlist a-spacing-pb--none')]//div[contains(@class,'column')]//ul//li").text.strip()
        feature = driver.find_element(By.XPATH, "//*[contains(@class,'m-columlist a-spacing-pb--none')]//div[1]//ul").text.strip()
        print("Feature...", feature)
    except:
        print("Feature Not Found")

    try:
        mpn = soup.find('div', class_='a-heading-h4').text.strip()
        print("number...", mpn)
    except:
        print("Mpn Not Found")

#
    try:
        desc = soup.find('h2', {"itemprop": "description"}).text.strip()
        print("description...", desc)
    except:
        desc = ''
        print("Not Found")

    application = driver.find_element(By.XPATH, "//div[contains(@class,'m-columlist a-spacing-pb--none')]//div[2]").text.strip().split('\n')
    print('application...', application)
    #

    #
    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]

    row = []
    #
    row.append({
        "Mpn": mpn,
        "L3_Name": l3_name,
        "Grainger_Sku": sku,
        "Product_title": Product_title,
        "Image_URL_1": images[1],
        "Image_URL_2": images[2],
        # "Image_URL_3": imgs3,
        # "Image_URL_4": imgs4,
        # "Image_URL_5": imgs5,
        "Product_Detail": desc,
        "Features": feature,
        # "item_ID": item,
        "Quantity": pack1,
        "Price(usd)": price,
        "Url": url,

    })

    # data_save(row, mylist)


# def data_save(row, cols):
#     # using save data into dataframe
#     df = pd.DataFrame(row, columns=cols)
#     print(df)
#     df.to_csv(save_files, header=False, index=False, lineterminator='\n')
#     print('save data into csv files')


def main():
    for csv_link in range(6, 7):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        driver.get(url)
        time.sleep(2)
        get_data(url, soup)


main()
