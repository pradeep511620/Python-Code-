import concurrent.futures
import time
from urllib.parse import urljoin
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

save_files = open("P:/Web-scrapings/A-MONTH-2024/July/Webstaurantstore-Brand-T&S.com/data/Webstaurantstore-Brand-T&S.csv", "a+", encoding="utf-8")
base_url = 'https://www.webstaurantstore.com/'
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
        try:
            driver.get(self.url)
            time.sleep(10)
            page_sources = driver.page_source
            pk = BeautifulSoup(page_sources, 'lxml')
        finally:
            driver.close()
            driver.quit()
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
            Brand = 'T&S'
            print('Brand.....', Brand)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Brand = ''
            print(f"An error occurred: {e} Brand -----: {Brand}")

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            l3_name_list = [l3.text.strip() for l3 in self.pk.select("ol.breadcrumb li a span")]
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
            product_title = self.pk.select_one("h1#page-header-description").text.strip()
            print('product_title.....', product_title)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")
        # -------------------------------------------------- Price -----------------------------------------------------
        try:
            qty = self.pk.select_one("div.pricing span.each.pr-1").text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            qty = ''
            print(f"An error occurred: {e} qty -----: {qty}")


        try:
            list_of_price = self.pk.select_one("div.pricing span.price").text.strip().split("/")[0]
            price = {'list_price': list_of_price + " " + qty, 'qty': '1', 'moq': '1'}
            print("Price.....", price)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print(f"An error occurred: {e} price -----: {price}")

        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.pk.select_one("span.item-number span.uppercase").text.strip()
            print('SKU.....', mpn)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            mpn = ''
            print(f"An error occurred: {e} mpn -----: {mpn}")

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
            description_2 = [feature.text.strip() for feature in self.pk.select("ul.highlights.no-margin li")]
            if not description_2:
                raise ValueError("No description_2 found")
            print('description_2.....', description_2)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            description_2 = []
            print(f"An error occurred: {e} description_2 -----: {description_2}")

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get('src'), "alt": img.get('alt')} for img in self.pk.select("#gallery img")]  # if "svg" not in img.get('src', '')
            print('images.....', images)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            images = ''
            print(f"An error occurred: {e} images -----: {images}")

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            attr_name = [th.text.strip() for th in self.pk.select("#specifications-group dl#tbSpecSheetRows dt")]
            attr_value = [td.text.strip() for td in self.pk.select("#specifications-group dl#tbSpecSheetRows dd")]
            specs = [{name: value} for name, value in zip(attr_name, attr_value)]
        except (AttributeError, TypeError, IndexError, Exception) as e:
            specs = ''
            print(f"An error occurred: {e}")
        try:
            Dimensions_name = []
            Dimensions_value = []
            data = self.pk.select_one("div#details-group p").get_text(strip=True, separator=">>")
            ss = data.split("Overall Dimensions:")[1]
            delete_list = ss.split(">>")
            del delete_list[0]
            for de in delete_list:
                spl = de.split(":")
                Dimensions_name.append(spl[0])
                Dimensions_value.append(spl[1])

            Dimensions = [{dime_name: dime_value} for dime_name, dime_value in zip(Dimensions_name, Dimensions_value)]
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Dimensions = ''
            print(f"An error occurred: {e}")


        specifications_1 = str(specs) + " " + str(Dimensions)
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
            related_url = [urljoin(base_url, href_link.get('href')) for href_link in self.pk.select("#related-items-carousel ul li a")]
            if not related_url:
                raise ValueError("No realated links found")
            accessories = {'accessories': related_url}
            print('accessories.....', accessories)
        except (AttributeError, TypeError, IndexError, Exception) as e:
            accessories = [{'accessories': []}]
            print(f"An error occurred: {e} realated -----: {accessories}")




        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            logo = urljoin(base_url, self.pk.select_one('div.side-section img.lazyLoad.b-loaded').get('src'))
        except (AttributeError, TypeError, IndexError, Exception) as e:
            logo = ''
            print(f"logo.....An error occurred: {e}\t{logo}")

        try:
            MFR = self.pk.select_one('span.mfr-number span.uppercase').text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            MFR = ''
            print(f"MFR.....An error occurred: {e}\t{MFR}")



        try:
            UPC_Code = self.pk.select_one("div.product__stat span.product__stat-desc").text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            UPC_Code = ''
            print(f"UPC_Code.....An error occurred: {e}\t{UPC_Code}")

        try:
            Quick_Shipping = self.pk.select_one('div.product__ship span.font-bold').text.strip()
        except (AttributeError, TypeError, IndexError, Exception) as e:
            Quick_Shipping = ''
            print(f"Quick_Shipping.....An error occurred: {e}\t{Quick_Shipping}")

        try:
            day_name = []
            day_value = []
            data = self.pk.select("div.map.map-override.mapP p.mapText.map3")
            for d in data:
                ss = d.get_text(strip=True, separator=">>").split("!>>")[1]
                sg = ss.split(">>")
                for day_div in sg:
                    day_element = day_div.split(":")
                    day_name.append(day_element[0])
                    day_value.append(day_element[1])
            days = [{d_name: d_value} for d_name, d_value in zip(day_name, day_value)]
        except (AttributeError, TypeError, IndexError, Exception) as e:
            days = ''
            print(f"days.....An error occurred: {e}\t{days}")


        miscellaneous = {"logo": logo, "UPC_Code": UPC_Code, "Quick_Shipping": Quick_Shipping, "MFR #": MFR, 'days': days}
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


# scraper_names = WebScraper('https://www.webstaurantstore.com/ts-b-2342-10-wall-mounted-double-pantry-faucet-with-8-centers/510B2342.html')
# scraper_names.Product_Details()



# ----------------------------------------------------------------------------------------------------------------------
def main():
    file_path = "P:/Web-scrapings/A-MONTH-2024/July/Webstaurantstore-Brand-T&S.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 4500
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

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
