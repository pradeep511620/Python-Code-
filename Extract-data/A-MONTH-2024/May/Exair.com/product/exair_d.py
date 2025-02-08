import smtplib
import time
import concurrent.futures
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# File paths and constants
CSV_FILE_PATH = "D:/Web-Scrapping/A-MONTH-2024/May/Exair.com/data/Exair.csv"
URL_FILE_PATH = "D:/Web-Scrapping/A-MONTH-2024/May/Exair.com/url/Product-url.csv"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "raptorsupplyuk@gmail.com"
SENDER_PASSWORD = "unwkbryielvgwiuk"
RECIPIENTS = ["pradeep@raptorsupplies.co.uk", "raptorsupplyuk@gmail.com"]
BRAND = "Exair"

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.pk = self.get_soup_and_driver()

    def get_soup_and_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={USER_AGENT}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        try:
            driver.get(self.url)
            time.sleep(2)
            page_sources = driver.page_source
            pk = BeautifulSoup(page_sources, 'lxml')
        finally:
            driver.quit()
        return pk

    @staticmethod
    def send_email(subject, body):
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = ','.join(RECIPIENTS)
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENTS, message.as_string())
        print("Email sent successfully")

    @staticmethod
    def data_save(row, cols):
        df = pd.DataFrame(row, columns=cols)
        print(df)
        df.to_csv(CSV_FILE_PATH, mode='a', header=False, index=False, lineterminator='\n')
        print('save data into csv files')

    def product_details(self):
        print("Product-url: ", self.url)
        l3_name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        try:
            names = [l3.text.strip() for l3 in self.pk.select("div.breadcrumbs ul li")]
            l3_name = "## ".join(names)
            print('l3_name: ', l3_name)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            print('l3_name: ', l3_name)

        if l3_name:
            categories = l3_name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]
            print('catlvl1: ', catlvl1)
            print('catlvl2: ', catlvl2)
            print('catlvl3: ', catlvl3)

        try:
            product_title = self.pk.find('h1', class_="page-title").find('span').text.strip()
            print('product_title: ', product_title)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            product_title = ''
            print('product_title: ', product_title)

        try:
            list_of_price = self.pk.select_one('.price').text.strip()
            price = {'list_price': list_of_price, 'qty': '1', 'moq': '1'}
            print("Price: ", price)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError) as e:
            print(f"An error occurred: {e}")
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}

        miscellaneous = ''
        print('miscellaneous: ', miscellaneous)

        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": BRAND, "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": "",
            "breadscrumbs": l3_name, "image_urls": "", "mpn": "",  # These fields are placeholders
            "specification_1": "", "specification_2": "", "datasheets": "",
            "product_description_1": "", "product_description_2": "",
            "accessories": "", "video_links": "", "miscellaneous": miscellaneous,
            "scraped_by": "Pradeep_RaptorTech",
        }]
        # self.data_save(raw_data, list_column)
        print('Complete all Your Program')



def main():
    url_links = pd.read_csv(URL_FILE_PATH)['URL']
    product_urls = url_links[:3].tolist()

    scraper = WebScraper(product_urls[2])
    # scraper.send_email("Script Execution Started", "Your web scraping script has been started")

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        try:
            executor.map(lambda url: WebScraper(url).product_details(), product_urls)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            scraper.send_email("Script Execution Error", f"An error occurred: {e}")
            raise RuntimeError("Error encountered. Program terminated.")

    # scraper.send_email("Script Execution Completed", "Your web scraping script has completed successfully")


if __name__ == "__main__":
    main()
