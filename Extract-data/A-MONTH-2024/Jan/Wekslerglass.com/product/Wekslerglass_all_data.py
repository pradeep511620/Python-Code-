import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# /var/www/html/webscr/destination_dir
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Wekslerglass.com/data/Wekslerglass-all-data.csv", 'a',
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
        bread = soup.find("div", {"class": "breadcrumbs"}).find_all('a')
        for l3 in bread:
            l3_name.append(l3.text.strip())
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = "N/A"
        print('l3_name.....', l3_name)

    # ------------------------------------------------ Title -----------------------------------------------------------
    try:
        product_title = soup.find("h3", {"class": "elementor-heading-title elementor-size-default"}).text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = "N/A"
        print('product_title.....', product_title)
        # try:
        #     product_title = soup.find("div", {"class": "fusion-text fusion-text-1"}).find("h2").text.strip()
        #     print('product_title.....', product_title)
        # except AttributeError:
        #
    # print(soup.prettify())


    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     mpns = soup.find("div", {"id": "content"}).find(class_="list-unstyled").text.strip().replace("\n", ">>").split(">>")
    #     data_mpn = mpns
    #     try:
    #         sku = data_mpn[0]
    #         print('sku.....', sku)
    #     except IndexError:
    #         sku = "N/A"
    #         print('sku.....', sku)
    #
    #     try:
    #         laval = data_mpn[1]
    #         print('laval.....', laval)
    #     except IndexError:
    #         laval = "N/A"
    #         print('laval.....', laval)
    # except Exception as e:
    #     sku = ''
    #     laval = ''
    #     print(f"{e} error")

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     price = soup.find("div", {"id": "content"}).find_all(class_="list-unstyled")[-1].text.strip()
    #     print('price.....', price)
    # except AttributeError:
    #     price = "N/A"
    #     print('price.....', price)

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     feature = soup.find('div', {"class": "post-content woocommerce-product-details__short-description"}).find(
    #         "p").text.strip().replace("\n", " >> ")
    #     print('feature.....', feature)
    # except AttributeError:
    #     feature = ["N/A"]
    #     print('feature.....', "N/A")

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     description = soup.find('div', {"id": "tab-description"}).text.strip().replace("\n", " >> ")
    #     print('description.....', description)
    # except AttributeError:
    #     description = "N/A"
    #     print('description.....', description)

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     logo = []
    #     log_link = soup.find('div', {"class": "post-content woocommerce-product-details__short-description"}).find_all(
    #         "a")
    #     for log_tag in log_link:
    #         logo.append("https:" + log_tag.get("href"))
    #     print('logo.....', logo)
    # except AttributeError:
    #     logo = "N/A"
    #     print('logo.....', logo)

    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Images  -----------------------------------------------------------
    try:
        image = []
        table = soup.find("div", {"class": "elementor-widget-container"})
        img_links = table.find_all('img')
        for img_link in img_links:
            href = img_link.get('src')
            if "#" not in href:
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
    #     for image_link in soup.find_all('div', class_="fusion-gallery-image"):
    #         for inm in image_link.find_all("a"):
    #             image_links = inm.get('href')
    #             images_href = image_links
    #             image.append(images_href)
    #     while len(image) < 5:
    #         image.append('')
    #     image = image[:5]
    #     print('image.....', image)
    # except AttributeError:
    #     image = ['N/A'] * 5
    #     print('object has no attribute ... image')
    # # print(soup.prettify())


    # --------------------------------------------- Datasheet ----------------------------------------------------------
    try:
        datasheet = []
        pdf_link = soup.find(class_="elementor-tabs").find_all('a')
        for pdf in pdf_link:
            pdf_links = pdf.get('href')
            datasheet.append(pdf_links)
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = "N/A"
        print('datasheet.....', datasheet)

    # ----------------------------------------------- Video ------------------------------------------------------------
    # try:
    #     video = []
    #     video_link = soup.find("div", {"class": "buttons-top"}).find_all('a')
    #     for video_href in video_link:
    #         video_links = video_href.get("href")
    #         if "youtube" in video_links:
    #             video.append(video_links)
    #     print('video.....', video)
    # except AttributeError:
    #     video = 'N/A'
    #     print('video.....', video)



    # ------------------------------------------------ Url -------------------------------------------------------------
    # try:
    #     related_url = []
    #     for relat in soup.find("div", {"id": "content"}).find_all(class_="image"):
    #         related_href = relat.find_all('a')
    #         # print(related_href)
    #         for url_related in related_href:
    #             href_tag = url_related.get('href')
    #             if "#" not in href_tag:
    #                 related_url.append(href_tag)
    #     print('related_url.....', related_url)
    # except AttributeError:
    #     related_url = "N/A"
    #     print(related_url)
    # print(soup.prettify()

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
        # "Grainger_Sku": laval,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": image1,
        # "Product_Detail": description,
        # "Features": feature,
        # "Accessories": part_desc,
        "Datasheet": datasheet,
        # "Item_Name": dimationsss,
        # "Accessories_1": related_url,
        # "Uses": designed,
        # "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Quantity": logo,
        # "Remarks": option,
        # "Cross_Reference": replacement,
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
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Wekslerglass.com/data/Wekslerglass-specs.txt", 'a+', encoding='utf-8')
    print('Tables')

    attr_name = []
    attr_value = []
    for td in soup.find_all("div", class_="col-4 px-0"):
        tab = td.text
        attr_name.append(tab)

    for th in soup.find_all("div", class_="col-8 px-0"):
        tab2 = th.text.strip().replace("\n", ">>")
        attr_value.append(tab2)

    for name, value in zip(attr_name, attr_value):
        print(name, "::", value)
        save.write(f"{url}\t{product_title}\t{name}\t{value}\n")
    print('save data')





def main():
    #   /var/www/html/webscr/source_dir/
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Wekslerglass.com/url/Wekslerglass-product-url.csv"
    url_link = pd.read_csv(file_path)["URL"]
    print("total url :-----", len(url_link))
    i = 0
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        soup = Get_Soup_Url(url)
        product_title = product_detail(url, soup)
        Get_Specs_Table(url, soup, product_title)

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
