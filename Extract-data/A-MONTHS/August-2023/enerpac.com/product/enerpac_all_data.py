import csv
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


save_files = open(
    "C:/Users/PK/Desktop/Python_project/scrape/Web-Scrapping/August-2023/enerpac.com/data/enerpac-all-data.csv", 'a',
    encoding='utf-8')

with open("C:/Users/PK/Desktop/Python_project/scrape/Web-Scrapping/August-2023/enerpac.com/url/enerpac_product_url.csv",
          'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


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
    time.sleep(3)
    return driver


def product_detail(url, driver):
    print('Driver')

    try:
        l3_name = []
        for bread in driver.find_elements(By.XPATH, "//div[@class='ProductBreadcrumbs container-fluid']//a"):
            l3_name.append(bread.text.strip())
        print('l3_name....', l3_name)
    except AttributeError:
        l3_name = ''
        print('object has no attribute')

    try:
        price = driver.find_element(By.XPATH, "//div[@class='ProductPrice col']//span").text.strip()
        print('price.....', price)
    except AttributeError:
        price = ''
        print('object has no attribute')
    except NoSuchElementException:
        price = ''
        print('Unable to locate element:')

    try:
        product_title = []
        for title in driver.find_elements(By.XPATH, "//div[@class='regionWrapper']//h1"):
            product_title.append(title.text.strip())
        print("product_title.....", product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute')

    try:
        description = []
        for desc in driver.find_elements(By.XPATH, "//div[@id='enerpacProductDescriptionSection']"):
            description.append(desc.text.replace('\n', '>>'))
        print('description.....', description)
    except AttributeError:
        description = ''
        print('object has no attribute')

    try:
        image = []
        for img in driver.find_elements(By.XPATH, "//div[@class='EnerpacProductImageViewer']//img"):
            image.append("https://www.enerpac.com/" + img.get_attribute('srcset'))
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
        # "Mpn": mpn,
        # # "Grainger_Sku": sku,
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
        # "Video_Url": video_d,
        # "Quantity": stock,
        "Price(usd)": price,
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


def get_specs(url, driver, product_title):
    print('Tables')

    driver.execute_script(f"window.scrollBy(0, {1000});")
    # time.sleep(1)
    # driver.execute_script(f"window.scrollBy(0, {600});")
    try:
        count1 = 0
        attr_name1 = []
        attr_value1 = []
        table = driver.find_element(By.XPATH, "//div[@id='imperialTable']")
        tabs = table.text.split('\n')
        for td in tabs:
            count1 += 1
            if count1 % 2 != 0:
                attr_name1.append(td)
            else:
                attr_value1.append("rp_" + td)
        for a1, b1 in zip(attr_name1, attr_value1):
            # print(a1, ".......", b1)
            save = open("C:/Users/PK/Desktop/Python_project/scrape/Web-Scrapping/August-2023/enerpac.com/data/enerpac_specs.txt",'a+', encoding='utf-8')
            save.write('\n' + url + "\t" + a1 + "\t" + b1 + "\t" + str(product_title))
        print('save data into table files...1')
    except NoSuchElementException:
        print('unable to locate the element')

    try:
        driver.find_element(By.XPATH, "//input[@value='Specs_Metric']").click()
        print('click')
    except:
        print('Not click click option')

    try:
        count2 = 0
        attr_name2 = []
        attr_value2 = []
        table2 = driver.find_element(By.XPATH, "//div[@id='metricTable']")
        tabs2 = table2.text.split('\n')
        for td2 in tabs2:
            count2 += 1
            if count2 % 2 != 0:
                attr_name2.append(td2)
            else:
                attr_value2.append("rp_" + td2)
        for a2, b2 in zip(attr_name2, attr_value2):
            # print(a2, ".......", b2)
            save = open("C:/Users/PK/Desktop/Python_project/scrape/Web-Scrapping/August-2023/enerpac.com/data/enerpac_specs.txt", 'a+', encoding='utf-8')
            save.write('\n' + url + "\t" + a2 + "\t" + b2 + "\t" + str(product_title))
        print('save data into table files...2')
    except NoSuchElementException:
        print('unable to locate the element')


def main():
    for csv_link in range(1190, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        # soup = get_soup_url(url)
        # mpn = product_detail(url, soup)

        # selenium calling here
        driver = getDriveUrls(url)
        product_title = product_detail(url, driver)
        get_specs(url, driver, product_title)


main()





















