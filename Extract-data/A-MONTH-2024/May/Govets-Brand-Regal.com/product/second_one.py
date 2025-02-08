import time
import concurrent.futures
# from urllib.parse import urljoin
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Proxy credentials
proxy = 'https://catalog:kCVftpL8r8fsw7Wmb7@gate.smartproxy.com:7000'
# proxy = {
#     'http': proxy_url,
#     'https': proxy_url
# }

save_files = open("D:/Web-Scrapping/A-MONTH-2024/May/Govets-Brand-Regal.com/data/Govets-Brand-Regal.csv", "a+", encoding="utf-8")
base_url = 'https://www.govets.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.pk = self.SendDriverOnly()
        # self.pk = self.SendDriverAndSoup()
        # self.pk = self.SendSoupOnly()

    def SendDriverAndSoup(self):
        chrome_options = Options()
        chrome_options.add_argument(f'--proxy-server={proxy}')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get(self.url)
            time.sleep(6)
            page_sources = driver.page_source
            pk = BeautifulSoup(page_sources, 'lxml')
        finally:
            driver.close()

        return pk

    def SendDriverOnly(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(2)
        return driver

    def SendSoupOnly(self):
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
        Brand = 'Regal'

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            names = [l3.text.strip() for l3 in self.pk.find_elements(By.CSS_SELECTOR, ".breadcrumbs .items li")]
            l3_Name = "## ".join(names)
            print('l3_Name.....', l3_Name)
        except (AttributeError, TypeError, IndexError, NoSuchElementException, Exception) as e:
            print(f"An error occurred: {e}")
            print('l3_Name.....', l3_Name)

        if l3_Name:
            categories = l3_Name.split("## ")
            catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(1, 4)]
            print('catlvl1.....', catlvl1)
            print('catlvl2.....', catlvl2)
            print('catlvl3.....', catlvl3)
        # -------------------------------------------------- Title -----------------------------------------------------
        try:
            product_title = self.pk.find_element(By.CSS_SELECTOR,".page-title").text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print('product_title.....', product_title)
            print(f"An error occurred: {e}")
        # -------------------------------------------------- Price -----------------------------------------------------

        try:
            list_of_price = self.pk.find_element(By.CSS_SELECTOR,'.product-info-price .price').text.strip()
            price = {'list_price': list_of_price, 'qty': '1', 'moq': '1'}
            print("Price.....", price)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            price = {'list_price': '$-.--', 'qty': '1', 'moq': '1'}
            print(f"An error occurred: {e}")
        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = self.pk.find_element(By.CSS_SELECTOR,"#product_info").text.strip().replace("Brand: RegalPart #: ", "")
            print('mpn.....', mpn)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            mpn = 'N/A'
            print('mpn:', mpn)
            print(f"An error occurred: {e}")
        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            short = self.pk.find_element(".descriptionsssssss").text.strip()
            short_desc = short
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            short_desc = ''
            print(f"An error occurred: {e}\t{short_desc}")

        #
        try:
            desc = [desc_text.get(strip=True, separator=">>>>").split(">>>>")[0] for desc_text in self.pk.find_elements(".product.attribute.description .value")]
            # if not desc:
            #     desc = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "//*[@itemprop='description']")]
            description_1 = {"desc": desc, 'instructions': [''], 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e}")
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [des_1.text.strip() for des_1 in self.pk.find_elements("#overview-tab-2 ul li")]
            print('description_2.....', description_2)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError,
                Exception) as e:
            print(f"An error occurred: {e}")
            description_2 = []
            print('description_2.....', description_2)

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get_attribute('src'), "alt": img.get_attribute('alt')} for img in self.pk.find_elements('[data-gallery-role="gallery"] img')]
            print('images.....', images)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"An error occurred: {e}")
            images = ''

        # --------------------------------------------- specifications_1 -----------------------------------------------
        """
        try:
            attr_name = [th.text.strip() for th in self.pk.select(".woocommerce-product-attributes.shop_attributes th")]
            attr_value = [td.text.strip() for td in self.pk.select(".woocommerce-product-attributes.shop_attributes td")]
            specs = [{name: value} for name, value in zip(attr_name, attr_value)]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specs = ''
            print(f"An error occurred: {e}")
        """
        try:
            row_count = 0
            attr_name = []
            attr_value = []
            for table_row in self.pk.find_elements(By.CSS_SELECTOR,".product.attribute.description ul li"):
                row_count += 1
                tab = table_row.text.strip().split(": ")
                if len(tab) == 2:
                    attr_name.append(tab[0])
                    attr_value.append(tab[1])
            specs = [{name_li: values_li} for name_li, values_li in zip(attr_name, attr_value)]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specs = ''
            print(f"An error occurred: {e}")
        specifications_1 = str(specs)
        print('specifications_1.....', specifications_1)


        # ----------------------------------------------- specifications_2 ---------------------------------------------
        try:
            specifications_2 = [th.text.strip() for th in self.pk.find_elements(By.XPATH, "//div[@id='collapse")]
            print('specifications_2.....', specifications_2)
        except (AttributeError, TypeError, IndexError, NoSuchElementException, JavascriptException):
            specifications_2 = []
            print('specifications_2.....', specifications_2)

        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = [pdf.get_attribute('href') for pdf in self.pk.find_elements(By.CSS_SELECTOR,"#resourcetable ul li a")]
            print('datasheet.....', datasheet)
        except (NoSuchElementException, ElementClickInterceptedException, AttributeError, TypeError, IndexError,
                Exception) as e:
            print(f"An error occurred: {e}")
            datasheet = []
            print('datasheet.....', datasheet)

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get_attribute('data-url') for video_link in self.pk.find_elements(By.CSS_SELECTOR,'.click-vlink')]
            print('video.....', video)
        except (NoSuchElementException, TypeError, IndexError, AttributeError):
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [href_link.get_attribute('href') for href_link in self.pk.find_elements(By.CSS_SELECTOR,".related.products .products.columns-3 li a")if "?add-to-cart" not in href_link.get_attribute("href", "")]
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, IndexError, TypeError, AttributeError):
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            Discount = self.pk.find_elements(By.CSS_SELECTOR,"#pricing_info span")[0].text.strip().replace("Discount: ", "")
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            Discount = ''
            print(f"An error occurred: {e}\t{Discount}")

        try:
            Shipping = self.pk.find_elements(By.CSS_SELECTOR, "#pricing_info span")[1].text.strip()
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            Shipping = ''
            print(f"An error occurred: {e}\t{Shipping}")

        try:
            logo = self.pk.find_element(By.CSS_SELECTOR, ".ambanners.ambanner-7 p img").get_attribute('src')
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            logo = ''
            print(f"An error occurred: {e}\t{logo}")




        try:
            sku_details = self.pk.find_element(".product.attribute.sku .value").text.strip()
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            sku_details = ''
            print(f"An error occurred: {e}\t{sku_details}")

        miscellaneous = {"SKU#": sku_details, "Discount": Discount, "Shipping": Shipping, "logo": logo}
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
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": '',
            "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": specifications_2, "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": description_2,
            "accessories": realated, "video_links": video, "miscellaneous": miscellaneous,
            "scraped_by": "Pradeep_RaptorTech",
        }]

        Data_Save(raw_data, list_column)
        print('Complete all Your Program')
        print()

        # except Exception as e:
        #     print(f"Error{e}")
        #     with open('remain_url.txt', "a+", encoding="utf-8") as file:
        #         file.write(f"{self.url}\n")




def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')



# scaper_name = WebScraper('https://www.govets.com/regal-310-58874033.html')
# scaper_name.Product_Details()


# ----------------------------------------------------------------------------------------------------------------------

def ReadUrlFromList():
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Govets-Brand-Regal.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    i = 0
    for url_count, url in enumerate(url_links[i:5], start=i):
        print('product_url.....', url_count)
        name = WebScraper(url)
        name.Product_Details()


# ReadUrlFromList()


def main():
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Govets-Brand-Regal.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    Product_url = []
    start_url = 172
    for url_count, url in enumerate(url_links[start_url:500], start=start_url):
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
