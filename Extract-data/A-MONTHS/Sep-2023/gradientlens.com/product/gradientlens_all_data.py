import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/gradientlens.com/data/gradientlens-all-data.csv", 'a', encoding='utf-8')


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
    # time.sleep(3)
    return driver


def product_detail(url, soup):
    print('Soup')

    l3_name = []
    bread = soup.find_all('span', {"class": "breadcrumbs"})
    for i in bread:
        cleaned_text = ' '.join(i.text.strip().split())
        l3_name.append(cleaned_text)
    print('l3_name.....', l3_name)

    try:
        product_title = soup.find('h1', class_="product_title").text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('Not Found')
    try:
        price = soup.find('p', {"class": "price"}).text.strip()
        print('price...', price)
    except AttributeError:
        price = ''
        print('object has no attribute', 'price')

    models = soup.find("div", {"class": "product_meta"}).text.strip().split("\n")
    model = models[0].split(':')[1].strip()
    print('model...', model)
    category = models[1].split(':')[1].strip()
    print('category...', category)

    features_1 = []
    for features in soup.find_all('div', class_="woocommerce-product-details__short-description"):
        features_1.append(features.text)
    print('features_1.....', features_1)

    description = []
    for desc in soup.find('div', {"id": "tab-description"}).find_all('p'):
        description.append(desc.text.strip().replace("\n", ""))
    print('description.....', description)

    try:
        datasheet = []
        table_data = soup.find('div', class_="wctm-teb-content").find('p').find_all('a')
        for tab_pdf in table_data:
            tab_pdf_data = tab_pdf.get('href')
            if 'add-to-cart' not in tab_pdf_data:
                datasheet.append(tab_pdf_data)
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = ''
        print('')
    try:
        download_software = soup.find('div', {"class": "wctm-teb-content"}).findAll(class_="panel entry-content wc-tab")[3]
    except IndexError:
        download_software = ''
        print('list index out of range')

    try:
        text_type = download_software.text.strip().replace("\n", "")
        print('text_type.....', text_type)
    except AttributeError:
        text_type = ''
        print()

    try:
        image_type = download_software.find('img').get('src')
        print('image_type.....', image_type)
    except AttributeError:
        image_type = ''
        print()

    try:
        href_type_exe = download_software.find('a').get('href')
        print('href_type.....', href_type_exe)
    except AttributeError:
        href_type_exe = ''
        print()

    # --------------------------------------- Images------------------------------------------------
    try:
        image = []
        for img_1 in soup.find('div', class_="product-gallery").find_all('a'):
            image.append(img_1.get('href'))
        # print("Images....", image)
    except AttributeError:
        image = ''
        print('object has no attribute')
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
        "Mpn": model,
        "Grainger_Sku": category,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Image_Name": image_type,
        "Product_Detail": description,
        "Features": features_1,
        "Accessories": href_type_exe,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video_d,
        # "Quantity": stock,
        "Price(usd)": price,
        "Cross_Reference": text_type,
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


def get_specs(url, soup, product_title):
    print('Tables')
    try:
        attr_name = []
        attr_value = []
        count_loop = 0
        table = soup.find('div', {"id": "tab-670"}).find_all('td')
        for th in table:
            count_loop += 1
            tab = str(th.text).replace('\r', '').replace('\n', ' ')
            if count_loop % 2 != 0:
                attr_name.append(tab)
            else:
                attr_value.append(tab)
        for a, b in zip(attr_name, attr_value):
            print(a, "..........", b)
            save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/gradientlens.com/data/gradientlens_specs.txt", 'a+', encoding='utf-8')
            save.write('\n' + url + " \t" + product_title + "\t" + a + "\t" + b)
    except AttributeError:
        print("'NoneType' object has no attribute 'table'")


    try:
        table1 = soup.find('table', {"class": "table pricing-table"}).find_all('tr')
        for td in table1:
            td_d = td.find_all('td')
            table_td = [ts.text for ts in td_d if ts.text.strip()]
            if table_td:
                table_save = "\t".join(table_td)
                # print(table_save)
                save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/gradientlens.com/data/gradientlens_specs.txt", 'a+', encoding='utf-8')
                save.write('\n' + url + " \t" + product_title + "\t" + table_save)
    except AttributeError:
        print("'NoneType' object has no attribute 'table'")




    #     if table_td:
    #         table_data.append(table_td)
    # if table_data:
    #     table_headers = []
    #     print(tabulate(table_data, headers=table_headers, tablefmt="grid"))



def main():
    url_link_count = 1
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/gradientlens.com/url/gradientlens_product_url.csv")['url']
    for url in url_link[1:]:
        url_link_count += 1
        print("Product-Length...", url_link_count)
        print("Product-Urls......", url)
        soup = Get_Soup_Url(url)
        product_title = product_detail(url, soup)
        get_specs(url, soup, product_title)

        # selenium calling here
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)
    print('loop End')


main()
