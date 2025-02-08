import time
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import concurrent.futures
import threading

# Initialize a thread lock
lock = threading.Lock()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}



class WebScraper:
    def __init__(self, url):
        self.url = url
        self.driver = self.send_driver_from_page()


    def send_driver_from_page(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(4)
        return driver


    final_data = []

    def Product_details(self):
        print("Product-url---: ", self.url)

        l3_name = ''
        try:
            bread = [l3.text.strip() for l3 in self.driver.find_elements(By.CSS_SELECTOR, "ol.MMM--breadcrumbs-list li [itemprop='name']")]
            l3_name = '## '.join(bread)
            print('l3_name-----:', l3_name)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {l3_name}")

        part_number = ''
        Product_Number = ''
        id_3m = ''
        upc_id = ''
        try:
            elements_div = self.driver.find_elements(By.CSS_SELECTOR, "ul.sps2-pdp_header--details_container_ids li")
            if not elements_div:
                print('No elements found with the given CSS selector')

            for element in elements_div:
                data_div = element.text.strip()

                if 'Part Number' in data_div:
                    part_number = 'rp_' + data_div.strip().replace('Part Number', '').strip()

                elif "Product Number" in data_div:
                    Product_Number = 'rp_' + data_div.replace('3M Product Number', '')

                elif "ID" in data_div:
                    id_3m = 'rp_' + data_div.replace('3M ID', '')

                elif "UPC" in data_div:
                    upc_id = 'rp_' + data_div.replace('UPC ', '')

                else:
                    print('No matching data found')

        except NoSuchElementException as e:
            print(f'Exception occurred: {e}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

        product_title = []
        try:
            product_title = self.driver.find_element(By.CSS_SELECTOR, "h1.sps2-pdp_header--name").text.strip()
            print('product_title-----: ', product_title)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {product_title}")

        images = []
        try:
            images = [{'src': img.get_attribute('src'), 'alt': img.get_attribute('alt')} for img in
                      self.driver.find_elements(By.CSS_SELECTOR, "div.sps2-pdp_gallery--box img")]
            print('images-----: ', images)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {images}")

        Highlights = []
        try:
            Highlights = [high.text.strip() for high in self.driver.find_elements(By.CSS_SELECTOR, "ul.sps2-pdp_details--highlights_list li")]
            print('Highlights -----: ', Highlights)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {Highlights}")

        feature = []
        try:
            feature = [fea.text.strip() for fea in
                       self.driver.find_elements(By.CSS_SELECTOR, "div.sps2-pdp_details--upper_details")]
            print('feature-----:', feature)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {feature}")

        table_dict = []
        try:
            rows = self.driver.find_elements(By.CSS_SELECTOR, "table.mds-dataTable tbody tr")
            table_dict = []
            for row in rows:
                tab = [cell.text.strip() for cell in row.find_elements(By.CSS_SELECTOR, "td")]
                if len(tab) == 2:
                    key, value = tab
                    table_dict.append({key: value})
            print('table_dict-----:', table_dict)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {table_dict}")
        product_name = []
        try:
            product_name = [name.text.strip() for name in self.driver.find_elements(By.CSS_SELECTOR, "span[data-for='shopName']")]
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {product_name}")

        datasheet = []
        try:
            datasheet = [pdf.get_attribute('href') for pdf in self.driver.find_elements(By.CSS_SELECTOR, "a.sps2-pdp_pSelector--dataSheets-mb-16")]
            if not datasheet:
                datasheet = [pdf.get_attribute('href') for pdf in self.driver.find_elements(By.CSS_SELECTOR, "div.mds-prodBar_item--link")]
            print('datasheet', datasheet)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {datasheet}")

        data = [self.url, l3_name, product_title, images, Highlights, feature, table_dict, product_name, datasheet, part_number, Product_Number, id_3m, upc_id]
        # self.final_data.append(data)
        # df = pd.DataFrame(self.final_data)
        #
        # df.to_csv('3m_files.csv', mode='w', index=False)
        # Locking access to final_data to prevent race conditions
        with lock:
            self.final_data.append(data)
        with lock:
            df = pd.DataFrame(self.final_data)
            df.to_csv('3m_files2.csv', mode='w', index=False)


    def close_driver(self):
        self.driver.quit()

#
# scraper = WebScraper('https://www.3m.com/3M/en_US/p/d/v000146426/')
# scraper.Product_details()
# scraper.close_driver()

def main():
    file_path = r"P:\Web-scrapings\Test-Purpose-Work\3m\3m_urlss.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 360
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")



if __name__ == "__main__":
    main()
