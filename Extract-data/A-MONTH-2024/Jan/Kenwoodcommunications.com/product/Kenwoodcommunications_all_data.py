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
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Kenwoodcommunications.com/data/Kenwoodcommunications-all-data.csv", 'a',
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
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    # with webdriver.Chrome() as driver:
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


def product_detail(url, driver):
    # print('driver')
    print('soup')
    # try:

    # --------------------------------------------- BreadCrumb ---------------------------------------------------------
    try:
        l3_name = []
        bread = driver.find_element(By.XPATH, "//div[@id='categories_path']//ul[@class='page-path clearfix']").find_elements(By.TAG_NAME, "li")
        for l3 in bread:
            l3_name.append(l3.text.strip())
        print('l3_name.....', l3_name)
    except NoSuchElementException:
        l3_name = "N/A"
        print('l3_name.....', l3_name)

    # ------------------------------------------------ Title -----------------------------------------------------------
    try:
        product_title = driver.find_element(By.XPATH, "//*[@class='product_description']").text.strip()
        print('product_title.....', product_title)
    except NoSuchElementException:
        product_title = "N/A"
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = driver.find_element(By.XPATH, "//div[@class='woocommerce-product-details__short-description']//p").text.strip().replace("\n", ">>")
        print('description.....', description)
    except NoSuchElementException:
        description = "N/A"
        print('description.....', description)


    try:
        sku = driver.find_element(By.XPATH, "//*[@class='product-code']").text.strip().replace("\n", ">>")
        print('sku.....', sku)
    except NoSuchElementException:
        sku = "N/A"
        print('sku.....', sku)

    # ------------------------------------------------------------------------------------------------------------------
    # dropdown = driver.find_element(By.XPATH, "//select[@id='select-lens-type']")
    # options = dropdown.find_elements(By.TAG_NAME, "option")
    # for option in options:
    #     option.click()
    #     time.sleep(2)



    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    try:
        feature = []
        for feature_1 in driver.find_elements(By.XPATH, "//div[@class='clearfix feature-columns']//table//td"):
            feature_data = feature_1.text.strip()
            feature.append(feature_data)
        print('feature.....', feature)
    except NoSuchElementException:
        feature = ["N/A"]
        print('feature.....', "N/A")

    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # ---------------------------------------------  Images  -----------------------------------------------------------
    try:
        image = []
        for img_tag in driver.find_elements(By.XPATH, "//div[@id='product-view-main']//div[@class='left']//a"):
            href = img_tag.get_attribute('href')
            if ".jpg" in href or "png" in href:
                image.append(href)
        image = list(set(image))
        while len(image) < 5:
            image.append('')
        image = image[:5]

        print("Images....", image)
    except NoSuchElementException:
        image = ['N/A'] * 5
        print('object has no attribute ... image')


    # --------------------------------------------- Datasheet ----------------------------------------------------------
    try:
        datasheet = []
        pdf_link = driver.find_elements(By.XPATH, "//div[@class='product-view-additional']//a")
        for pdf in pdf_link:
            pdf_links = pdf.get_attribute('href')
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
    try:
        related_url = []
        for url_tag in driver.find_elements(By.XPATH, "//div[@id='products-in-the-category']//a"):
            href_tag = url_tag.get_attribute("href")
            related_url.append(href_tag)
        related_url = list(set(related_url))
        print('related_url.....', related_url)
    except AttributeError:
        related_url = "N/A"
        print(related_url)

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
        "Datasheet": datasheet,
        # "Item_Name": dimationsss,
        "Accessories_1": related_url,
        # "Uses": key_value_pairs,
        # "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Quantity": logo,
        # "Remarks": warranty,
        # "Cross_Reference": advantage,
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


# def Get_Specs_Table(url, soup, product_title):
def Get_Specs_Table(url, driver, product_title, sku):
    #   /var/www/html/webscr/destination_dir
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Kenwoodcommunications.com/data/Kenwoodcommunications-specs.txt", 'a+',
                encoding='utf-8')
    print('Tables*****************************************************************************************************')

    driver.find_element(By.XPATH, "(//a[normalize-space()='Specifications'])[1]").click()
    time.sleep(3)
    row = 0
    attr_name = []
    attr_value = []
    for table in driver.find_elements(By.XPATH, "(//table)[position() >= 3]//tr//td"):
        specs = table.text.replace("\n", ">>")
        row += 1
        if row % 2 != 0:
            attr_name.append(specs.strip())
        else:
            attr_value.append("rp_" + specs.strip().replace("\n", " "))
    for name, value in zip(attr_name, attr_value):
        print(name, ":::::", value)
        save.write(f"{url}\t{sku}\t{product_title}\t{name}\t{value}\n")


def main():
    #   /var/www/html/webscr/source_dir/
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Kenwoodcommunications.com/url/Product-url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))
    i = 63
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        # soup = Get_Page_Source(url)
        # product_title = product_detail(url, soup)
        # Get_Specs_Table(url, soup, product_title)
        # Get_Specs_Table(url, soup)

        # selenium calling here
        driver = Get_Driver_Urls(url)
        product_title, sku = product_detail(url, driver)
        Get_Specs_Table(url, driver,product_title, sku)
        driver.close()
    print('loop End')

    # msg = "Your web scraping script has completed "
    # send_email(msg)
    # print(msg)


if __name__ == "__main__":
    main()
