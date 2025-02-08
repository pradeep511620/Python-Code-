import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/Aircat.com/data/aircat-all-data.csv", 'a', encoding='utf-8')


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
    bread = soup.find_all('ul', {"class": "breadcrumbs-product-detail"})
    for l3 in bread:
        cleaned_text = ' '.join(l3.text.strip().split())
        l3_name.append(cleaned_text)
    print('l3_name.....', l3_name)

    try:
        product_title = soup.find('h2', class_="text-uppercase").text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute ... product_title')


    try:
        features_1 = []
        for features in soup.find('div', class_="tab-features-inner").find_all('li'):
            features_1.append(features.text)
        print('features_1.....', features_1)
    except AttributeError:
        features_1 = ''
        print('object has no attribute ... features_1')
    try:
        description = []
        for desc in soup.find('h4', {"class": "red text-semi"}):
            description.append(desc.text.strip().replace("\n", ""))
        print('description.....', description)
    except TypeError:
        description = ''
        print('object is not iterable')

    try:
        datasheet = []
        for pdf in soup.find('div', {"class": "four-buttons-others"}).find_all('a'):
            pdfs = pdf.get('href')
            datasheet.append(pdfs)
        # print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = ''
        print('object has no attribute ... datasheet')

    try:
        for pdf_1 in soup.find_all('div', class_="col-xs-6 pd-b-item-lg"):
            if pdf_1.find('button').get('onclick') is not None:
                pdf_2 = pdf_1.find('button').get('onclick').split("'")[1]
                datasheet.append(pdf_2)
                print('pdf_2...', pdf_2)
                continue
    except AttributeError:
        pdf_2 = ''
        print('object has no attribute ... video')
    print('datasheet.....', datasheet)
    # --------------------------------------- Images------------------------------------------------
    try:
        image = []
        for img_1 in soup.find_all('div', {"id": "productZoom"}):
            img_2 = img_1.find_all('img')
            for img2 in img_2:
                src = img2.get('src')
                image.append(src)
        print("Images....", image)
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
        # "Mpn": model,
        # "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        # "Image_Name": image_type,
        "Product_Detail": description,
        "Features": features_1,
        # "Accessories": href_type_exe,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price,
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


def get_specs(url, soup, product_title):
    print('Tables')

    try:
        attr_name = []
        attr_value = []
        for th in soup.find_all('div', {"class": "spec-name"}):
            ths = th.text.strip()
            attr_name.append(ths)

        for td in soup.find_all('div', {"class": "spec-value"}):
            tds = td.text.strip()
            attr_value.append(f'rp_{tds}')

        for a, b in zip(attr_name, attr_value):
            print(a, "..........", b)
            save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/Aircat.com/data/aircat_specs.txt", 'a+', encoding='utf-8')
            save.write(f"{url}\t{product_title}\t{a}\t{b}\n")
        print('save data into table files')
    except AttributeError:
        print("'NoneType' object has no attribute 'table'")

    #     if table_td:
    #         table_data.append(table_td)
    # if table_data:
    #     table_headers = []
    #     print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


def main():
    url_link_count = 53
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/Aircat.com/url/aircat_product_url.csv")[
        'url']
    for url in url_link[53:]:
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


if __name__ == "__main__":
    main()
