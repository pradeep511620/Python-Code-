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
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Dynashop.com/data/Dynashop-all-data.csv", 'a',
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
        bread = soup.find("div", {"id": "breadcrumbs"})
        for l3 in bread:
            l3_name.append(l3.text.strip())
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = "N/A"
        print('l3_name.....', l3_name)

    # ------------------------------------------------ Title -----------------------------------------------------------
    try:
        product_title = soup.find("h1", {"class": "product_title"}).text.strip()
        print('product_title.....', product_title)
    except NoSuchElementException:
        product_title = "N/A"
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find("span", {"class": "woocommerce-Price-amount amount"}).text.strip()
        print('price.....', price)
    except AttributeError:
        price = "N/A"
        print('price.....', price)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        sku = soup.find("span", {"class": "sku_wrapper"}).text.strip()
        print('sku.....', sku)
    except AttributeError:
        sku = "N/A"
        print('sku.....', sku)

    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = soup.find('div', {"id": "tab-description"}).find("p").text.strip().replace("\n", " >> ")
        print('description.....', description)
    except (AttributeError, IndexError):
        description = "N/A"
        print('description.....', description)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    try:
        Categories = soup.find("span", {"class": "posted_in"}).text.strip().replace("\n", ">>")
        print('Categories.....', Categories)
    except (AttributeError, IndexError):
        Categories = 'N/A'
        print('Categories.....', Categories)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        top_manual = soup.find('div', {"id": "tab-description"}).find_all("p")[2].text.strip().replace("\n", ">>")
        print('top_manual.....', top_manual)
    except (AttributeError, IndexError):
        top_manual = "N/A"
        print('top_manual.....', top_manual)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        part = soup.find('div', {"id": "tab-description"}).find_all("p")[3].text.strip().replace("\n", ">>")
        print('part.....', part)
    except (AttributeError, IndexError):
        part = "N/A"
        print('part.....', part)

    # ------------------------------------------------------------------------------------------------------------------

    try:
        service_repair = soup.find('div', {"id": "tab-description"}).find_all("p")[-2].text.strip().replace("\n", ">>")
        print('service_repair.....', service_repair)
    except (AttributeError, IndexError):
        service_repair = "N/A"
        print('service_repair.....', service_repair)

    # ---------------------------------------------  Images  -----------------------------------------------------------
    try:
        image = []
        table = soup.find("div", {"class": "woocommerce-product-gallery__wrapper"})
        img_links = table.find_all('img')
        for img_link in img_links:
            href = img_link.get('src')
            if ".jpg" in href:
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


    # ----------------------------------------------- Video ------------------------------------------------------------


    # ------------------------------------------------ Url -------------------------------------------------------------
    try:
        related_url = []
        for relat in soup.find_all('section', {"class": "related products wt-related-products"}):
            related_href = relat.find_all('a')
            for url_related in related_href:
                href_tag = url_related.get('href')
                if "dynashop.co.uk/product/" in href_tag:
                    related_url.append(href_tag)
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
        "Mpn": sku,
        "Grainger_Sku": Categories,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": dimationsss,
        "Product_Detail": description,
        # "Features": feature,
        "Accessories": part,
        # "Datasheet": datasheet,
        # "Item_Name": dimationsss,
        "Accessories_1": related_url,
        "Uses": top_manual,
        # "Video_Url": video,
        # "Quantity": stock,
        "Price(usd)": price,
        # "Quantity": logo,
        # "Remarks": Categories,
        "Cross_Reference": service_repair,
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
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Dynashop.com/data/Dynashop-specs.txt", 'a+', encoding='utf-8')
    print('Tables')

    attr_name = []
    attr_value = []
    for th in soup.find_all('th', {"class": "woocommerce-product-attributes-item__label"}):
        ths = th.text.strip().replace("\n", ">>")
        attr_name.append(ths)
    for td in soup.find_all('td', {"class": "woocommerce-product-attributes-item__value"}):
        tds = td.text.strip().replace("\n", ">>")
        attr_value.append("rp_" + tds)
    for name, value in zip(attr_name, attr_value):
        print(name, "::", value)
        save.write(f"{url}\t{sku}\t{product_title}\t{name}\t{value}\n")
    print('save data in table')


# ----------------------------------------------------------------------------------------------------------------------


def main():
    #   /var/www/html/webscr/source_dir/
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Dynashop.com/url/Dynashop-product-url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))
    i = 10863
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        soup = Get_Soup_Url(url)
        product_title, product_title_1 = product_detail(url, soup)
        Get_Specs_Table(url, soup, product_title, product_title_1)

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
