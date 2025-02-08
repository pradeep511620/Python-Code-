import concurrent.futures
import time
from itertools import zip_longest

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
# from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import threading

from selenium.webdriver.common.by import By

lock = threading.Lock()
save_files = open("P:/Web-scrapings/A-MONTH-2024/Sep/Sloan-products/data/Sloan-products.csv", "a+",encoding="utf-8")
base_url = 'https://sloan.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.pk = self.send_requests_and_driver_from_page_sources()

    def send_requests_and_driver_from_page_sources(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(3)

        return driver



    def Product_Details(self):
        print("Product-url---: ", self.url)

        try:
            l3_name = [l3.text.strip() for l3 in self.pk.find_elements(By.CSS_SELECTOR, "div#block-sloan-breadcrumbs ol a")]
            L3_Name = "## ".join(l3_name)
            print(f"L3 Name: {L3_Name}")
        except Exception as e:
            L3_Name = 'N/A'
            print(f"Error extracting L3 Name: {str(e)}")

        try:
            product_title = self.pk.find_element(By.CSS_SELECTOR, "div.slo-product-info .row h1").text.strip()
            print(f"Product Title: {product_title}")
        except Exception as e:
            product_title = 'N/A'
            print(f"Error extracting Product Title: {str(e)}")

        try:
            short = self.pk.find_element(By.CSS_SELECTOR, "div.slo-product-info .row .mt-2xs.text-xl p").text.strip()
            print(f"Short Description: {short}")
        except Exception as e:
            short = 'N/A'
            print(f"Error extracting Short Description: {str(e)}")

        try:
            description_1 = self.pk.find_elements(By.CSS_SELECTOR, "div.slo-product-info .row .mt-2xs p")[-1].text.strip()
            print(f"Description 1: {description_1}")
        except Exception as e:
            description_1 = 'N/A'
            print(f"Error extracting Description 1: {str(e)}")

        try:
            description_2 = [feature.text.strip().replace('\n', ">>") for feature in
                             self.pk.find_elements(By.CSS_SELECTOR, "section.product-section.product-features-list ul")]
            print(f"Description 2: {description_2}")
        except Exception as e:
            description_2 = []
            print(f"Error extracting Description 2: {str(e)}")

        try:
            description_3 = self.pk.find_element(By.CSS_SELECTOR, "span.text-trimmed").text.strip()
            print(f"Description 3: {description_3}")
        except Exception as e:
            description_3 = 'N/A'
            print(f"Error extracting Description 3: {str(e)}")

        try:
            image_list_1 = self.pk.find_element(By.CSS_SELECTOR, "div.product-media-images .responsive-image.ratio.ratio-1.active img").get_attribute('src')
            print(f"Image List 1: {image_list_1}")
        except Exception as e:
            image_list_1 = ''
            print(f"Error extracting Image List: {str(e)}")

        try:
            source_of_related = [source.get_attribute('href') for source in self.pk.find_elements(By.CSS_SELECTOR, 'div.product-teaser .row a')]
            print(f"Source of Related Products: {source_of_related}")
        except Exception as e:
            source_of_related = []
            print(f"Error extracting Related Product Sources: {str(e)}")

        try:
            button = self.pk.find_element(By.CSS_SELECTOR, "li.py-md button")
            button.click()
            print("Button clicked successfully.")
        except (NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException):
            print("Error: The element was not found.")

        h4_texts = []
        h3_texts = []
        try:
            h4_elements = self.pk.find_elements(By.CSS_SELECTOR, "h4.filter-title.flex-1.text-base.fw-strong")
            h4_texts = [h4.text.strip() for h4 in h4_elements if h4.is_displayed()]

            h3_elements = self.pk.find_elements(By.CSS_SELECTOR, "div.flex-1.ais-RefinementList")
            h3_texts = [h3.text.strip() for h3 in h3_elements if h3.is_displayed()]
        except Exception as e:
            print(f"Error extracting specifications: {str(e)}")

        specs_1 = [{name: value} for name, value in zip_longest(h4_texts, h3_texts, fillvalue='N/A')]
        print("Extracted Specifications:", specs_1)

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
                    time.sleep(2)
                    print("Clicked on Downloads")
                    break
        except Exception as e:
            print(f"An error occurred while trying to click 'Downloads': {e}")

        pdf_list = []
        pdf = self.pk.find_elements(By.CSS_SELECTOR, "#downloads article")
        for source in pdf:
            try:
                source_pdf = source.find_element(By.CSS_SELECTOR, "a.download-type").get_attribute('href')
            except Exception as e:
                source_pdf = 'N/A'
                print(f"Error extracting PDF link: {str(e)}")
            pdf_list.append(source_pdf)
        print('Extracted PDFs:', pdf_list)

        try:
            while True:
                last_button = self.pk.find_element(By.XPATH, "//button[normalize-space()='View More Variations']")
                if last_button:
                    last_button.click()
                    print("Clicked on the last variation button.")
                    time.sleep(2)
                else:
                    print("No more buttons to click.")
                    break
        except Exception as e:
            print("No more buttons to click. 2 ")


        image_list = []
        mpn_list = []
        number_list = []
        price_list = []
        discontinued_list = []
        inner_description_list = []
        product_variations = self.pk.find_elements(By.CSS_SELECTOR, "#variations ul li.product-variation-item")
        for variation in product_variations:
            try:
                image = variation.find_element(By.CSS_SELECTOR, "div.slo-product-image img").get_attribute('src')
            except:
                image = 'N/A'
            image_list.append(image)

            try:
                mpn = variation.find_element(By.CSS_SELECTOR, "h4").text.strip()
            except:
                mpn = 'N/A'
            mpn_list.append(mpn)

            try:
                number = variation.find_element(By.CSS_SELECTOR, ".items-baseline p").text.strip()
            except:
                number = 'N/A'
            number_list.append(number)

            try:
                price = variation.find_element(By.CSS_SELECTOR, "div.price-info--price-wrapper").text.strip()
            except:
                price = 'N/A'
            price_list.append(price)

            try:
                discontinued = variation.find_element(By.CSS_SELECTOR, ".items-baseline span").text.strip()
            except:
                discontinued = 'N/A'
            discontinued_list.append(discontinued)

            try:
                inner_description = variation.find_element(By.CSS_SELECTOR, "p.mt-sm.text-sm").text.strip()
            except:
                inner_description = 'N/A'
            inner_description_list.append(inner_description)
        # print(number_list)

        lists_to_pad = [image_list, mpn_list, number_list, price_list, discontinued_list, pdf_list, inner_description_list]
        max_length = max(len(image_list), len(mpn_list), len(number_list), len(price_list), len(discontinued_list),
                         len(pdf_list), len(inner_description_list))

        # Ensure all lists are of the same length
        for lst in lists_to_pad:
            while len(lst) < max_length:
                lst.append('')

        # Example data structure to save
        data_save = {
            'URL': self.url,
            'l3_name': [L3_Name] * len(image_list),
            'product_title': product_title,
            'Images_1': image_list_1,
            'Images_List': image_list,
            'MPN': mpn_list,
            'Number': number_list,
            'Price': price_list,
            'Discontinued': discontinued_list,
            'Datasheet': pdf_list,
            'Inner_description': inner_description_list,
            'Description_1': description_1,
            'Description_2': description_2 * len(image_list),
            'Description_3': description_3,
            'Specification_1': str(specs_1),

        }

        # Save data to DataFrame
        df = pd.DataFrame(data_save)
        df.to_csv('product_data1.csv', mode='a+', index=False)

        print("Data saved successfully!")


# scraper_names = WebScraper('https://www.sloan.com/commercial-bathroom-products/flushometers/ecos/ecos-111')
# scraper_names = WebScraper('https://www.sloan.com/commercial-bathroom-products/faucets/basys/efx-100')
# scraper_names.Product_Details()

list_of_url = [

    'https://www.sloan.com/commercial-bathroom-products/faucets/basys/efx-100',
    'https://www.sloan.com/commercial-bathroom-products/flushometers/ecos/ecos-111',
]
for index, url in enumerate(list_of_url):
    print(f"Processing URL {index + 1}: {url}")
    scraper = WebScraper(url)
    scraper.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------
def main():
    file_path = r"P:\Web-scrapings\A-MONTH-2024\Sep\Fabory-products\url\Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 0
    for url_count, url in enumerate(url_links[start_url:200], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


#
# if __name__ == "__main__":
#     main()
