import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

# /var/www/html/webscr/destination_dir
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/kingstonbrass.com/data/kingstonbrass-all-data.csv",
                  'a', encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def Get_Soup_Url(url):
    r = requests.get(url, headers=headers)
    time.sleep(1)
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
    # time.sleep(3)
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
    # try:

    try:
        l3_name = []
        bread = soup.find_all('nav', {"class": "breadcrumbs-container"})
        for l3 in bread:
            breadcrumb = l3.text.strip().replace("\n\n\n", ">>")
            l3_name.append(breadcrumb)
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = 'N/A'
        print('object has no attribute ... l3_name')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find('h1', {"class": "product-title"}).text.strip()
        product_title = product_title.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
        print('product_title.....', product_title)
    except AttributeError:
        product_title = 'N/A'
        print('object has no attribute ... product_title')

    # ------------------------------------------------------------------------------------------------------------------


    mix_datas = []
    sku_1 = soup.find('div', class_="product-sku").find_all('span')
    for sku_details in sku_1:
        mix_datas.append(sku_details.text.strip().replace('\xa0\xa0', ">>").split(">>"))
    single_list = mix_datas[0]

    try:
        sku = single_list[0]
        print('sku.....', sku)
    except IndexError:
        sku = 'N/A'
        print('list index of range')
    try:
        brand = single_list[-2]
        print('brand.....', brand)
    except IndexError:
        brand = 'N/A'
        print('list index of range')
    try:
        Ship_Weight = single_list[-1]
        print('Ship_Weight.....', Ship_Weight)
    except IndexError:
        Ship_Weight = 'N/A'
        print('list index of range')


    # ------------------------------------------------------------------------------------------------------------------

    try:
        price = soup.find('div', {"class": "price__current"}).text.strip().replace('\n', '')
        print('price.....', price)
    except AttributeError:
        price = 'N/A'
        print('object has no attribute ... price')


    # ------------------------------------------------------------------------------------------------------------------
    try:
        feature = soup.find('div', {"class": "product-description"}).find_all(class_="easytabs-content-holder")[1].text.strip().replace("\n", " >> ")
        print('feature.....', feature)
    except AttributeError:
        feature = 'N/A'
        print('object has no attribute ... description')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = []
        description_1 = soup.find('div', {"class": "product-description"}).find(class_="easytabs-content-holder").find_all('p')
        for description_details in description_1:
            description.append(description_details.text.strip().replace('\n', '>>'))
        print('description.....', description)
    except AttributeError:
        description = 'N/A'
        print('object has no attribute ... description')


    # ------------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        pdf = soup.find('div', {"class": "product-description"}).find_all(class_="easytabs-content-holder")[2].find_all('a')
        for pdf_link in pdf:
            download = pdf_link.get('href')
            datasheet.append(download)
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = 'N/A'
        print('object has no attribute ... datasheet')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        parts = []
        comptable_part = soup.find('div', {"class": "product-description"}).find_all(class_="easytabs-content-holder")[3]
        for part in comptable_part:
            parts.append(part.text.strip())
        print('parts.....', parts)
    except AttributeError:
        parts = 'N/A'
        print("noo")


    # ------------------------------------------------------------------------------------------------------------------
    try:
        return_shipping = soup.find('div', {"class": "product-description"}).find_all(class_="easytabs-content-holder")[-1]
        return_shipping_info = return_shipping.text.strip()
        print('return_shipping_info.....', return_shipping_info)
    except AttributeError:
        return_shipping_info = 'N/A'
        print("noo")


    # ------------------------------------------------------------------------------------------------------------------
    try:
        stock_value = soup.find('div', {"id": "neon-stock-info-widget"})
        stock = stock_value.get("data-product-stock")+" In Stock. (Leaves Warehouse in 1-2 Business Days)"
        print('stock.....', stock)
    except AttributeError:
        stock = 'N/A'
        print("noo")



    # --------------------------------------  Images  ------------------------------------------------------------------
    try:
        image = []
        table = soup.find('div', {"class": "gallery-navigation--scroller"})
        img_links = table.find_all('img')
        for img_link in img_links:
            href = img_link.get('src').replace("//", '')
            image.append(href)
        while len(image) < 5:
            image.append('')

        print("Images....", image)
    except AttributeError:
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
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories_1", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]  # save data here

    row = [{
        # "Mpn": mpn,
        "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": src_values,
        "Product_Detail": description,
        "Features": feature,
        "Accessories": brand,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video,
        "Quantity": stock,
        "Price(usd)": price,
        "Spare_Parts": parts,
        "weight(kg)": Ship_Weight,
        # "Quantity":product_quantities,
        "Cross_Reference": return_shipping_info,
        "Url": url,

    }]  # save data here

    Data_Save(row, mylist)
    return product_title, sku

#
# except Exception as e:
#     print('Error...', e)
#     send_email(f'Error... {e}')


def Data_Save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, product_title, sku):
    #   /var/www/html/webscr/destination_dir
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/kingstonbrass.com/data/kingstonbrass-specs.txt", 'a+',encoding='utf-8')

    print('Tables')

    table = soup.find('div', class_="easytabs-content-item-static").find_all('div')[1]
    text_details = "\n".join(div.text.strip() for div in table if div.text.strip())
    tab = text_details.replace("\n", ">>").split(">>")
    # print(tab)
    for th in tab:
        table_row = "\t".join(th.strip().split(': '))
        print(table_row)
        save.write(f"{url}\t{product_title}\t{sku}\t{table_row}\n")
    print('save data')


def main():
    #   /var/www/html/webscr/source_dir/
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/kingstonbrass.com/url/kingston-product-url.csv")['URL']
    print(len(url_link))
    i = 0
    for url_count, url in enumerate(url_link[i:1], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        soup = Get_Soup_Url(url)
        product_title, sku = product_detail(url, soup)
        # Get_Specs_Table(url, soup, product_title, sku)



        # selenium calling here
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)
    # print('loop End')
    # msg = "Your web scraping script has completed "
    # send_email(msg)
    # print(msg)



if __name__ == "__main__":
    main()
