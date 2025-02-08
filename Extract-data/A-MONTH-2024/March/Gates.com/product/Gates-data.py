from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import concurrent.futures
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Gates.com/data/Gates.csv", 'a+',
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
        print()
        try:
            try:
                self.driver.find_element(By.XPATH, "//*[@title='Accept Cookies']").click()
            except (ElementClickInterceptedException, NoSuchElementException):
                print('No cookies accept button found')

            l3_name = ''

            # --------------------------------------------------------------------------------------------------------------
            try:
                l3_name = []
                for bread in self.driver.find_elements(By.XPATH, "//ol[@class='breadcrumbs']//li"):
                    l3 = bread.text.strip()
                    l3_name.append(l3)
                l3_Name = "## ".join(l3_name)
                print('l3_name.....', l3_Name)
            except NoSuchElementException:
                l3_Name = 'N/A'
                print('l3_name.....', l3_Name)

            # --------------------------------------------------------------------------------------------------------------
            try:
                product_title = self.driver.find_element(By.XPATH, "//*[@class='product__title']").text.strip()
                print('product_title.....', product_title)
            except:
                product_title = ''
                print('product_title.....', product_title)

            # --------------------------------------------------------------------------------------------------------------
            try:
                part_number = self.driver.find_element(By.XPATH, "//*[@class='product__number']").text.strip().split("# ")[1]
                mpn = part_number
                print('mpn.....', mpn)
            except NoSuchElementException:
                mpn = 'N/A'
                print('mpn.....', mpn)
            # --------------------------------------------------------------------------------------------------------------
            try:
                description_1 = []
                for des in self.driver.find_elements(By.XPATH, "//div[@class='product__description']//p"):
                    texts = des.text.strip()
                    if texts:
                        description_1.append({"desc": [texts]})
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
                for tem in self.driver.find_elements(By.CLASS_NAME, "s7thumb"):
                    images_html = tem.get_attribute('style').split('("')[1].replace('");', "")
                    if images_html:
                        image_src = images_html
                        alt_tag = 'N/A'
                        image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                        images.append(image_tag_and_alt_tag)
                print('images.....', images)
            except NoSuchElementException:
                images = ''
                print('images.....', images)

            # --------------------------------------------------------------------------------------------------------------
            try:
                datasheet = [pdf.get_attribute('href') for pdf in self.driver.find_elements(By.XPATH, "//div[@class='product-selected__resources']//a")]
                print('datasheet:', datasheet)
            except NoSuchElementException:
                datasheet = []
                print('datasheet: N/A')

            # --------------------------------------------------------------------------------------------------------------
            for options in self.driver.find_elements(By.XPATH, "//div[@id='product-tabs']//li"):
                option_text = options.text.strip()
                if "CONSTRUCTION" in option_text:
                    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                        (By.XPATH, "(//a[@role='tab'][normalize-space()='Construction'])[1]")))
                    if element:
                        element.click()
                elif "NOTES" in option_text:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Notes']")))
                    if element:
                        element.click()
                elif "PACKAGING DETAILS" in option_text:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Packaging details']")))
                    if element:
                        element.click()
                # Adjust sleep time or remove it as needed
                time.sleep(2)

            try:
                attr_name = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//div[@id='product-tabs']//table//th")]
                attr_value = [th.text.strip() for th in self.driver.find_elements(By.XPATH, "//div[@id='product-tabs']//table//td")]
                specifications_1 = [{name: value} for name, value in zip(attr_name, attr_value)]
                print('specifications_1:', specifications_1)
            except NoSuchElementException:
                specifications_1 = []
                print('specifications_1: N/A')

            list_column = [
                "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
                "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
                "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
                "scraped_by"
            ]
            raw_data = [{
                "brand": "GATES", "catlvl1": "", "catlvl2": "", "catlvl3": "", "url": self.url,
                "title": product_title, "price_value": 'N/A', "unit": "USD", "shipping_weight": 'N/A',
                "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
                "specification_1": specifications_1, "specification_2": [], "datasheets": datasheet,
                "product_description_1": description_1, "product_description_2": description_2,
                "accessories": [{'accessories': []}], "video_links": [], "miscellaneous": 'miscellaneous',
                "scraped_by": "Pradeep Kumar",
            }]

            print('Complete all Your Program')
            print()
            if l3_name:
                for p in range(1, min(len(l3_name), 4)):
                    raw_data[0][f"catlvl{p}"] = l3_name[p]
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
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Gates.com/url/Product-url.csv"
    url_list = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_list))
    i = 0
    for url_count, url in enumerate(url_list[i:5000], start=i):
        product_url.append(url)
        # CREATING AN OBJECTS FOR CLASS WebScraper
        # scraper_name = WebScraper(url)
        # scraper_name.Product_details()

    # print(urls)
    return product_url


# Example usage:
def main():
    urls = ReadFromListUrl()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        try:
            executor.map(lambda url: WebScraper(url).Product_details(), urls)
            print('*******************************************************************************************************')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")

if __name__ == "__main__":
    main()
