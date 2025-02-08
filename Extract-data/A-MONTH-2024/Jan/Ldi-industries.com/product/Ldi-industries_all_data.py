import json
import re
from itertools import zip_longest
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# /var/www/html/webscr/destination_dir
save_files = open(
    "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Ldi-industries.com/data/Ldi-industries-all-data.csv", 'a',
    encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def Get_Page_Source(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(options=opts)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    return soup


def Get_Soup_Url(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def Get_Driver_Urls(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=opts)
    # driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    return driver


def send_email(msg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = ["nkmishra@nextgenesolutions.com", "raptorsupplyuk@gmail.com", ]
    # sender_email = ["nkmishra@nextgenesolutions.com", "nirbhay@raptorsupplies.com", "tajender@raptorsupplies.com"]
    smtp_username = "raptorsupplyuk@gmail.com"
    smtp_password = "unwkbryielvgwiuk"
    # "unwk bryi elvg wiuk"
    message = MIMEMultipart()
    message["From"] = smtp_username
    message["To"] = ','.join(sender_email)
    message["Subject"] = "Script Execution Status"

    body = msg
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, sender_email, message.as_string())
    print("Email sent successfully")


# mgs = "Your web scraping script has been started"
# send_email(mgs)
# print(mgs)


def product_detail(url, soup):
    print('soup')

    # --------------------------------------------- BreadCrumb ---------------------------------------------------------
    try:
        l3_name = []
        bread = soup.find("div", {"id": "breadCrumbContainer"}).find_all("li")
        for l3 in bread:
            l3_name.append(l3.text.strip())
        print('l3_name.....', l3_name)
    except (AttributeError, TypeError):
        l3_name = "N/A"
        print('l3_name.....', l3_name)

    # ------------------------------------------------ Title -----------------------------------------------------------
    try:
        product_title = soup.find("div", {"id": "titleBarContainer"}).h1.text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = "N/A"
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     price = soup.find("span", {"class": "woocommerce-Price-amount amount"}).text.strip()
    #     print('price.....', price)
    # except AttributeError:
    #     price = "N/A"
    #     print('price.....', price)

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     sku = soup.find("span", {"class": "sku_wrapper"}).text.strip()
    #     print('sku.....', sku)
    # except AttributeError:
    #     sku = "N/A"
    #     print('sku.....', sku)

    # ------------------------------------------------------------------------------------------------------------------
    caution = []
    Standard_Materieals = []
    Standard_features = []
    for mor_details in soup.find('div', class_='productDescription').find_all("p"):
        # print(mor_details.text.strip())
        if 'Standard Features:' in mor_details.text.strip():
            stand1 = mor_details.find_next("ul").text.strip().replace("\n", ">>")
            Standard_features.append(stand1)

        elif 'Standard Materieals:' in mor_details.text.strip() or 'Standard Materials:' in mor_details.text.strip():
            Standard = mor_details.find_next("ul").text.strip().replace("\n", ">>")
            Standard_Materieals.append(Standard)

        elif 'Caution:' in mor_details.text.strip():
            cut_det = mor_details.find_next('ul').text.strip().replace("\n", ">>")
            caution.append(cut_det)

    print('Standard_features.....', Standard_features)
    print('Standard_Materieals.....', Standard_Materieals)
    print('caution.....', caution)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = []
        for mor_details_1 in soup.find('div', class_='productDescription').find_all("p"):
            description.append(mor_details_1.text.strip())
        print('description.....', description)
    except (AttributeError, IndexError):
        description = "N/A"
        print('description.....', description)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    try:
        feature = []
        feature_data = soup.find("div", {"id": "pdtDesc3"}).find_all('li')
        for fea in feature_data:
            feature.append(fea.text.strip())
        print('feature.....', feature)
    except (AttributeError, IndexError):
        feature = "N/A"
        print('feature.....', feature)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Images  -----------------------------------------------------------
    try:
        image = []
        img_links = soup.find(class_='photos').find_all("img")
        for img_link in img_links:
            href = img_link.get('src').split("?")[0]
            image.append("https://www.ldi-industries.com/" + href)
        image = list(set(image))
        while len(image) < 5:
            image.append('')
        image = image[:5]
        print("Images....", image)
    except AttributeError:
        image = ['N/A'] * 5
        print('object has no attribute ... image')

    # --------------------------------------------- Datasheet ----------------------------------------------------------
    try:
        datasheet = []
        for pdf in soup.find('div', class_="files").find_all("a"):
            pdf_list = pdf.get('href')
            datasheet.append("https://www.ldi-industries.com/" + pdf_list)
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = "N/A"
        print('datasheet.....', datasheet)

    # ----------------------------------------------- Video ------------------------------------------------------------
    # try:
    #     video = soup.find('div', {"id": "videos"}).find("iframe").get('src')
    #     print('video.....', video)
    # except AttributeError:
    #     video = "N/A"
    #     print('video.....', video)

    # ------------------------------------------------ Url -------------------------------------------------------------
    try:
        related_url = []
        for relat in soup.find_all('div', {"class": "items"}):
            related_href = relat.find_all('a')
            for url_related in related_href:
                href_tag = url_related.get('href')
                # if "dynashop.co.uk/product/" in href_tag:
                related_url.append("https://www.ldi-industries.com/" + href_tag)
        print('related_url.....', related_url)
    except AttributeError:
        related_url = "N/A"
        print(related_url)

    # ------------------------------------------------------------------------------------------------------------------
    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories_1", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]
    # save data here

    row = [{
        # "Mpn": sku,
        # "Grainger_Sku": Categories,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": dimationsss,
        "Product_Detail": description,
        "Features": feature,
        # "Accessories": part,
        "Datasheet": datasheet,
        # "Item_Name": dimationsss,
        "Accessories_1": Standard_features,
        "Uses": Standard_Materieals,
        # "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price,
        "Accessories": related_url,
        # "Remarks": Categories,
        "Cross_Reference": caution,
        "Url": url,

    }]  # save data here

    Data_Save(row, mylist)
    return product_title

    # except Exception as e:
    #     print('Error...', e)
    # send_email(f'Error... {e}')


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, product_title):
    #   /var/www/html/webscr/destination_dir
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Ldi-industries.com/data/Ldi-industries-specs.txt",
                'a+', encoding='utf-8')
    print('Tables ****************************************************************************************************')
    table_t = []
    img_table = []
    unique_images = set()
    try:
        table_img = soup.find("table", {"id": "super-product-table"}).find_all('img')

        for img_tag in table_img:
            img_url = img_tag.get("src")
            # img_table.append(img_url)
            if img_url not in unique_images:
                unique_images.add(img_url)
    except AttributeError:
        unique_images = ''
        print(f"{'NoneType object has no attribute find_all'}")



# ----------------------------------------------------------------------------------------------------------------------




def main():
    #   /var/www/html/webscr/source_dir/
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Ldi-industries.com/url/Ldi-industries-product-url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))
    i = 0
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        soup = Get_Soup_Url(url)
        product_title = product_detail(url, soup)
        # Get_Specs_Table(url, soup, product_title)

        # selenium calling here
        # driver = Get_Driver_Urls(url)
        # product_title = product_detail(url, driver)
        # Get_Specs_Table(url, driver, product_title)

    print('loop End')

    # msg = "Your web scraping script has completed "
    # send_email(msg)
    # print(msg)


if __name__ == "__main__":
    main()
