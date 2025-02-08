import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/webshop.toolflo.com/data/webshop-all-data.csv", 'a',
                  encoding='utf-8')


def Get_Soup_Url(url):
    try:
        r = requests.get(url, timeout=30)  # Increase the timeout value as needed
        r.raise_for_status()
        soup = BeautifulSoup(r.content, "html.parser")
        return soup
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")




def Get_Driver_Urls(url):
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
    print('Soup')

    l3_name = []
    bread = soup.find('div', {"class": "breadcrumbs"}).find_all('a')
    for l3 in bread:
        # print(l3.text.strip().replace('\n', ">>"))
        # # cleaned_text = ''.join(l3.text.strip().split())
        l3_name.append(l3.text.strip())
    print('l3_name.....', l3_name)

    try:
        product_title = soup.find('div', class_="product_header_text").h1.text.strip()
        product_title = product_title.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute ... product_title')

    numbers_data = []
    for number in soup.find_all("div", {"class": "product_constant_fields"}):
        data = number.text.replace('\n', ">>").split('>>>>>>')
        cleaned_data = [string.strip('>>>>') for string in data]
        # data = [item.strip() for item in number.text.strip().split('\n') if item.strip()]
        numbers_data = cleaned_data
        # print('numbers_data....', numbers_data)

    try:
        Item = numbers_data[0]
        print('Item.....', Item)
    except IndexError:
        Item = ''
        print('List Index out of Range')

    try:
        UNSPSC = numbers_data[1]
        print('UNSPSC.....', UNSPSC)
    except IndexError:
        UNSPSC = 'Not Found'
        print('List Index out of Range')

    try:
        BrandName = numbers_data[-2]
        print('BrandName.....', BrandName)
    except IndexError:
        BrandName = ''
        print('List Index out of Range')

    try:
        ManufacturerNo = numbers_data[-1]
        print('ManufacturerNo.....', ManufacturerNo)
    except IndexError:
        ManufacturerNo = ''
        print('List Index out of Range')


    try:
        price = soup.find("div", {"class": "no-price-guest"}).text.strip()
        price = price.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
        print('price...', price)
    except AttributeError:
        price = ''
        print('object has no attribute ... price')

    try:
        shopping = soup.find('div', {"class": "shipping_details"}).text.strip().replace('\n', " >> ")
        print('shopping.....', shopping)
    except AttributeError:
        shopping = ''
        print('object has no attribute ... shopping')

    try:
        features_1 = []
        for features in soup.find_all('div', id="product_features"):
            features_1.append(features.text.strip().replace('\n', '>>'))
        print('features_1.....', features_1)
    except AttributeError:
        features_1 = ''
        print('object has no attribute ... features_1')

    try:
        datasheet = []
        for pdf in soup.find('div', {"id": "related_docs"}).find_all('a'):
            datasheet.append(pdf.get('href'))
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = ''
        print('object has no attribute ... datasheet')


    # --------------------------------------- Images------------------------------------------------
    try:
        image = []
        for img_1 in soup.find_all('div', {"class": "product_image_wrap"}):
            img_2 = img_1.find_all('img')
            for img_3 in img_2:
                image.append("https://webshop.toolflo.com"+img_3.get('src'))
        # print("Images....", image)
    except AttributeError:
        image = ''
        print('object has no attribute ... image')
    #
    try:
        imgs = image[0]
        print('imgs...', imgs)
    except IndexError:
        imgs = ''
        print('List out of index')
    try:
        imgs1 = image[1]
        print('imgs1...', imgs1)
    except IndexError:
        imgs1 = ''
        print('List out of index')
    try:
        imgs2 = image[2]
        print('imgs2...', imgs2)
    except IndexError:
        imgs2 = ''
        print('List out of index')
    try:
        imgs3 = image[3]
        print('imgs3...', imgs3)
    except IndexError:
        imgs3 = ''
        print('List out of index')
    try:
        imgs4 = image[4]
        print('imgs4...', imgs4)
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
        "Mpn": ManufacturerNo,
        "item_ID": UNSPSC,
        "Grainger_Sku": Item,
        "Item_Name": BrandName,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        # "Image_Name": image_type,
        # "Product_Detail": description,
        "Features": features_1,
        "Accessories": shopping,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video,
        # "Quantity": stock,
        "Price(usd)": price,
        # "Cross_Reference": category,
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
    print('Tables')

    try:
        attr_name = []
        attr_value = []
        count_number = 0
        table = soup.find('div', {"id": "product_specs"}).find_all('td')
        for th in table:
            count_number += 1
            td = th.text.strip().replace('\n', '>>')
            td = td.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
            if count_number % 2 != 0:
                attr_name.append(td)
            else:
                attr_value.append(td)
        for a, b in zip(attr_name, attr_value):
            # print(a, "..........", b)
            with open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/webshop.toolflo.com/data/webshop_specs.txt", 'a+', encoding='utf-8') as save:
                line_to_write = f"{url}\t{product_title}\t{a}\t{b}\n"
                save.write(line_to_write)
            # save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/webshop.toolflo.com/data/webshop_specs.txt", 'a+',encoding='utf-8')
            # save.write('\n' + url + " \t" + product_title + "\t" + a + "\t" + b)
        print('save data into table files')
    except AttributeError:
        print("'NoneType' object has no attribute 'table'")

    #     if table_td:
    #         table_data.append(table_td)
    # if table_data:
    #     table_headers = []
    #     print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


def main():
    url_link_count = 7215
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/webshop.toolflo.com/url/webshop_product_url.csv")['url']
    print(len(url_link))
    for url in url_link[7215:]:
        url_link_count += 1
        print("Product-Length...", url_link_count)
        print("Product-Urls......", url)
        soup = Get_Soup_Url(url)
        product_title = product_detail(url, soup)
        Get_Table_Specs(url, soup, product_title)

        # selenium calling here
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)
    print('loop End')


if __name__ == "__main__":
    main()
