import concurrent.futures
import time
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


save_files = open("P:/Web-scrapings/A-MONTH-2024/Jun/Eberbachlabtools-product.com/data/Eberbachlabtoolsa1_2.csv", "a+", encoding="utf-8")
base_url = 'https://eberbachlabtools.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.pk = self.send_selenium_from_driver()

    def send_selenium_from_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

        driver.get(self.url)
        time.sleep(2)

        return driver




    def Product_Details(self):
        print("Product-url---: ", self.url)

        try:
            Brand = self.pk.find_element(By.CSS_SELECTOR, ".product-meta__reference a").text.strip()
            print('Brand.....', Brand)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            Brand = ''
            print(f"An error occurred: {e} Brand -----: {Brand}")

        # -------------------------------------------------- Title -----------------------------------------------------
        try:
            product_title = self.pk.find_element(By.CSS_SELECTOR,'.product-meta h1').text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print(f"An error occurred: {e} product_title -----: {product_title}")
        # -------------------------------------------------- Price -----------------------------------------------------
        try:
            price = ''
            price_element = self.pk.find_element(By.CSS_SELECTOR, ".product-form__info-content .price-list")
            if price_element.is_displayed():
                prices = price_element.text.strip().replace("Sale price", '')
                price = {'list_price': prices + " /EA", 'qty': '1', 'moq': '1'}
            print("Price.....", price)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print(f"An error occurred: {e} price -----: {price}")
        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.pk.find_element(By.CSS_SELECTOR,".product-meta__sku-number").text.strip()
            print('SKU.....', mpn)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            mpn = ''
            print(f"An error occurred: {e} mpn -----: {mpn}")
        # ---------------------------------------------- Description_1 -------------------------------------------------




        # --------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": Brand, "catlvl1": 'catlvl1', "catlvl2": 'catlvl2', "catlvl3": 'catlvl3', "url": self.url,
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": 'weight',
            "breadscrumbs": 'l3_Name', "image_urls": 'images', "mpn": mpn,
            "specification_1": 'specifications_1', "specification_2": 'specifications_2', "datasheets": 'datasheet',
            "product_description_1": 'description_1', "product_description_2": 'description_2',
            "accessories": 'realated', "video_links": 'video', "miscellaneous": 'miscellaneous',
            "scraped_by": "Pradeep_RaptorTech",
        }]

        Data_Save(raw_data, list_column)
        print('Complete all Your Program')
        print()

        self.pk.close()
        self.pk.quit()





def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')



# scraper_names = WebScraper('https://eberbachlabtools.com/products/heavy-duty-variable-speed-cutting-mills?_pos=1&_sid=8ce5eb120&_ss=r&variant=41952585547954')
# scraper_names.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------

def ReadUrlFromList():
    file_path = "P:/Web-scrapings/A-MONTH-2024/Jun/Eberbachlabtools-product.com/url/Product-url - Copy.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:], start=i):
        print('product_url.....', url_count)
        scraper_name = WebScraper(url)
        scraper_name.Product_Details()


# ReadUrlFromList()


def main():
    file_path = "P:/Web-scrapings/A-MONTH-2024/Jun/Eberbachlabtools-product.com/url/Product-url - Copy.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 0
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
