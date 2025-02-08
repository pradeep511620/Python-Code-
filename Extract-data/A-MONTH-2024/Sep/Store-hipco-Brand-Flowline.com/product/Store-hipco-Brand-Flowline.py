import concurrent.futures
import time
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

save_files = open("P:/Web-scrapings/A-MONTH-2024/Sep/Store-hipco-Brand-Flowline.com/data/Store-hipco-Brand-Flowline.csv", "a+",encoding="utf-8")
base_url = 'https://store.hipco.com/'
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
        time.sleep(1)
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
        weight = ''
        try:
            Brand = 'Flowline'
            print('Brand.....', Brand)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Brand = ''
            print(f"An error occurred: {e} Brand -----: {Brand}")

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            names = [l3.text.strip() for l3 in self.pk.select("div.crumbTrail a")]
            l3_Name = "## ".join(names)
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
            product_title = self.pk.select_one("h1.pageTitle").text.strip()
            print('product_title.....', product_title)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")        

        # --------------------------------------------------- MPN ------------------------------------------------------
        mpn = ''
        try:
            mpn = 'rp_' + self.pk.select_one("div.prodNum").text.strip().split('#')[1].strip()
            print('Mpn.....', mpn)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} mpn -----: {mpn}")
            
        # --------------------------------------------------- QTY ------------------------------------------------------
        pr_qty = ''
        try:
            pr_qty = self.pk.select_one("div.prodData .umDiv").text.strip().split(':')[1].strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} pr_qty -----: {pr_qty}")
            
        # -------------------------------------------------- Price -----------------------------------------------------
        product_price = ''
        try:
            product_price = self.pk.select_one("span[itemprop='price']").text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} product_price -----: {product_price}")

        price = {'list_price': '$-.--' + pr_qty, 'qty': '1', 'moq': '1'}
        print('price.....', price)



        # ---------------------------------------------- Description_1 -------------------------------------------------
        short_desc = ''
        try:
            short = self.pk.select_one("h1.prodDesc").text.strip()
            short_desc = short
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} short_desc -----: {short_desc}")

        description_1 = {"desc": []}
        try:
            desc = [des.text.strip().replace('\n', '>>')for des in self.pk.select("div#full")]
            description_1 = {"desc": desc, 'instructions': [], 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} description_1 -----: {description_1}")

        # ---------------------------------------------- Description_2 -------------------------------------------------
        description_2 = []
        try:
            description_2 = [find_div.get_text(strip=True, separator=">>") for find_div in self.pk.select("#spec ul li")]
            if not description_2:
                raise ValueError("No description_2 found")
            print('description_2.....', description_2)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} description_2 -----: {description_2}")

        # -------------------------------------------------- Images ----------------------------------------------------
        images = ''
        try:
            images = [{"src": urljoin(base_url, img.get('src')), "alt": img.get('alt')} for img in self.pk.select("div#product-row img")]
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} images -----: {images}")

        # --------------------------------------------- specifications_1 -----------------------------------------------
        specs = []
        try:
            name_1 = []
            value_1 = []
            attr_name = [th.text.strip() for th in self.pk.select("table.specTable tbody tr td")]
            row_count = 0
            for tab in attr_name:
                row_count += 1
                if row_count % 2 != 0:
                    name_1.append(tab)
                else:
                    value_1.append(tab)
            specs = [{name: value} for name, value in zip(name_1, value_1)]
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} specifications_1 -----: {specs}")

        specifications_1 = str(specs)
        print('specifications_1.....', specifications_1)

        # ----------------------------------------------- specifications_2 ---------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.pk.select("#kikk")]
            if not specifications_2:
                raise ValueError("No specifications found")
            print('specifications_2.....', specifications_2)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            specifications_2 = []
            print(f"An error occurred: {e} specifications_2 -----: {specifications_2}")

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [urljoin(base_url, pdf.get('href')) for pdf in self.pk.select("ul.more-info-wrap #link li a")]
            if not datasheet:
                raise ValueError("No datasheet found")
            print('datasheet.....', datasheet)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            datasheet = []
            print(f"An error occurred: {e} datasheet -----: {datasheet}")

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('src') for video_link in self.pk.select('.productView-images img') if 'jpg' not in video_link.get('src', '')]
            if not video:
                raise ValueError("No video links found")
            print('video.....', video)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            video = []
            print(f"An error occurred: {e} video -----: {video}")

        # ------------------------------------------------- Realated ---------------------------------------------------
        related_url = [{'accessories': []}]
        try:
            related_url = [urljoin(base_url, href_link.get('href')) for href_link in self.pk.select("div.prodListProd.cartable.list .imageCol a")]
            if not related_url:
                raise ValueError("No realated links found")
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} realated -----: {related_url}")

        spare_url = [{'spare_url': []}]
        try:
            spare_url = [urljoin(base_url, href_link.get('href')) for href_link in self.pk.select("#relatedItems ul li a") if href_link.get('href') is not None]
            if not spare_url:
                raise ValueError("No realated links found")
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} spare_url -----: {spare_url}")


        accessories = {'accessories': related_url, 'spare': spare_url}
        print('accessories.....', accessories)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        logo = ''
        try:
            logo = urljoin(base_url, self.pk.select_one("div.prodpagemfglogo span img").get('src'))
        except (AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} logo -----: {logo}")



        miscellaneous = {''}
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
            "accessories": accessories, "video_links": video, "miscellaneous": miscellaneous,
            "scraped_by": "Pradeep_RaptorTech",
        }]

        Data_Save(raw_data, list_column)
        print('Complete all Your Program')
        print()



def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# scraper_names = WebScraper('https://dealerselectric.com/TP-E1U.asp')
# scraper_names = WebScraper('https://store.hipco.com/product/AT12-1614')
# scraper_names.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------
def main():
    file_path = r"P:\Web-scrapings\A-MONTH-2024\Sep\Store-hipco-Brand-Flowline.com\url\Product-url - Copy.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 0
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")



if __name__ == "__main__":
    main()
