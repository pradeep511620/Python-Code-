# import smtplib
import concurrent.futures
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

save_files = open("P:/Web-scrapings/A-MONTH-2024/July/Humboldtmfg-products.com/data/Humboldtmfg-products.csv", "a+",encoding="utf-8")
base_url = 'https://www.humboldtmfg.com'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.pk = self.send_requests_from_soup()
        # self.driver = self.send_selenium_from_driver()
        # self.pk = self.send_requests_and_driver_from_page_sources()

    def send_requests_and_driver_from_page_sources(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        try:
            driver.get(self.url)
            time.sleep(3)
            page_sources = driver.page_source
            pk = BeautifulSoup(page_sources, 'lxml')
        finally:
            driver.close()
            driver.quit()
        return pk

    def send_selenium_from_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        return driver

    def send_requests_from_soup(self):
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
        weight = ''
        try:
            Brand = 'walter'
            print('Brand.....', Brand)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            Brand = ''
            print(f"An error occurred: {e} Brand -----: {Brand}")

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            names = [l3.text.strip() for l3 in self.pk.select("#breadcrumb a")]
            l3_Name = "## ".join(names)
            print('l3_Name.....', l3_Name)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} l3_Name -----: {l3_Name}")

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)
        # -------------------------------------------------- Title -----------------------------------------------------
        try:
            product_title = self.pk.select_one("#prod-description-container h1").text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")
        # -------------------------------------------------- Price -----------------------------------------------------
        # try:
        #     qty = self.pk.select_one(".mqty").text.strip()
        # except (AttributeError, TypeError, IndexError, NoSuchElementException, Exception) as e:
        #     qty = ''
        #     print(f"An error occurred: {e} qty -----: {qty}")

        try:
            list_of_price = self.pk.select_one(".product-info-price .price").text.strip()
            price = {'list_price': list_of_price + " /EA", 'qty': '1', 'moq': '1'}
            print("Price.....", price)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print(f"An error occurred: {e} price -----: {price}")

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.pk.select_one("product-details-price .product-detail-data-table span.value").text.strip()
            print('SKU.....', mpn)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            mpn = ''
            print(f"An error occurred: {e} mpn -----: {mpn}")

        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            short = self.pk.select_one("h2.product-detail-code").text.strip()
            short_desc = short
        except (AttributeError, TypeError, IndexError, NoSuchElementException, Exception) as e:
            short_desc = ''
            print(f"An error occurred: {e} short_desc -----: {short_desc}")

        try:
            desc = [des_div.text.strip() for des_div in self.pk.select(".product-description p")]
            description_1 = {"desc": desc, 'instructions': [], 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            description_1 = {"desc": []}
            print(f"An error occurred: {e} description_1 -----: {description_1}")

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [find_div.get_text(strip=True, separator=">>") for find_div in
                             self.pk.select(".design-type.ng-star-inserted div")]
            if not description_2:
                raise ValueError("No description_2 found")
            print('description_2.....', description_2)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            description_2 = []
            print(f"An error occurred: {e} description_2 -----: {description_2}")

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": urljoin(base_url, img.get('src')), "alt": img.get('alt')} for img in self.pk.select("#prod-image-container picture img")]
            print('images.....', images)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            images = ''
            print(f"An error occurred: {e} images -----: {images}")

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            attr_name = []
            attr_value = []
            row_count = 0
            for table in self.pk.select(".specs-chart tr td"):
                row_count += 1
                tab = table.text.strip()
                if row_count % 2 != 0:
                    attr_name.append(tab)
                else:
                    attr_value.append(tab)
            specs = [{name: value} for name, value in zip(attr_name, attr_value)]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specs = []
            print(f"An error occurred: {e} specs -----: {specs}")



        try:
            attr_name2 = [th.text.strip().replace(":", "") for th in self.pk.select(".twoColumn table th")]
            attr_value2 = [td.text.strip() for td in self.pk.select(".twoColumn table td")]
            specs_1 = [{name2: value2} for name2, value2 in zip(attr_name2, attr_value2)]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specs_1 = []
            print(f"An error occurred: {e} specifications_1 -----: {specs_1}")

        try:
            header = [th.text.strip().replace("\n\t\t\t\t\t\t\t", "") for th in self.pk.select(".spec-chart-container thead tr th")]
            data_list = []
            for row in self.pk.select(".spec-chart-container tbody tr"):
                row_table = row.get_text(strip=True, separator=">>").split(">>")
                row_dict = {header[i]: row_table[i] if i < len(row_table) else '' for i in range(len(header))}
                data_list.append(row_dict)
            multiple_order = []
            for item in data_list:
                for key, value in item.items():
                    multiple_order.append({key: value})
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            multiple_order = []
            print(f"An error occurred: {e} multiple_order -----: {multiple_order}")


        specifications_1 = str(specs_1) + ", " + str(multiple_order) + ", " + str(specs)
        print('specifications_1.....', specifications_1)

        # ----------------------------------------------- specifications_2 ---------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.pk.select("#collapse")]
            if not specifications_2:
                raise ValueError("No specifications found")
            print('specifications_2.....', specifications_2)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specifications_2 = []
            print(f"An error occurred: {e} specifications_2 -----: {specifications_2}")

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [urljoin(base_url, pdf.get('href')) for pdf in
                         self.pk.select(".product-info-list a[href*='pdf']")]
            if not datasheet:
                raise ValueError("No datasheet found")
            print('datasheet.....', datasheet)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            datasheet = []
            print(f"An error occurred: {e} datasheet -----: {datasheet}")

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('src') for video_link in self.pk.select('.productView-images img') if
                     'jpg' not in video_link.get('src', '')]
            if not video:
                raise ValueError("No video links found")
            print('video.....', video)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            video = []
            print(f"An error occurred: {e} video -----: {video}")

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [urljoin(base_url, href_link.get('href')) for href_link in
                           self.pk.select(".productSubTable .sku") if href_link.get('href') is not None]
            if not related_url:
                raise ValueError("No realated links found")
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            related_url = [{'accessories': []}]
            print(f"An error occurred: {e} realated -----: {related_url}")

        try:
            spare_url = [urljoin(base_url, href_link.get('href')) for href_link in
                         self.pk.select("#relatedItems ul li a") if href_link.get('href') is not None]
            if not spare_url:
                raise ValueError("No realated links found")
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            spare_url = [{'spare_url': []}]
            print(f"An error occurred: {e} spare_url -----: {spare_url}")

        accessories = {'accessories': related_url, 'spare': spare_url}
        print('accessories.....', accessories)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------

        try:
            standard = [st.text.strip() for st in self.pk.select(".product-info-list p")[2:]]
            Standards = {"Standards": standard}
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Standards = ''
            print(f"An error occurred: {e} standard -----: {Standards}")

        miscellaneous = str(Standards)
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
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": weight,
            "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": specifications_2, "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": description_2,
            "accessories": accessories, "video_links": video, "miscellaneous": miscellaneous,
            "scraped_by": "Pradeep_RaptorTech",
        }]

        Data_Save(raw_data, list_column)
        print('Complete all Your Program')
        print()
        # self.pk.driver.close()
        # self.pk.driver.quit()


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# scraper_names = WebScraper('https://www.humboldtmfg.com/flexural-testing-machine-230v-50-60hz-3ph.html')
# scraper_names.Product_Details()
#
# scraper_names = WebScraper('https://www.humboldtmfg.com/universal-splitter.html')
# scraper_names.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------
def main():
    file_path = "P:/Web-scrapings/A-MONTH-2024/July/Humboldtmfg-products.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 0
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
