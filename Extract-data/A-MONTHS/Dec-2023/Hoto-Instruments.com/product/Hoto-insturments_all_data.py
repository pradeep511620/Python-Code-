import re
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# /var/www/html/webscr/destination_dir
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Dec-2023/Hoto-Instruments.com/data/Hoto-Instruments-all-data.csv", 'a',
                  encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def Get_Soup_Url(url):
    r = requests.get(url, headers=headers)
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
    # print('driver')
    print('soup')
    # try:

    # --------------------------------------------- BreadCrumb ---------------------------------------------------------
    l3_name = []
    try:
        bread = soup.find('div', {"class": "breadcrumb"})
        for l3 in bread:
            l3_name.append(l3.text.strip())
        l3_name = list(filter(None, l3_name))
        if not l3_name:
            l3_name = 'N/A'
        print('L3_name.....', l3_name)
    except AttributeError:
        l3_name = 'N/A'
        print('L3_name.....', l3_name)

    # ------------------------------------------------ Title -----------------------------------------------------------
    try:
        product_title = soup.find('h1', {"class": "product_title"}).text.strip().encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
        print('product_title.....', product_title)
    except AttributeError:
        product_title = "N/A"
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    try:
        short_description = soup.find('h2', {"itemprop": "description"}).text.strip().replace('\n', " >> ")
        print('short_description.....', short_description)
    except AttributeError:
        short_description = "N/A"
        print('short_description.....', short_description)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        feature = soup.find('div', {"id": "tab-standard-features"}).text.strip().replace('\n', " >> ")
        print('feature.....', feature)
    except AttributeError:
        feature = "N/A"
        print('feature.....', feature)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = soup.find('div', {"id": "tab-description"}).text.strip().replace("\n", ">>")
        print('description.....', description)
    except AttributeError:
        description = "N/A"
        print('description.....', description)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Images  -----------------------------------------------------------
    try:
        image = []
        table = soup.find('div', {"class": "images"})
        img_links = table.find_all('a')
        for img_link in img_links:
            # print(img_link)
            href = img_link.get('href')
            image.append(href)
        image = list(set(image))
        while len(image) < 5:
            image.append('')
        image = image[:5]

        print("Images....", image)
    except AttributeError:
        image = ['N/A'] * 5
        print('object has no attribute ... image')

    # try:
    #     image = []
    #     for image_link in soup.find_all('img', class_="overlay-ui"):
    #         image_links = image_link.get('src')
    #         if "data:image" not in image_links and 'logo' not in image_links:
    #             images_href = image_links.replace("//", "")
    #             image.append(images_href)
    #     while len(image) < 5:
    #         image.append('')
    #     image = image[:5]
    #     print('image.....', image)
    # except AttributeError:
    #     image = ['N/A'] * 5
    #     print('object has no attribute ... image')

    # --------------------------------------------- Datasheet ----------------------------------------------------------
    try:
        datasheet = []
        pdf_link = soup.find("div", {"class": "buttons-top"}).find_all('a')
        # print(pdf_link)
        for pdf in pdf_link:
            pdf_links = pdf.get('href')
            if ".pdf" in pdf_links:
                datasheet.append(pdf_links)
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = "N/A"
        print('datasheet.....', datasheet)

    # ----------------------------------------------- Video ------------------------------------------------------------
    try:
        video = []
        video_link = soup.find("div", {"class": "buttons-top"}).find_all('a')
        for video_href in video_link:
            video_links = video_href.get("href")
            if "youtube" in video_links:
                video.append(video_links)
        print('video.....', video)
    except AttributeError:
        video = 'N/A'
        print('object has no attribute ... video')

    # ------------------------------------------------ Url -------------------------------------------------------------
    # try:
    #     related_url = []
    #     for relat in soup.find_all('figure', {"class": "product-card_image"}):
    #         related_href = relat.find_all('a')
    #         for url_related in related_href:
    #             href_tag = url_related.get('href')
    #             related_url.append("https://www.velab.net"+href_tag)
    #     print('related_url.....', related_url)
    # except AttributeError:
    #     related_url = "N/A"
    #     print(related_url)

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
        # "Grainger_Sku": category,
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
        # "Accessories": accessories,
        "Datasheet": datasheet,
        # "Item_Name": dimationsss,
        # "Accessories_1": related_url,
        # "Uses": uses_d,
        "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Quantity":product_quantities,
        # "Remarks": warranty,
        "Cross_Reference": short_description,
        "Url": url,

    }]  # save data here

    Data_Save(row, mylist)
    return product_title

    # except Exception as e:
    #     print('Error...', e)
    # send_email(f'Error... {e}')


def Data_Save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, product_title):
    # def Get_Specs_Table(url, soup):
    #   /var/www/html/webscr/destination_dir
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Dec-2023/Hoto-Instruments.com/data/Hoto-Instruments-specs.txt", 'a+',
                encoding='utf-8')

    try:
        table = soup.find('table', {"class": "tablepress"}).find_all('tr')
        for td in table:
            tab = td.get_text(separator=">>", strip=True)
            table_row = tab.split(">>")
            if table_row:
                table_data = "\t".join(table_row)
                print(table_data)
                save.write(f"{url}\t{product_title}\t{table_data}\n")
        print('save data.....1')
    except AttributeError:
        print('table.....1 N/A')

    try:
        ranges = soup.find('div', {"id": "tab-specifications"}).find_all('tr')
        for td_1 in ranges:
            tab_1 = td_1.get_text(separator=">>", strip=True)
            table_row_1 = tab_1.split(">>")
            if table_row_1:
                table_data_1 = "\t".join(table_row_1).encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
                print(table_data_1)
                save.write(f"{url}\t{product_title}\t{table_data_1}\n")
    except AttributeError:
        print('table.....2 N/A')

    """ 
    try:
        table_count = 0
        attr_name = []
        attr_value = []
        table2 = soup.find('div', {"id": "tab-specifications"}).find_all('td')
        for td_1 in table2:
            table_count += 1
            tab_1 = td_1.text.strip()
            if table_count % 2 != 0:
                attr_name.append(tab_1)
            else:
                attr_value.append(tab_1)

        for a, b in zip(attr_name, attr_value):
            print(a, ":::::", b)
        #     save.write(f"{url}\t{product_title}\t{a}\t{b}\n")
        # print('save data.....2')
    except AttributeError:
        print('N/A')
"""



def main():
    #   /var/www/html/webscr/source_dir/
    url_link = \
    pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Dec-2023/Hoto-Instruments.com/url/Hoto-instruments-product-url.csv")[
        'URL']
    print("total url :-----", len(url_link))
    i = 0
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        soup = Get_Soup_Url(url)
        product_title = product_detail(url, soup)
        Get_Specs_Table(url, soup, product_title)
        # Get_Specs_Table(url, soup)


        # selenium calling here
        # driver = Get_Driver_Urls(url)
        # product_title = product_detail(url, driver)
        # Get_Specs_Table(url, driver)
    print('loop End')
    # msg = "Your web scraping script has completed "
    # send_email(msg)
    # print(msg)


if __name__ == "__main__":
    main()
