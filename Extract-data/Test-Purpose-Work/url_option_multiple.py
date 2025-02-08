import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


class UrlScraper:
    def __init__(self, url):
        self.url = url
        self.pk = self.SendDriverOnly()

    def SendDriverOnly(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(6)

        return driver

    def ProductUrl(self):
        print('Product_url', self.url)

        try:
            self.pk.find_element(By.CSS_SELECTOR, ".seeall_link.all_btnseeallproducts").click()
            time.sleep(3)
        except NoSuchElementException:
            print("click not found1")

        for i in range(1, 15):
            print('count...', i)
            while True:
                print('while')
                script = f'return document.querySelector("#PublicWrapper > main > section > div.search_maincontent > div:nth-child(4) > div.search_tabcontent.Products.search_active > div > pis-products-instance > pis-products-loading-indicator > pis-products-search-view > div > div.col-9.product_col_9 > pis-products-search-pagination").shadowRoot.querySelector("nav > div > ul > li:nth-child({i}) > a").click()'
                self.pk.execute_script(script)
                time.sleep(4)

                for url_tag in range(1, 24):
                    model = self.pk.execute_script(f'return document.querySelector("#PublicWrapper > main > section > div.search_maincontent > div:nth-child(4) > div.search_tabcontent.Products.search_active > div > pis-products-instance > pis-products-loading-indicator > pis-products-search-view > div > div.col-9.product_col_9 > pis-products-list-view > pis-products-search-list").shadowRoot.querySelector("div > div > div:nth-child({url_tag}) > div > div:nth-child(4) > a > strong")').text.strip()
                    model_number = self.pk.execute_script(f'return document.querySelector("#PublicWrapper > main > section > div.search_maincontent > div:nth-child(4) > div.search_tabcontent.Products.search_active > div > pis-products-instance > pis-products-loading-indicator > pis-products-search-view > div > div.col-9.product_col_9 > pis-products-list-view > pis-products-search-list").shadowRoot.querySelector("div > div > div:nth-child({url_tag}) > div > div:nth-child(4) > div.small.text-muted.fw-bold")').text.strip()
                    add_string = f"https://new.abb.com/products/{model}/{model_number}"
                    print(add_string)



url_scrape = UrlScraper('https://new.abb.com/search/en/results#query=Superstrut#lang=en')
url_scrape.ProductUrl()
