import csv
import time

from selenium import webdriver
from selenium .webdriver.common.by import By
import pandas as pd
import requests
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.maximize_window()
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

save_files = open("aquor-water-system-all-data.csv", 'a', encoding='utf-8')

with open('brah-electric.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

#   -------------------------------------------------------------------------------------------------------------------


def product_detail(url, soup, driver):
    try:
        l3_name = []
        for k in soup.find('div', {"class": "flex flex-wrap"}).find_all('span'):
            l3_name.append(k.text.strip().replace("/\xa0", ""))
        print('l3_name...', l3_name)
    except AttributeError:
        l3_name = ''
        print('Not Found')

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        Product_title = soup.find('div', {"class": "col-span-2 py-3 text-left"}).find('h1').text.strip()
        print('title...', Product_title)
    except:
        Product_title = ''
        pass

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        number = []
        for unic in driver.find_elements(By.XPATH, "//div[@class='flex gap-8 justify-between']//div"):
            number.append(unic.text.strip().replace('\n', ''))
        Cross_Reference = number[0]
        print("Cross_Reference...", Cross_Reference)
    except IndexError:
        Cross_Reference = ''
        print("list index out of range")

    # #   ---------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find('div', {"class": "flex flex-row items-center justify-start"}).find('label').text.strip()
        print("price...", price)
    except:
        price = ''

    try:
        stock = soup.find('span', class_="text-green-600").text.strip()
        print('stock...', stock)
    except:
        stock = ''
        pass

    #   ---------------------------------------------------------------------------------------------------------------

    image = []
    for img in soup.find('div', {"class": "flex flex-col md:flex-row gap-4 flex-nowrap"}).find_all('img'):
        images = img.get('src')
        if "www.w3.org" not in images and '///' not in images:
            image.append("https://www.brahelectric.com/" + images)
    # print("images...", image)
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

    #  ---------------------------------------------------------------------------------------------------------------
    try:
        desc = soup.find('div', {"class": "p-8"}).text.strip().replace('\n', '')
        print("Description...", desc)
    except:
        desc = ''
        print("Not Found")

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        driver.find_element(By.XPATH, "//a[normalize-space()='Catalog']").click()
        for pdf in driver.find_elements(By.XPATH, "//div[@class='p-8']//div[@class='mx-auto py-4']//a"):
            datasheet.append(pdf.get_attribute("href"))
            print('datasheet...', datasheet)
    except AttributeError:
        datasheet = ''
        print("Not Found")

    #   ---------------------------------------------------------------------------------------------------------------
    # try:
    #     related_url = []
    #     for related in soup.find('div', class_="complete-pro-slider").find_all('a'):
    #         related_url.append("https://www.aquorwatersystems.com"+related.get("href"))
    #     print(related_url)
    # except AttributeError:
    #     related_url = ''
    #     print("NON Type")

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
        # "Mpn": mpn,
        # "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": Product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": desc,
        # "Features": feature,
        # "Accessories": related_url,
        "Datasheet": datasheet,
        # "item_ID": item,
        "Quantity": stock,
        "Price(usd)": price,
        "Cross_Reference": Cross_Reference,
        "Url": url,

    }]

    data_save(row, mylist)
    return Product_title


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(soup, url, Product_title):
    try:
        name = []
        value = []
        table = soup.find_all('div', class_='py-4')
        for j in table:
            td = j.find_all('div', class_="text-right col-span-2 bg-neutral-200 pr-2 py-1")
            for jj in td:
                name.append(jj.text.strip().replace("\n", ""))
        for y in table:
            td1 = y.find_all('div', class_="col-span-4 py-1")
            for jj1 in td1:
                value.append(jj1.text.strip().replace("\n", ""))
        for a, b in zip(name, value):
            print(a, "......", b)
            save = open('aquor-water-system-table.txt', 'a+', encoding='utf-8')
            save.write("\n" + url + "\t" + Product_title + "\t" + a + "\t" + b)
        print('save data into tables files')
    except IndexError:
        print('string index out of range')
    except AttributeError:
        print('Attribute error')

    #


def main():
    for csv_link in range(1396, 1590):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        driver.get(url)
        time.sleep(1)
        soup = get_url(url)
        Product_title = product_detail(url, soup, driver)
        get_specs(soup, url, Product_title)


main()
