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
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Kennametal.com/data/Kennametal-all-data1.csv", 'a',
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
        bread = soup.find("ul", {"id": "breadcrumb"}).find_all('li')
        for l3 in bread:
            l3_name.append(l3.text.strip())
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = "N/A"
        print('l3_name.....', l3_name)

    # ------------------------------------------------ Title -----------------------------------------------------------
    try:
        product_title = soup.find("div", {"class": "product-name-content"}).h1.text.strip()
        print('product_title.....', product_title)
    except NoSuchElementException:
        product_title = "N/A"
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title_1 = soup.find("div", {"class": "product-name-content"}).h3.text.strip()
        print('product_title_1.....', product_title_1)
    except AttributeError:
        product_title_1 = "N/A"
        print('product_title_1.....', product_title_1)

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # print(soup.prettify())
    # ------------------------------------------------------------------------------------------------------------------
    try:
        feature = []
        feature_1 = soup.find("div", {"id": "features-benefits__content"}).find_all("li")
        for fea in feature_1:
            feature_data = fea.text.strip().replace("</li>", "/")
            feature.append(feature_data)
        print('feature.....', feature_1)
    except AttributeError:
        feature = ["N/A"]
        print('feature.....', "N/A")

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     description = soup.find('div', {"class": "elementor-text-editor elementor-clearfix"}).find(
    #         'p').text.strip().replace('\n', " >> ")
    #     print('description.....', description)
    # except AttributeError:
    #     description = "N/A"
    #     print('description.....', description)


    # ------------------------------------------------------------------------------------------------------------------
    try:
        logo = []
        log_link = soup.find(class_="icon-list").find_all('img')
        for log_tag in log_link:
            logo.append(log_tag.get("src"))
        print('logo.....', logo)
    except AttributeError:
        logo = "N/A"
        print('logo.....', logo)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        alphabets = soup.find("div", {"class": "product-work-piece aem-GridColumn aem-GridColumn--default--6"})
        alpha = alphabets.text.strip().replace("\n", ">>").replace("  ", "").split(">>>>")
        print('alpha.....', alpha)
    except AttributeError:
        alpha = 'N/A'
        print('alpha.....', alpha)
    # ------------------------------------------------------------------------------------------------------------------




    # ---------------------------------------------  Images  -----------------------------------------------------------
    try:
        image = []
        table = soup.find("div", {"class": "product-main-image"})
        img_links = table.find_all('img')
        for img_link in img_links:
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
    # print(soup.prettify())

    # --------------------------------------------- Datasheet ----------------------------------------------------------
    # try:
    #     datasheet = []
    #     pdf_link = driver.find_elements(By.XPATH, "//div[@class='related-container']//a")
    #     for pdf in pdf_link:
    #         pdf_links = pdf.get_attribute('href')
    #         datasheet.append(pdf_links)
    #     print('datasheet.....', datasheet)
    # except AttributeError:
    #     datasheet = "N/A"
    #     print('datasheet.....', datasheet)

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
    #     for relat in soup.find_all('section', {"class": "related products"}):
    #         related_href = relat.find_all('a')
    #         for url_related in related_href:
    #             href_tag = url_related.get('href')
    #             if "#" not in href_tag:
    #                 related_url.append(href_tag)
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
        "Mpn": product_title_1,
        # "Grainger_Sku": category,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": dimationsss,
        # "Product_Detail": description,
        "Features": feature,
        # "Accessories": accessories,
        # "Datasheet": datasheet,
        # "Item_Name": dimationsss,
        # "Accessories_1": related_url,
        "Uses": alpha,
        # "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price,
        "Quantity": logo,
        # "Remarks": warranty,
        # "Cross_Reference": advantage,
        "Url": url,

    }]  # save data here

    Data_Save(row, mylist)
    return product_title, product_title_1

    # except Exception as e:
    #     print('Error...', e)
    # send_email(f'Error... {e}')


def Data_Save(row, cols):       # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, product_title, product_title_1):
    #   /var/www/html/webscr/destination_dir
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Kennametal.com/data/Kennametal-specs1.txt", 'a+', encoding='utf-8')
    print('Tables')

    num = 0
    attr_name = []
    attr_value = []
    table = soup.find('table', class_="p-esp-table").find_all("td")
    for tab in table:
        num += 1
        tabs = tab.text.strip()
        if num % 2 != 0:
            attr_name.append(tabs)
        else:
            attr_value.append(tabs)
    for name, value in zip(attr_name, attr_value):
        print(name, "::", value)
        save.write(f"{url}\t{product_title}\t{product_title_1}\t{name}\t{value}\n")
    print('save data in table')






def main():
    #   /var/www/html/webscr/source_dir/
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Kennametal.com/url/Kennametal-product-url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))
    i = 26039
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
