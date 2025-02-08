import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidArgumentException, ElementClickInterceptedException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# /var/www/html/webscr/destination_dir
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/heath-zenith.com/data/zenith-all-data.csv", 'a',
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
    time.sleep(5)
    return driver


def send_email(msg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = ["nkmishra@nextgenesolutions.com", "raptorsupplyuk@gmail.com"]
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


def product_detail(url, driver):
    print('driver')

    # try:
    #     l3_name = []
    #     bread = soup.find('nav', {"class": "breadcrumb"}).find_all('a')
    #     for l3 in bread:
    #         breadcrumb = l3.text.strip()
    #         l3_name.append(breadcrumb)
    #     print('l3_name.....', l3_name)
    # except AttributeError:
    #     l3_name = 'N/A'
    #     print('object has no attribute ... l3_name')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = driver.find_element(By.XPATH, "//*[@class='container-fluid']//h4").text.strip()
        product_title = product_title.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
        print('product_title.....', product_title)
    except NoSuchElementException:
        print('object has no attribute ... product_title')
        product_title = driver.find_element(By.XPATH, "//div[@id='product-description']//h2").text.strip()
        print('product_title.....1', product_title)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        sku = driver.find_element(By.XPATH, "//*[@class='container-fluid']//h2").text.strip()
        print('sku.....', sku)
    except NoSuchElementException:
        print('Not Found')
        sku = driver.find_element(By.XPATH, "//div[@id='product-description']//h1").text.strip()
        print('sku.....1', sku)

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     price = soup.find('div', {"class": "current-price"}).text.strip()
    #     print('price.....', price)
    # except AttributeError:
    #     price = 'N/A'
    #     print('Not Found')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        features_1 = []
        for features in driver.find_elements(By.XPATH, "//*[@class='col-sm-6']//ul[1]//li"):
            features_1.append(features.text.replace('\n', '').replace('\t', '').replace('\r', '').encode('latin-1',errors='ignore').decode('utf-8', errors='ignore'))
        print('features_1.....', features_1)
    except NoSuchElementException:
        features_1 = 'N/A'
        print('object has no attribute ... features_1')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = []
        description_1 = driver.find_element(By.XPATH,"//*[@class='col-sm-6']//ul[2]//li").text.strip()
        description.append(description_1.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore'))
        print('description.....', description)
    except NoSuchElementException:
        description = []
        print('object has no attribute ... description')
        for des in driver.find_elements(By.XPATH, "//div[@class='well']"):
            des_1 = des.text.strip().encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
            description.append(des_1)
        print('description.....1', description)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        service_2 = []
        for service in driver.find_elements(By.XPATH, "//*[@class='col-sm-4 col-sm-offset-2']//ul//li"):
            service_1 = service.text.strip().encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
            service_2.append(service_1)
        print("service_1.....", service_2)
    except NoSuchElementException:
        service_2 = 'N/A'
        print('Not Found')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        for download in driver.find_elements(By.XPATH, "//div[@id='specs']//a"):
            pdf = download.get_attribute('href')
            datasheet.append(pdf)
        print('datasheet.....', datasheet)
    except NoSuchElementException:
        datasheet = 'N/A'
        print('object has no attribute ... datasheet')

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     driver.find_element(By.XPATH, "//a[normalize-space()='Warranty']").click()
    #     time.sleep(1)
    # except NoSuchElementException:
    #     print('Not click 1')
    try:
        Cross_Reference = []
        for warranty in driver.find_elements(By.XPATH, "//div[@id='warranty']//p"):
            Cross_Reference.append(warranty.text.strip())
        print('Cross_Reference.....', Cross_Reference)
    except NoSuchElementException:
        Cross_Reference = 'N/A'
        print('Not Found')
    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     zip_card = []
    #     card = soup.find('div', {"class": "cad-tab-links"}).find_all('a')
    #     for card_links in card:
    #         zip_card.append(card_links.get("href"))
    #     print('zip_card.....', zip_card)
    # except AttributeError:
    #     zip_card = 'N/A'
    #     print('object has no attribute ... zip_card')

    # --------------------------------------  Images  ------------------------------------------------------------------
    try:
        image = []
        for img_1 in driver.find_elements(By.XPATH, "//div[@id='product-images']//a"):
            img_2 = img_1.get_attribute('href')
            image.append(img_2)

        while len(image) < 5:
            image.append('')

        print("Images....", image)
    except NoSuchElementException:
        image = ['N/A'] * 5

    try:
        image1 = []
        for img_3 in driver.find_elements(By.XPATH,"//div[@class='col-sm-4 col-sm-offset-2']//img"):
            img_4 = img_3.get_attribute('src')
            image1.append(img_4)
            print("Images....1", image1)
    except NoSuchElementException:
        image1 = ''
        print('')

    # ----------------------------------------------- Video ------------------------------------------------------------
    try:
        video = []
        video_link = driver.find_elements(By.XPATH, "//div[@id='videos']//iframe")
        for video_href in video_link:
            video.append(video_href.get_attribute("src"))
        print('video.....', video)
    except InvalidArgumentException:
        video = 'N/A'
        print('object has no attribute ... video')

    # ------------------------------------------------------------------------------------------------------------------
    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories_1", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]  # save data here

    row = [{
        # "Mpn": mpn,
        "Grainger_Sku": sku,
        # "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        "Image_Name": image1,
        "Product_Detail": description,
        "Features": features_1,
        "Accessories": service_2,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Kits/Components": part_accessories,
        # "Label": product_manufacturer,
        # "Quantity":product_quantities,
        "Cross_Reference": Cross_Reference,
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


def Get_Specs_Table(url, driver, product_title, sku):
    #   /var/www/html/webscr/destination_dir
    print('Tables')
    try:
        driver.find_element(By.XPATH, "//a[normalize-space()='See More Details']").click()
        time.sleep(2)
    except ElementClickInterceptedException:
        print('Not click 2')
    except NoSuchElementException:
        print('Not click 22')

    try:
        attr_name = []
        attr_value = []
        for table in driver.find_elements(By.CLASS_NAME, "product-property-name"):
            tab = table.text.strip()
            attr_name.append(tab)

        for table1 in driver.find_elements(By.CLASS_NAME, "product-property-value"):
            tab1 = table1.text.strip()
            attr_value.append(tab1.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore'))

        for a, b in zip(attr_name, attr_value):
            print(a, ".....", b)
            # save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/heath-zenith.com/data/zenith-specs.txt", 'a+',
            #             encoding='utf-8')
            # save.write(f"{url}\t{product_title}\t{sku}\t{a}\t{b}\n")
        print('save data')
    except NoSuchElementException:
        print('nn')


def main():
    #   /var/www/html/webscr/source_dir/
    url_link = \
    pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/heath-zenith.com/url/zenith-product-url.csv")[
        'URL']
    i = 140
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)
        # soup = Get_Soup_Url(url)
        # product_detail(url, soup)
        # try:
        #     product_title, mpn = product_detail(url, soup)
        #     # Get_Specs_Table(url, soup, product_title, mpn)
        # except Exception:
        #     break

        # selenium calling here

        driver = Get_Driver_Urls(url)
        product_title, sku = product_detail(url, driver)
        Get_Specs_Table(url, driver, product_title, sku)

    print('loop End')
    # msg = "Your web scraping script has completed "
    # send_email(msg)
    # print(msg)


if __name__ == "__main__":
    main()
