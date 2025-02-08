import time
import concurrent.futures
# from urllib.parse import urljoin
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, JavascriptException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Proxy credentials
# proxy = 'https://catalog:kCVftpL8r8fsw7Wmb7@gate.smartproxy.com:7000'
# proxy = {
#     'http': proxy_url,
#     'https': proxy_url
# }

save_files = open("D:/Web-Scrapping/A-MONTH-2024/May/Widia.com/data/Widia.csv", "a+", encoding="utf-8")
base_url = 'https://www.widia.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

class WebScraper:
    def __init__(self, url):
        self.url = url
        # self.pk = self.SendDriverOnly()
        self.pk = self.SendDriverAndSoup()
        # self.pk = self.SendSoupOnly()

    def SendDriverAndSoup(self):
        chrome_options = Options()
        # chrome_options.add_argument(f'--proxy-server={proxy}')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get(self.url)
            time.sleep(5)
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
        Brand = 'Johnson Controls'

        # -------------------------------------------------- BreadCrumb ------------------------------------------------
        try:
            names = [l3.text.strip() for l3 in self.pk.select("#breadcrumb li a")]
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
            product_title = self.pk.select_one(".product-name-title").text.strip()
            print('product_title.....', product_title)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            product_title = ''
            print('product_title.....', product_title)
            print(f"product_title..... An error occurred: {e}")
        # -------------------------------------------------- Price -----------------------------------------------------

        try:
            list_of_price = self.pk.select_one('.gUKiTB.ProductQuantityAdjustorsPriceText-sc-1faew0k-0.cRBogh').text.strip().replace("\xa0 ", "")
            price = {'list_price': list_of_price, 'qty': 'each', 'moq': '1'}
            print("Price.....", price)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            price = {'list_price': '$-.--', 'qty': 'each', 'moq': '1'}
            print(f"Price..... An error occurred: {e}")
        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            mpn = next((spe.findNext("td").text.strip() for spe in self.pk.select(".p-esp-table tbody tr td") if "ANSI Catalog Number" == spe.text.strip()), None)
            print('mpn.....', mpn)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            mpn = 'N/A'
            print('mpn:', mpn)
            print(f"mpn..... An error occurred: {e}")
        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            short = self.pk.select_one(".product-name-content h3").text.strip()
            short_desc = short
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            short_desc = ''
            print(f"short_desc..... An error occurred: {e}\t{short_desc}")


        try:
            desc = [desc_text.get_text(strip=True, separator=">>>").split(">>>")[0] for desc_text in self.pk.select_one(".ProductPageDescription__ProductPageDescriptionText-sc-1i7espa-2")]
            # if not desc:
            #     desc = [desc_text.text.strip() for desc_text in self.driver.find_elements(By.XPATH, "//*[@itemprop='description']")]
            description_1 = {"desc": desc, 'instructions': [''], 'short_desc': short_desc}
            print('description_1.....', description_1)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"description_1...... An error occurred: {e}")
            description_1 = {"desc": [], 'instructions': [''], 'short_desc': short_desc}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
        try:
            description_2 = [feature.text.strip() for feature in self.pk.select(".product-features-and-benefits-content .list__squares li")]
            print('description_2.....', description_2)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"description_2..... An error occurred: {e}")
            description_2 = []
            print('description_2.....', description_2)


        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = [{"src": img.get('src'), "alt": img.get('alt')} for img in self.pk.select(".product-main-image__thumb img") ]
            print('images.....', images)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"images..... An error occurred: {e}")
            images = ''

        # --------------------------------------------- specifications_1 -----------------------------------------------
        # try:
        #     attr_name = [th.text.strip() for th in self.pk.select(".ProductPageSpecifications__Table-sc-dy0arh-0 tbody tr th")]
        #     attr_value = [td.text.strip() for td in self.pk.select(".ProductPageSpecifications__Table-sc-dy0arh-0 tbody tr td")]
        #     specs = [{name: value} for name, value in zip(attr_name, attr_value)]
        # except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
        #     specs = ''
        #     print(f"An error occurred: {e}")


        try:
            attr_name2 = []
            attr_value2 = []
            table_count = 0
            for table_div in self.pk.select(".p-esp-table tbody tr td"):
                table_count += 1
                table_td = table_div.text.strip()
                if table_count % 2 != 0:
                    attr_name2.append(table_td)
                else:
                    attr_value2.append(table_td)
            specs_2 = [{name_li: values_li} for name_li, values_li in zip(attr_name2, attr_value2)]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            specs_2 = ''
            print(f"An error occurred: {e}")

        specifications_1 = str(specs_2)
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
            datasheet = [pdf.get('href') for pdf in self.pk.select(".Box-sc-1z9git-0.Flex-sc-1qhr4qe-0.StackContainer-sc-15uql32-0.gIHGkO a")]
            print('datasheet.....', datasheet)
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            print(f"datasheet..... An error occurred: {e}")
            datasheet = []
            print('datasheet.....', datasheet)

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = [video_link.get('src') for video_link in self.pk.select('.Box-sc-1z9git-0.fyQmaI iframe')]
            print('video.....', video)
        except (NoSuchElementException, TypeError, IndexError, AttributeError, Exception) as e:
            print(f"video..... An error occurred: {e}")
            video = []
            print('video.....', video)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = [href_link.get('href') for href_link in self.pk.select(".compatible-product__content a")]
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except (NoSuchElementException, IndexError, TypeError, AttributeError, Exception) as e:
            print(f"realated..... An error occurred: {e}")
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # ------------------------------------------------ Miscellaneous -----------------------------------------------
        try:
            Workpiece_Materials = [alfa.get_text(strip=True, separator=">>>").split(">>>") for alfa in self.pk.select('.product-work-piece.aem-GridColumn.aem-GridColumn--default--6 .material')]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            Workpiece_Materials = ''
            print(f"Brands.....An error occurred: {e}\t{Workpiece_Materials}")

        try:
            Uses_and_application = [logo.get('src') for logo in self.pk.select('.component-content .icon-list li img')]
        except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
            Uses_and_application = ''
            print(f"Brands.....An error occurred: {e}\t{Uses_and_application}")





        miscellaneous = {"Workpiece_Materials": Workpiece_Materials, "Uses_and_application": Uses_and_application}
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



# scaper_name = WebScraper('https://www.widia.com/us/en/products/p.varimill-4x47-4x48-4-flute-metric.6071113.html')
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
    file_path = "D:/Web-Scrapping/A-MONTH-2024/May/Supplyhouse-Brand-Johnson-control/url/Product-url - Copy.csv"
    url_links = pd.read_csv(file_path)['URL']
    Product_url = []
    start_url = 0
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).Product_Details(), url_1)
            print('------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")



# if __name__ == "__main__":
#     main()
