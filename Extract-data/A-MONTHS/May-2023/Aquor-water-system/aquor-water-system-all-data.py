import csv

import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

save_files = open("aquor-water-system-all-data.csv", 'a', encoding='utf-8')

with open('aquor-water-system-urls.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)


def get_url(url):
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

#   -------------------------------------------------------------------------------------------------------------------


def get_data(url, soup):
    try:
        l3_name = []
        for k in soup.find_all('nav', {"class": "breadcrumb_navigation"}):
            l3_name.append(k.text.strip().replace('\n', ''))
        print('l3_name...', l3_name)
    except AttributeError:
        l3_name = ''
        print('Not Found')

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        Product_title = soup.find('h1', {"class": "product__title"}).text.strip()
        print('title...', Product_title)
    except:
        Product_title = ''
        pass

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        sku = soup.find('div', {"class": "product_sku"}).find('span').text.strip()
        print("Sku-number...", sku)
    except:
        sku = ''

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find('div', {"class": "price__regular"}).find('h5').text.strip()
        print("price...", price)
    except:
        price = ''

    #   ---------------------------------------------------------------------------------------------------------------

    image = []
    for img in soup.find('div', {"class": "product__media-wrapper"}).find_all('img'):
        images = img.get('src')
        if images is not None:
            image.append("https:" + images)
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

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        desc = soup.find('div', {"class": "product__description"}).find('p').text.strip().replace('\n', '')
        print("Description...", desc)
    except:
        desc = ''
        print("Not Found")

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        for pdf in soup.find('div', {"class": "pdf-file"}).find_all('a'):
            datasheet.append(pdf.get("href"))
        print('datasheet...', datasheet)
    except AttributeError:
        datasheet = ''
        print("Not Found")

    #   ---------------------------------------------------------------------------------------------------------------
    try:
        related_url = []
        for related in soup.find('div', class_="complete-pro-slider").find_all('a'):
            related_url.append("https://www.aquorwatersystems.com"+related.get("href"))
        print(related_url)
    except AttributeError:
        related_url = ''
        print("NON Type")

    """    # dat = soup.find('script', type='application/ld+json').text
    json_data = json.loads(soup.find('script', type='application/ld+json').text)
    for data in json_data['offers']:
        print(data['sku'], ">>>>>>>>>>>>", data['url'], ">>>>>>>>>>>>>>", data['price'])

    print(json_data)
"""  # using json
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
        "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": Product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Product_Detail": desc,
        # "Features": feature,
        "Accessories": related_url,
        "Datasheet": datasheet,
        # "item_ID": item,
        "Price(usd)": price,
        "Url": url,

    }]

    data_save(row, mylist)
    return sku


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(soup, url, sku):
    try:
        inc = 0
        name = []
        value = []
        table = soup.find('div', class_='product-tech-space-inner').find_all('table')
        for j in table:
            td = j.find_all('td')
            # for jj in td:

            for tab in td:
                inc += 1
                if inc % 2 != 0:
                    name.append(tab.text.strip())
                else:
                    value.append(tab.text.strip())
            for i in range(len(value)):
                if isinstance(value[i], (int, float)):
                    value[i] = 'rp_' + str(value[i])
                elif isinstance(value[i], str) and value[i][0].isdigit():
                    value[i] = 'rp_' + value[i]
        for a, b in zip(name, value):
            print(a, "......", b)
            save = open('aquor-water-system-table.txt', 'a+', encoding='utf-8')
            save.write("\n" + url + "\t" + sku + "\t" + a + "\t" + b)
        print('save data into tables files')
    except IndexError:
        print('string index out of range')
    except AttributeError:
        print('Attribute error')

    #


def main():
    for csv_link in range(103, csv_length):
        url = csv_list[csv_link][0]
        print("Product-Length...", csv_link)
        print("Product-Urls......", url)
        soup = get_url(url)
        sku = get_data(url, soup)
        get_specs(soup, url, sku)


main()
