# import smtplib
import concurrent.futures
import smtplib
import time
from urllib.parse import urljoin
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

save_files = open("P:/Web-scrapings/A-MONTH-2024/Jun/Arrowpneumatics-products.com/data/Arrowpneumatics-productssas.csv",
                  "a+", encoding="utf-8")
base_url = 'https://www.arrowpneumatics.com/'
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
            time.sleep(3)
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
        # time.sleep(6)
        return soup



    def Product_Details(self):
        print("Product-url---: ", self.url)

        l3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        weight = ''
        desc2 = list()
        try:
            Brand = 'arrowpneumatics'
            print('Brand.....', Brand)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            Brand = ''
            print(f"An error occurred: {e} Brand -----: {Brand}")

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            names = [l3.text.strip() for l3 in self.pk.select("nav[data-test-selector='pageBreadcrumbs'] a")]
            l3_Name = "## ".join(names)
            print('l3_Name.....', l3_Name)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} l3_Name -----: {l3_Name}")

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)
        # -------------------------------------------------- Title -----------------------------------------------------
        try:
            product_title = self.pk.select_one('.items_description_box p').text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")
        # -------------------------------------------------- Price -----------------------------------------------------
        try:
            qty = self.pk.select_one("[data-test-selector='productPrice_unitOfMeasureLabel']").text.strip()
        except (AttributeError, TypeError, IndexError, NoSuchElementException, Exception) as e:
            qty = ''
            print(f"An error occurred: {e} qty -----: {qty}")

        try:
            list_of_price = self.pk.select_one(
                ".sc-bczRLJ.jNwdcG [data-test-selector='productPrice_unitNetPrice']").text.strip()
            price = {'list_price': list_of_price + " /EA", 'qty': qty, 'moq': '1'}
            print("Price.....", price)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print(f"An error occurred: {e} price -----: {price}")
        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.pk.select_one(".items_description_box p").text.strip().replace(" ", "/").split('/')[0]
            print('SKU.....', mpn)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            mpn = ''
            print(f"An error occurred: {e} mpn -----: {mpn}")
        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            short = self.pk.select_one(".items_description_box p").text.strip()
            short_desc = short
        except (AttributeError, TypeError, IndexError, NoSuchElementException, Exception) as e:
            short_desc = ''
            print(f"An error occurred: {e} short_desc -----: {short_desc}")
        desc = ''
        try:
            div = self.pk.select_one('.right_content .right_description')
            if div:
                if div.h2:
                    div.h2.decompose()
                desc = div.get_text(separator="\t").strip().replace("\n", "").replace("\t", "")
            # desc = [des.next_sibling.text.strip() for des in self.pk.select(".right_description br")]
            # if not desc:
            #     desc = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "//*[@itemprop='description']")]
            description_1 = {"desc": desc, 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            description_1 = {"desc": []}
            print(f"An error occurred: {e} description_1 -----: {description_1}")



        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": urljoin(base_url, img.get('src')), "alt": img.get('alt')} for img in self.pk.select("#center_container_pages img")]
            print('images.....', images)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            images = ''
            print(f"An error occurred: {e} images -----: {images}")

        # --------------------------------------------- specifications_1 -----------------------------------------------
        try:
            dimensions = list()
            for dimension_elm in self.pk.find('div', class_='scheme_description_text').get_text().replace('\n', '#').replace(
                    '\xa0\xa0', '').split('#'):
                if '-' in dimension_elm:
                    dimension = dimension_elm.split('-')
                    dimensions.append({dimension[0].strip(): dimension[1].strip()})
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            dimensions = []
            print(f"An error occurred: {e} dimensions -----: {dimensions}")

        try:
            spec1 = list()
            for i in self.pk.find('div', class_='right_description_text').get_text().replace('\n', '#').split('#'):
                if '-' in i:
                    spec_elm = i.split(' - ')
                    spec1.append({spec_elm[0]: spec_elm[1]})

                elif 'WARNING' in i or 'SPECIFICATIONS' in i:
                    continue

                elif '•' or '      ' in i:
                    if len(i) > 10:
                        desc2.append(i.replace('• ', '').strip())
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            spec1 = []
            print(f"An error occurred: {e} spec1 -----: {spec1}")

        specifications_1 = str(dimensions) + ", " + str(spec1)
        print('specifications_1......', specifications_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = desc2
            print('description_2.....', description_2)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            description_2 = []
            print(f"An error occurred: {e} description_2 -----: {description_2}")

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
            datasheet = [pdf.get('href') for pdf in self.pk.select(".verification a")]
            print('datasheet.....', datasheet)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            datasheet = []
            print(f"An error occurred: {e} datasheet -----: {datasheet}")

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('data-url') for video_link in self.pk.select('.click-vlink')]
            if not video:
                raise ValueError("No video links found")
            print('video.....', video)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            video = []
            print(f"An error occurred: {e} video -----: {video}")

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [href_link.get('href') for href_link in self.pk.select("#block-related li a")]
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            realated = [{'accessories': []}]
            print(f"An error occurred: {e} realated -----: {realated}")

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        war_list = []
        war = self.pk.select("#center_container_pages .right_description_text")
        for w in war:
            war_text = w.text.strip().replace('\n', '>>>').split(">>>")
            for warn in war_text:
                if "WARNING!" in warn or "Warning!" in warn:
                    war_list.append(warn)

        try:
            warning = war_list
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            warning = ''
            print(f"An error occurred: {e} manufacturer -----: {warning}")

        miscellaneous = {'warning': warning}
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
            "accessories": realated, "video_links": video, "miscellaneous": miscellaneous,
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


# scraper_names = WebScraper('https://www.arrowpneumatics.com/l452w.html')
# scraper_names = WebScraper('https://www.arrowpneumatics.com/f333w.html')
# scraper_names.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------

def ReadUrlFromList():
    file_path = "P:/Web-scrapings/A-MONTH-2024/Jun/Arrowpneumatics-products.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:1], start=i):
        print('product_url.....', url_count)
        scraper_name = WebScraper(url)
        scraper_name.Product_Details()


# ReadUrlFromList()


def main():
    file_path = "P:/Web-scrapings/A-MONTH-2024/Jun/Arrowpneumatics-products.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 0
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
