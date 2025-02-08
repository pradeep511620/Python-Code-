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
from selenium import webdriver



urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Apr/Purvisindustries.com/data/Purvisindustries.csv", "a+",
                  encoding="utf-8")
# base_url = 'https://hosewarehouse.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}




class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = self.GetSoupUrl()
        self.driver = self.get_driver()

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
        datasheet = ''


        try:
            names = [l3.text.strip() for l3 in self.soup.find('ul', {"class": "breadcrumb"}).find_all('li')]
            l3_Name = "## ".join(names)
            print('l3_Name.....', l3_Name)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            print('l3_Name.....', l3_Name)

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(2, 5)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)

        # --------------------------------------------------------------------------------------------------------------
        try:
            product_title = self.soup.find("h3", class_="cimm_prodDetailTitle").text.strip()
            print('product_title.....', product_title)
        except NoSuchElementException:
            product_title = ''
            print('product_title.....', product_title)

        # -------------------------------------------------- Price-- ---------------------------------------------------
        try:
            product_price_1 = self.driver.find_element(By.XPATH, "//ul[@class='priceWrap formatPrice']").text.strip()
            price = {'list_price': product_price_1, 'qty': '1', 'moq': '1'}
            print('price.....', price)
        except (NoSuchElementException, AttributeError, ElementClickInterceptedException):
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print('product_price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.soup.find("li", id="sitePartNo").find("span").text.strip()
            print('SKU.....', mpn)
        except NoSuchElementException:
            mpn = 'N/A'
            print('SKU:', mpn)


        # ---------------------------------------------- Description_1 -------------------------------------------------

        try:
            short = self.soup.find('p', class_="cimm_itemShortDesc").text.strip()
            short_desc = short
        except(AttributeError, IndexError, NoSuchElementException):
            short_desc = ''

        try:
            des = [desc_text.text.strip() for desc_text in self.soup.find('div', id="descriptionSection").find_all('p')]
            description_1 = {"desc": des, 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (AttributeError, IndexError, NoSuchElementException):
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [des_1.text.strip() for des_1 in self.soup.find('ul', class_="featureAttributeWrap").find_all('li')]
            print('description_2.....', description_2)
        except (NoSuchElementException, TypeError, IndexError, AttributeError):
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get('src'), "alt": img.get('alt')} for img in self.soup.find('ul', id="gallery").find_all('img')]
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, NoSuchElementException):
            images = ''

        # try:
        #     images = []
        #     for images_html in self.soup.find('ul', id="gallery").find_all('img'):
        #         if images_html:
        #             image_src = images_html.get('src')
        #             alt_tag = images_html.get('alt')
        #             image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
        #             images.append(image_tag_and_alt_tag)
        #     print('images.....', images)
        # except NoSuchElementException:
        #     images = ''
        #     print('images.....', images)


        try:
            attr_name = [th.text.strip() for th in self.soup.find('div', id="specificationSection").find('table').find_all('b')]
            # attr_name_1 = [item_1 for item_1 in attr_name if item_1]
            attr_value = [td.text.strip().replace(":", "") for td in self.soup.find('div', id="specificationSection").find('table').find_all('span')]
            attr_value_2 = [item_2 for item_2 in attr_value if item_2]
            specs_one = [{name: value} for name, value in zip(attr_name, attr_value_2)]
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError):
            specs_one = ''



        specifications_1 = str(specs_one)
        print('specifications.....', specifications_1)


        # --------------------------------------------------------------------------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//div[@id='collapse")]
            print('specifications_2.....', specifications_2)
        except(AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            specifications_2 = []
            print('specifications_2.....', specifications_2)

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        # try:
        #     datasheet = [pdf.get('onclick') for pdf in self.soup.find('div', id="documentsSection").find_all('a')]
        #     print('datasheet.....', datasheet)
        # except(NoSuchElementException, TypeError, IndexError):
        #     datasheet = []
        #     print('datasheet.....', datasheet)
        import re

        try:
            datasheet = []
            documents_section = self.soup.find('div', id="documentsSection")
            if documents_section:
                pdf_links = documents_section.find_all('a', onclick=re.compile(r'\.pdf'))
                datasheet = [re.search(r"'([^']*)'", link.get('onclick')).group(1) for link in pdf_links]
            print('datasheet.....', datasheet)
        except (AttributeError, TypeError) as e:
            print('Error:', e)

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = []
            for video_details in self.driver.find_elements(By.XPATH, "//div[@class='descriptionVideo mb-4 row']//iframe"):
                video.append(video_details.get_attribute('src'))
            print('video.....', video)
        except(NoSuchElementException, TypeError, IndexError, AttributeError):
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = []
            for href in self.driver.find_elements(By.XPATH, "//*[@class='styles__ProductList-xd5d4-2 gUZfvD']//li//a"):
                resources = href.get_attribute('href')
                related_url.append(resources)
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, IndexError, TypeError, AttributeError):
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            part_details = self.soup.find('li', id="sitePartNo").find('span').text.strip()
            part_number = {'Item#': part_details}
        except (NoSuchElementException, AttributeError, ElementClickInterceptedException):
            part_number = ''

        try:
            upc_details = self.soup.find('li', id="upcNo").find('span').text.strip()
            upc_number = {'upc#': upc_details}
        except (NoSuchElementException, AttributeError, ElementClickInterceptedException):
            upc_number = ''


        miscellaneous = str(part_number) + ", " + str(upc_number)
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

        # Data_Save(raw_data, list_column)
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


# scaper_name = WebScraper('https://www.purvisindustries.com/grove-gear-gr-hmq813-30-h1-56-10')
# scaper_name.Product_Details()

# ----------------------------------------------------------------------------------------------------------------------


def ReadUrlFromList():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Apr/Purvisindustries.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:], start=i):
        urls.append(url)
        # print('product_url.....', url_count, url)

        # scaper_name = WebScraper(url)
        # scaper_name.Product_Details()
    return urls


# ReadUrlFromList()



def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        try:
            executor.map(lambda url: WebScraper(url).Product_Details(), url_1)
            print('---------------------------------------------------------------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
