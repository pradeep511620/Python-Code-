import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/xpower.com/data/xpower-all-data.csv", 'a',
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
    # time.sleep(3)
    return driver


def product_detail(url, soup):
    print('Soup')

    l3_name = []
    bread = soup.find_all('nav', {"class": "woocommerce-breadcrumb"})
    for l3 in bread:
        cleaned_text = ' '.join(l3.text.strip().split())
        l3_name.append(cleaned_text)
    print('l3_name.....', l3_name)

    try:
        product_title = soup.find('h1', class_="product-title").text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute ... product_title')

    try:
        sku = soup.find("span", {"class": "sku_wrapper"}).text.strip()
        print('sku...', sku)
    except AttributeError:
        sku = ''
        print('object has no attribute ... sku')

    try:
        category = soup.find('h5').text.strip()
        print('category...', category)
    except AttributeError:
        category = ''
        print('object has no attribute ... category')

    try:
        features_1 = []
        for features in soup.find('div', class_="product-short-description").find_all('li'):
            features_1.append(features.text)
        print('features_1.....', features_1)
    except AttributeError:
        features_1 = ''
        print('object has no attribute ... features_1')

    description = []
    for desc in soup.find('div', {"id": "tab-description"}).find_all('p'):
        description.append(desc.text.strip().replace("\n", ""))
    print('description.....', description)

    try:
        datasheet = []
        for pdf in soup.find('div', {"class": "product-support"}).find_all('a'):
            datasheet.append(pdf.get('href'))
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = ''
        print('object has no attribute ... datasheet')

    try:
        video = soup.find('div', class_="video").find('a').get('href')
        print('video...', video)
    except AttributeError:
        video = ''
        print('object has no attribute ... video')

    # --------------------------------------- Images------------------------------------------------
    try:
        unique_images = set()
        image = []
        for img_1 in soup.find_all('div', {"class": "product-gallery"}):
            img_2 = img_1.find_all('img')
            for img2 in img_2:
                src = img2.get('src')
                if src not in unique_images:
                    unique_images.add(src)
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
        "Grainger_Sku": sku,
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
        "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price,
        "Cross_Reference": category,
        "Url": url,

    }]  # save data here

    data_save(row, mylist)
    return sku


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(url, soup, sku):
    print('Tables')

    try:
        attr_name = []
        attr_value = []
        table = soup.find('table', {"class": "rwd-table"}).find_all('tr')
        for th in table:
            td = th.text.strip().replace('\n', '>>')
            tab = td.split('>>')
            attr_name.append(tab[0])
            attr_value.append(f'rp_{tab[1]}')
        for a, b in zip(attr_name, attr_value):
            print(a, "..........", b)
            save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/xpower.com/data/xpower_specs.txt", 'a+',
                        encoding='utf-8')
            save.write('\n' + url + " \t" + sku + "\t" + a + "\t" + b)
        print('save data into table files')
    except AttributeError:
        print("'NoneType' object has no attribute 'table'")

    #     if table_td:
    #         table_data.append(table_td)
    # if table_data:
    #     table_headers = []
    #     print(tabulate(table_data, headers=table_headers, tablefmt="grid"))


def main():
    url_link_count = 192
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/xpower.com/url/xpower_product_url.csv")[
        'url']
    for url in url_link[192:]:
        url_link_count += 1
        print("Product-Length...", url_link_count)
        print("Product-Urls......", url)
        soup = Get_Soup_Url(url)
        sku = product_detail(url, soup)
        get_specs(url, soup, sku)

        # selenium calling here
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)
    print('loop End')


if __name__ == "__main__":
    main()
