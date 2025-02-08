from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import concurrent.futures
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Gates acorn-ind.co.uk/data/Gates.csv", 'a+',
                  encoding='utf-8')

product_url = []


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.driver = self.get_driver()

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(3)
        return driver

    def Product_details(self):
        print("Running....", self.url)
        mpn = ''
        l3_Name = ''
        try:
            try:
                self.driver.find_element(By.XPATH, "//*[@title='Accept Cookies']").click()
            except (ElementClickInterceptedException, NoSuchElementException):
                print('No cookies accept button found')

            # --------------------------------------------------------------------------------------------------------------
            try:
                for bread in self.driver.find_elements(By.XPATH, "//div[@class='breadcrumbs mod-overlay mod-insideblock']//nav"):
                    l3 = bread.text.strip().replace("Where you are:>>", "").replace('\n', ">>").split(">>>>>")
                    l3_Name = "## ".join(l3)
                    print('l3_name.....', l3_Name)
            except NoSuchElementException:
                l3_Name = 'N/A'
                print('l3_name.....', l3_Name)

            # --------------------------------------------------------------------------------------------------------------
            try:
                product_title = self.driver.find_element(By.XPATH, "//div[@class='ec-product']//h1").text.strip()
                print('product_title.....', product_title)
            except:
                product_title = ''
                print('product_title.....', product_title)

            # --------------------------------------------------------------------------------------------------------------
            try:
                for more in self.driver.find_elements(By.XPATH, "(//table[@class='ec-meta'])[1]"):
                    if "MFR PART NO." in more.text.strip():
                        part_details = more.find_element(By.XPATH, "(//div[@class='ec-product-summary']//tbody//tr)[2]//td").text.strip()
                        mpn = part_details
                        print('mpn.....', mpn)
            except NoSuchElementException:
                mpn = 'N/A'
                print('mpn.....', mpn)

            # --------------------------------------------------------------------------------------------------------------
            try:
                price_details = self.driver.find_element(By.XPATH, "//div[@class='ec-product-actions-price']//p").text.strip()
                price = {"List_price": price_details}
                print('price.....', price)
            except NoSuchElementException:
                price = {'List_price': '$-.--'}
                print('price.....', price)
            # --------------------------------------------------------------------------------------------------------------
            short_desc = ''
            description_1 = ''
            try:
                short_desc = self.driver.find_element(By.XPATH, "//div[@class='ec-product']//p").text.strip()
            except NoSuchElementException:
                print('Not')

            try:
                texts_list = [des.text.strip().replace('\n', "','") for des in self.driver.find_elements(By.XPATH, "//div[@class='u-pt-sm']//p")]
                if texts_list:
                    description_1 = {"desc": texts_list, 'short-desc': short_desc}
                print('description_1.....', description_1)
            except NoSuchElementException:
                description_1 = {"desc": []}
                print('description_1.....', description_1)

            # --------------------------------------------------------------------------------------------------------------
            try:
                description_2 = []
                for des_1 in self.driver.find_elements(By.XPATH, "//ul[@class='red-bullets']//li"):
                    text_1 = des_1.text.strip()
                    if text_1:
                        description_2.append(text_1)
                print('description_2.....', description_2)
            except NoSuchElementException:
                description_2 = []
                print('description_2.....', description_2)
            # --------------------------------------------------------------------------------------------------------------
            try:
                images = []
                for images_html in self.driver.find_elements(By.XPATH, "//div[@class='ec-imageViewer']//img"):
                    if images_html:
                        image_src = images_html.get_attribute('src')
                        alt_tag = images_html.get_attribute('alt')
                        image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                        images.append(image_tag_and_alt_tag)
                print('images.....', images)
            except NoSuchElementException:
                images = ''
                print('images.....', images)

            # --------------------------------------------------------------------------------------------------------------
            try:
                datasheet = [pdf.get_attribute('href') for pdf in self.driver.find_elements(By.XPATH, "//a[@class='submenu-link mod-doc']")]
                print('datasheet:', datasheet)
            except NoSuchElementException:
                datasheet = []
                print('datasheet: N/A')

            # ----------------------------------------------------------------------------------------------------------
            try:
                related_url = [related_href.get_attribute('href') for related_href in self.driver.find_elements(By.XPATH, "//article[@class='ec-result']//a")]
                related = [{'accessories': related_url}]
                print("related_url.....", related)
            except NoSuchElementException:
                related = [{'accessories': []}]
                print("related_url.....", related)

            # ----------------------------------------------------------------------------------------------------------
            try:
                attr_name_1 = [th_1.text.strip() for th_1 in self.driver.find_elements(By.XPATH, "//div[@class='ec-product-summary']//table//th")]
                attr_value_1 = [td_1.text.strip() for td_1 in self.driver.find_elements(By.XPATH, "//div[@class='ec-product-summary']//table//td")]
                specs_1 = [{name_1: value_1} for name_1, value_1 in zip(attr_name_1, attr_value_1)]
                # print('specs.....', specs_1)
            except NoSuchElementException:
                specs_1 = []
                print('specs.....', specs_1)

            try:
                attr_name = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//table[@class='plain']//tbody//th")]
                attr_value = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//table[@class='plain']//tbody//td")]
                specs_2 = [{name: value} for name, value in zip(attr_name, attr_value)]
                # print('specifications_1:', specs_2)
            except NoSuchElementException:
                specs_2 = []
                print('specifications_1: N/A')

            specifications_1 = str(specs_1) + "," + str(specs_2)
            print(specifications_1)

            list_column = [
                "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
                "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
                "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
                "scraped_by"
            ]
            raw_data = [{
                "brand": "GATES", "catlvl1": "", "catlvl2": "", "catlvl3": "", "url": self.url,
                "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": 'N/A',
                "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
                "specification_1": specifications_1, "specification_2": [], "datasheets": datasheet,
                "product_description_1": description_1, "product_description_2": description_2,
                "accessories": related, "video_links": [], "miscellaneous": 'miscellaneous',
                "scraped_by": "Pradeep Kumar",
            }]

            print('Complete all Your Program')
            print()
            if l3_Name:
                categories = l3_Name.split("## ")
                for p in range(1, min(len(categories), 4)):
                    # print(categories[p])
                    raw_data[0][f"catlvl{p}"] = categories[p]

            # if l3_Name:
            #     for p in range(1, min(len(l3_Name.split("## ")), 4)):
            #         print(l3_Name)
            #         raw_data[0][f"catlvl{p}"] = l3_Name[p]
            Data_Save(raw_data, list_column)
            self.driver.quit()
        except Exception as e:
            print(f"Error...{e}")
            with open('remain.txt', 'a+', encoding='utf-8') as file_s:
                file_s.write(f"{self.url}\n")


# class SaveFunction():
def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def ReadFromListUrl():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Gates acorn-ind.co.uk/url/Product-url.csv"
    url_list = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_list))
    i = 12648
    for url_count, url in enumerate(url_list[i:], start=i):
        product_url.append(url)
        # CREATING AN OBJECTS FOR CLASS WebScraper
        # scraper_name = WebScraper(url)
        # scraper_name.Product_details()

    # print(urls)
    return product_url


# Example usage:
def main():
    urls = ReadFromListUrl()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        try:
            executor.map(lambda url: WebScraper(url).Product_details(), urls)
            print('*******************************************************************************************************')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")

if __name__ == "__main__":
    main()
