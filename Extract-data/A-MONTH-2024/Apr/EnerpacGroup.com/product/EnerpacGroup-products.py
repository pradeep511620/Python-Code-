import concurrent.futures
# from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
from selenium.common import NoSuchElementException, ElementClickInterceptedException, JavascriptException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
from selenium import webdriver



urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Apr/EnerpacGroup.com/data/EnerpacGroup1.csv", "a+",
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
        try:

            l3_Name = ''
            catlvl1 = ''
            catlvl2 = ''
            catlvl3 = ''


            try:
                names = []
                for l3 in self.driver.find_elements(By.XPATH, "//*[@class='ProductBreadcrumbs__BreadcrumbLink']"):
                    l3_details = l3.text.strip()
                    if l3_details:
                        names.append(l3_details)
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
                product_title = self.driver.find_element(By.XPATH, "(//*[@class='regionWrapper']//h1)[2]").text.strip()
                print('product_title.....', product_title)
            except NoSuchElementException:
                product_title = ''
                print('product_title.....', product_title)

            # -------------------------------------------------- Price-- ---------------------------------------------------
            try:
                product_price_1 = self.driver.find_element(By.XPATH, "((//section[@class='Region col-12'])[2]//span)[1]").text.strip()
                price = {'list_price': product_price_1, 'qty': '1', 'moq': '1'}
                print('price.....', price)
            except (NoSuchElementException, AttributeError, ElementClickInterceptedException):
                price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
                print('product_price.....', price)

            # --------------------------------------------------- MPN ------------------------------------------------------
            try:
                more_details = self.driver.find_element(By.XPATH, "//div[@class='py-1']").text.strip().replace('\n', '>').split('   |  ')
            except (NoSuchElementException, AttributeError, ElementClickInterceptedException):
                more_details = ''

            try:
                mpn = more_details[0].replace('Model: ', '')
                print('SKU.....', mpn)
            except NoSuchElementException:
                mpn = 'N/A'
                print('SKU:', mpn)


            # ---------------------------------------------- Description_1 -------------------------------------------------

            try:
                short = self.driver.find_element(By.ID, "shortdesc").text.strip()
                short_desc = short
            except(AttributeError, IndexError, NoSuchElementException):
                short_desc = ''

            try:
                des = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "//div[@class='long-description-features pt-2']//p")]
                description_1 = {"desc": des, 'short_desc': short_desc}
                # description_1.update(short_desc)
                print('description_1.....', description_1)
            except (AttributeError, IndexError, NoSuchElementException):
                description_1 = {"desc": []}
                print('description_1.....', description_1)

            # ---------------------------------------------- Description_2 -------------------------------------------------
            try:
                description_2 = [des_1.text.strip() for des_1 in self.driver.find_elements(By.XPATH, "//ul[@class='notBold']//li")]
                print('description_2.....', description_2)
            except (NoSuchElementException, TypeError, IndexError):
                description_2 = []
                print('description_2.....', description_2)

            # -------------------------------------------------- Images ----------------------------------------------------
            try:
                images = []
                for images_html in self.driver.find_elements(By.XPATH, "//div[@class='EnerpacProductImageViewer']//img"):
                    if images_html:
                        image_src = images_html.get_attribute('src')
                        alt_tag = images_html.get_attribute('alt')
                        image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                        images.append(image_tag_and_alt_tag)
                print('images.....', images)
            except NoSuchElementException:
                images = ''
                print('images.....', images)


            try:
                attr_name = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//*[@class='key col-6 col-sm-7']")]
                attr_name_1 = [item_1 for item_1 in attr_name if item_1]
                attr_value = [td.text.strip() for td in self.driver.find_elements(By.XPATH, "//*[@class='value col-6 col-sm-5']")]
                attr_value_2 = [item_2 for item_2 in attr_value if item_2]
                specs_one = [{name: value} for name, value in zip(attr_name_1, attr_value_2)]
            except (NoSuchElementException, ElementClickInterceptedException):
                specs_one = ''
            try:
                self.driver.execute_script("document.querySelector('input[value=\"Specs_Metric\"]').click();")
                th = [table_one.text.strip() for table_one in self.driver.find_elements(By.XPATH, "//*[@class='key col-6 col-sm-7']")]
                th = [item for item in th if item]
                td = [table_td.text.strip() for table_td in self.driver.find_elements(By.XPATH, "//*[@class='value col-6 col-sm-5']")]
                td = [item_td for item_td in td if item_td]
                specs_2 = [{name_2: value_2} for name_2,value_2 in zip(th, td)]
            except (NoSuchElementException, ElementClickInterceptedException):
                specs_2 = ''


            specifications_1 = str(specs_one) + " " + str(specs_2)
            print('specifications.....', specifications_1)

            try:
                self.driver.execute_script("document.querySelector(\"button[class='false dimCollapse w-100'] h2\").click();")
                time.sleep(2)
                print('click Dimensions')
            except (JavascriptException, NoSuchElementException):
                print("javascript error: Cannot read properties of null (reading 'click')")
            try:
                attr_name = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//*[@class='key col-6 col-sm-7']")]
                attr_name_1 = [item_1 for item_1 in attr_name if item_1]
                attr_value = [td.text.strip() for td in self.driver.find_elements(By.XPATH, "//*[@class='value col-6 col-sm-5']")]
                attr_value_2 = [item_2 for item_2 in attr_value if item_2]
                specs_one = [{name: value} for name, value in zip(attr_name_1, attr_value_2)]
            except (NoSuchElementException, ElementClickInterceptedException):
                specs_one = ''
            try:
                self.driver.execute_script("document.querySelector('input[value=\"Specs_Metric\"]').click();")
                th = [table_one.text.strip() for table_one in self.driver.find_elements(By.XPATH, "//*[@class='key col-6 col-sm-7']")]
                th = [item for item in th if item]
                td = [table_td.text.strip() for table_td in self.driver.find_elements(By.XPATH, "//*[@class='value col-6 col-sm-5']")]
                td = [item_td for item_td in td if item_td]
                specs_2 = [{name_2: value_2} for name_2, value_2 in zip(th, td)]
            except (NoSuchElementException, ElementClickInterceptedException):
                specs_2 = ''
            specifications_2 = str(specs_one) + " " + str(specs_2)
            print('specifications.....', specifications_2)

            # --------------------------------------------------------------------------------------------------------------
            # try:
            #     specifications_2 = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//div[@id='collapse")]
            #     print('specifications_2.....', specifications_2)
            # except(AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            #     specifications_2 = []
            #     print('specifications_2.....', specifications_2)

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
                for video_details in self.driver.find_elements(By.XPATH, "//div[@class='descriptionVideo mb-4 row']//iframe"):
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

            # for more_detail in self.driver.find_elements(By.XPATH, "//*[@class='++++++++++++-']"):
            #     data = more_detail.text.strip()
            #     print(data)

            try:
                more_details = self.driver.find_element(By.XPATH, "//div[@class='py-1']").text.strip().replace('\n','>').split('   |  ')
            except (NoSuchElementException, AttributeError, ElementClickInterceptedException):
                more_details = ''


            miscellaneous = str(more_details)
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
                "specification_1": specifications_1, "specification_2": specifications_2, "datasheets": datasheet,
                "product_description_1": description_1, "product_description_2": description_2,
                "accessories": realated, "video_links": video, "miscellaneous": miscellaneous,
                "scraped_by": "Pradeep_RaptorTech",
            }]

            Data_Save(raw_data, list_column)
            print('Complete all Your Program')
            print()
        except Exception as e:
            print(f"Error{e}")
            with open('remain_url.txt', "a+", encoding="utf-8") as file:
                file.write(f"{self.url}\n")


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# scaper_name = WebScraper('https://www.enerpac.com/en-us/reducers/hexagon-reducer-imperial/W15407R210')
# scaper_name.Product_Details()

# ----------------------------------------------------------------------------------------------------------------------

#
def ReadUrlFromList():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Apr/EnerpacGroup.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 300
    for url_count, url in enumerate(url_links[i:], start=i):
        urls.append(url)
        # print('product_url.....', url_count, url)

        # scaper_name = WebScraper(url)
        # scaper_name.Product_Details()
    return urls


# ReadUrlFromList()



def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        try:
            executor.map(lambda url: WebScraper(url).Product_Details(), url_1)
            print('---------------------------------------------------------------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
