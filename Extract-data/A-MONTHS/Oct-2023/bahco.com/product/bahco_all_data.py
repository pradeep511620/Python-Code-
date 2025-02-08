import json
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate

from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/bahco.com/data/bahco-all-data.csv", 'a',
                  encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def Get_Soup_Url(url):
    r = requests.get(url, headers=headers)
    # time.sleep(4)
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
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup


def send_email(msg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = ["nkmishra@nextgenesolutions.com", "nirbhay@raptorsupplies.com", "tajender@raptorsupplies.com"]
    smtp_username = "pk.s7723337@gmail.com"
    smtp_password = "yaeveqnzcbfafods"
    # "yaev eqnz cbfa fods"
    message = MIMEMultipart()
    message["From"] = smtp_username
    message["To"] = ','.join(sender_email)
    message["Subject"] = "Script Execution Completed"

    body = msg
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, sender_email, message.as_string())
    print("Email sent successfully")


send_email("Your web scraping script has been started")


def product_detail(url):
    # print(soup)
    soup = Get_Soup_Url(url)

    # try:
    #     l3_name = []
    #     bread = soup.find('ul', {"class": "items"}).find_all('li')
    #     print(bread)
    #     for l3 in bread:
    #         cleaned_text = ' '.join(l3.text.strip().split())
    #         cleaned_text = cleaned_text.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
    #         l3_name.append(cleaned_text)
    #     print('l3_name.....', l3_name)
    # except AttributeError:
    #     l3_name = ''
    #     print('object has no attribute ... l3_name')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find('h1', {"class": "page-title"}).text.strip()
        product_title = product_title.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
        print('product_title.....', product_title)
    except AttributeError:
        product_title = 'N/A'
        print('object has no attribute ... product_title')

    product_title1 = soup.find('h1', {"class": "page-title"}).text.strip()
    l3_name = f"{'home'} > " + product_title1
    l3_name = l3_name.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')

    print('l3_name.....', l3_name)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        mpn = soup.find('div', {"itemprop": "sku"}).text.strip()
        mpn = mpn.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')

        print('mpn.....', mpn)
    except AttributeError:
        mpn = 'N/A'
        print('Not Found')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find('span', {"itemprop": "price"}).text.strip()
        print('price.....', price)
    except AttributeError:
        price = 'N/A'
        print('Not Found')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        features_1 = []
        for features in soup.find('ul', {"class": "product-details-list"}).find_all('li'):
            features_1.append(features.text.replace('\n', '').replace('\t', '').replace('\r', ''))
        print('features_1.....', features_1)
    except AttributeError:
        features_1 = 'N/A'
        print('object has no attribute ... features_1')

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    try:
        # datasheet = []
        pdf = soup.find(id='pc_pdf_link')['href']
        datasheet = pdf
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = 'N/A'
        print('object has no attribute ... datasheet')
    except TypeError:
        datasheet = 'N/A'
        print('object is not subscriptable ... datasheet')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        part_accessories = []
        part_ass = soup.find('div', {"id": "tab-parts_tab"}).find_all('a')
        for accessories in part_ass:
            part_accessories.append(accessories.get("href"))
        print('part_accessories.....', part_accessories)
    except AttributeError:
        part_accessories = 'N/A'
        print('object has no attribute.......part_accessories')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        zip_card = []
        card = soup.find('div', {"class": "product attribute product-media"}).find_all('img')
        for card_links in card:
            zip_card.append(card_links.get("data-src"))
        print('zip_card.....', zip_card)
    except AttributeError:
        zip_card = 'N/A'
        print('object has no attribute ... zip_card')

    # --------------------------------------  Images  ------------------------------------------------------------------
    try:
        image = []
        images = soup.find(class_='columns').find('script', {"type": "text/x-magento-init"})
        data = json.loads(images.text)['[data-gallery-role=gallery-placeholder]']['mage/gallery/gallery']['data']
        for img in data:
            src = img['img']
            image.append(src)

        while len(image) < 5:
            image.append('')

        print("Images....", image)
    except AttributeError:
        image = ['N/A'] * 5
        print('object has no attribute ... image')
    except KeyError:
        image = ['N/A'] * 5
        print('object has no attribute ... image')

    # ----------------------------------------------- Video ------------------------------------------------------------
    try:
        video = []
        video_link = soup.find("div", {"class": "video_container"}).find_all('iframe')
        for video_href in video_link:
            video.append(video_href.get("src"))
        print('video.....', video)
    except AttributeError:
        video = 'N/A'
        print('object has no attribute ... video')

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
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": image_type,
        # "Product_Detail": description,
        "Features": features_1,
        # "Accessories": href_type_exe,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        "Video_Url": video,
        # "Quantity": stock,
        "Price(usd)": price,
        "Kits/Components": part_accessories,
        "Cross_Reference": zip_card,
        "Url": url,

    }]  # save data here

    # Data_Save(row, mylist)
    return product_title, mpn


def Data_Save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, product_title, mpn):
    soup = Get_Soup_Url(url)
    print('Tables')

    try:
        table = soup.find('table', {"id": "super-product-table"}).find('tbody').find_all('tr')
        for ttd in table:
            table_td = ttd.find_all('td')
            table_th = []
            for dd in table_td:
                row = dd.text.strip().replace('\n', " ")
                table_th.append(row)
            if table_th:
                data_table = '\t'.join(table_th)
                data_table = data_table.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
                # print(data_table)
                # save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/bahco.com/data/bahco-specs.txt", 'a+',
                #             encoding='utf-8')
                # save.write(f"{url}\t{product_title}\t{mpn}\t{data_table}\n")
                # save.write(f"{url}\t{data_table}\n")
        print('save data')
    except AttributeError:
        print('.....')


def main():
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/bahco.com/url/bahco-product-url.csv")[
        'URL']
    i = 0
    for url_count, url in enumerate(url_link[i:5], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)
        product_title, mpn = product_detail(url)
        Get_Specs_Table(url, product_title, mpn)

        # selenium calling here
        # driver = getDriveUrls(url, driver)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)
    send_email("Your web scraping script has completed ")

        # print(image)
    print('loop End')


if __name__ == "__main__":
    main()
