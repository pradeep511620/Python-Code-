import concurrent.futures
# from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from selenium.common import NoSuchElementException, ElementClickInterceptedException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium import webdriver



urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Apr/Turnersupply.com/data/Turnersupply.csv", "a+",
                  encoding="utf-8")
# base_url = 'https://hosewarehouse.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}




class WebScraper:
    def __init__(self, url):
        self.url = url
        # self.soup = self.GetSoupUrl()
        self.driver = self.get_driver()

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(11)
        return driver

    def GetSoupUrl(self):
        ress = requests.get(self.url, verify=False, headers=headers)
        soup = BeautifulSoup(ress.content, "lxml")
        return soup

    def Product_Details(self):
        print("Product-url---: ", self.url)
        # try:
        # try:
        #     self.driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']").click()
        #     time.sleep(4)
        # except (NoSuchElementException, ElementClickInterceptedException):
        #     print('click not found')

        l3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''


        try:
            names = []
            for l3 in self.driver.find_elements(By.XPATH, "//nav[@aria-label='breadcrumbs']//span"):
                l3_details = l3.text.strip().replace("/", "")
                if l3_details:
                    names.append(l3_details)
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
            product_title = self.driver.find_element(By.XPATH, "//div[@class='GridItemStyle--1uambol hjTqLE']//h1").text.strip()
            print('product_title.....', product_title)
        except NoSuchElementException:
            product_title = ''
            print('product_title.....', product_title)

        # -------------------------------------------------- Price-- ---------------------------------------------------
        try:
            product_price_1 = self.driver.find_element(By.XPATH, "(//*[@data-test-selector='priceIncludeVat'])[2]").text.strip()
            price = {'list_price': product_price_1, 'qty': '1', 'moq': '1'}
            print('price.....', price)
        except (NoSuchElementException, AttributeError, ElementClickInterceptedException):
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print('product_price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.driver.find_element(By.XPATH, "(//*[@class='TypographyStyle--11lquxl emIsOC'])[2]").text.strip().replace("MFG #: ", "")
            print('SKU.....', mpn)
        except NoSuchElementException:
            mpn = 'N/A'
            print('SKU:', mpn)

        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            des = self.driver.find_element(By.XPATH, "//div[@id='Description']").text.strip()
            description_1 = {"desc": [des]}
            print('description_1.....', description_1)
        except (AttributeError, IndexError, NoSuchElementException):
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = []
            for des_1 in self.driver.find_elements(By.XPATH, "//div[@id='collapse-show-details']//ul//li"):
                text_1 = des_1.text.strip()
                if text_1:
                    description_2.append(text_1)
            print('description_2.....', description_2)
        except (NoSuchElementException, TypeError, IndexError):
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = []
            for images_html in self.driver.find_elements(By.XPATH, "//div[@class='sc-bczRLJ iNuFMN']//img"):
                if images_html:
                    image_src = images_html.get_attribute('src')
                    alt_tag = images_html.get_attribute('alt')
                    image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                    images.append(image_tag_and_alt_tag)
            print('images.....', images)
        except NoSuchElementException:
            images = ''
            print('images.....', images)

        # --------------------------------------------------------------------------------------------------------------
        # try:
        #     self.driver.find_element(By.XPATH, "(//button[@id='show-more-attributes']//span)[1]").click()
        #     time.sleep(1)
        # except (NoSuchElementException, ElementClickInterceptedException):
        #     print('click not found')
        try:
            attr_name = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//*[@class='TypographyStyle--11lquxl kYoBPc']")]
            attr_value = [td.text.strip() for td in self.driver.find_elements(By.XPATH, "//*[@class='TypographyStyle--11lquxl kpLLHA']")]
            specs_one = [{name: value} for name, value in zip(attr_name, attr_value)]
        except (NoSuchElementException, ElementClickInterceptedException):
            specs_one = ''

        try:
            count_one = 0
            attr_name_one_1 = []
            attr_value_one_1 = []
            for table_one in self.driver.find_elements(By.XPATH, "//*[@class='sc-bczRLJ imvgKf']"):
                tab_one = table_one.text.strip()
                count_one += 1
                if count_one % 2 != 0:
                    attr_name_one_1.append(tab_one)
                else:
                    attr_value_one_1.append(tab_one)
            specs_two = [{name_one: value_one} for name_one, value_one in zip(attr_name_one_1, attr_value_one_1)]
        except(NoSuchElementException, ElementClickInterceptedException, TypeError, IndexError):
            specs_two = ''


        specifications_1 = str(specs_one) + " " + str(specs_two)
        print('specifications.....', specifications_1)



        # --------------------------------------------------------------------------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//div[@id='collapse")]
            print('specifications_2.....', specifications_2)
        except(AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            specifications_2 = []
            print('specifications_2.....', specifications_2)

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [pdf.get_attribute('href') for pdf in self.driver.find_elements(By.XPATH, "//*[@class='GridItemStyle--1uambol bqJqKi']//a")]
            print('datasheet.....', datasheet)
        except(NoSuchElementException, TypeError, IndexError):
            datasheet = []
            print('datasheet.....', datasheet)
        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = []
            for video_details in self.driver.find_elements(By.XPATH, "//div[@class='GridColumn-sc-1yc67ea-0 bTOOwX']//iframe"):
                video.append(video_details.get_attribute('src'))
            print('video.....', video)
        except(NoSuchElementException, TypeError, IndexError):
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
        except (NoSuchElementException, IndexError, TypeError):
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------

        for more_detail in self.driver.find_elements(By.XPATH, "//*[@class='++++++++++++-']"):
            data = more_detail.text.strip()
            print(data)



        try:
            application_details = self.driver.find_element(By.XPATH, "(//*[@class='sc-bczRLJ bAJJQB'])[2]").text.strip().replace("\n", ">>").split('>>')
            key1 = application_details[0]
            value1 = application_details[1]
            application = {key1: value1}
        except (NoSuchElementException, IndexError, TypeError):
            application = ''

        try:
            Includes_details = self.driver.find_element(By.XPATH, "(//*[@class='sc-bczRLJ bAJJQB'])[3]").text.strip().replace("\n", ">>").split('>>')
            key1 = Includes_details[0]
            value1 = Includes_details[1]
            Includes = {key1: value1}
        except (NoSuchElementException, IndexError, TypeError):
            Includes = ''

        try:
            Item_Includes_details = self.driver.find_element(By.XPATH, "(//*[@class='sc-bczRLJ bAJJQB'])[4]").text.strip().replace("\n", ">>").split('>>')
            key1 = Item_Includes_details[0]
            value1 = Item_Includes_details[1]
            Item_Includes = {key1: value1}
        except (NoSuchElementException, IndexError, TypeError):
            Item_Includes = ''

        try:
            Standards_details = self.driver.find_element(By.XPATH, "(//*[@class='sc-bczRLJ bAJJQB'])[5]").text.strip().replace("\n", ">>").split('>>')
            key1 = Standards_details[0]
            value1 = Standards_details[1]
            Standards = {key1: value1}
        except (NoSuchElementException, IndexError, TypeError):
            Standards = ''

        try:
            Warranty_details = self.driver.find_element(By.XPATH, "(//*[@class='sc-bczRLJ bAJJQB'])[6]").text.strip().replace("\n", ">>").split('>>')
            key1 = Warranty_details[0]
            value1 = Warranty_details[1]
            Warranty = {key1: value1}
            # print(Warranty)
        except (NoSuchElementException, IndexError, TypeError):
            Warranty = ''


        miscellaneous = str(application) + "," + str(Includes) + "," + str(Item_Includes) + "," + str(Standards) + "," + str(Warranty)
        print('miscellaneous.....', miscellaneous)

        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": "ENERPAC", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": '',
            "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": [], "datasheets": datasheet,
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


scaper_name = WebScraper('https://www.turnersupply.com/Product/283520378')
scaper_name.Product_Details()

# ----------------------------------------------------------------------------------------------------------------------


# def ReadUrlFromList():
#     file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Apr/Turnersupply.com/url/Product-url.csv"
#     url_links = pd.read_csv(file_path)['URL']
#     # print(url_links)
#     i = 0
#     for url_count, url in enumerate(url_links[i:], start=i):
#         urls.append(url)
#         # print('product_url.....', url_count, url)
#
#         # scaper_name = WebScraper(url)
#         # scaper_name.Product_Details()
#     return urls


# ReadUrlFromList()



# def main():
#     url_1 = ReadUrlFromList()
#
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         try:
#             executor.map(lambda url: WebScraper(url).Product_Details(), url_1)
#             print('---------------------------------------------------------------------------------------------------')
#         except Exception as e:
#             print(f"Error: {e}")
#             print("Breaking the process due to error encountered.")
#             raise RuntimeError("Error encountered. Program terminated.")
#
#
# if __name__ == "__main__":
#     main()
