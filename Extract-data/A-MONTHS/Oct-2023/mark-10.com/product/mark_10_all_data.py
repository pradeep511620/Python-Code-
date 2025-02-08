import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

# /var/www/html/webscr/destination_dir
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/mark-10.com/data/mark-10-all-data.csv", 'a', encoding='utf-8')

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
    try:
        try:
            l3_name = []
            bread = soup.find('div', {"class": "breadcrumb-wrap"})
            for l3 in bread:
                breadcrumb = l3.text.strip().encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
                l3_name.append(breadcrumb)
            print('l3_name.....', l3_name)
        except AttributeError:
            l3_name = 'N/A'
            print('object has no attribute ... l3_name')

        # ------------------------------------------------------------------------------------------------------------------
        try:
            product_title = soup.find('h5', {"class": "product-subhead"}).text.strip()
            product_title = product_title.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
            print('product_title.....', product_title)
        except AttributeError:
            try:
                product_title = soup.find('div', class_="row").find(class_="h2").text.strip()
                print('product_title.....', product_title)
            except AttributeError:
                product_title = 'N/A'
                print('object has no attribute ... product_title')


        # ------------------------------------------------------------------------------------------------------------------
        try:
            series = soup.find('div', {"class": "d-none d-md-block"}).find('h1').text.strip()
            print('series.....', series)
        except AttributeError:
            try:
                series = soup.find('div', class_="row").find("a").text.strip()
                print('series.....', series)
            except AttributeError:
                series = 'N/A'
                print('Not Found')

    # ------------------------------------------------------------------------------------------------------------------
        try:
            des = ''
            discontinued = soup.find('div', {"class": "col-md-8"})
            if discontinued:
                des = discontinued.find("span").text.strip()
                print('discontinued.....', des)
        except AttributeError:
            des = 'N/A'
            print("Not")

        # try:
        #     price = soup.find('div', {"class": "price-value-wrapper"}).text.strip().replace('\n', '')
        #     print('price.....', price)
        # except AttributeError:
        #     price = 'N/A'
        #     print('object has no attribute ... price')

        # ------------------------------------------------------------------------------------------------------------------


        try:
            feature = soup.find('div', {'class': 'product-tab-content'}).text.strip().replace("\n", " >>> ").encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
            print('feature.....', feature)
        except AttributeError:
            feature = 'N/A'
            print('object has no attribute ... feature')

        # ------------------------------------------------------------------------------------------------------------------
        try:
            description = []
            description_1 = soup.find('div', {"class": "product-description"})
            for description_details in description_1:
                description.append(
                    description_details.text.strip().replace('\n', '>>').encode('latin-1', errors='ignore').decode('utf-8', errors='ignore'))
            print('description.....', description)
        except AttributeError:
            description = 'N/A'
            print('object has no attribute ... description')
        except TypeError:
            description = 'N/A'
            print('object has no attribute ... description')

        # ------------------------------------------------------------------------------------------------------------------
        try:
            datasheet = []
            pdf = soup.find('ul', {"class": "download_links"}).find_all('a')
            for pdf_link in pdf:
                download = "https://mark-10.com"+pdf_link.get('href')
                datasheet.append(download)
            print('datasheet.....', datasheet)
        except AttributeError:
            datasheet = 'N/A'
            print('object has no attribute ... datasheet')

        # ------------------------------------------------------------------------------------------------------------------
        try:
            dimationsss = []
            dimenstions = soup.find_all("img", {"decoding": "async"})
            for img_1 in dimenstions:
                dim_img = img_1.get('src')
                if "dim" in dim_img:
                    dimationsss.append("https://mark-10.com"+dim_img)
            print('dimationsss.....', dimationsss)
        except AttributeError:
            dimationsss = 'N/A'
            print("Not")

        # ------------------------------------------------------------------------------------------------------------------
        try:
            inbox_list = []
            inbox = soup.find('div', class_="itb-image").find('img')['src']
            inbox_datas_data = ''
            inbox_data = soup.find('div', class_="row").find_all(class_="col-sm-6")
            for inbox_datas in inbox_data:
                inbox_datas_data = inbox_datas.text.strip().replace("\n", ">>")
            In_box = inbox + " >> " + inbox_datas_data
            inbox_list.append(In_box)
            print('inbox_list.....', inbox_list)
        except AttributeError:
            inbox_list = ''
            print('Not')
        # ------------------------------------------------------------------------------------------------------------------

        # --------------------------------------  Images  ------------------------------------------------------------------
        try:
            image = []
            table = soup.find('div', {"class": "gallery-column"})
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
            related_url = soup.find('div', {"class": "related-products"}).find_all('a')
            unique_urls = set()
            for related_urls in related_url:
                urls = related_urls.get('href')
                if urls not in unique_urls:
                    unique_urls.add(urls)
            print('related_urls.....', unique_urls)
        except AttributeError:
            unique_urls = ''
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
            "Grainger_Sku": series,
            "L3_Name": l3_name,
            "Product_title": product_title,
            "Image_URL_1": image[0],
            "Image_URL_2": image[1],
            "Image_URL_3": image[2],
            "Image_URL_4": image[3],
            "Image_URL_5": image[4],
            "Image_Name": dimationsss,
            "Product_Detail": description,
            "Features": feature,
            # "Accessories": brand,
            "Datasheet": datasheet,
            # "Item_Name": dimationsss,
            # "item_ID": attr_value,
            # "Uses": uses_d,
            # "Video_Url": video,
            # "Quantity": stock,
            # "Price(usd)": price,
            "Spare_Parts": inbox_list,
            # "weight(kg)": Ship_Weight,
            # "Quantity":product_quantities,
            "Remarks": des,
            "Cross_Reference": unique_urls,
            "Url": url,

        }]  # save data here

        Data_Save(row, mylist)
        return product_title, series

    except Exception as e:
        print('Error...', e)
        # send_email(f'Error... {e}')


def Data_Save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, product_title, series):
    #   /var/www/html/webscr/destination_dir
    save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/mark-10.com/data/mark-10-specs.txt", 'a+', encoding='utf-8')

    print('Tables')


    # try:  table-striped
    # table = soup.find(class_="table-striped table-oi").find_all('tr')
    # for tables in table:
    #     tab = tables.text.strip().replace("\n", ">>").split(">>")
    #     if tab:
    #         table_row = "\t".join("rp_" + item for item in tab)
    #         print(table_row)
    #             save.write(f"{url}\t{product_title}\t{table_row}\n")
    #     print('save data into table')
    # except AttributeError:
    #     print('pass')
    try:
        table = soup.find(class_="table-striped").find_all('tr')
        for tables in table:
            tab = tables.text.strip().replace("\n", ">>").split(">>")
            if tab:
                table_row = " \t ".join("rp_"+item.strip() for item in tab).encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
                print(table_row)
                save.write(f"{url}\t{product_title}\t{series}\t{table_row}\n")
    except AttributeError:
        pass



def main():
    #   /var/www/html/webscr/source_dir/
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/mark-10.com/url/mark-10-product-url.csv")[
        'URL']
    print(len(url_link))
    i = 35
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)

        soup = Get_Soup_Url(url)

        product_title, series = product_detail(url, soup)
        Get_Specs_Table(url, soup, product_title, series)


        # selenium calling here
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)
    print('loop End')
    # msg = "Your web scraping script has completed "
    # send_email(msg)
    # print(msg)


if __name__ == "__main__":
    main()
