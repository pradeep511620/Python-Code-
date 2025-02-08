import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.by import By

# /var/www/html/webscr/destination_dir
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Dec-2023/Dixon.com/data/Dixon-all-data.csv", 'a', encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def Get_Soup_Url(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup



def Get_Driver_Urls(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    return soup
    # return driver


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


    # ------------------------------------------------------------------------------------------------------------------
    l3_name = []
    try:
        bread = soup.find('ul', {"class": "breadcrumb"}).find_all('li')
        for l3 in bread:
            l3_name.append(l3.text.strip())
        # l3_name = list(filter(None, l3_name))
        # if not l3_name:
        #     l3_name = 'N/A'
        print('L3_name.....', l3_name)
    except AttributeError:
        l3_name = 'N/A'
        print('L3_name.....', l3_name)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find('h1', {"class": "cimm_prodDetailTitle"}).text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = "N/A"
        print('product_title.....', product_title)
    # .encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
    # ------------------------------------------------------------------------------------------------------------------
    try:
        sku = soup.find('li', {"id": "mPartNo"}).text.strip().replace("\n", "")
        print('sku.....', sku)
    except AttributeError:
        sku = "N/A"
        print('sku.....', sku)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        upcs = soup.find('li', {"id": "upcNo"}).text.strip().replace("\n", "")
        upc = "rp_"+upcs
        print('upc.....', upc)
    except AttributeError:
        upc = "N/A"
        print('upc.....', upc)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find('div', {"class": "price"}).text.strip().replace("\n", "> ")
        print('price.....', price)
    except AttributeError:
        price = "N/A"
        print('price.....', price)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        short_description = soup.find('p', {"class": "cimm_itemShortDesc"}).text.strip()
        print('short_description.....', short_description)
    except AttributeError:
        short_description = "N/A"
        print('short_description.....', short_description)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        feature = []
        features = soup.find('div', {"id": "featureSection"}).find_all("li")
        for li in features:
            li_feature = li.text.strip()
            feature.append(li_feature)
        print('feature.....', feature)
    except AttributeError:
        feature = "N/A"
        print('feature.....', feature)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = ''
        desc = soup.find_all('div', {"id": "descriptionSection"})
        for lists in desc:
            description = lists.text.strip().replace('\n', " >> ")
        print('description.....', description)
    except AttributeError:
        description = "N/A"
        print('description.....', description)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    Mixed_data = soup.find('ul', {"id": "productDetailList"}).find_all('li')
    for li in Mixed_data:
        tab = li.text.strip().replace("\n", "").split(":")
        if tab:
            Mixed_data_table = "\t".join("" + str(single_tab) for single_tab in tab)
            print(Mixed_data_table)
            save1 = open("mixed data.txt", "a+", encoding='utf-8')
            save1.write(f"{url}\t{product_title}\t{sku}\t{Mixed_data_table}\n")
    # print('save data in mixed data files')

    # ------------------------------------------------------------------------------------------------------------------

    # --------------------------------------  Images  ------------------------------------------------------------------
    try:
        image = []
        table = soup.find('div', {"class": "cimm_itemdetail-image"})
        # print(table)
        img_links = table.find_all('img')
        for img_link in img_links:
            # print(img_link)
            href = img_link.get('src')
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
        pdf_links = soup.find("div", {"id": "documentsSection"}).find_all('a')
        for link in pdf_links:
            pdf = link.get("onclick")
            pdf_ta = "https://shop.tipcotech.com" + pdf.split("('")[1].split("mywindow")[0]
            datasheet.append(pdf_ta)
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = "N/A"
        print('datasheet.....', datasheet)

    # ----------------------------------------------- Video ------------------------------------------------------------
    # try:
    #     video = []
    #     video_link = soup.find("div", {"class": "video_container"}).find_all('iframe')
    #     for video_href in video_link:
    #         video.append(video_href.get("src"))
    #     print('video.....', video)
    # except AttributeError:
    #     video = 'N/A'
    #     print('object has no attribute ... video')

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
        "Mpn": sku,
        "Grainger_Sku": upc,
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
        # "Video_Url": video,
        # "Quantity": stock,
        "Price(usd)": price,
        # "Quantity":product_quantities,
        # "Remarks": warranty,
        "Cross_Reference": short_description,
        "Url": url,

    }]  # save data here

    Data_Save(row, mylist)
    return product_title, sku

    # except Exception as e:
    #     print('Error...', e)
    # send_email(f'Error... {e}')


def Data_Save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, product_title, sku):
    # def Get_Specs_Table(url, soup):
    #   /var/www/html/webscr/destination_dir
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Dec-2023/Dixon.com/data/Dixon-specs.txt", 'a+', encoding='utf-8')
    print('Tables')

    try:
        table = soup.find("div", {"id": "specificationSection"}).find_all('tr')
        for td in table:
            tabs = td.text.strip().replace("\n", "").replace("     ", "").split(":")
            if tabs:
                specs_table = "\t".join(tabs)
                print(specs_table)
                save.write(f"{url}\t{product_title}\t{sku}\t{specs_table}\n")
        print('save data into table')
    except AttributeError:
        print('N/A')



def main():
    #   /var/www/html/webscr/source_dir/
    url_link = \
        pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Dec-2023/Dixon.com/url/Dixon-product-url.csv")['URL']
    print("total url :-----", len(url_link))
    i = 459
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        # soup = Get_Soup_Url(url)
        # product_title = product_detail(url, soup)
        # Get_Specs_Table(url, soup, product_title, sku)
        # Get_Specs_Table(url, soup)

        soup = Get_Driver_Urls(url)
        product_title, sku = product_detail(url, soup)
        Get_Specs_Table(url, soup, product_title, sku)

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
# product_detail("https://shop.tipcotech.com/1000318/product/n/dixon-dxn-ghyv")
# Get_Specs_Table("https://shop.tipcotech.com/1000318/product/n/dixon-dxn-ghyv")
