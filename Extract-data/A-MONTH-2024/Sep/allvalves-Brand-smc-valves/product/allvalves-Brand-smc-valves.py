import concurrent.futures
import os
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import threading

from selenium.webdriver.common.by import By

lock = threading.Lock()
# save_files = open("P:/Web-scrapings/A-MONTH-2024/Sep/Sloan-products/data/Sloan-products.csv", "a+",encoding="utf-8")
base_url = 'https://sloan.com/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


class WebScraper:
    def __init__(self, URL):
        self.url = URL
        self.pk = self.send_requests_and_driver_from_page_sources()

    def send_requests_and_driver_from_page_sources(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        page_sources = driver.page_source
        pk = BeautifulSoup(page_sources, 'lxml')
        return pk



    def Product_Details(self):
        # print("Product-url---: ", self.url)

        L3_Name = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        try:
            try:
                Brand = 'smc vales'
                print('Brand.....', Brand)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                Brand = ''
                print(f"An error occurred: {e} Brand -----: {Brand}")

            # -------------------------------------------------- BreadCrumb ------------------------------------------------
            try:
                l3_name = [l3.text.strip() for l3 in self.pk.select("#crumbtrail a")]
                L3_Name = "## ".join(l3_name)
                print(f"L3 Name: {L3_Name}")
            except Exception as e:
                print(f"Error extracting L3 Name: {str(e)}")

            if L3_Name:
                categories = L3_Name.split("## ")
                catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(2, 5)]
                print('catlvl1.....', catlvl1)
                print('catlvl2.....', catlvl2)
                print('catlvl3.....', catlvl3)



            try:
                product_title = self.pk.select_one("#pageTitle h1").text.strip()
                print(f"Product Title: {product_title}")
            except Exception as e:
                product_title = 'N/A'
                print(f"Error extracting Product Title: {str(e)}")

            try:
                mpn = self.pk.select_one("#content h2 strong").text.strip().split(' -')[0]
                print(f"Product Mpn: {mpn}")
            except Exception as e:
                mpn = 'N/A'
                print(f"Error extracting Product Title: {str(e)}")

            try:
                number = self.pk.select("div.flex-col.gap-md.py-md .flex-column.flex-1 p")[0].text.strip()
                print(f"Product number: {number}")
            except Exception as e:
                number = 'N/A'
                print(f"Error extracting Product Title: {str(e)}")

            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            try:
                list_of_price = self.pk.find_element(By.CSS_SELECTOR, "div.slo-price-info div.price-info--price-wrapper").text.strip()
                if list_of_price:
                    price = {'list_price': list_of_price + " /EA", 'qty': '1', 'moq': '1'}
                    print("Price.....", price)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                print(f"An error occurred: {e} price -----: {price}")
            if price:
                USD = 'USD'
            else:
                USD = ''

            try:
                short_desc = self.pk.find_element(By.CSS_SELECTOR, "div.slo-product-info .row .mt-2xs.text-xl p").text.strip()
                print(f"Short Description: {short_desc}")
            except Exception as e:
                short_desc = 'N/A'
                print(f"Error extracting short_desc Description: {str(e)}")

            try:
                desc = [des.text.strip() for des in self.pk.select("div#content p")[2:-1]]
                description_1 = {"desc": desc, 'instructions': [], 'short_desc': short_desc}
                print(f"Description 1: {description_1}")
            except Exception as e:
                description_1 = 'N/A'
                print(f"Error extracting Description 1: {str(e)}")



            try:
                description_2 = [feature.text.strip() for feature in self.pk.select("section.product-features-list ul li")]
                print(f"Description 2: {description_2}")
            except Exception as e:
                description_2 = []
                print(f"Error extracting Description 2: {str(e)}")


            try:
                images = [{"src": img.get('src'), "alt": img.get('alt')} for img in self.pk.select("div.mainProductImage img")]
                print(f"Image List 1: {images}")
            except Exception as e:
                images = ''
                print(f"Error extracting Image List: {str(e)}")

            # --------------------------------------------------------------------------------------------------------------
            data_row = []
            for table in self.pk.select('table#productTable tbody tr'):
                table_row = table.get_text(strip=True, separator='>>')
                data_row.append(table_row.split('>>'))

            specs = []
            try:
                tables = self.pk.select("section#specifications span")
                it = iter(tables)
                specs = [{name.text.strip(): value.text.strip()} for name, value in zip(it, it)]
            except Exception as e:
                print(f"Specifications not found: {e}")

            specifications_1 = specs
            print('specifications_1 -----: ', specifications_1)

            # --------------------------------------------------------------------------------------------------------------


            datasheet = []
            try:
                datasheet = [pdf.get_attribute('href') for pdf in self.pk.select("#downloads article a")]
            except Exception as e:
                print(f"Error extracting PDF link: {str(e)}")

            print('Extracted PDFs:', datasheet)

            try:
                source_of_related = [source.get_attribute('href') for source in self.pk.select('div.product-teaser .row a')]
            except Exception as e:
                source_of_related = []
                print(f"Error extracting Related Product Sources: {str(e)}")

            accessories = {'accessories': source_of_related}
            print(f"Source of Related Products: {accessories}")

            miscellaneous = {"number": number}
            print('miscellaneous.....', miscellaneous)

            # --------------------------------------------------------------------------------------------------------------
            flattened_data = []

            for row in data_row:
                flattened_data.append({
                    'brand': Brand,
                    'catlvl1': catlvl1,
                    'catlvl2': catlvl2,
                    'catlvl3': catlvl3,
                    'url': self.url,
                    'title': product_title,
                    'price_value': price,
                    'unit': USD,
                    'shipping_weight': "N/A",
                    'breadscrumbs': str(L3_Name),
                    'image_urls': str(images),
                    'mpn': mpn,
                    'specification_1': row,
                    'specification_2': [[]],
                    'datasheets': str(datasheet),
                    'product_description_1': str(description_1),
                    # 'tr_value_row': row,
                    'product_description_2': str(description_2),
                    'accessories': str(accessories),
                    'video_links': [[]],
                    'miscellaneous': miscellaneous,
                    'scraped_by': 'Pradeep_RaptorTech', 
                })

            # Create DataFrame outside the loop
            df = pd.DataFrame(flattened_data)
            print(df)

            # Check if the file exists
            file_path = 'product_data.csv'
            file_exists = os.path.exists(file_path)

            # Append data to the CSV, only write the header if the file doesn't exist
            df.to_csv(file_path, mode='a+', header=not file_exists, index=False)
            print("Data saved successfully!")

        finally:
            # self.pk.quit()
            print("Driver quit successfully.")

        # --------------------------------------------------------------------------------------------------------------

list_of_url = [
    'https://www.allvalves.co.uk/actuator-valves/knife-gate-valve-bi-directional-pneumatic-actuated-tecofi',

]
for index, url in enumerate(list_of_url):
    print(f"Processing URL {index + 1}: {url}")
    scraper = WebScraper(url)
    scraper.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------
def main():
    file_path = r"P:\Web-scrapings\A-MONTH-2024\Sep\Sloan-products\url\Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 100
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



# if __name__ == "__main__":
#     main()
