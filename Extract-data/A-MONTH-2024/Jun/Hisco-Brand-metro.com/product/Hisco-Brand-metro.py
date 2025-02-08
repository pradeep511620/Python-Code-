# import smtplib
import concurrent.futures
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

save_files = open("P:/Web-scrapings/A-MONTH-2024/Jun/Hisco-Brand-metro.com/data/metron.csv", "a+", encoding="utf-8")
base_url = ''
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

class WebScraper:
    def __init__(self, url):
        self.url = url
        # self.pk = self.send_requests_from_soup()
        # self.driver = self.send_selenium_from_driver()
        self.pk = self.send_requests_and_driver_from_page_sources()

    def send_requests_and_driver_from_page_sources(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        try:
            driver.get(self.url)
            time.sleep(25)
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
            Brand = 'Metron'
            print('Brand.....', Brand)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            Brand = ''
            print(f"An error occurred: {e} Brand -----: {Brand}")

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            names = [l3.text.strip() for l3 in self.pk.select("nav[data-test-selector='pageBreadcrumbs'] a")]
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
            product_title = self.pk.select_one('.GridItemStyle--1uambol.cAFhPW h1').text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")
        # -------------------------------------------------- Price -----------------------------------------------------
        try:
            qty = self.pk.select_one("[data-test-selector='productPrice_unitOfMeasureLabel']").text.strip()
        except (AttributeError, TypeError, IndexError, NoSuchElementException, Exception) as e:
            qty = ''
            print(f"An error occurred: {e} qty -----: {qty}")

        try:
            list_of_price = self.pk.select_one(".sc-bczRLJ.jNwdcG [data-test-selector='productPrice_unitNetPrice']").text.strip()
            price = {'list_price': list_of_price+" /EA", 'qty': qty, 'moq': '1'}
            print("Price.....", price)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print(f"An error occurred: {e} price -----: {price}")
        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.pk.select("[data-test-selector='productNumbersPlusIcons_container'] p")[-1].text.strip().replace("MFG #:", "")
            print('SKU.....', mpn)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            mpn = ''
            print(f"An error occurred: {e} mpn -----: {mpn}")
        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            short = self.pk.select_one("[data-test-selector='productDetails_htmlContent'] p").text.strip()
            short_desc = short
        except (AttributeError, TypeError, IndexError, NoSuchElementException, Exception) as e:
            short_desc = ''
            print(f"An error occurred: {e} short_desc -----: {short_desc}")

        try:

            desc = self.pk.select_one(".sc-bczRLJ.gmKXUi [data-test-selector='productDetails_htmlContent'] p").text.strip()
            # if not desc:
            #     desc = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "//*[@itemprop='description']")]
            description_1 = {"desc": [desc], 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            description_1 = {"desc": []}
            print(f"An error occurred: {e} description_1 -----: {description_1}")


        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [find_div.text.strip() for find_div in self.pk.select(".description li")]
            print('description_2.....', description_2)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            description_2 = []
            print(f"An error occurred: {e} description_2 -----: {description_2}")


        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get('src'), "alt": img.get('alt')} for img in self.pk.select(".GridItemStyle--1uambol.UfGAs img")]
            print('images.....', images)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            images = ''
            print(f"An error occurred: {e} images -----: {images}")

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            attr_name2 = []
            attr_value2 = []
            for da in self.pk.select("[data-test-selector='productDetails_htmlContent'] ul li"):
                tab = da.text.strip().split(":")
                attr_name2.append(tab[0])
                attr_value2.append(tab[1])
            specs_1 = [{name2: value2} for name2, value2 in zip(attr_name2, attr_value2)]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specs_1 = []
            print(f"An error occurred: {e} specifications_1 -----: {specs_1}")

        try:
            attr_name = [th.text.strip() for th in self.pk.select("[data-test-selector='productDetailsSpecs_Attributes'] .TypographyStyle--11lquxl.eHQwTu")]
            attr_value = [td.text.strip() for td in self.pk.select("[data-test-selector='productDetailsSpecs_Attributes'] .TypographyStyle--11lquxl.klBFg")]
            specs = [{name: value} for name, value in zip(attr_name, attr_value)]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specs = []
            print(f"An error occurred: {e} specifications_1 -----: {specs}")

        specifications_1 = str(specs_1) + ", " + str(specs)
        print('specifications_1.....', specifications_1)

        try:
            data_list = []
            header = [th.text.strip().lower() for th in self.pk.select(".DataTableStyle--1xfex8z thead th")]
            for row in self.pk.select(".DataTableStyle--1xfex8z tbody tr"):
                row_table = row.get_text(strip=True, separator=">>").split(">>")
                row_dict = {header[i]: row_table[i] if i < len(row_table) else '' for i in range(len(header))}
                data_list.append(row_dict)
            multiple_order = []
            for item in data_list:
                for key, value in item.items():
                    multiple_order.append({key: value})
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            multiple_order = ''
            print(f"An error occurred: {e} multiple_order -----: {multiple_order}")



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
            datasheet = [pdf.get('href') for pdf in self.pk.select(".verification a")]
            print('datasheet.....', datasheet)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            datasheet = []
            print(f"An error occurred: {e} datasheet -----: {datasheet}")

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('data-url') for video_link in self.pk.select('.click-vlink')]
            if not video:
                raise ValueError("No video links found")
            print('video.....', video)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            video = []
            print(f"An error occurred: {e} video -----: {video}")

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [href_link.get('href') for href_link in self.pk.select("#block-related li a")]
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            realated = [{'accessories': []}]
            print(f"An error occurred: {e} realated -----: {realated}")

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            part_number = self.pk.select_one("[data-test-selector='ProductDetailsPartNumber']").text.strip().replace("Hisco #:", "")
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            part_number = ''
            print(f"An error occurred: {e} part_number -----: {part_number}")

        try:
            manufacturer = self.pk.select_one("[data-test-selector='minOrderQtyDescription']").text.strip()
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            manufacturer = ''
            print(f"An error occurred: {e} manufacturer -----: {manufacturer}")


        miscellaneous = {"part_number": part_number, "Ships direct from manufacturer": manufacturer, "Item must be ordered in multiples of 1": multiple_order}
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
            "accessories": realated, "video_links": video, "miscellaneous": miscellaneous,
            "scraped_by": "Pradeep_RaptorTech",
        }]

        Data_Save(raw_data, list_column)
        print('Complete all Your Program')
        print()





def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')



# scraper_names = WebScraper('https://www.hisco.com/Brands/Metro/Catalog/All/5MESD-37280')
# scraper_names.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------

def ReadUrlFromList():
    file_path = "D:/Web-scraping/A-MONTH-2024/Jun/Hisco-Brand-metro.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:2], start=i):
        print('product_url.....', url_count)
        scraper_name = WebScraper(url)
        scraper_name.Product_Details()


# ReadUrlFromList()


def main():
    file_path = "P:/Web-scrapings/A-MONTH-2024/Jun/Hisco-Brand-metro.com/url/Product-url - Copy.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 0
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
