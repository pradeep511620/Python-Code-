# import concurrent.futures
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# import time
# from selenium.common import NoSuchElementException, ElementClickInterceptedException
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# from selenium import webdriver


urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Advance-Tabco.com/data/Advance-Tabco.csv", "a+", encoding="utf-8")
base_url = 'https://www.gatescarbondrive.com/'
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
        mpn = ''

        try:
            bread = self.soup.find_all('script', type="application/ld+json")
            for data in bread:
                l3 = json.loads(data.text)
                item_list = l3.get('itemListElement', [])
                names = [item.get('item', {}).get('name', '') for item in item_list]
                if names:
                    l3_Name = "## ".join(names)
                    print('l3_Name.....', l3_Name)
        except (AttributeError, TypeError, IndexError):
            print('l3_Name.....', l3_Name)

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]

        # --------------------------------------------------------------------------------------------------------------
        try:
            product_title = self.soup.find("h1", {"class": "page-title"}).text.strip()
            print('product_title.....', product_title)
        except AttributeError:
            product_title = ''
            print('product_title.....', product_title)

        # -------------------------------------------------- Price-- ---------------------------------------------------
        try:
            product_price_1 = self.soup.find("span", {"class": "price"}).text
            price = {'list_price': product_price_1}
            print('product_price.....', price)
        except AttributeError:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print('product_price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            part_number = self.soup.find(class_="product attribute sku").get_text(strip=True)
            print('SKU.....', part_number)
        except AttributeError:
            mpn = 'N/A'
            print('SKU:', mpn)

        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            des = self.soup.find('section', {"id": "overview"}).find_next('p').text.strip()
            description_1 = {"desc": [des]}
            print('description_1.....', description_1)
        except (AttributeError, IndexError):
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = []
            for des_1 in self.soup.find(id="tab-description").find('ol').find_all('li'):
                text_1 = des_1.text.strip()
                if text_1:
                    description_2.append(text_1)
            print('description_2.....', description_2)
        except (AttributeError, TypeError):
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = []
            for images_html in self.soup.find('div', {"id": "product-carousel"}).find_all('img'):
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
            i = 0
            attr_name_one = []
            attr_value_one = []
            for table in self.soup.find('div', id="product-details-info").find('table').find_all('td'):
                tab = table.text.strip().replace(":", "")
                i += 1
                if i % 2 != 0:
                    attr_name_one.append(tab)
                else:
                    attr_value_one.append(tab)
            specifications_1 = [{name: value} for name, value in zip(attr_name_one, attr_value_one)]
            print('specifications_1.....', specifications_1)
        except:
            specifications_1 = []
            print('specifications_1.....', specifications_1)

        # --------------------------------------------------------------------------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in
                                self.soup.find(By.XPATH, "(//table[@class='highlighted'])[1]//td")]
            print('specifications_2.....', specifications_2)
        except TypeError:
            specifications_2 = []
            print('specifications_2.....', specifications_2)

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [pdf.get_attribute('href') for pdf in self.soup.find_elements(By.XPATH,
                                                                                      "(//*[@class='technical-documents-component_documents__3toCx'])[2]//a")]
            print('datasheet.....', datasheet)
        except TypeError:
            datasheet = []
            print('datasheet.....', datasheet)
        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = []
            for video_details in self.soup.find(class_="embed-responsive embed-responsive-16by9").find_all('iframe'):
                video.append(video_details.get('src'))
            print('video.....', video)
        except (AttributeError, TypeError):
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = []
            for href in self.soup.find_all(class_="space-y-24")[1].find_all('a'):
                resources = href.get('href')
                if "resources" in resources:
                    related_url.append(resources)
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (AttributeError, IndexError):
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            shock_details = [shock.text.strip().replace('\n', '') for shock in self.soup.find_all('p', {'class': "disclaimer"})]
            shock_no = {"disclaimer": shock_details}
        except (TypeError, KeyError, AttributeError):
            shock_no = ''
            print('cad_details.....', shock_no)

        miscellaneous = str(shock_no)
        print('miscellaneous.....', miscellaneous)

        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": "GATES", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
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


# scaper_name = WebScraper('https://www.burkett.com/advance-tabco-hf-5e-240-78-5-well-electric-steam-table-5000-watts')
# scaper_name.Product_Details()

# ----------------------------------------------------------------------------------------------------------------------


"""
def ReadUrlFromList():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Gatescarbondrive.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:110], start=i):
        urls.append(url)
        # print('product_url.....', url_count, url)

        scaper_name = WebScraper(url)
        scaper_name.Product_Details()
    return urls

ReadUrlFromList()
"""

"""
def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        try:
            executor.map(lambda url: WebScraper(url). Product_Details(), url_1)
            print('---------------------------------------------------------------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
"""
