# import mysql.connector

import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/wpg.com/data/wpg-all-data.csv", 'a',
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
    bread = soup.find_all('ul', {"class": "crumbs"})
    for l3 in bread:
        cleaned_text = ' '.join(l3.text.strip().split('/'))
        l3_name.append(cleaned_text)
    print('l3_name.....', l3_name)

    try:
        product_title = soup.find('h1', class_="product-name").text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute ... product_title')

    sku_models = []
    for sku_model in soup.find_all("div", {"class": "sku"}):
        sku_models.append(sku_model.text.strip())
    try:
        stock = sku_models[0]
        print('Stock.....', stock)
    except IndexError:
        stock = ''
        print('object has no attribute ... Stock')

    try:
        model = sku_models[1]
        print('model.....', model)
    except IndexError:
        model = ''
        print('object has no attribute ... model')

    try:
        price = soup.find('div', {"class": "product-price"}).text.strip()
        print('price.....', price)
    except AttributeError:
        price = ''
        print('object has no attribute ... model')



    features_details_data = []
    feature = soup.find_all('div', class_="product-content")
    for features in feature:
        features_d = features.find_all('li')
        for features_details in features_d:
            features_details_data.append(features_details.text.strip())
    print("features_details_data.....", features_details_data)

    description = []
    for desc in soup.find('div', {"class": "product-content"}).find_all('p'):
        description.append(desc.text.strip().replace("\n", ""))
    print('description.....', description)

    try:
        datasheet = []
        pdf = soup.find_all('div', class_="product-content")
        for pdfs in pdf:
            pdf_d = pdfs.find_all(class_="attribute")
            for a_tag in pdf_d:
                a_tags = a_tag.find_all('a')
                for tag in a_tags:
                    datasheet.append(tag.get('href'))
        print('datasheet....', datasheet)
    except AttributeError:
        datasheet = ''
        print('object has no attribute ... datasheet')

    datasheet = []
    for pdf in soup.find_all('tr', class_="grouped-product-item"):
        for pds in pdf.find_all('a'):
            datasheet.append(pds.get('href'))
    print('pdf_href_tag....', datasheet)

    # video_d = []
    # try:
    #     video = soup.find('div', class_="box-description").find(class_='center').find_all('iframe')
    #     for v in video:
    #         video_d.append(v['src'])
    #     print('video...', video_d)
    # except AttributeError:
    #     video = soup.find(class_='product-details').find('div', class_="product-content").find_all('iframe')
    #     for v in video:
    #         video_d.append(v['src'])
    #     print('video...', video_d)
    #     # print('object has no attribute ... video')

    video_d = []
    try:
        video_div = soup.find('div', class_="box-description").find(class_='center')
        if video_div:
            video = video_div.find_all('iframe')
            for v in video:
                video_d.append(v['src'])
            print('video...', video_d)
    except AttributeError:
        try:
            product_details = soup.find(class_='product-details')
            if product_details:
                product_content = product_details.find('div', class_="product-content")
                if product_content:
                    video = product_content.find_all('iframe')
                    for v in video:
                        video_d.append(v['src'])
                    print('video...', video_d)
        except AttributeError:
            print('No video found on this page.')

    try:
        img_1 = soup.find('div', class_="product-media").find('img').get('src')
        print('image...', img_1)
    except AttributeError:
        img_1 = ''
        print('object has no attribute ... img_1')

    # --------------------------------------- Images------------------------------------------------
    try:
        image = []
        for img_2 in soup.find('div', class_="product-media").find_all('a'):
            image.append(img_2.get("href"))
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
        "Mpn": model,
        "Grainger_Sku": stock,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": imgs,
        "Image_URL_2": imgs1,
        "Image_URL_3": imgs2,
        "Image_URL_4": imgs3,
        "Image_URL_5": imgs4,
        "Image_Name": img_1,
        "Product_Detail": description,
        "Features": features_details_data,
        # "Accessories": href_type_exe,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        "Video_Url": video_d,
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


def get_specs(url, soup, product_title):
    """    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test",
        port=3306
    )
    print('local database connected')
    cursor = conn.cursor()
            # cursor.execute("INSERT INTO scrape_files (url, name, value) VALUES (%s, %s, %s)", (url, a, b))
    conn.commit()
    conn.close()
    """         # save data into database using python


    attr_name = []
    attr_value = []
    span = soup.find_all('span', {"class": "attribute-label"})[3:]
    for ths in span:
        th = ths.text.strip()
        attr_name.append(th)

    for tds in span:
        td = tds.find_next_sibling(string=True).strip()
        attr_value.append(td)

    for a, b in zip(attr_name, attr_value):
        print(a, "...", b)
        save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/wpg.com/data/wpg_specs1.txt", 'a+', encoding='utf-8')
        save.write('\n' + url + " \t" + product_title + "\t" + a + "\t" + b)
    print('save data into table files ................1')

    try:
        data = []
        for tr in soup.find_all('tr', class_="grouped-product-item"):
            s = []
            for td in tr.find_all('td'):
                row_data = td.text.strip()
                s.append(row_data.replace('\t', '').replace('\n', ''))
                data.append(s)
        for tds in data:
            pass
            # print(tds)
            save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/wpg.com/data/wpg_specs2.txt", 'a+', encoding='utf-8')
            save.write('\n' + url + "\t" + product_title + "\t".join(tds))
        print('save data into table files ................2')
    except:
        print('')




    #         save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/wpg.com/data/wpg_specs.txt", 'a+',
    #                     encoding='utf-8')
    #         save.write('\n' + url + " \t" + sku + "\t" + a + "\t" + b)
    #     print('save data into table files')
    # except AttributeError:
    #     print("'NoneType' object has no attribute 'table'")



def main():
    url_link_count = 796
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/wpg.com/url/wpg_product_url.csv")[
        'url']
    for url in url_link[796:]:
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
