import concurrent.futures
import time
from urllib.parse import urljoin
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import re

save_files = open("P:/Web-scrapings/A-MONTH-2024/Aug/Onlinecomponents-Brand-Eaton.com/data/Onlinecomponents-Brand-Eaton.csv", "a+",encoding="utf-8")
base_url = 'https://www.onlinecomponents.com'
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
        # try:
        #     driver.get(self.url)
        #     time.sleep(3)
        #     page_sources = driver.page_source
        #     pk = BeautifulSoup(page_sources, 'lxml')
        # finally:
        #     driver.close()
        #     driver.quit()
        # return pk

        driver.get(self.url)
        time.sleep(7)
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
            Brand = self.pk.select_one("#divSupplier a").text.strip()
            print('Brand.....', Brand)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            Brand = ''
            print(f"An error occurred: {e} Brand -----: {Brand}")

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            names = [l3.text.strip() for l3 in self.pk.select("#BreadcrumbScrollToView nav ul li [itemprop='name']")]
            l3_Name = "## ".join(names)
            print('l3_Name.....', l3_Name)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} l3_Name -----: {l3_Name}")

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(2, 5)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)
        # -------------------------------------------------- Title -----------------------------------------------------
        try:
            product_title = self.pk.select_one(".wordbreak h1").text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")
        # -------------------------------------------------- Price -----------------------------------------------------

        try:
            list_of_price = self.pk.select_one(".product-info-price .price").text.strip()
            price = {'list_price': list_of_price + " /EA", 'qty': '1', 'moq': '1'}
            print("Price.....", price)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print(f"An error occurred: {e} price -----: {price}")

        # --------------------------------------------------- MPN ------------------------------------------------------
        mpn = ''
        try:
            part_no_div = self.pk.find('div', string="Part No:").find_next('div', class_='col-7 col-md-8')
            if part_no_div:
                mpn = part_no_div.get_text(strip=True)
            print('SKU.....', mpn)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} mpn -----: {mpn}")

        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            short = self.pk.select_one("h2.product-detail-code").text.strip()
            short_desc = short
        except (AttributeError, TypeError, IndexError, NoSuchElementException, Exception) as e:
            short_desc = ''
            print(f"An error occurred: {e} short_desc -----: {short_desc}")

        try:
            desc = self.pk.find_all("div", class_="col-12 font-size-14 font-weight-400 text-oxford-mid-blue pb-15 d-none d-md-block")[0].text.strip().replace('\n', '')
            # desc = [des_div.text.strip() for des_div in self.pk.select("#divFullDescription")]
            description_1 = {"desc": [desc], 'instructions': [], 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            description_1 = {"desc": []}
            print(f"An error occurred: {e} description_1 -----: {description_1}")

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [find_div.get_text(strip=True, separator=">>") for find_div in self.pk.select(".design-type.ng-star-inserted div")]
            if not description_2:
                raise ValueError("No description_2 found")
            print('description_2.....', description_2)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            description_2 = []
            print(f"An error occurred: {e} description_2 -----: {description_2}")

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": urljoin(base_url, img.get('src')), "alt": img.get('alt')} for img in self.pk.select("div.img-product.product-img img")]
            print('images.....', images)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            images = ''
            print(f"An error occurred: {e} images -----: {images}")

        # --------------------------------------------- specifications_1 -----------------------------------------------
        price_details = []
        try:
            price_name = []
            price_value = []
            for price_table in self.pk.select('#divPriceListLeft .row.mx-0.priceLine'):
                price_row = price_table.get_text(strip=True, separator='>>').split('>>')
                price_name.append("Qty " + price_row[0])
                price_value.append("Unit Price " + price_row[1])
            price_details = [{names: values} for names, values in zip(price_name, price_value)]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} price_details -----: {price_details}")


        try:
            attr_name2 = [th.text.strip() for th in self.pk.select(".lstSpecs li .col-5.col-md-4")]
            attr_value2 = [re.sub(r'\s+', ' ', td.text.strip().replace('\n  ', ' ')) for td in self.pk.select(".lstSpecs li .col-7.col-md-8")]
            specs_1 = [{name2: value2} for name2, value2 in zip(attr_name2, attr_value2)]
            # print(specs_1)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specs_1 = []
            print(f"An error occurred: {e} specifications_1 -----: {specs_1}")




        specifications_1 = str(specs_1) + ", " + str(price_details)  # + ", " + str(specs)
        print('specifications_1.....', specifications_1)

        # ----------------------------------------------- specifications_2 ---------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.pk.select("#collapse")]
            if not specifications_2:
                raise ValueError("No specifications found")
            print('specifications_2.....', specifications_2)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specifications_2 = []
            print(f"An error occurred: {e} specifications_2 -----: {specifications_2}")

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [urljoin(base_url, pdf.get('href')) for pdf in self.pk.select(".product-info-list a[href*='pdf']")]
            if not datasheet:
                raise ValueError("No datasheet found")
            print('datasheet.....', datasheet)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            datasheet = []
            print(f"An error occurred: {e} datasheet -----: {datasheet}")

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('src') for video_link in self.pk.select('.productView-images img') if 'jpg' not in video_link.get('src', '')]
            if not video:
                raise ValueError("No video links found")
            print('video.....', video)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            video = []
            print(f"An error occurred: {e} video -----: {video}")

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [urljoin(base_url, href_link.get('href')) for href_link in self.pk.select(".productSubTable .sku") if href_link.get('href') is not None]
            if not related_url:
                raise ValueError("No realated links found")
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            related_url = [{'accessories': []}]
            print(f"An error occurred: {e} realated -----: {related_url}")

        try:
            spare_url = [urljoin(base_url, href_link.get('href')) for href_link in self.pk.select("#relatedItems ul li a") if href_link.get('href') is not None]
            if not spare_url:
                raise ValueError("No realated links found")
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            spare_url = [{'spare_url': []}]
            print(f"An error occurred: {e} spare_url -----: {spare_url}")

        accessories = {'accessories': related_url, 'spare': spare_url}
        print('accessories.....', accessories)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------

        try:
            min_order_div = self.pk.select('.col-7.text-slate-grey.font-weight-400.font-size-15')[2].text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            min_order_div = ''
            print(f"An error occurred: {e} min_order_div -----: {min_order_div}")

        try:
            Out_of_stock = self.pk.select_one('#trInstock span.text-salmon-red').get_text(strip=True, separator=' ')
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Out_of_stock = ''
            print(f"An error occurred: {e} Out_of_stock -----: {Out_of_stock}")

        try:
            Factory_Lead_Time = self.pk.select('.col-7.text-slate-grey.font-weight-400.font-size-15')[-1].get_text(strip=True, separator=' ')
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Factory_Lead_Time = ''
            print(f"An error occurred: {e} Factory_Lead_Time -----: {Factory_Lead_Time}")

        try:
            Manufacturer_stock = self.pk.select_one("#trfactorystock").get_text(strip=True, separator=' ').replace('Manufacturer Stock: ', '')
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Manufacturer_stock = ''
            print(f"An error occurred: {e} Manufacturer_stock -----: {Manufacturer_stock}")


        miscellaneous = {"Manufacturer_stock": Manufacturer_stock, "min_order_div": min_order_div, "Factory_Lead_Time": Factory_Lead_Time, "Out_of_stock": Out_of_stock}
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
        # self.pk.driver.close()
        # self.pk.driver.quit()


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# scraper_names = WebScraper('https://www.onlinecomponents.com/en/productdetail/tripp-lite-by-eaton/p00512n-44063717.html')
# scraper_names.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------
def main():
    file_path = "P:/Web-scrapings/A-MONTH-2024/Aug/Onlinecomponents-Brand-Eaton.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 4000
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
