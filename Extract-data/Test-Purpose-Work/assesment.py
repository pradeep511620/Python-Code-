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
save_files = open("gates-all-data.csv", 'a', encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def Get_Soup_Url(url):
    r = requests.get(url, headers=headers)
    # time.sleep(3)
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


def product_detail(url, driver):
    print('driver')
    # try:

    # ------------------------------------------------------------------------------------------------------------------
    try:
        l3_name = driver.find_element(By.XPATH, "//div[@class='row breadcrumb py-0']//a").text.strip()
        print('l3_name.....', l3_name)
    except NoSuchElementException:
        l3_name = 'N/A'
        print('Not')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = driver.find_element(By.XPATH, "//div[@class='summary entry-summary']//h1").text.strip()
        print('product_title.....', product_title)
    except NoSuchElementException:

        try:
            product_title = driver.find_element(By.XPATH, "//*[@class='et_pb_text_inner']//h1").text.strip()
            print('product_title.....', product_title)
        except NoSuchElementException:
            product_title = "N/A"
            print("Not")
    # ------------------------------------------------------------------------------------------------------------------
    prices = []
    try:
        price = driver.find_element(By.XPATH, "//p[@class='price']").text.strip()
        prices.append(price)
        print('prices.....', prices)
    except NoSuchElementException:
        price = 'N/A'
        print('Not')


    # ------------------------------------------------------------------------------------------------------------------
    try:
        short_description = driver.find_element(By.XPATH, "//div[@class='woocommerce-product-details__short-description']").text.strip().replace("\n", ">>")
        print('short_description.....', short_description)
    except NoSuchElementException:
        try:
            short_descriptionss = []
            short_descriptions = driver.find_elements(By.XPATH,"//*[@class='et_pb_module_inner']//p")
            for desc in short_descriptions:
                short_descriptionss.append(desc.text.strip())
            try:
                short_description = short_descriptionss[-1]
            except IndexError:
                short_description = 'N/A'
            print('short_description.....', short_description)
        except NoSuchElementException:
            short_description = 'N/A'
            print('Not')


    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = []
        for des in driver.find_elements(By.XPATH, "//div[@id='tab-description']//p"):
            des_1 = des.text.strip()
            description.append(des_1)
        print('description.....', description)
    except AttributeError:
        description = 'N/A'
        print('object has no attribute ... description')


    # ------------------------------------------------------------------------------------------------------------------
    skus = []
    try:
        sku = driver.find_element(By.XPATH, "//div[@class='product_meta']//span[1]").text.strip()
        skus.append(sku)
        print('skus.....', skus)
    except NoSuchElementException:
        sku = 'N/A'
        print('No')
    # ------------------------------------------------------------------------------------------------------------------
    categorys = []
    try:
        category = driver.find_element(By.XPATH, "//div[@class='product_meta']//span[2]").text.strip()
        categorys.append(category)
        print('categorys.....', categorys)
    except NoSuchElementException:
        category = 'N/A'
        print('Not')

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # --------------------------------------  Images  ------------------------------------------------------------------

    try:
        image = []
        img_1 = driver.find_element(By.XPATH, "//div[@class='woocommerce-product-gallery woocommerce-product-gallery--with-images woocommerce-product-gallery--columns-4 images']")
        image_tag = img_1.find_elements(By.TAG_NAME, "a")
        for img_3 in image_tag:
            image_href = img_3.get_attribute('href')
            image.append(image_href)

        while len(image) < 5:
            image.append('')

        print('image.....', image)
    except Exception as e:
        image = ['N/A'] * 5
        print('object has no attribute ... image')


        # try:
        #     image = []
        #     table = soup.find('div', {"class": "gallery gallery-new"})
        #     img_links = table.find_all('img')
        #     for img_link in img_links:
        #         href = img_link.get('data-src').replace("//", 'https://')
        #         image.append(href)
        #     image = list(set(image))
        #     while len(image) < 5:
        #         image.append('')
        #     image = image[:5]
        #
        #     print("Images....", image)
        # except AttributeError:
        #     image = ['N/A'] * 5
        #     print('object has no attribute ... image')

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

        # ------------------------------------------------------------------------------------------------------------------

    try:
        related_url = []
        for relat in driver.find_elements(By.XPATH, "//section[@class='related products']//li//a"):
            related = relat.get_attribute('href')
            related_url.append(related)
        print('related_url.....', related_url)
    except AttributeError:
        related_url = ''
        print('nn')   

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
        "Mpn": skus,
        "Grainger_Sku": categorys,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": dimationsss,
        "Product_Detail": description,
        "Features": short_description,
        # "Accessories": brand,
        # "Datasheet": datasheet,
        # "Item_Name": dimationsss,
        # "item_ID": attr_value,
        # "Uses": uses_d,
        # "Video_Url": video,
        # "Quantity": stock,
        "Price(usd)": prices,
        # "Spare_Parts": inbox_list,
        # "weight(kg)": Ship_Weight,
        # "Quantity":product_quantities,
        # "Remarks": des,
        # "Cross_Reference": unique_urls,
        "Url": url,

    }]  # save data here

    Data_Save(row, mylist)
    return product_title, skus

    # except Exception as e:
    #     print('Error...', e)
        # send_email(f'Error... {e}')


def Data_Save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, driver, product_title, skus):
    #   /var/www/html/webscr/destination_dir

    save = open("gates-specs.txt", 'a+', encoding='utf-8')
    print('Tables')
    # print(soup.prettify())

    driver.find_element(By.XPATH, "//a[normalize-space()='Additional information']").click()
    time.sleep(3)
    attr_name = []
    attr_value = []

    for th in driver.find_elements(By.XPATH, "//th[@class='woocommerce-product-attributes-item__label']"):
        tab = th.text.strip()
        attr_name.append(tab)

    for td in driver.find_elements(By.XPATH, "//td[@class='woocommerce-product-attributes-item__value']"):
        tab_1 = td.text.strip()
        attr_value.append(tab_1)

    for a, b in zip(attr_name, attr_value):
        print(a, ":::::", b)
        save.write(f"{url}\t{product_title}\t{skus}\t{a}\t{b}\n")
    print('save data')

    #     save.write(f"{url}\t{product_title}\t{a}\t{b}\n")



def main():
    #   /var/www/html/webscr/source_dir/
    url_link = pd.read_csv("Gates_product_url.csv")['URL']
    print(len(url_link))
    i = 0
    for url_count, url in enumerate(url_link[i:2], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        # soup = Get_Soup_Url(url)

        # product_title, mpn = product_detail(url, soup)
        # Get_Specs_Table(url, soup, product_title, mpn)


        # selenium calling here
        driver = Get_Driver_Urls(url)
        product_title, skus = product_detail(url, driver)
        # Get_Specs_Table(url, driver, product_title, skus)
    print('loop End')
    # driver.quit()

    # msg = "Your web scraping script has completed "
    # send_email(msg)
    # print(msg)


if __name__ == "__main__":
    main()

# product_detail("https://www.motion.com/products/sku/00333029")
