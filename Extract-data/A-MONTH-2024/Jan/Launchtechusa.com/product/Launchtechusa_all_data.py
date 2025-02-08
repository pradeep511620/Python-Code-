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
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Launchtechusa.com/data/Launchtechusa-all-data.csv", 'a', encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def Get_Page_Source(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=opts)
    # driver = webdriver.Chrome()
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


def product_detail(url, driver):
    print('soup')

    # --------------------------------------------- BreadCrumb ---------------------------------------------------------
    try:
        l3_name = []
        bread = driver.find_elements(By.XPATH, "//div[@data-hook='breadcrumbs']//a")
        for l3 in bread:
            l3_name.append(l3.text.strip())
        print('l3_name.....', l3_name)
    except NoSuchElementException:
        l3_name = "N/A"
        print('l3_name.....', l3_name)

    # ------------------------------------------------ Title -----------------------------------------------------------
    try:
        product_title = driver.find_element(By.XPATH, "//h1[@data-hook='product-title']").text.strip()
        print('product_title.....', product_title)
    except NoSuchElementException:
        product_title = "N/A"
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    try:
        sku = driver.find_element(By.XPATH, "(//pre[@class='skK8UF'])").text.strip().replace("\n", ">>").split(">>")[0]
        print('sku.....', sku)
    except NoSuchElementException:
        sku = "N/A"
        print('sku.....', sku)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        driver.find_element(By.XPATH, "(//p[normalize-space()='FEATURES'])[1]").click()
        # driver.find_element(By.XPATH, "//ul[@class='gaCUP4']//li[2]").click()
        time.sleep(2)
        print('click features')
    except NoSuchElementException:
        print("Not click feature options..")

    try:
        feature = []
        for features in driver.find_elements(By.XPATH, "//div[@class='O0VfEq']//ul//li"):
            feature.append(features.text.strip().replace("\n", " >> "))
        print('feature.....', feature)
    except NoSuchElementException:
        feature = "N/A"
        print('feature.....', feature)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = []
        for des in driver.find_element(By.XPATH, "(//pre[@class='skK8UF'])").find_elements(By.TAG_NAME, 'p')[1:]:
            description.append(des.text.strip())
        print('description.....', description)
    except (NoSuchElementException, IndexError):
        description = "N/A"
        print('description.....', description)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    try:
        driver.find_element(By.XPATH, "(//p[normalize-space()='PURCHASE GUIDANCE'])[1]").click()
        time.sleep(2)
        print('click purchase')
    except NoSuchElementException:
        print('click purchase')

    try:
        buy_link = driver.find_element(By.XPATH, "//div[@class='O0VfEq']//a").get_attribute('href')
        print('buy_link.....', buy_link)
    except NoSuchElementException:
        buy_link = "N/A"
        print('buy_link.....', buy_link)

    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------


    # ---------------------------------------------  Images  -----------------------------------------------------------
    try:
        image = []
        for image_tag in driver.find_elements(By.XPATH, "//div[@class='vEIMC5']//img"):
            href = image_tag.get_attribute("src")
            image.append(href)
        image = list(set(image))
        while len(image) < 5:
            image.append('')
        image = image[:5]

        print("Images....", image)
    except NoSuchElementException:
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
    # try:
    #     datasheet = []
    #     pdf_link = driver.find(class_="elementor-tabs").find_all('a')
    #     for pdf in pdf_link:
    #         pdf_links = pdf.get('href')
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
    try:
        related_url = []
        for relat in driver.find_elements(By.XPATH, "//div[@class='slick-slider lA18NV slick-initialized']//div[@class='slick-list']//a"):
            href_tag = relat.get_attribute('href')
            related_url.append(href_tag)
        unique_url = list(set(related_url))
        print('related_url.....', unique_url)
    except NoSuchElementException:
        unique_url = "N/A"
        print(unique_url)

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
        # "Grainger_Sku": laval,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": image1,
        "Product_Detail": description,
        "Features": feature,
        # "Accessories": part_desc,
        # "Datasheet": datasheet,
        # "Item_Name": dimationsss,
        "Accessories_1": unique_url,
        # "Uses": designed,
        # "Video_Url": video,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Quantity": logo,
        # "Remarks": option,
        "Cross_Reference": buy_link,
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


def Get_Specs_Table(url, driver, product_title, sku):
    #   /var/www/html/webscr/destination_dir
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Launchtechusa.com/data/Launchtechusa-specs.txt", 'a+', encoding='utf-8')
    print('*****************************************************************************************************Tables')
    try:
        driver.find_element(By.XPATH, "(//p[normalize-space()='PRODUCT SPECIFICATION'])[1]").click()
        time.sleep(2)
    except NoSuchElementException:
        print("not click PRODUCT SPECIFICATION")

    try:
        driver.find_element(By.XPATH, "(//p[normalize-space()='PRODUCT SPECIFICATIONS'])[1]").click()
        time.sleep(2)
    except NoSuchElementException:
        print("not click 2 PRODUCT SPECIFICATIONS")

    table_data_row = []
    for table_details in driver.find_elements(By.XPATH, "//footer[@class='hvOSi3']//div[@class='QfrfFD cell']//li"):
        if "PRODUCT SPECIFICATION" in table_details.text.strip() or "Product Specifications" in table_details.text.strip():
            tables = table_details.find_elements(By.XPATH, "//div[@class='O0VfEq']//ul//li")
            for tab in tables:
                table = tab.text.strip().split(":")
                if table:
                    table_row = "\t".join(table)
                    table_data_row.append(table_row)
    for value in table_data_row:
        print(value)
        save.write(f"{url}\t{sku}\t{product_title}\t{value}\n")
    print('save data')


    print(" ")




def main():
    #   /var/www/html/webscr/source_dir/
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Launchtechusa.com/url/Launchtechusa-product-url.csv"
    url_link = pd.read_csv(file_path)["URL"]
    print("total url :-----", len(url_link))
    i = 0
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)
        print("")

        # soup = Get_Soup_Url(url)
        # product_title = product_detail(url, soup)
        # Get_Specs_Table(url, soup, product_title)

        # selenium calling here
        driver = Get_Driver_Urls(url)
        product_title, sku = product_detail(url, driver)
        Get_Specs_Table(url, driver, product_title, sku)
        driver.quit()
    print('loop End')

    # msg = "Your web scraping script has completed "
    # send_email(msg)
    # print(msg)


if __name__ == "__main__":
    main()
