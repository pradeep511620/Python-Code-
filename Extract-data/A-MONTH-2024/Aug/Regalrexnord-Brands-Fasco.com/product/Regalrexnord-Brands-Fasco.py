import concurrent.futures
import time
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

save_files = open("P:/Web-scrapings/A-MONTH-2024/Aug/Regalrexnord-Brands-Fasco.com/data/Regalrexnord-Brands-Fasco.csv", "a+", encoding="utf-8")
base_url = 'https://www.regalrexnord.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


class WebScraper:
    def __init__(self, url):
        self.url = url
        # self.pk = self.send_requests_from_soup()
        self.pk = self.send_requests_and_driver_from_page_sources()

    def send_requests_and_driver_from_page_sources(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(14)
        page_sources = driver.page_source
        pk = BeautifulSoup(page_sources, 'lxml')
        return pk

    def send_requests_from_soup(self):
        sess = requests.Session()
        ress = sess.get(self.url, headers=headers)
        soup = BeautifulSoup(ress.content, "lxml")
        return soup

    def Product_Details(self):
        print("Product-url---: ", self.url)
        l3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        mpns = ''

        try:
            Brand = 'Fasco'
            print('Brand.....', Brand)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Brand = ''
            print(f"An error occurred: {e} Brand -----: {Brand}")

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            l3_name_list = [l3.text.strip() for l3 in self.pk.select("ol.breadcrumb li a")]
            # l3_list = [item for item in l3_name_list if item != '/']
            l3_Name = "## ".join(l3_name_list)
            print('l3_Name.....', l3_Name)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} l3_Name -----: {l3_Name}")

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(2, 5)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)


        # -------------------------------------------------- Title -----------------------------------------------------
        try:
            product_title = self.pk.select_one("div.page-title h1").text.strip()
            print('product_title.....', product_title)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")
        # -------------------------------------------------- Price -----------------------------------------------------

        price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
        try:
            some_data_div = self.pk.select(".product-cart .param-row")
            for div_element in some_data_div:
                if 'MAP Price:' in div_element.text.strip():
                    prices = div_element.text.strip().replace('\n', '').split("$")[1]
                    price = {'list_price': "$" + prices, 'qty': '1', 'moq': '1'}
                    break
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e}")

        print('price.....', price)

        # --------------------------------------------------- MPN ------------------------------------------------------
        catalog_number = ''
        model_number = ''
        some_data = self.pk.select(".page-subtitle .param-row")
        for some_number in some_data:
            if 'Part #' in some_number.text.strip():
                part_number = some_number.text.strip().replace('Part #:', '')
                mpns = part_number

            elif 'Catalog #' in some_number.text.strip():
                catalog_number = some_number.text.strip().replace('Catalog #:', '')

            elif 'Model #' in some_number.text.strip():
                model_number = some_number.text.strip().replace('Model #:', '')
            else:
                print('Not found any number')

        try:
            mpn = "'" + mpns
            print('MPN.....', mpn)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            mpn = None
            print(f"An error occurred: {e} MPN -----: {mpn}")


        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:

            short = self.pk.select_one("div#details-group h2").text.strip()
            short_desc = short
        except (AttributeError, TypeError, IndexError, Exception) as e:
            short_desc = ''
            print(f"An error occurred: {e} short_desc -----: {short_desc}")

        try:
            # desc = [des.text.strip() for des in self.pk.select("[data-testid='introduction'] div.template-text p")]
            data = self.pk.select_one("div#details-group p").get_text(strip=True, separator=">>")
            desc = data.split("Overall Dimensions:")[0]
            description_1 = {"desc": [desc], 'instructions': [], 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            description_1 = {"desc": []}
            print(f"An error occurred: {e} description_1 -----: {description_1}")

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [feature.text.strip() for feature in self.pk.select("div.product-info ul li")]
            if not description_2:
                raise ValueError("No description_2 found")
            print('description_2.....', description_2)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            description_2 = []
            print(f"An error occurred: {e} description_2 -----: {description_2}")

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get('src'), "alt": img.get('alt')} for img in self.pk.select("div[data-cxa-component-class='ProductImages'] img")]  # if "svg" not in img.get('src', '')
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            images = ''
            print(f"An error occurred: {e} images -----: {images}")

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            row_count = 0
            attr_name = []
            attr_value = []
            for table_row in self.pk.select("table.specifications-table tbody tr td"):
                row_count += 1
                tab = table_row.text.strip().replace(":", "")
                if row_count % 2 != 0:
                    attr_name.append(tab)
                else:
                    attr_value.append(tab)
            specs_li = [{name_li: values_li} for name_li, values_li in zip(attr_name, attr_value)]
        except (AttributeError, TypeError, IndexError, Exception) as e:
            specs_li = []
            print(f"An error occurred: {e} specifications_1 -----: {specs_li}")

        specifications_1 = str(specs_li)
        print('specifications_1.....', specifications_1)

        # ----------------------------------------------- specifications_2 ---------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.pk.select("#collapse")]
            if not specifications_2:
                raise ValueError("No specifications found")
            print('specifications_2.....', specifications_2)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            specifications_2 = []
            print(f"An error occurred: {e} specifications_2 -----: {specifications_2}")

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [urljoin(base_url, pdf.get('href')) for pdf in self.pk.select("div#resources-group div.downloads a")]
            if not datasheet:
                raise ValueError("No datasheet found")
            print('datasheet.....', datasheet)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            datasheet = []
            print(f"An error occurred: {e} datasheet -----: {datasheet}")


        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('src') for video_link in self.pk.select('div.video-media video source')]
            if not video:
                raise ValueError("No video links found")
            print('video.....', video)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            video = []
            print(f"An error occurred: {e} video -----: {video}")

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [urljoin(base_url, href_link.get('href')) for href_link in self.pk.select("div#ProductSubstitutePanel div.product-card__title a")]
            if not related_url:
                raise ValueError("No realated links found")
            accessories = {'accessories': related_url}
            print('accessories.....', accessories)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            accessories = [{'accessories': []}]
            print(f"An error occurred: {e} realated -----: {accessories}")




        # ------------------------------------------------ Miscellaneous -----------------------------------------------

        Weight_lbs = ''
        try:
            some_data_div = self.pk.select(".product-cart .param-row")
            for div_element in some_data_div:
                if 'Weight:' in div_element.text.strip():
                    Weight = div_element.text.strip().replace('Weight:', '')
                    Weight_lbs = {"Shipping weight": Weight}
            print('Weight.....', Weight_lbs)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Weight_lbs = ''
            print(f"An error occurred: {e} Weight_lbs -----: {Weight_lbs}")

        uom_number = ''
        try:
            some_data_div = self.pk.select(".product-cart .param-row")
            for div_element in some_data_div:
                if 'UOM:' in div_element.text.strip():
                    uom_number = div_element.text.strip().replace('UOM:', '')
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} uom_number -----: {uom_number}")

        brand_logo = ''
        try:
            brand_logo = self.pk.select_one(".product-cart__logo img").get('src')
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} brand_logo -----: {brand_logo}")

        flags = ''
        try:
            flags = self.pk.select_one(".product-flag span").text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} flags -----: {flags}")

        Discontinued = ''
        try:
            Discontinued = self.pk.select_one("div.alert-freeshipping div.alert-text").text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} Discontinued -----: {Discontinued}")

        miscellaneous = {"catalog_number": catalog_number, "model_number": model_number, "flags": flags, "uom_number": uom_number, "Discontinued": Discontinued, "brand_logo": brand_logo}
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
            "title": product_title, "price_value": price, "unit": '', "shipping_weight": '',
            "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": specifications_2, "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": description_2,
            "accessories": accessories, "video_links": video, "miscellaneous": miscellaneous,
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


# scraper_names = WebScraper('https://www.regalrexnord.com/products/blowers/centrifugal-blowers/rectangular-outlet-permanent-split-capacitor-centrifugal-blower-115-230-volts-flange-no-a1200')
# scraper_names.Product_Details()



# ----------------------------------------------------------------------------------------------------------------------
def main():
    file_path = "P:/Web-scrapings/A-MONTH-2024/Aug/Regalrexnord-Brands-Fasco.com/url/Product-url - Copy.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 0

    for index_url, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)
        print(f"Processed URL: {index_url} URL count: {url}")

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print(f"{'--'*30} Thread Running {'--'*30}")
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
