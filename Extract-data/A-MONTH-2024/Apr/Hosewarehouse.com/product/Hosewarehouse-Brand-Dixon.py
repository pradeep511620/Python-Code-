import concurrent.futures
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
# import time
# from selenium.common import NoSuchElementException, ElementClickInterceptedException
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# from selenium import webdriver


urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Apr/Hosewarehouse.com/data/Hosewarehouse1.csv", "a+",
                  encoding="utf-8")
base_url = 'https://hosewarehouse.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.soup = self.GetSoupUrl()
        # self.driver = self.get_driver()

    # def get_driver(self):
    #     chrome_options = Options()
    #     chrome_options.add_argument('--headless')
    #     chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
    #     driver = webdriver.Chrome(options=chrome_options)
    #     # driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.get(self.url)
    #     time.sleep(3)
    # return driver

    def GetSoupUrl(self):
        ress = requests.get(self.url)
        soup = BeautifulSoup(ress.content, "lxml")
        return soup

    def Product_Details(self):
        print("Product-url---: ", self.url)
        # try:

        l3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''


        try:
            names = []
            for l3 in self.soup.find('div', {'class': 'breadcrumbs'}).find_all('a'):
                l3_details = l3.text.strip()
                names.append(l3_details)
            l3_Name = "## ".join(names)
            print('l3_Name.....', l3_Name)
        except (AttributeError, TypeError, IndexError):
            print('l3_Name.....', l3_Name)

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)

        # --------------------------------------------------------------------------------------------------------------
        try:
            product_title = self.soup.find("h1", {"class": "product-title"}).text.strip()
            print('product_title.....', product_title)
        except AttributeError:
            product_title = ''
            print('product_title.....', product_title)

        # -------------------------------------------------- Price-- ---------------------------------------------------
        try:
            product_price_1 = self.soup.find("div", {"class": "price__current"}).text.strip().replace("Current price\n\n        ", "")
            price = {'list_price': product_price_1, 'qty': '1', 'moq': '1'}
            print('price.....', price)
        except AttributeError:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print('product_price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.soup.find(class_="table table-hover").get_text(strip=True).split('SKU: ')[1].split(' Dixon')[0]
            print('SKU.....', mpn)
        except AttributeError:
            mpn = 'N/A'
            print('SKU:', mpn)

        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            des = self.soup.find_all('div', {"class": "paragraph--type--product-detail"})[0].text.strip()
            description_1 = {"desc": [des]}
            print('description_1.....', description_1)
        except (AttributeError, IndexError):
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = []
            for des_1 in self.soup.find(class_="custom-liquid").find_all('p'):
                text_1 = des_1.text.strip()
                if text_1:
                    description_2.append(text_1)
            print('description_2.....', description_2)
        except (AttributeError, TypeError, IndexError):
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = []
            for images_html in self.soup.find('div', {"class": "product-gallery--image-background"}).find_all('img'):
                if images_html:
                    image_src = images_html.get('src')
                    alt_tag = images_html.get('alt')
                    image_tag_and_alt_tag = {"src": urljoin(base_url, image_src), "alt": alt_tag}
                    images.append(image_tag_and_alt_tag)
            print('images.....', images)
        except AttributeError:
            images = ''
            print('images.....', images)

        # --------------------------------------------------------------------------------------------------------------
        try:
            count_one = 0
            attr_name_one_1 = []
            attr_value_one_1 = []
            for table_one in self.soup.find(class_="table table-hover").find_all('td'):
                tab_one = table_one.text.strip().replace(':', '')
                count_one += 1
                if count_one % 2 != 0:
                    attr_name_one_1.append(tab_one)
                else:
                    attr_value_one_1.append(tab_one)
            specs = [{name_one: value_one} for name_one, value_one in zip(attr_name_one_1, attr_value_one_1)]
        except(AttributeError, TypeError, IndexError):
            specs = ''
        try:
            specs_one = ''
            tables_th = [th.text.strip() for th in self.soup.find(class_="0table").find('tbody').find_all('th')]
            tables_tr = self.soup.find(class_="0table").find('tbody').find_all('tr')
            for tr in tables_tr:
                tds = tr.find_all('td')
                row_data = [td.text.strip() for td in tds]
                if mpn in row_data:
                    if row_data:
                        specs_one = [{name1: value1} for name1, value1 in zip(tables_th, row_data)]
        except(AttributeError, TypeError, IndexError):
            specs_one = ''

        specifications_1 = str(specs) + " " + str(specs_one)
        print('specifications.....', specifications_1)



        # --------------------------------------------------------------------------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.soup.find(By.XPATH, "(//table[@class='highlighted'])[1]//td")]
            print('specifications_2.....', specifications_2)
        except(AttributeError, TypeError, IndexError):
            specifications_2 = []
            print('specifications_2.....', specifications_2)

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [urljoin(base_url, pdf.get('href')) for block in
                         self.soup.find_all(class_="block-field-blocknodeproduct-resourcefield-attachments") for pdf in
                         block.find_all('a')]
            print('datasheet.....', datasheet)
        except(AttributeError, TypeError, IndexError):
            datasheet = []
            print('datasheet.....', datasheet)
        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = []
            for video_details in self.soup.find(class_="embed-responsive embed-responsive-16by9").find_all('iframe'):
                video.append(video_details.get('src'))
            print('video.....', video)
        except(AttributeError, TypeError, IndexError):
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = []
            for href in self.soup.find(class_="product-section--content").find_all('a'):
                print(href)
                resources = href.get('href')
                related_url.append(urljoin(base_url, resources))
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (AttributeError, IndexError, TypeError):
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            variant_mpn_details = [mpns.text.strip()for mpns in self.soup.find(class_="0table").find('tbody').find_all('a')]
            variant_mpn = {"variant": True, 'variant_mpn': variant_mpn_details}
        except (AttributeError, IndexError, TypeError):
            variant_mpn = ''

        try:
            attr_name_miss = [th.text.strip().replace(':', '') for th in self.soup.find(class_="pd-text-wrapper rte table table-hover").find('tbody').find_all('th')]
            attr_value_miss = [td.text.strip() for td in self.soup.find(class_="pd-text-wrapper rte table table-hover").find('tbody').find_all('td')]
            miss = [{name: value} for name, value in zip(attr_name_miss, attr_value_miss)]
            # print('miscellaneous.....', miss)
        except(AttributeError, TypeError, IndexError):
            miss = []


        miscellaneous = str(variant_mpn) + " " + str(miss)
        print('miscellaneous.....', miscellaneous)

        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": "DIXON", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": '',
            "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": [], "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": description_2,
            "accessories": realated, "video_links": [], "miscellaneous": miscellaneous,
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


# scaper_name = WebScraper('https://hosewarehouse.com/products/2-dfc-2-dixon-instrumentation-fitting-stainless-steel-female-connector-1-8-tube-od-1-8-27-female-npt?variant=11769676365860')
# scaper_name.Product_Details()

# ----------------------------------------------------------------------------------------------------------------------


def ReadUrlFromList():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Apr/Hosewarehouse.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 17000
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
            print('---------------------------------------------------------------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
