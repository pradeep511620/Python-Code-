import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define constants
SAVE_FILE_PATH = "D:/Web-Scrapping/A-MONTH-2024/May/Trico-oilers.com/data/Trico-oilers.csv"
BASE_URL = 'https://megadepot.com'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.driver = None
        self.soup = None

    def get_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument('--headless')
        chrome_options.add_argument(f'user-agent={HEADERS["User-Agent"]}')
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def send_driver_and_soup(self):
        self.driver = self.get_driver()
        try:
            self.driver.get(self.url)
            time.sleep(3)
            page_source = self.driver.page_source
            self.soup = BeautifulSoup(page_source, 'lxml')
        finally:
            self.driver.quit()
            self.driver = None

        return self.soup

    def send_driver_only(self):
        self.driver = self.get_driver()
        try:
            self.driver.get(self.url)
            time.sleep(2)
            return self.driver
        except Exception as e:
            self.driver.quit()
            self.driver = None
            raise e

    def send_soup_only(self):
        sess = requests.Session()
        res = sess.get(self.url, headers=HEADERS)
        self.soup = BeautifulSoup(res.content, "lxml")
        return self.soup


# Usage example
if __name__ == "__main__":
    url = 'https://www.gordonelectricsupply.com/p/S-Strut-Sec-A-Channel-End-Cap/5999584?ID=/ABB-Inc-Thomas-Betts/T-B-Superstrut/mfr-1IC5'
    scraper = WebScraper(url)

    # Get only driver
    try:
        driver = scraper.send_driver_only()
        print(driver)
    finally:
        if scraper.driver:
            scraper.driver.close()

    # Get only soup
    # soup = scraper.send_soup_only()
    # print(soup)

    # Get both driver and soup
    soup = scraper.send_driver_and_soup()
    print(soup)
