# import os
import smtplib
import time
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import concurrent.futures
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


urls = []
save_files = open("D:/Web-Scrapping/A-MONTH-2024/May/Regalrexnord-Marathon.com/data/MarathonMix.csv", "a+", encoding="utf-8")
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
        driver.maximize_window()
        try:
            driver.get(self.url)
            time.sleep(1)
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
        time.sleep(1)
        # print(ress.status_code)
        # print(soup)
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
        mpns = ''
        models = ''
        catalogs = ''

        try:
            names = [l3.text.strip() for l3 in self.pk.find('ol', class_="breadcrumb").find_all('li')]
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
            product_title = self.pk.find('div', class_="page-title").h1.text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            product_title = ''
            print('product_title.....', product_title)

        # -------------------------------------------------- Price-- ---------------------------------------------------
        """            
        price = ''
        try:
            list_of_some = self.pk.find(class_="product-cart")
            prices_details = list_of_some.text.strip().replace("\n", ">>").split(">>>>>>")
            for prices in prices_details:
                if "List Price" in prices:
                    product_price_1 = prices.replace(">>List Price:>>>>", "").replace("List Price:>>>>", "")
                    price = {'list_price': product_price_1, 'qty': '1', 'moq': '1'}
            print('price.....', price)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print('product_price.....', price)"""
        price = ''
        try:
            list_of_some = self.pk.find(class_="product-cart")
            if list_of_some:
                prices_details = list_of_some.text.strip().replace("\n", ">>").split(">>>>>>")
                for prices in prices_details:
                    if "List Price" in prices:
                        product_price_1 = prices.replace(">>List Price:>>>>", "").replace("List Price:>>>>", "")
                        price = {'list_price': product_price_1, 'qty': '1', 'moq': '1'}
                        break
            if not price:
                price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError) as e:
            print(f"An error occurred: {e}")
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}

        print('price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            param_rows = self.pk.find(class_='param-row-list')
            all_model = param_rows.text.strip().replace("\n", ">>").split(">>>>>>")
        except AttributeError:
            all_model = ''
        for mode in all_model:
            if "Part #" in mode:
                mpns = "rp_" + mode
            elif "Catalog #" in mode:
                catalogs = mode
            elif "Model #" in mode:
                models = mode

        try:
            mpn = mpns.replace("Part #:", "")
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

        try:
            desc = [desc_text.text.strip() for desc_text in
                    self.pk.find(class_="product attribute description").find_all('span')]
            # if not desc:
            #     desc = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "//*[@itemprop='description']")]
            description_1 = {"desc": desc, 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [des_1.text.strip() for des_1 in self.pk.find(class_="product-info").find_all('li')]
            print('description_2.....', description_2)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get('href'), "alt": img.get('alt')} for img in
                      self.pk.find('div', class_="row product-gallery app-figure").find_all('a')]
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            images = ''

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            row_count = 0
            attr_name = []
            attr_value = []
            for table_row in self.pk.find_all(class_="specifications-table_col col-md-3 col-print-3 pull-left"):
                row_count += 1
                tab = table_row.text.strip().replace(":", "")
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
            datasheet = [pdf.get('onclick') for pdf in self.pk.find('div', class_="product-social-links").find_all('a') if pdf.get('onclick') is not None]
            print('datasheet.....', datasheet)
        except (AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            datasheet = []
            print('datasheet.....', datasheet)

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('src') for video_link in
                     self.pk.find('div', class_="install-instructions").find_all('iframe')]
            print('video.....', video)
        except (NoSuchElementException, TypeError, IndexError, AttributeError):
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = ["https://www.regalrexnord.com/" + href_link.get('href') for href_link in self.pk.find_all(class_="row flex-row flex-wrap")[0].find_all('a') if "products" in href_link.get('href', '')]
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, IndexError, TypeError, AttributeError):
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------

        Weight_lbs = ''
        try:
            list_of_some = self.pk.find(class_="product-cart")
            weight_details = list_of_some.text.strip().replace("\n", ">>").split(">>>>>>")
            for weights in weight_details:
                if "Weight" in weights:
                    weight = weights.replace("Weight:", "")
                    Weight_lbs = {"Shipping weight": weight}
            print('Weight.....', Weight_lbs)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            Weight_lbs = ''

        try:
            catalog = {"Catalog #": catalogs.replace("Catalog #:", "")}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            catalog = ''

        try:
            model = {"model#": models.replace("Model #:", "")}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            model = ''

        try:
            LEESON = {"Leeson": self.pk.find('span', class_="rrx-badge-products-head").text}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            LEESON = ''

        try:
            flags = {'flag': self.pk.find(class_="product-flag new").find('span').text.strip()}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            flags = ''

        miscellaneous = str(catalog) + "," + str(model) + "," + str(LEESON) + "," + str(flags)
        print('miscellaneous.....', miscellaneous)

        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": "LEESON", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": Weight_lbs,
            "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": specifications_2, "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": description_2,
            "accessories": realated, "video_links": video, "miscellaneous": miscellaneous,
            "scraped_by": "Pradeep_RaptorTech",
        }]

        Data_Save(raw_data, list_column)
        print('Complete all Your Program')
        print()

        # def close_driver(self):
        #     self.driver.quit()

def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# scaper_name = WebScraper('https://www.regalrexnord.com/products/electric-motors/miscellaneous/200-1800-tefc-445tsc-3-60-575-yd-445tstfn16053')
# scaper_name = WebScraper('https://www.regalrexnord.com/products/electric-motors/ac-motors-nema/general-purpose-motors/general-purpose-motor-0-75-hp-3-ph-60-hz-575-v-3600-rpm-56-frame-tefc-056t34f5334')
# scaper_name.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------


def ReadUrlFromList():
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Regalrexnord-Marathon.com/url/Leeson_Marathon URLs.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:], start=i):
        urls.append(url)
        # print('product_url.....', url_count)

        # scaper_name = WebScraper(url)
        # scaper_name.Product_Details()
        # scaper_name.close_driver()
    return urls


# ReadUrlFromList()


def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        try:
            executor.map(lambda url: WebScraper(url).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
