# import smtplib
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import concurrent.futures
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

urls = []
save_files = open("D:/Web-Scrapping/A-MONTH-2024/May/Mitchellinstrument-Cementex.com/data/Mitchellinstrument.csv", "a+", encoding="utf-8")
base_url = ''
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
        Special = ''
        Regular = ''
        # print(self.pk.prettify())

        try:
            titles = [l3.text.strip() for l3 in self.pk.find_all('h1', class_="page-title")]
            names = ["Home"] + titles
            l3_Name = "## ".join(names)

            print('l3_Name.....', l3_Name)

            # names = "Home" + [l3.text.strip() for l3 in self.pk.find('h1', class_="page-title")]
            # l3_Name = "## ".join(names)
            # print('l3_Name.....', l3_Name)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            print('l3_Name.....', l3_Name)

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)
        # print(self.soup.prettify())
        # --------------------------------------------------------------------------------------------------------------
        try:
            product_title = self.pk.find('h1', class_="page-title").text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f'An error occurred: {e}')
            print('product_title.....', product_title)

        # -------------------------------------------------- Price-- ---------------------------------------------------

        try:
            price_details = self.pk.find(class_="product-info-price").text.strip().replace("\n", ">>").split(">>>>>>>>>>")
        except (NoSuchElementException,  AttributeError, TypeError, IndexError, Exception) as e:
            price_details = ''
            print(f"An error occurred: {e}")
        try:
            Special = price_details[0].replace("Special Price>>", "") + "/ Special Price"
        except (NoSuchElementException,  AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e}")
        try:
            Regular = price_details[1].replace("Regular Price>>", "") + "/ Regular Price"
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e}")
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}

        data = Special, Regular
        price = {'list_price': data, 'qty': '1', 'moq': '1'}
        print('price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            param_rows = self.pk.find(class_='product-info')
            # print(param_rows)
            all_model = param_rows.text.strip().replace("\n", ">>").split(">>>>>>")
        except AttributeError:
            all_model = ''
        for mode in all_model:
            if "Mitchell Part Number" in mode:
                mpns = mode



        try:
            mpn = mpns.replace("Mitchell Part Number:", "")
            print('SKU.....', mpn)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f'An error occurred: {e}')
            mpn = 'N/A'
            print('SKU:', mpn)

        # ---------------------------------------------- Description_1 -------------------------------------------------

        try:
            short = self.pk.find(class_="product attribute overview").find(class_='value').text.strip()
            short_desc = short
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f'An error occurred: {e}')
            short_desc = ''

        try:
            desc = [desc_text.text.strip() for desc_text in self.pk.find(class_="product attribute description").find_all(class_='value')]
            # if not desc:
            #     desc = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "//*[@itemprop='description']")]
            description_1 = {"desc": desc, 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e}")
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [des_1.text.strip() for des_1 in self.pk.find(class_="reviews-actions")]
            print('description_2.....', description_2)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e}")
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get('href'), "alt": img.get('alt')} for img in self.pk.find('div', class_="product-gallery").find_all('a')]
            print('images.....', images)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e}")
            images = ''
            print('images.....', images)

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            attr_name = [th.text.strip() for th in self.pk.find_all('th', class_="col label")]
            attr_value = [td.text.strip() for td in self.pk.find_all('td', class_="col data")]
            specs_li = [{name: value} for name, value in zip(attr_name, attr_value)]
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f'An error occurred: {e}')
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
            video = [video_link.get('src') for video_link in self.pk.find('div', class_="install-instructions").find_all('iframe')]
            print('video.....', video)
        except (NoSuchElementException, TypeError, IndexError, AttributeError, Exception) as e:
            print(f"An error video: {e}")
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [href_link.get('href') for href_link in self.pk.find_all(class_="row flex-row flex-wrap")[0].find_all('a') if "products" in href_link.get('href', '')]
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, IndexError, TypeError, AttributeError, Exception) as e:
            print(f"An error realated: {e}")
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------

        try:
            LEESON = {"Availability": self.pk.find('div', class_="stock available").find(class_='value').text.strip()}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e}")
            LEESON = ''


        miscellaneous = str(LEESON)
        print('miscellaneous.....', miscellaneous)

        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": "Cementex", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
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


    # def close_driver(self):
    #     self.driver.quit()



def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# scaper_name = WebScraper('https://www.mitchellinstrument.com/cementex-bew-36sr-insulated-box-end-wrench.html')
# scaper_name.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------

def ReadUrlFromList():
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Mitchellinstrument-Cementex.com/url/Product-url.csv"
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        try:
            executor.map(lambda url: WebScraper(url).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
