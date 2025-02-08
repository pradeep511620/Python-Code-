import concurrent.futures
import time
from urllib.parse import urljoin
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import threading


lock = threading.Lock()
save_files = open("P:/Web-scrapings/A-MONTH-2024/Sep/Supplyhouse-Brand-Rheem.com/data/Supplyhouse-Brand-Rheem.csv", "a+", encoding="utf-8")
base_url = 'https://www.supplyhouse.com/'
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
        time.sleep(20)
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

        try:
            Brand = self.pk.select_one('div.Box-sc-1z9git-0.Flex-sc-1qhr4qe-0.bIWqhl.dNxDHg a').text.strip()
            print('Brand.....', Brand)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Brand = ''
            print(f"An error occurred: {e} Brand -----: {Brand}")

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            l3_name_list = [l3.text.strip() for l3 in self.pk.select("div.BreadcrumbLinks__BreadcrumbLinkContainer-sc-1251clj-0 a")]
            # l3_list = [item for item in l3_name_list if item != '/']
            l3_Name = "## ".join(l3_name_list)
            print('l3_Name.....', l3_Name)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} l3_Name -----: {l3_Name}")

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)


        # -------------------------------------------------- Title -----------------------------------------------------
        try:
            product_title = self.pk.select_one("div.Box-sc-1z9git-0.cOgTzu h1").text.strip()
            print('product_title.....', product_title)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")
        # -------------------------------------------------- Price -----------------------------------------------------
        try:
            qty = self.pk.select_one(".Box-sc-1z9git-0.ogFZS").text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            qty = ''
            print(f"An error occurred: {e} qty -----: {qty}")

        price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
        try:
            list_of_price = self.pk.select_one("div.Box-sc-1z9git-0.ProductQuantityAdjustorsPriceContainer-sc-148i33m-0.gUKiTB.blxbRl span").text.strip()
            price = {'list_price': list_of_price + qty, 'qty': '1', 'moq': '1'}
            print("Price.....", price)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} price -----: {price}")

        if price:
            USD = "USD"
        else:
            USD = ""

        # --------------------------------------------------- MPN ------------------------------------------------------
        mpn = ''
        try:
            mpn = "rp_" + self.pk.select_one("div.iXetAF.ProductPageHeaderDetailsValue-sc-1sia5h6-0").text.strip()
            print('SKU.....', mpn)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} mpn -----: {mpn}")

        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            short_description = []
            some_data = self.pk.select("div.ProductPageDescription__ProductPageDescriptionText-sc-1i7espa-2 b")
            for product_div in some_data:
                if 'Product Application' == product_div.text.strip():
                    for appication_div in product_div.findAllNext('li'):
                        short_description.append(appication_div.text.strip())
            short = ''.join(short_description)
            short_desc = short
        except (AttributeError, TypeError, IndexError, Exception) as e:
            short_desc = ''
            print(f"An error occurred: {e} short_desc -----: {short_desc}")

        try:
            desc = self.pk.select_one(".ProductPageDescription__ProductPageDescriptionText-sc-1i7espa-2").get_text(strip=True, separator=">>>>").split('.>>>>Product Application>>>>')
            description_1 = {"desc": desc, 'instructions': [], 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            description_1 = {"desc": []}
            print(f"An error occurred: {e} description_1 -----: {description_1}")

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = []
            some_data = self.pk.select("div.ProductPageDescription__ProductPageDescriptionText-sc-1i7espa-2 b")
            for feature_div in some_data:
                if 'Product Features' == feature_div.text.strip():
                    for application in feature_div.findAllNext('li'):
                        description_2.append(application.text.strip())
            if not description_2:
                raise ValueError("No description_2 found")
            print('description_2.....', description_2)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            description_2 = []
            print(f"An error occurred: {e} description_2 -----: {description_2}")

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get('src'), "alt": img.get('alt')} for img in self.pk.select(".isMediumStyle img") if "svg" not in img.get('src', '')]
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            images = ''
            print(f"An error occurred: {e} images -----: {images}")

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            attr_name = [th.text.strip() for th in
                         self.pk.select(".ProductPageSpecifications__Table-sc-dy0arh-0 tbody tr th")]
            attr_value = [td.text.strip() for td in
                          self.pk.select(".ProductPageSpecifications__Table-sc-dy0arh-0 tbody tr td")]
            specs = [{name: value} for name, value in zip(attr_name, attr_value)]
        except (AttributeError, TypeError, IndexError, Exception) as e:
            specs = ''
            print(f"An error occurred: {e}")

        try:
            attr_name2 = []
            attr_value2 = []
            for more_detail in self.pk.select(".ProductPageDescription__ProductPageDescriptionText-sc-1i7espa-2"):
                feature_data = more_detail.find_all('b')
                for li_tag_specs in feature_data:
                    if li_tag_specs.text == 'Specifications:':
                        table_data = li_tag_specs.findNext('ul').find_all('li')
                        for table_div in table_data:
                            table_details = table_div.text.strip().split(":")
                            if len(table_details) == 2:
                                attr_name2.append(table_details[0])
                                attr_value2.append(table_details[1])
            specs_2 = [{name_li: values_li} for name_li, values_li in zip(attr_name2, attr_value2)]
        except (AttributeError, TypeError, IndexError, Exception) as e:
            specs_2 = ''
            print(f"An error occurred: {e}")

        specifications_1 = str(specs) + ", " + str(specs_2)
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
            datasheet = [urljoin(base_url, pdf.get('href')) for pdf in self.pk.select("div.ProductPageManuals__ProductPageManualsStack-sc-1b5hgj5-2.jznyez a")]
            if not datasheet:
                raise ValueError("No datasheet found")
            print('datasheet.....', datasheet)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            datasheet = []
            print(f"An error occurred: {e} datasheet -----: {datasheet}")


        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('src') for video_link in self.pk.select('.productView-images img') if
                     'jpg' not in video_link.get('src', '')]
            if not video:
                raise ValueError("No video links found")
            print('video.....', video)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            video = []
            print(f"An error occurred: {e} video -----: {video}")

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [href_link.get('href') for href_link in self.pk.select(".ProductTileName__ProductTileNameLink-sc-1fe0vqu-0")]
            if not related_url:
                raise ValueError("No realated links found")
            accessories = {'accessories': related_url}
            print('accessories.....', accessories)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            accessories = [{'accessories': []}]
            print(f"An error occurred: {e} realated -----: {accessories}")




        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            Brands = self.pk.select_one('.fDOPef.ProductPageHeaderDetailsValue-sc-1sia5h6-0').text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Brands = ''
            print(f"Brands.....An error occurred: {e}\t{Brands}")

        try:
            stock = self.pk.select_one('div.gUKiTB.ProductInventoryStatusAndPromiseMessageText-sc-p14sra-0').text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            stock = ''
            print(f"stock.....An error occurred: {e}\t{stock}")

        try:
            replace_details = self.pk.select_one('.ProductPageObsoleteProducts__ProductPageObsoleteProductsProductIds-sc-k9q5jb-1').text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            replace_details = ''
            print(f"replace_details.....An error occurred: {e}\t{replace_details}")

        try:
            Free_Shipping = self.pk.select_one('.Box-sc-1z9git-0.cbDscn').text.strip().replace("Free Shipping ", "")
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Free_Shipping = ''
            print(f"Free_Shipping.....An error occurred: {e}\t{Free_Shipping}")

        try:
            Easy_Returns = self.pk.select_one('.Box-sc-1z9git-0.fVanSC').text.strip().replace("Easy Returns No ", "")
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Easy_Returns = ''
            print(f"Easy_Returns.....An error occurred: {e}\t{Easy_Returns}")
            
        try:
            product = [high_light.text.strip() for high_light in self.pk.select(".ProductPageProductHighlight__ProductPageProductHighlightContainer-sc-xxp3px-0")]
            product_high_light = ' >> '.join(product)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            product_high_light = ''
            print(f"Easy_Returns.....An error occurred: {e}\t{product_high_light}")

        miscellaneous = {"Brand": Brands, "This item replaces": replace_details, "stock": stock,
                         "Free_Shipping": Free_Shipping, "Easy_Returns": Easy_Returns, "product_high_light": product_high_light}
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
            "title": product_title, "price_value": price, "unit": USD, "shipping_weight": '',
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
    with lock:
        df = pd.DataFrame(row, columns=cols)
        print(df)
        df.to_csv(save_files, header=False, index=False, lineterminator='\n')
        print('save data into csv files')


# scraper_names = WebScraper('https://www.supplyhouse.com/Rheem-001051F-Stud-Bolt-Kit-134-383-33')
# scraper_names.Product_Details()



# ----------------------------------------------------------------------------------------------------------------------
def main():
    file_path = r"P:\Web-scrapings\A-MONTH-2024\Sep\Supplyhouse-Brand-Rheem.com\url\Product-url - Copy.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 0
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print(f"{'--'*30} Thread Running {'--'*30}")
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
