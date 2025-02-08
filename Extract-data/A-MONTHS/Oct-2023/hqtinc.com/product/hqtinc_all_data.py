import smtplib
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
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/hqtinc.com/data/hqtinc-all-data.csv", 'a', encoding='utf-8')

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
    # time.sleep(3)
    return driver


def send_email(msg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = ["nkmishra@nextgenesolutions.com", "raptorsupplyuk@gmail.com",]
    # sender_email = ["nkmishra@nextgenesolutions.com", "nirbhay@raptorsupplies.com", "tajender@raptorsupplies.com", "pradeepkumar@raptorsupplies.com"]
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


mgs = "Your web scraping script has been started"
send_email(mgs)
print(mgs)


def product_detail(url, soup):

    try:
        l3_name = []
        bread = soup.find('nav', {"class": "breadcrumb"}).find_all('a')
        for l3 in bread:
            breadcrumb = l3.text.strip()
            l3_name.append(breadcrumb)
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = 'N/A'
        print('object has no attribute ... l3_name')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find('h1', {"itemprop": "name"}).text.strip()
        product_title = product_title.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
        print('product_title.....', product_title)
    except AttributeError:
        product_title = 'N/A'
        print('object has no attribute ... product_title')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_manufacturer = soup.find('div', {"class": "product-manufacturer"}).text.strip().replace('\n', '>>')
        print('product_manufacturer.....', product_manufacturer)
    except AttributeError:
        product_manufacturer = 'N/A'
        print('Not Found')

    try:
        product_reference = soup.find('div', {"class": "product-reference"}).text.strip().replace('\n', '>>')
        print('product_reference.....', product_reference)
    except AttributeError:
        product_reference = 'N/A'
        print('Not Found')

    try:
        product_quantities = soup.find('div', {"class": "product-quantities"}).text.strip().replace('\n', '>>')
        print('product_quantities.....', product_quantities)
    except AttributeError:
        product_quantities = 'N/A'
        print('Not Found')


    # ------------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find('div', {"class": "current-price"}).text.strip()
        print('price.....', price)
    except AttributeError:
        price = 'N/A'
        print('Not Found')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        features_1 = []
        for features in soup.find('div', {"itemprop": "description"}):
            features_1.append(features.text.replace('\n', '').replace('\t', '').replace('\r', ''))
        print('features_1.....', features_1)
    except AttributeError:
        features_1 = 'N/A'
        print('object has no attribute ... features_1')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = soup.find('div', {"class": "product-description"}).text.strip()
        print('description.....', description)
    except AttributeError:
        description = 'N/A'
        print('object has no attribute ... description')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        popular_downloads = soup.find('popular-downloads')
        if popular_downloads:
            items_json = popular_downloads[':items']
            items = json.loads(items_json)
            datasheet.append([item['scene7Url'] for item in items])
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = 'N/A'
        print('object has no attribute ... datasheet')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        part_accessories = []
        part_ass = soup.find('div', {"class": "blockreassurance_product"}).find_all('p')
        for accessories in part_ass:
            part_accessories.append(accessories.text.strip())
        print('part_accessories.....', part_accessories)
    except AttributeError:
        part_accessories = 'N/A'
        print('object has no attribute.......part_accessories')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        zip_card = []
        card = soup.find('div', {"class": "cad-tab-links"}).find_all('a')
        for card_links in card:
            zip_card.append(card_links.get("href"))
        print('zip_card.....', zip_card)
    except AttributeError:
        zip_card = 'N/A'
        print('object has no attribute ... zip_card')




    # --------------------------------------  Images  ------------------------------------------------------------------
    try:
        image = []
        img_1 = soup.find('meta', {"property": "og:image"}).get('content')
        image.append(img_1)

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
        # "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": src_values,
        "Product_Detail": description,
        "Features": features_1,
        # "Accessories": href_type_exe,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        "Video_Url": video,
        # "Quantity": stock,
        "Price(usd)": price,
        "Kits/Components": part_accessories,
        "Label": product_manufacturer,
        "Quantity":product_quantities,
        "Cross_Reference": product_reference,
        "Url": url,

    }]  # save data here

    Data_Save(row, mylist)
    return product_title

# except Exception as e:
#     print('Error...', e)
    # send_email(f'Error... {e}')


def Data_Save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, product_title, mpn):
    #   /var/www/html/webscr/destination_dir
    print('Tables')
    table = soup.find('section', {"id": "ecat-specifications"}).find('specification').attrs[':specification-items']
    all_table_data = json.loads(table)
    attr_name = []
    attr_value = []
    for table_data in all_table_data:
        try:
            for data in table_data['specifications']:
                attr_name.append(data['label'])
                attr_value.append("rp_"+data['value'].encode('latin-1', errors='ignore').decode('utf-8', errors='ignore'))


        except KeyError:
            print('No specification in table')

    for a, b in zip(attr_name, attr_value):
        print(a, '........', b)
        save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/hqtinc.com/data/hqtinc-specs.txt", 'a+',encoding='utf-8')
        save.write(f"{url}\t{product_title}\t{mpn}\t{a}\t{b}\n")
    print('save data')


def main():
    #   /var/www/html/webscr/source_dir/
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/hqtinc.com/url/hqtinc-product-url.csv")['URL']
    i = 0
    for url_count, url in enumerate(url_link[i:3], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)
        soup = Get_Soup_Url(url)
        product_detail(url, soup)
        # try:
        #     product_title, mpn = product_detail(url, soup)
        #     # Get_Specs_Table(url, soup, product_title, mpn)
        # except Exception:
        #     break

        # selenium calling here
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)
    print('loop End')
    msg = "Your web scraping script has completed "
    send_email(msg)
    print(msg)


if __name__ == "__main__":
    main()
