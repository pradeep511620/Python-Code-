import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
from itertools import zip_longest

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# /var/www/html/webscr/destination_dir
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Kukzall.com/data/Kukzall-all-data.csv", 'a',
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
        bread = soup.find("div", {"class": "breadcrumb"}).find_all('li')
        for l3 in bread:
            l3_name.append(l3.text.strip())
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = "N/A"
        print('l3_name.....', l3_name)

    # ------------------------------------------------ Title -----------------------------------------------------------
    try:
        product_title = soup.find("div", {"class": "product-single__box__block--title"}).h1.text.strip()
        print('product_title.....', product_title)
    except (AttributeError, IndexError):
        product_title = "N/A"
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     mor_data = []
    #     for skus in soup.find("div", {"class": "product_meta"}).find_all('span'):
    #         mor_data.append(skus.text.strip())
    #     # print(mor_data)
    # except (AttributeError, IndexError):
    #     mor_data = "N/A"
    # try:
    #     category = mor_data[-1]
    #     print('category.....', category)
    # except IndexError:
    #     category = "N/A"
    #     print('category.....', category)


    try:
        sku = soup.find('div', {"data-sku-label": "SKU: "}).text.strip()
        print('sku.....', sku)
    except IndexError:
        sku = "N/A"
        print('sku.....', sku)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find("div", {"class": "price__text"}).text.strip().replace("\n", ">>")
        print('price.....', price)
    except AttributeError:
        price = "N/A"
        print('price.....', price)

    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = []
        for des in soup.find("div", {"class": "product-single__box__block product-single__box__block--description"}).find_all("p"):
            description.append(des.text.strip())
        print('description.....', description)
    except (AttributeError, IndexError):
        description = "N/A"
        print('description.....', description)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    try:
        drow_image = []
        for draw in soup.find_all('img', {'class': 'image-with-text__media-img image-with-text__media-img--crop'}):
            draw_tag = draw.get("src")
            drow_image.append(draw_tag)
        print('drow_image.....', drow_image)
    except AttributeError:
        drow_image = "N/A"
        print('drow_image.....', drow_image)

    # ------------------------------------------------------------------------------------------------------------------

    # print(soup.prettify())

    # ------------------------------------------------------------------------------------------------------------------
    try:
        feature = []
        for product_feature in soup.find_all('div', {"class": "image-with-text__text rte"}):
            feature.append(product_feature.text.strip())
        print('feature.....', feature)
    except (AttributeError, IndexError):
        feature = "N/A"
        print('feature.....', feature)

    # ------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Images  -----------------------------------------------------------
    try:
        image = []
        for img_tag in soup.find_all("img", {"class": "media-gallery__thumb-image"}):
            href = img_tag.get('srcset')
            image.append(href)
        image = list(set(image))
        while len(image) < 5:
            image.append('')
        image = image[:5]
        print("Images....", image)
    except AttributeError:
        image = ['N/A'] * 5
        print('object has no attribute ... image')


    # --------------------------------------------- Datasheet ----------------------------------------------------------
    # try:
    #     datasheet = []
    #     for pdf in soup.find("div", {"id": "tab-attached-documents"}).find_all("a"):
    #         pdf_tag = pdf.get("href")
    #         # if "youtube" not in pdf_tag:
    #         datasheet.append("http://www.kwikool.com" + pdf_tag)
    #     datasheet = list(set(datasheet))
    #     print('datasheet.....', datasheet)
    # except (AttributeError, IndexError):
    #     datasheet = "N/A"
    #     print('datasheet.....', datasheet)

    # ----------------------------------------------- Video ------------------------------------------------------------
    try:
        video = []
        for video_link in soup.find_all("video", {"class": "home-carousel__video-video"}):
            video.append(video_link.get("src"))
        print('video.....', video)
    except AttributeError:
        video = 'N/A'
        print('video.....', video)
    # ------------------------------------------------ Url -------------------------------------------------------------

    # try:
    #     related_url = []
    #     for related_tag in soup.find("div", {"id": "related-products"}).find_all("a"):
    #         href_tag = related_tag.get("href")
    #         related_url.append(href_tag)
    #     related_url = list(set(related_url))
    #     print('related_url.....', related_url)
    # except AttributeError:
    #     related_url = "N/A"
    #     print('related_url.....', related_url)

    print("-----------------------------------------------------------------------------------------------------------")
    print(" ")
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
        "Mpn": sku,
        # "Grainger_Sku": category,
        # "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        "Image_Name": drow_image,
        "Product_Detail": description,
        "Features": feature,
        # "Accessories": part,
        # "Datasheet": datasheet,
        # "Accessories_1": related_url,
        # "Uses": top_manual,
        "Video_Url": video,
        # "Quantity": stock,
        "Price(usd)": price,
        # "Quantity": order,
        # "Remarks": Categories,
        # "Cross_Reference": standard,
        "Url": url,

    }]  # save data here

    Data_Save(row, mylist)
    return product_title, sku

    # except Exception as e:
    #     print('Error...', e)
    # send_email(f'Error... {e}')


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, product_title, sku):
    #   /var/www/html/webscr/destination_dir
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Kukzall.com/data/Kukzall-specs.txt", 'a+', encoding='utf-8')
    print('Tables ****************************************************************************************************')
    attr_name = []
    attr_value = []


    for table in soup.find('table', {"class": "tablepress"}).find_all("tr"):
        tab = table.getText(separator=">>", strip=True).split(">>")
        if tab:
            table_rows = "\t".join(tab)
            print(table_rows)
            save.write(f"{url}\t{sku}\t{product_title}\t{table_rows}\n")

    # for td in soup.find_all(class_="label_text"):
    #     tab_1 = td.text.strip()
    #     attr_name.append(tab_1)
    #
    # for th in soup.find_all(class_="get_value"):
    #     tab_2 = th.text.strip().replace("\n", "").replace("N/A ", "")
    #     attr_value.append(tab_2)


    # for name, value in zip_longest(attr_name, attr_value):
    #     print(name, "::", value)
    #     save.write(f"{url}\t{sku}\t{product_title}\t{name}\t{value}\n")




# ----------------------------------------------------------------------------------------------------------------------




def main():
    #   /var/www/html/webscr/source_dir/
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Kukzall.com/url/Product-url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))
    i = 9
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        soup = Get_Soup_Url(url)
        product_title, sku = product_detail(url, soup)
        # Get_Specs_Table(url, soup, product_title, sku)

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
