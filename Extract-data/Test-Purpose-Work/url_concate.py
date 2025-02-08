import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import concurrent.futures


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


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
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        time.sleep(3)

        return driver


    def ProductUrl(self):
        print('Product_url', self.url)

        # try:
        #     self.pk.find_element(By.CSS_SELECTOR, "#onetrust-button-group .accept-btn-container").click()
        #     time.sleep(1)
        # except NoSuchElementException:
        #     print("click not found")


        try:
            for product_cate in self.pk.find_elements(By.CSS_SELECTOR, ".data a"):
                product_url = product_cate.get_attribute("href")
                print(product_url)
                with open('systems.csv', 'a+', encoding='utf-8') as file_save:
                    file_save.write(f"{product_url}\n")
        except NoSuchElementException:
            print("Not Found")
            with open('systenm.txt', 'a+', encoding='utf-8') as file_save:
                file_save.write(f"{self.url}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.pk.close()

def main():
    file_path = "D:/Web-Scrapping/Test-Purpose-Work/system.csv"
    url_links = pd.read_csv(file_path)['URL']
    Product_url = []
    start_url = 200
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
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



