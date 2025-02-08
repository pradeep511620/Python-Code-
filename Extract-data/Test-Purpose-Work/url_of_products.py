import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import concurrent.futures
from bs4 import BeautifulSoup
from urllib.parse import urljoin


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
base_url = "https://www.widia.com/"

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.pk = self.SendDriverOnly()

    def SendDriverOnly(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(6)
        page_sources = driver.page_source
        driver.quit()
        pk = BeautifulSoup(page_sources, 'lxml')

        return pk


    def ProductUrl(self):
        product_urls = []
        print('Product_url', self.url)

        # try:
        #     self.pk.find_element(By.CSS_SELECTOR, ".dp-bar-actions .cc-compliance").click()
        #     time.sleep(2)
        # except NoSuchElementException:
        #     print("click not found")
        # try:
        #     option = self.pk.find_elements(By.CSS_SELECTOR, ".product-row-availability select option")
        #     [opn.click() for opn in option if opn.text.strip() == "All"]
        #     time.sleep(5)
        # except (NoSuchElementException, AttributeError, TypeError, IndexError, Exception) as e:
        #     print(f"product_title..... An error occurred: {e}")
        # print(self.pk.current_url)
        try:
            for product_cate in self.pk.select("td.product-code a"):
                product_url = urljoin(base_url, product_cate.get('href'))
                product_urls.append(product_url)
                print(product_url)

        except NoSuchElementException:
            print("Not Found")
        except Exception as e:
            print(f"An error occurred: {e}")

        df = pd.DataFrame(product_urls, columns=['URL'])
        df.to_csv('widia_url.csv', mode='a', header=not pd.io.common.file_exists('widia_url.csv'), index=False)

def main():
    file_path = r"P:\Web-scrapings\A-MONTH-2024\Aug\Widia.com\url\Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    Product_url = []
    start_url = 500
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        try:
            executor.map(lambda url_link: WebScraper(url_link).ProductUrl(), url_1)
            print(
                '------------------------------------ Thread Running -----------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()



