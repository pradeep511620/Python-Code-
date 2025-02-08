import concurrent.futures
# import re

# from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from selenium.common import NoSuchElementException, ElementClickInterceptedException, JavascriptException
# from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# import random
import undetected_chromedriver as uc
# from selenium import webdriver

urls = []
save_files = open("D:/Web-Scrapping/A-MONTH-2024/May/Lovejoy/data/Lovejoy.csv", "a+", encoding="utf-8")
base_url = ''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept":
        "text/html,application/xhtml+xml, application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}


class WebScraper:
    def __init__(self, url):
        self.url = url
        # self.soup = self.GetSoupUrl()
        self.driver = self.get_driver()

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        # driver = uc.Chrome(options=chrome_options)
        driver = uc.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(3)
        return driver

    def GetSoupUrl(self):
        sess = requests.Session()
        ress = sess.get(self.url, headers=headers)
        soup = BeautifulSoup(ress.content, "lxml")
        # print(ress.status_code)
        # print(soup)
        return soup

    def Product_Details(self):
        print("Product-url---: ", self.url)
        # try:
        l3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''

        try:
            names = [l3.text.strip() for l3 in self.driver.find_elements(By.XPATH, "//nav[@class='container']//li")]
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
        # print(self.soup.prettify())
        # --------------------------------------------------------------------------------------------------------------
        try:
            product_title = self.driver.find_element(By.XPATH, "(//*[@class='mt-8 xl:mt-0'])[1]//h1").text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            product_title = ''
            print('product_title.....', product_title)

        # -------------------------------------------------- Price-- ---------------------------------------------------
        try:
            product_price_1 = self.driver.find_element(By.XPATH, "//*[@id='totalPriceId']").text.strip()
            price = {'list_price': product_price_1, 'qty': '1', 'moq': '1'}
            print('price.....', price)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print('product_price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.driver.find_element(By.XPATH, "(//*[@class='flex justify-between text-sm xl:text-base']//p)[2]").text.strip()
            print('SKU.....', mpn)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            mpn = 'N/A'
            print('SKU:', mpn)

        # ---------------------------------------------- Description_1 -------------------------------------------------

        try:
            short = self.soup.find('div', class_="product-details-sales-description-value").text.strip()
            short_desc = short
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            short_desc = ''

        try:
            desc = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "(//*[@class='mt-8 xl:mt-0'])[1]//p[2]")]
            description_1 = {"desc": desc, 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [des_1.text.strip() for des_1 in
                             self.soup.find(class_="moreinfo-desc").find('ul').find_all('li')]
            print('description_2.....', description_2)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get_attribute('src'), "alt": img.get_attribute('alt')} for img in
                      self.driver.find_elements(By.XPATH, "//*[@class='bg-white xl:flex']//img")]
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            images = ''

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:

            attr_name = [table.text.strip() for table in self.driver.find_elements(By.XPATH,
                                                                                   "//*[@class='border-r px-6 py-5 text-monochromes leading-4 text-sm md:text-base']")]
            attr_value = [table.text.strip() for table in self.driver.find_elements(By.XPATH,
                                                                                    "//*[@class='px-6 py-5 text-monochromes leading-4 text-sm md:text-base']")]
            specs_li = [{name_li: values_li} for name_li, values_li in zip(attr_name, attr_value)]
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            specs_li = ''

        try:
            attr_name_1 = [table1.text.strip() for table1 in self.driver.find_elements(By.XPATH, "//*[@class='py-2 text-monochromes leading-4 text-sm md:text-base']")]
            attr_value_1 = [table1.text.strip() for table1 in self.driver.find_elements(By.XPATH, "//*[@class='py-2 text-monochromes leading-4 text-right text-sm md:text-base']")]
            specs_li_1 = [{name_li_1: values_li_1} for name_li_1, values_li_1 in zip(attr_name_1, attr_value_1)]
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            specs_li_1 = ''

        specifications_1 = str(specs_li) + "," + str(specs_li_1)
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
            datasheet = [pdf.get('onclick') for pdf in self.soup.find('div', id="documentsSection").find_all('a')]
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
        try:
            related_url = []
            for href in self.driver.find_elements(By.XPATH, "(//*[@id='alternate-collapsed-mode'])[1]//a"):
                resources = href.get_attribute('href')
                related_url.append(resources)
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, IndexError, TypeError, AttributeError):
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            part_details = self.driver.find_element(By.XPATH,
                                                    "(//*[@class='flex justify-between text-sm xl:text-base']//p)[1]").text.strip()
            part_number = {'Catalog Number': part_details}
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
            part_number = ''

        # try:
        #     upc_details = self.soup.find('li', id="upcNo").find('span').text.strip()
        #     upc_number = {'upc#': upc_details}
        # except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError):
        #     upc_number = ''

        miscellaneous = str(part_number)
        print('miscellaneous.....', miscellaneous)

        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": "Lovejoy", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
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


    def close_driver(self):
        self.driver.quit()


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# scaper_name = WebScraper('https://www.mscdirect.com/product/details/35407246')
# scaper_name.Product_Details()



# ----------------------------------------------------------------------------------------------------------------------



def ReadUrlFromList():
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Lovejoy/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:3], start=i):
        urls.append(url)
        # print('product_url.....', url_count, url)

        scaper_name = WebScraper(url)
        scaper_name.Product_Details()
        scaper_name.close_driver()
    return urls


ReadUrlFromList()



# def main():
#     url_1 = ReadUrlFromList()
#
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         try:
#             executor.map(lambda url: WebScraper(url).Product_Details(), url_1)
#             print('------------------------------------ Thread Running -----------------------------------------------')
#         except Exception as e:
#             print(f"Error: {e}")
#             print("Breaking the process due to error encountered.")
#             raise RuntimeError("Error encountered. Program terminated.")
#
#
# if __name__ == "__main__":
#     main()
