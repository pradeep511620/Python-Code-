import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

save_files = open(
    "C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/anamet_canada.com/data/anamet-canada-all-data.csv", 'a',
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
    bread = soup.find('ul', {"class": "uk-breadcrumb"}).find_all('li')
    for l3 in bread:
        l3_name.append(l3.text.strip())
        # cleaned_text = '/'.join(l3.text.strip().split())
        # l3_name.append(cleaned_text)
    print('l3_name.....', l3_name)

    try:
        product_title = soup.find('h1', class_="uk-h3").text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute ... product_title')

    try:
        mpn = soup.find('span', {"class": "pn"}).text.strip()
        print('mpn.....', mpn)
    except AttributeError:
        mpn = ''
        print('Not Found')

    try:
        price = soup.find('h2', {"id": "prodPrice"}).text.strip()
        print('price.....', price)
    except AttributeError:
        price = ''
        print('Not Found')

    try:
        features_1 = []
        features_1 = soup.find("p").text.strip()
        print('features_1.....', features_1)
    except AttributeError:
        features_1 = ''
        print('object has no attribute ... features_1')

    description = []
    for desc in soup.find('ul', {"class": "uk-list"}).find_all('li'):
        description.append(desc.text.strip().replace('\n', ">>"))
    print('description.....', description)

    try:
        datasheet = []
        pdf_details = soup.find('div', {"class": "uk-align-"}).find_all('a')
        for pdf in pdf_details:
            pdf_href = pdf.get('href')
            if pdf_href is not None:
                datasheet.append("https://www.anametcanada.com/" + pdf_href)
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = ''
        print('object has no attribute ... datasheet')

    # --------------------------------------- Images------------------------------------------------
    try:
        image = []
        for img_1 in soup.find_all('div', {"class": "wc_image"}):
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
        "Mpn": mpn,
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
        "Price(usd)": price,
        # "Cross_Reference": category,
        "Url": url,

    }]  # save data here

    data_save(row, mylist)
    return product_title, mpn


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(url, soup, product_title):
    print('Tables')
    with open('C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/anamet_canada.com/data/anamet-canada-table.txt',
              'a', encoding='utf-8') as data_write:

        try:
            table = soup.find('table', class_="uk-table").find_all('tr')
            for td in table:
                th_d = td.find_all('th')
                table_th = [th.text for th in th_d if th.text.strip()]
                if table_th:
                    table_saves = "\t".join(table_th)
                    print(table_saves)
                    data_write.write(f"\n{url}\t{product_title}\t{table_saves}")
                # continue
                td_d = td.find_all('td')
                table_td = [ts.text for ts in td_d if ts.text.strip()]
                if table_td:
                    table_save = '\t'.join(table_td)
                    print(table_save)
                    data_write.write(f"\n{url}\t{product_title}\t{table_save}")
            print('save data into table files...2')
        except AttributeError:
            print('unable to do anythings to get')



def main():
    url_link_count = 33
    url_link = pd.read_csv(
        "C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/anamet_canada.com/url/anamet_canada_product_url.csv")[
        'url']
    for url in url_link[33:]:
        url_link_count += 1
        print("Product-Length...", url_link_count)
        print("Product-Urls......", url)
        soup = Get_Soup_Url(url)
        product_title, mpn = product_detail(url, soup)
        get_specs(url, soup, product_title)

        # selenium calling here
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)
    print('loop End')


if __name__ == "__main__":
    main()
