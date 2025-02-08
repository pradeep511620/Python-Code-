# import smtplib
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import concurrent.futures
from urllib.parse import urljoin
import json
import pandas as pd
import requests
# from itertools import zip_longest
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Proxy credentials
proxy_url = 'https://catalog:kCVftpL8r8fsw7Wmb7@gate.smartproxy.com:7000'
proxy = {
    'http': proxy_url,
    'https': proxy_url
}

save_files = open("D:/Web-Scrapping/A-MONTH-2024/May/Megadepot-Dixon.com/data/Megadepot-Dixon.csv", "a+", encoding="utf-8")
base_url = 'https://megadepot.com'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.pk = self.GetSoupUrl()
        # self.driver = self.get_driver()
        # self.pk = self.GetSoupAndDriver()
        self.driver = None

    def GetSoupAndDriver(self):
        chrome_options = Options()
        chrome_options.add_argument(f'--proxy-server={proxy_url}')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        try:
            driver.get(self.url)
            time.sleep(3)
            page_sources = driver.page_source
            pk = BeautifulSoup(page_sources, 'lxml')
        finally:
            driver.quit()

        return pk

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        return driver

    def GetSoupUrl(self):
        sess = requests.Session()
        ress = sess.get(self.url, headers=headers, proxies=proxy)
        soup = BeautifulSoup(ress.content, "lxml")
        return soup

    def send_email(self):
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = ["nkmishra@nextgenesolutions.com", "raptorsupplyuk@gmail.com", ]
        # sender_email = ["nkmishra@nextgenesolutions.com", "nirbhay@raptorsupplies.com", "tajender@raptorsupplies.com"]
        smtp_username = "raptorsupplyuk@gmail.com"
        smtp_password = "unwkbryielvgwiuk"
        message = MIMEMultipart()
        message["From"] = smtp_username
        message["To"] = ','.join(sender_email)
        message["Subject"] = "Script Execution Status"
        body = self.pk.msg
        message.attach(MIMEText(body, "plain"))
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, sender_email, message.as_string())
        print("Email sent successfully")


        # mgs = "Your web scraping script has been started"
        # send_email(mgs)
        # print(mgs)


    def Product_Details(self):
        print(f"Product-url---: {self.url}")
        # try:
        l3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        Brand = 'Dixon Valve'

        try:
            names = [l3.text.strip() for l3 in self.pk.find_all("li", itemprop='itemListElement')]
            l3_Name = "## ".join(names)
            print('l3_Name.....', l3_Name)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            print('l3_Name.....', l3_Name)

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)
        # --------------------------------------------------------------------------------------------------------------
        try:
            product_title = self.pk.find('h1', {'id': 'product-name'}).text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            product_title = ''
            print('product_title.....', product_title)

        # -------------------------------------------------- Price-- ---------------------------------------------------
        try:
            product_price_1 = self.pk.find("span", class_="price hot").text.strip()
            price = {'list_price': product_price_1 + '/EACH', 'qty': '1', 'moq': '1'}
            print('price.....', price)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print('product_price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.pk.select_one('.product .part-number[itemprop="mpn"]').text.strip()
            print('SKU.....', mpn)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            mpn = 'N/A'
            print('SKU:', mpn)

        # ---------------------------------------------- Description_1 -------------------------------------------------

        try:
            short = self.pk.find('dd', class_="last-visible").text.strip()
            short_desc = short
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            short_desc = ''

        try:
            desc = [desc_text.text.strip() for desc_text in self.pk.find(id="productDescription").find_all('p')]
            # if not desc:
            #     desc = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "//*[@itemprop='description']")]
            description_1 = {"desc": desc, 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [des_1.text.strip() for des_1 in self.pk.select(".description-wrapper ul li")]
            print('description_2.....', description_2)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": urljoin(base_url, img.get('src')), "alt": img.get('alt')} for img in self.pk.find('figure', class_="logo").find_all('img')]
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            images = ''



        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            row_count = 0
            attr_name = []
            attr_value = []
            table_specs = self.pk.find('section', {'id': 'specification'}).find('table').find_all('td')
            for table_row in table_specs:
                row_count += 1
                tab = table_row.text.strip()
                if row_count % 2 != 0:
                    attr_name.append(tab)
                else:
                    attr_value.append(tab)
            specs_li = [{name_li: values_li} for name_li, values_li in zip(attr_name, attr_value)]
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            specs_li = ''

        specifications_1 = str(specs_li)
        print('specifications_1.....', specifications_1)

        # ----------------------------------------------- specifications_2 ---------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//div[@id='collapse")]
            print('specifications_2.....', specifications_2)
        except (AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            specifications_2 = []
            print('specifications_2.....', specifications_2)

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [pdf.get('onclick') for pdf in self.pk.find('div', id="documentsSection").find_all('a')]
            print('datasheet.....', datasheet)
        except (AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            datasheet = []
            print('datasheet.....', datasheet)

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = []
            for video_details in self.driver.find_elements(By.XPATH, "//*[@id='product-video-frame']//iframe"):
                video.append(video_details.get_attribute('src'))
            print('video.....', video)
        except (NoSuchElementException, TypeError, IndexError, AttributeError):
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        # try:
        #     related_url = [urljoin(base_url, href_tag.get("href")) for href_tag in self.pk.select(".principals.list.mobile-slider.no-slider article a") if "product" in href_tag.get("href", "")]
        #     realated = [{'accessories': related_url}]
        #     print("realated.....", realated)
        # except (NoSuchElementException, IndexError, TypeError, AttributeError):
        #     realated = [{'accessories': []}]
        #     print("realated.....", realated)
        realated = ''
        href_tag = self.pk.find('a', class_='btn-principals')
        if href_tag:
            data_uri_list_str = href_tag.get('data-uri-list')
            if data_uri_list_str:
                data_uri_list = json.loads(data_uri_list_str)
                related_url = list(data_uri_list.values())
                realated = [{'accessories': related_url}]
                print("realated.....", realated)
            else:
                print("data-uri-list attribute not found")

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            Availability = {"Availability": self.pk.select_one(".status.typically-in-stock .text").text.strip()}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            Availability = ''

        try:
            Condition = {"Condition": self.pk.select_one(".text.condition .visible-text").text.strip()}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            Condition = ''

        try:
            Notes_details = self.pk.find('p', id="note-shipping").text.strip()
            Notes = {'Notes': Notes_details}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            Notes = '1'
        try:
            Notes_warning = self.pk.find('div', id="notes-warning").text.strip()
            warning = {'Notes warning': Notes_warning}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            warning = '1'




        miscellaneous = str(Availability) + ", " + str(Condition) + ", " + str(Notes) + ", " + str(warning)
        print('miscellaneous.....', miscellaneous)

        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": Brand, "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": '',
            "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": specifications_2, "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": description_2,
            "accessories": realated, "video_links": video, "miscellaneous": miscellaneous,
            "scraped_by": "Pradeep_RaptorTech",
        }]

        Data_Save(raw_data, list_column)
        print('Complete all Your Program')
        print()
        # except Exception as e:
        #     print(f"Error{e}")
        #     with open('remain_url.txt', "a+", encoding="utf-8") as file:
        #         file.write(f"{self.url}\n")




def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')



# scaper_name = WebScraper('https://megadepot.com/product/dixon-valve-vr4040cs-als45-dixon-vapor-recovery-coupler-x-45deg-swivel-hose-shank')
# scaper_name.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------

def ReadUrlFromList():
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Megadepot-Dixon.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    i = 0
    for url_count, url in enumerate(url_links[i:20], start=i):
        print('product_url.....', url_count)
        scaper_name = WebScraper(url)
        scaper_name.Product_Details()


# ReadUrlFromList()


def main():
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Megadepot-Dixon.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    Product_url = []
    start_url = 1500
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
