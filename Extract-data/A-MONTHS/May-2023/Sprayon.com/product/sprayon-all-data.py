import pandas as pd
import requests
from bs4 import BeautifulSoup

import csv

# driver = webdriver.Chrome()
# driver.maximize_window()

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

save_files = open("sprayon-all-data.csv", 'a', encoding='utf-8')

with open('sprayon-url.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


#   -------------------------------------------------------------------------------------------------------------------


def product_detail(url, soup):
    try:
        l3_name = []
        for k in soup.find('div', {"id": "breadcrumbs"}).find('span'):
            l3_name.append(k.text.strip())
        print('l3_name...', l3_name)
    except AttributeError:
        l3_name = ''
        print('Not Found')

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        Product_title = soup.find('div', {"class": "summary entry-summary"}).find('h1').text.strip()
        print('title...', Product_title)
    except AttributeError:
        Product_title = ''

    #   ---------------------------------------------------------------------------------------------------------------

    uses = soup.find('div', class_="grid-row product-special-meta").find('p')
    uses_d = uses.text.strip().replace('\n', '')
    print('uses...', uses_d)

    #   ---------------------------------------------------------------------------------------------------------------

    feature = soup.find('div', class_="grid-row product-special-meta").find('ul')
    features = feature.text.strip().replace('\n', '')
    print('features...', features)

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        desc = soup.find('div', {"class": "woocommerce-product-details__short-description"}).find(
            'p').text.strip().replace('\n', '')
        print("Description...", desc)
    except:
        desc = ''
        print("Not Found")

    #   ---------------------------------------------------------------------------------------------------------------
    image = []
    for img in soup.find('div', {"id": "image-section"}).find_all('img'):
        images = img.get('src')
        image.append(images)
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

    #   ---------------------------------------------------------------------------------------------------------------

    datasheet = []
    try:
        for pdf in soup.find('div', class_="variations-table").find_all('tr'):
            for pds in pdf.find_all('a'):
                datasheet.append(pds.get('href'))
        print(datasheet)
    except AttributeError:
        datasheet = ''
        print("Not Found")

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        related_url = []
        for related in soup.find('div', class_="related products").find_all('a'):
            related_url.append(related.get("href"))
        print('related_url...', related_url)
    except AttributeError:
        related_url = ''
        print("NON Type")

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
        "Features": features,
        "Accessories": related_url,
        "Datasheet": datasheet,
        # "item_ID": item,
        "Uses": uses_d,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Cross_Reference": Cross_Reference,
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
        i = 0
        name = []
        value = []
        table = soup.find('table', class_='shop_attributes').find_all('tr')
        for th in table:
            tab = th.text.strip()
            tabss = tab.replace('\n', '_')
            jj = tabss.split('_')
            for j in jj:
                i += 1
                # print(i)
                # print(j)
                if i % 2 != 0:
                    name.append(j)
                else:
                    value.append(j)
        for a, b in zip(name, value):
            print(a, "......", b)
            save = open('sprayon-table1.txt', 'a+', encoding='utf-8')
            save.write("\n" + url + "\t" + Product_title + "\t" + a + "\t" + b)
        print('save data into tables files')
    except IndexError:
        print('string index out of range')
    except AttributeError:
        print('Attribute error')

    name1 = []
    name2 = []
    name3 = []
    table1 = soup.find('table', class_="formatted").find('tbody').findAll('tr')
    for tt in table1:
        td = tt.find('td')
        name1.append(td.text.strip())
        tdd = tt.find_all('td', {'data-attr': "pa_size"})
        for thh in tdd:
            name2.append(thh.text)
        tdd1 = tt.find_all('td', {'data-attr': "pa_product-type"})
        for thh1 in tdd1:
            name3.append(thh1.text)
    for a1, b1, c1 in zip(name1, name2, name3):
        print(a1, ".....", b1, ".....", c1)
        save = open('sprayon-table2.txt', 'a+', encoding='utf-8')
        save.write("\n" + url + "\t" + Product_title + "\t" + a1 + "\t" + b1 + "\t" + c1)
    print('save data into tables files')


def main():
    for csv_link in range(3, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        # driver.get(url)
        # time.sleep(1)
        soup = get_url(url)
        Product_title = product_detail(url, soup)
        # get_specs(soup, url, Product_title)


main()
