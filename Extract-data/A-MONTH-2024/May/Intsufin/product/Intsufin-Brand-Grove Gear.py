import concurrent.futures
# import re

from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from selenium.common import NoSuchElementException, ElementClickInterceptedException, JavascriptException
# from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# import random
from selenium import webdriver

urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/May/Intsufin/data/Intsufin.csv", "a+",
                  encoding="utf-8")
base_url = 'https://lntsufin.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = self.GetSoupUrl()
        # self.driver = self.get_driver()

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(3)
        return driver

    def GetSoupUrl(self):
        ress = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(ress.content, "lxml")
        return soup

    def Product_Details(self):
        print("Product-url---: ", self.url)
        # try:
        l3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        mpn = ''

        try:
            names = [l3.text.strip() for l3 in self.soup.find('ol', {"class": "breadcrumb pb-0"}).find_all('li')]
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
            product_title = self.soup.find("h1", class_="pdp-product-label").text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            product_title = ''
            print('product_title.....', product_title)

        # -------------------------------------------------- Price-- ---------------------------------------------------
        try:
            product_price_1 = self.soup.find('div', class_="pdp-price").text.strip()
            price = {'list_price': product_price_1, 'qty': '1', 'moq': '1'}
            print('price.....', price)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print('product_price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = ''
            for mpn_details in self.soup.find_all(class_="row pt-1"):
                text = mpn_details.text.strip()
                if "Model No." in text:
                    mpn = text.replace('\n', '').replace("Model No.", '')
                    break
                elif "UNSPSC No." in text:
                    mpn = text.replace('\n', '').replace("UNSPSC No.", '')
                    break
            print('MPN.....', mpn)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError) as e:
            mpn = ''
            print(f'Error while extracting MPN: {e}')
            print('MPN.....', mpn)

        # ---------------------------------------------- Description_1 -------------------------------------------------

        try:
            short = self.soup.find('div', class_="product-details-sales-description-value").text.strip()
            short_desc = short
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            short_desc = ''

        try:
            desc = [desc_text.text.strip() for desc_text in self.soup.find(class_="mb-3 pt-1").find_all('p')]
            description_1 = {"desc": desc, 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [des_1.text.strip() for des_1 in self.soup.find_all(class_="mb-3 pt-1")[1].find_all('p')]
            print('description_2.....', description_2)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": urljoin(base_url, img.get('src')), "alt": img.get('alt')} for img in
                      self.soup.find('div', id="stickyProductImage").find_all('img')]
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            images = ''

        # --------------------------------------------- specifications_1 -----------------------------------------------
        # try:
        #     attr_name = [table.get_text(strip=True) for table in self.soup.find_all(class_="pdp-spec-heading")]
        #     attr_value = [table.get_text(strip=True) for table in self.soup.find_all(class_="col font-14")]
        #     specs_li = [{name_li: values_li} for name_li, values_li in zip(attr_name, attr_value)]
        # except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
        #     specs_li = ''

        try:
            specs_li_1 = [{name: value} for some in self.soup.find_all(class_="row pt-1") for name, value in
                          [some.get_text(strip=True, separator='>>').split(">>")]]
            # print('attr_data.....', specs_li_1)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            specs_li_1 = ''

        specifications_1 = str(specs_li_1)
        print('specifications_1.....', specifications_1)

        # attr_name = []
        # attr_value = []
        # for some in self.soup.find_all(class_="row pt-1"):
        #     attr_name.append(some.get_text(strip=True, separator='>>').split(">>")[0])
        #     attr_value.append(some.get_text(strip=True, separator='>>').split(">>")[1])
        # some_data = [{name: value} for name, value in zip(attr_name, attr_value)]
        # print('some_data.....', some_data)

        # ----------------------------------------------- specifications_2 ---------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//div[@id='collapse")]
            print('specifications_2.....', specifications_2)
        except(AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            specifications_2 = []
            print('specifications_2.....', specifications_2)

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [pdf.get('onclick') for pdf in self.soup.find('div', id="documentsSection").find_all('a')]
            print('datasheet.....', datasheet)
        except(AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            datasheet = []
            print('datasheet.....', datasheet)

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('src') for video_link in
                     self.soup.find(class_="embed-responsive embed-responsive-16by9 pdp-rfq-video").find_all('iframe')]
            print('video.....', video)
        except(NoSuchElementException, TypeError, IndexError, AttributeError):
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [
                urljoin(base_url, href_link.get("onclick")).replace("similarProdTileClick('", "").rstrip("')").split(",'")[0]
                for href_link in self.soup.find(class_="similar_prod_tiles").find_all('div', class_="h-100") if
                href_link.get("onclick")]
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, IndexError, TypeError, AttributeError):
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            color = self.soup.find(class_="pdp-select-btn pdp-select-active").get_text(strip=True)
            size = self.soup.find_all(class_="pdp-select-btn pdp-select-active")[-1].get_text(strip=True)
            shoes = {color: size}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            shoes = ''

        try:
            Country = self.soup.find_all('p', class_="font-14")[-2].get_text(strip=True)
            Country_of = {'Country of Origin': Country}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            Country_of = ''

        try:
            warranty = self.soup.find('p', class_="font-14 mb-0 mb-lg-2").get_text(strip=True)
            warranty_of = {'warranty': warranty}
            print(warranty_of)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            warranty_of = 'N/A'
            print('warranty_of.....', warranty_of)

        miscellaneous = str(Country_of) + ", " + str(shoes) + ", " + str(warranty_of)
        print('miscellaneous.....', miscellaneous)

        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": "GROVE GEAR", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
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


# scaper_name = WebScraper('https://lntsufin.com/product/impact-by-honeywell-buff-suede-leather-steel-toe-safety-shoes-brown/16896-972')
# scaper_name = WebScraper('https://lntsufin.com/product/grove-gear-worm-1750-rpm-gear-reducer/16647-404')
# scaper_name.Product_Details()

# ----------------------------------------------------------------------------------------------------------------------
#
#
def ReadUrlFromList():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/May/Intsufin/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 500
    for url_count, url in enumerate(url_links[i:], start=i):
        urls.append(url)
        # print('product_url.....', url_count, url)

        # scaper_name = WebScraper(url)
        # scaper_name.Product_Details()
    return urls


# ReadUrlFromList()



def main():
    url_1 = ReadUrlFromList()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        try:
            executor.map(lambda url: WebScraper(url).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
