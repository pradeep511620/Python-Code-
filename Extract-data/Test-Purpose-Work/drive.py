import concurrent.futures
import time
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

save_files = open("P:/Web-scrapings/A-MONTH-2024/July/Abb-Brand-Super-Strut.com/data/Abb-Brand-Super-Strut11.csv", "a+",encoding="utf-8")
base_url = 'https://new.abb.com/'
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
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        try:
            driver.get(self.url)
            time.sleep(16)
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
        l3_Names = ''
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        Brand = 'Super-Strut'
        scripts = self.pk.find_all('script')
        for script in scripts:
            if 'var model = {"ProductViewModel":' in script.text:
                json_data = script.text.split('var model = ')[1].split(';')[0]
                # Parse the JSON content
                data_parse = json.loads(json_data)

                # -------------------------------------------------- Title -----------------------------------------------------
                try:
                    product_title = data_parse['ProductViewModel']['Product']['productDetails']['item']['attributes']['ExtendedProductType']['values'][0]['text']
                    print('product_title.....', product_title)
                except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
                    product_title = ''
                    print(f"An error occurred: {e} product_title -----: {product_title}")
                # -------------------------------------------------- Price -----------------------------------------------------

                price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}

                # --------------------------------------------------- MPN ------------------------------------------------------
                try:
                    mpn = data_parse['ProductViewModel']['Product']['productDetails']['item']['productId']
                    print('SKU.....', mpn)
                except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
                    mpn = ''
                    print(f"An error occurred: {e} mpn -----: {mpn}")

                # ---------------------------------------------- Description_1 -------------------------------------------------
                try:
                    short = data_parse['ProductViewModel']['Product']['productDetails']['item']['attributes']['CatalogDescription']['values'][0]['text']
                    short_desc = short
                except (AttributeError, TypeError, IndexError, NoSuchElementException, Exception) as e:
                    short_desc = ''
                    print(f"An error occurred: {e} short_desc -----: {short_desc}")

                try:
                    desc = data_parse['ProductViewModel']['Product']['productDetails']['item']['attributes']['LongDescription']['values'][0]['text']
                    description_1 = {"desc": [desc], 'instructions': [], 'short_desc': short_desc}
                    print('description_1.....', description_1)
                except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
                    description_1 = {"desc": []}
                    print(f"An error occurred: {e} description_1 -----: {description_1}")

                # ---------------------------------------------- Description_2 -------------------------------------------------


                # -------------------------------------------------- Images ----------------------------------------------------
                try:
                    images = ''
                    image_div = data_parse['ProductViewModel']['Product']['productDetails']['item']['images']
                    for image_div in image_div:
                        img = {image_div['url']}
                        images = {'src': img, 'alt': ''}
                        print('images.....', images)
                except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
                    images = ''
                    print(f"An error occurred: {e} images -----: {images}")

                # --------------------------------------------- specifications_1 -----------------------------------------------
                try:
                    attribute_groups_table = data_parse['ProductViewModel']['Product']['attributeGroups']['items']
                    attri_name = []
                    attri_value = []
                    for group in attribute_groups_table:
                        attributes = group['attributes']
                        for attribute in attributes.values():
                            attribute_name = attribute['attributeName']
                            attri_name.append(attribute_name)
                            attribute_value = attribute['values']
                            texts = [value['text'] for value in attribute_value]
                            attri_value.append('>'.join(texts))

                    specs = [{name: value} for name, value in zip(attri_name, attri_value)]
                except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
                    specs = []
                    print(f"An error occurred: {e} specs -----: {specs}")


                specifications_1 = str(specs)
                print('specifications_1.....', specifications_1)



                # --------------------------------------------------------------------------------------------------------------
                list_column = [
                    "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
                    "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
                    "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
                    "scraped_by"
                ]
                raw_data = [{
                    "brand": Brand, "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
                    "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": 'weight',
                    "breadscrumbs": l3_Names, "image_urls": images, "mpn": mpn,
                    "specification_1": specifications_1, "specification_2": 'specifications_2', "datasheets": 'datasheet',
                    "product_description_1": description_1, "product_description_2": 'description_2',
                    "accessories": 'accessories', "video_links": 'video', "miscellaneous": 'miscellaneous',
                    "scraped_by": "Pradeep_RaptorTech",
                }]

                Data_Save(raw_data, list_column)
                print('Complete all Your Program')
                print()
                # self.pk.driver.close()
                # self.pk.driver.quit()


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# scraper_names = WebScraper('https://new.abb.com/products/7TAA005070R0001/700-1-1-4-str')
# scraper_names.Product_Details()



# ----------------------------------------------------------------------------------------------------------------------
def main():
    file_path = "P:/Web-scrapings/A-MONTH-2024/July/Abb-Brand-Super-Strut.com/url/Product-url - Copy.csv"
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
            print(f"{'--'*30} Thread Running {'--'*30}")
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
