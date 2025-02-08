# import smtplib
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import concurrent.futures
import pandas as pd
import requests
# from itertools import zip_longest
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


save_files = open("D:/Web-Scrapping/A-MONTH-2024/May/Exair.com/data/Exair.csv", "a+", encoding="utf-8")
base_url = ''
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

class WebScraper:
    def __init__(self, url):
        self.url = url
        # self.pk = self.GetSoupUrl()
        # self.driver = self.get_driver()
        self.pk = self.GetSoupAndDriver()
        self.driver = None

    def GetSoupAndDriver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get(self.url)
            time.sleep(2)
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
        ress = sess.get(self.url, headers=headers)
        soup = BeautifulSoup(ress.content, "lxml")
        # time.sleep(6)

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
        print("Product-url---: ", self.url)

        l3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        Brand = 'Exair'
        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            names = [l3.text.strip() for l3 in self.pk.select("div.breadcrumbs ul li")]
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
        # -------------------------------------------------- Title -----------------------------------------------------
        try:
            product_title = self.pk.find('h1', class_="page-title").find('span').text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            product_title = ''
            print('product_title.....', product_title)
        # -------------------------------------------------- Price -----------------------------------------------------
        try:
            list_of_price = self.pk.select_one('.price').text.strip()
            price = {'list_price': list_of_price, 'qty': '1', 'moq': '1'}
            print("Price.....", price)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError) as e:
            print(f"An error occurred: {e}")
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.pk.find(class_="product attribute sku").find(itemprop="sku").text.strip()
            print('SKU.....', mpn)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            mpn = 'N/A'
            print('SKU:', mpn)
        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            short = self.pk.find('div', itemprop="description").text.strip()
            short_desc = short
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            short_desc = ''
        #
        try:
            desc = [desc_text.text.strip() for desc_text in self.pk.select('.item.content.tab-1')[1]]
            # if not desc:
            #     desc = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "//*[@itemprop='description']")]
            description_1 = {"desc": desc, 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [des_1.text.strip() for des_1 in self.pk.select("#overview-tab-2 ul li")]
            print('description_2.....', description_2)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get('src'), "alt": img.get('alt')} for img in self.pk.find('div', class_="product media vertical-md").find_all('img')]
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            images = ''

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            header_row = []
            th_data = ''
            # Extracting header row
            for th_d in self.pk.select('#performance-tab-1 table tbody tr')[2:3]:
                header_row = th_d.get_text(strip=True, separator=">>").replace('"H>>2>>O', "H2O").split(">>")
            # Extracting data rows
            th_data = [th.get_text(strip=True, separator=">>").split(">>") for th in self.pk.select('#performance-tab-1 table tbody tr')[3:-1]]
            row_dicts = []
            for data_row in th_data:
                row_dict = {}
                for header, value in zip(header_row, data_row):
                    row_dict[header] = value
                row_dicts.append(row_dict)
            specs_li = [{key: value} for row_dict in row_dicts for key, value in row_dict.items()]
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            specs_li = ''

        specifications_1 = str(specs_li)
        print('specifications_1.....', specifications_1)



        try:
            for table_details in self.pk.select('#performance-tab-1 table tbody tr'):
                tab_1 = table_details.get_text(strip=True, separator=">>").replace('"H>>2>>O', "H2O").split(">>")
                if tab_1:
                    table_rows = "\t".join(tab_1)
                    print(table_rows)
                    with open("table_data.txt", "a+", encoding='utf-8') as file_save:
                        file_save.write(f"{self.url}\t{mpn}\t{product_title}\t{table_rows}\n")
        except (AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            print('Not found')

        # ----------------------------------------------- specifications_2 ---------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//div[@id='collapse")]
            print('specifications_2.....', specifications_2)
        except (AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            specifications_2 = []
            print('specifications_2.....', specifications_2)

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [pdf.get('onclick') for pdf in self.pk.find('div', class_="product-social-links").find_all('a') if pdf.get('onclick') is not None]
            print('datasheet.....', datasheet)
        except (AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            datasheet = []
            print('datasheet.....', datasheet)

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('data-url') for video_link in self.pk.select('.click-vlink')]
            print('video.....', video)
        except (NoSuchElementException, TypeError, IndexError, AttributeError):
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [href_link.get('href') for href_link in self.pk.select("div.slick-list.draggable li a")]
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, IndexError, TypeError, AttributeError):
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            advantage_details = [ad.text.strip() for ad in self.pk.select("#overview-tab-3 ul li")]
            Advantages = {"Advantages": advantage_details}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            Advantages = ''

        try:
            WARNING_details = [ad.text.strip() for ad in self.pk.select("#moreinfo-tab-1 p")]
            WARNING = {"WARNING": WARNING_details}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            WARNING = ''

        try:
            include_details = [ad.text.strip() for ad in self.pk.select("#overview-tab-5 ul li")]
            Included = {"What's Included": include_details}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            Included = ''



        miscellaneous = str(Advantages) + ", " + str(Included) + ", " + str(WARNING)
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
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": "",
            "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": specifications_2, "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": description_2,
            "accessories": realated, "video_links": video, "miscellaneous": miscellaneous,
            "scraped_by": "Pradeep_RaptorTech",
        }]

        Data_Save(raw_data, list_column)
        print('Complete all Your Program')
        print()


        self.pk.quit()


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')



# scaper_name = WebScraper('https://www.exair.com/vg-collection.html')
# scaper_name.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------

def ReadUrlFromList():
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Exair.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:15], start=i):
        print('product_url.....', url_count)
        scaper_name = WebScraper(url)
        scaper_name.Product_Details()


ReadUrlFromList()


def main():
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Exair.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    Product_url = []
    start_url = 50
    for url_count, url in enumerate(url_links[start_url:500], start=start_url):
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


# if __name__ == "__main__":
#     main()
