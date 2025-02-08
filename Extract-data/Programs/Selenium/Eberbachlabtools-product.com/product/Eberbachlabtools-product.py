import concurrent.futures
import time
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import threading


lock = threading.Lock()

save_files = open("P:/Web-scrapings/A-MONTH-2024/Sep/Sloan-products/data/Sloan-products.csv", "a+", encoding="utf-8")
base_url = 'https://sloan.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.pk = self.send_selenium_from_driver()

    def send_selenium_from_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        return driver




    def Product_Details(self):
        print("Product-url---: ", self.url)

        # --------------------------------------------------------------------------------------------------------------
        L3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        try:
            l3_name = [l3.text.strip() for l3 in self.pk.find_elements(By.CSS_SELECTOR, "div#block-sloan-breadcrumbs nav ol a")]
            L3_Name = '## '.join(l3_name) if l3_name else ''
            print('L3_Name -----:', L3_Name)
        except Exception as e:
            print(f"An error occurred while fetching L3 name: {e}")

        if L3_Name:
            categories = L3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)


        # -------------------------------------------------- Title -----------------------------------------------------
        try:
            product_title = self.pk.find_element(By.CSS_SELECTOR,'div.product h1').text.strip()
            print('product_title -----:', product_title)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")

        # -------------------------------------------------- Price -----------------------------------------------------
        price = ''
        try:
            price_element = self.pk.find_element(By.CSS_SELECTOR, ".product-form__info-content .price-list")
            if price_element.is_displayed():
                prices = price_element.text.strip().replace("Sale price", '')
                price = {'list_price': prices + " /EA", 'qty': '1', 'moq': '1'}
            print("Price.....", price)
        except NoSuchElementException:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}

        # --------------------------------------------------- MPN ------------------------------------------------------
        mpn = ''
        try:
            mpn = self.pk.find_element(By.CSS_SELECTOR,"div.product h1").text.strip()
            print('MPN -----:', mpn)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e} mpn -----: {mpn}")

        # ---------------------------------------------- Description_1 -------------------------------------------------
        short_desc = ''
        try:
            short_desc = self.pk.find_element(By.CSS_SELECTOR, "div.product .slo-product-info p.my-md").text.strip()
        except Exception as e:
            print(f"Short description not found: {e}")

        description_1 = {"desc": []}
        try:
            desc = [des.text.strip() for des in self.pk.find_elements(By.CSS_SELECTOR, "#adp-product-description")]
            description_1 = {"desc": desc, 'instructions': [], 'short_desc': short_desc}
            print('description_1 -----:', description_1)
        except Exception as e:
            print(f"Short description not found: {e}")

        # --------------------------------------------------------------------------------------------------------------
        try:
            description_2 = [feature.text.strip() for feature in self.pk.find_elements(By.CSS_SELECTOR, "section.product-section.product-features-list ul li")]
            print('description_2 -----:', description_2)
        except Exception as e:
            print(f"Product features not found: {e}")



        # --------------------------------------------------------------------------------------------------------------
        images = []
        try:
            images = [{"src": img.get_attribute('src'), "alt": img.get_attribute('alt')} for img in self.pk.find_elements(By.CSS_SELECTOR, "div.product-media img")]
            print('images -----:', images)
        except Exception as e:
            print(f"Images not found: {e}")

        # --------------------------------------------------------------------------------------------------------------
        source_of_related = []
        try:
            source_of_related = [source.get_attribute('href') for source in self.pk.find_elements(By.CSS_SELECTOR, 'div.related-products-grid header a')]
            print('source_of_related ----- :', source_of_related)
        except Exception as e:
            print(f"Related products not found: {e}")

        # --------------------------------------------------------------------------------------------------------------
        try:
            for Specifications_button in self.pk.find_elements(By.CSS_SELECTOR, "article nav li button"):
                button_text = Specifications_button.text.strip()
                if button_text == "Specifications":
                    Specifications_button.click()
                    time.sleep(1)
                    print("Clicked on Specifications")
                    break
        except Exception as e:
            print(f"An error occurred while trying to click 'Specifications': {e}")

        specs = []
        try:
            tables = self.pk.find_elements(By.CSS_SELECTOR, "section#specifications span")
            it = iter(tables)
            specs = [{name.text.strip(): value.text.strip()} for name, value in zip(it, it)]
        except Exception as e:
            print(f"Specifications not found: {e}")

        specifications_1 = specs
        print('specifications_1 -----: ', specifications_1)
        # --------------------------------------------------------------------------------------------------------------
        try:
            for download_button in self.pk.find_elements(By.CSS_SELECTOR, "article nav li button"):
                button_text = download_button.text.strip()
                if button_text == "Downloads":
                    download_button.click()
                    time.sleep(1)
                    print("Clicked on Downloads")
                    break
        except Exception as e:
            print(f"An error occurred while trying to click 'Downloads': {e}")

        datasheet = []
        try:
            datasheet = [pdf.get_attribute('href') for pdf in self.pk.find_elements(By.CSS_SELECTOR, '#downloads article a')]
            print('datasheet -----:', datasheet)
        except Exception as e:
            print(f"Related products not found: {e}")

        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": 'Sloan', "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": 'weight',
            "breadscrumbs": 'l3_Name', "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": 'specifications_2', "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": 'description_2',
            "accessories": source_of_related, "video_links": 'video', "miscellaneous": 'miscellaneous',
            "scraped_by": "Pradeep_RaptorTech",
        }]

        # Data_Save(raw_data, list_column)
        print('Complete all Your Program')
        print()

        self.pk.close()
        self.pk.quit()





def Data_Save(row, cols):  # using save data into dataframe
    with lock:
        df = pd.DataFrame(row, columns=cols)
        print(df)
        df.to_csv(save_files, header=False, index=False, lineterminator='\n')
        print('save data into csv files')



scraper_names = WebScraper('https://www.sloan.com/commercial-bathroom-products/hand-dryers/optima/ehd-420?variation_sku=33660015')
scraper_names.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------
