import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import json
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

# /var/www/html/webscr/destination_dir
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/shoplinco.com/data/shoplinco-all-data.csv",
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

    global h, k
    try:
        l3_name = []
        bread = soup.find('nav', {"class": "breadcrumbs"}).find_all('a')
        for l3 in bread:
            breadcrumb = l3.text.strip()
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

    try:
        mix_datas = []
        number = 0
        attr_name = []
        attr_value = []
        sku_1 = soup.find('div', class_="product-detail-container").find_all('span')
        for sku_details in sku_1:
            mix_datas.append(sku_details.text.strip())
        for tab in mix_datas:
            number += 1
            if number % 2 != 0:
                attr_name.append(tab)
            else:
                attr_value.append(tab)
        print(attr_name)
        print(attr_value)
        # for k, h in zip(attr_name, attr_value):
        #     print(k, ".....", h)
    except AttributeError:
        attr_name = ''
        attr_value = ''
        print('nn')


    sku = []
    for skus in soup.find('li', {"class": "product-detail-sku"}).findAll('span'):
        sku.append(skus.text.strip())
    print('sku.....', sku)

    # ------------------------------------------------------------------------------------------------------------------

    try:
        price = soup.find('div', {"class": "price-value-wrapper"}).text.strip().replace('\n', '')
        print('price.....', price)
    except AttributeError:
        price = 'N/A'
        print('object has no attribute ... price')


    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     feature = soup.find('div', {"class": "product-description"}).find_all(class_="easytabs-content-holder")[1].text.strip().replace("\n", " >> ")
    #     print('feature.....', feature)
    # except AttributeError:
    #     feature = 'N/A'
    #     print('object has no attribute ... feature')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = []
        description_1 = soup.find('div', {"id": "description"}).find("p")
        for description_details in description_1:
            description.append(description_details.text.strip().replace('\n', '>>').encode('latin-1', errors='ignore').decode('utf-8', errors='ignore'))
        print('description.....', description)
    except AttributeError:
        description = 'N/A'
        print('object has no attribute ... description')


    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     datasheet = []
    #     pdf = soup.find('div', {"class": "product-description"}).find_all(class_="easytabs-content-holder")[2].find_all('a')
    #     for pdf_link in pdf:
    #         download = pdf_link.get('href')
    #         datasheet.append(download)
    #     print('datasheet.....', datasheet)
    # except AttributeError:
    #     datasheet = 'N/A'
    #     print('object has no attribute ... datasheet')

    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------


    # --------------------------------------  Images  ------------------------------------------------------------------
    try:
        image = []
        table = soup.find('div', {"class": "product-images"})
        img_links = table.find_all('img')
        for img_link in img_links:
            href = img_link.get('src')
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
    try:
        related_url = soup.find('section', {"class": "products-related product-details"}).find_all('a')
        unique_urls = set()
        for related_urls in related_url:
            urls = related_urls.get('href')
            if urls not in unique_urls and 'id=' not in unique_urls:
                unique_urls.add(urls)
        print('related_urls.....', unique_urls)
    except AttributeError:
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
        # "Features": feature,
        # "Accessories": brand,
        # "Datasheet": datasheet,
        "Item_Name": attr_name,
        "item_ID": attr_value,
        # "Uses": uses_d,
        # "Video_Url": video,
        # "Quantity": stock,
        "Price(usd)": price,
        # "Spare_Parts": parts,
        # "weight(kg)": Ship_Weight,
        # "Quantity":product_quantities,
        # "Cross_Reference": return_shipping_info,
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
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/shoplinco.com/data/shoplinco-specs.txt", 'a+', encoding='utf-8')

    print('Tables')
    try:

        try:
            attr_name3 = []
            attr_value3 = []
            table3 = soup.find("div", class_="specs").find_all('p')
            for p in table3:
                tab3 = p.text.strip().replace(": ", ">>").split(">>")
                attr_name3.append(tab3[0])
                try:
                    attr_value3.append(str("rp_"+tab3[1]).encode('latin-1', errors='ignore').decode('utf-8', errors='ignore'))
                except IndexError:
                    attr_value3.append("N/A")
            for a3, b3 in zip(attr_name3, attr_value3):
                print(a3, ".....", b3)
                save.write(f"{url}\t{product_title}\t{sku}\t{a3}\t{b3}\n")
            print('save data middle')
        except AttributeError:
            print('table -2')
            try:
                attr_name1 = []
                attr_value1 = []
                table1 = soup.find("table", {"id": "productDetails_techSpec_section_1"})
                for th in table1.find_all('th'):
                    th_1 = th.text.strip().encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
                    attr_name1.append(th_1)
                for td in table1.find_all('td'):
                    td_1 = td.text.strip().encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
                    attr_value1.append("rp_"+td_1)
                for a1, b1 in zip(attr_name1, attr_value1):
                    print(a1, ".....", b1)
                    save.write(f"{url}\t{product_title}\t{sku}\t{a1}\t{b1}\n")
                print('save data last')
            except AttributeError:
                print('table -3')
                try:
                    count = 0
                    attr_name = []
                    attr_value = []
                    table = soup.find('div', class_="tab-product-description").find('table').find_all('td')
                    for td in table:
                        if "PRODUCT SPECIFICATIONS" not in td:
                            # print(td.text.strip())
                            count += 1
                            tab = td.text.strip().encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
                            if count % 2 != 0:
                                attr_name.append(tab)
                            else:
                                attr_value.append("rp_"+tab)
                    for a, b in zip(attr_name, attr_value):
                        print(a, "..........", b)
                        save.write(f"{url}\t{product_title}\t{sku}\t{a}\t{b}\n")
                    print('save data start')
                except AttributeError:
                    print('table -1')

    except Exception as e:
        print(e)




def main():
    #   /var/www/html/webscr/source_dir/
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/shoplinco.com/url/shoplinco-product-url.csv")['URL']
    print(len(url_link))
    i = 0
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        soup = Get_Soup_Url(url)
        product_title, sku = product_detail(url, soup)
        Get_Specs_Table(url, soup, product_title, sku)



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
