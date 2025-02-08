import time
import os

import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



def Get_Driver_Urls(product_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(2)
    return driver




def DownloadImages(driver):
    img = []
    images = driver.find_elements(By.TAG_NAME, 'img')
    image_urls = [img.get_attribute('src') for img in images]
    for url_1 in image_urls:
        if any(ext in url_1.lower() for ext in [".jpg", ".svg", ".webp", ".png", ".gif"]):
            img.append(url_1)
    for data in img:
        print(data)


def ReadUrlFromFile():
    compare_url_1 = []
    compare_url = pd.read_csv("lasturl.csv")['URL']
    for compare_urls in compare_url:
        compare_url_1.append(compare_urls.strip())
    return compare_url_1



class RunFunctions:

    def UsingList(self):
        url_link = [
            "https://stage.raptorsupplies.com/c/electrical-gloves",
            "https://www.functionize.com/blog/big-data-potential-for-small-and-medium-businesses",
            "https://www.functionize.com/blog/welcome-to-the-party-bizdevops",
            "https://stage.raptorsupplies.com/c/adjustable-frequency-drive-accessories",
            "https://www.functionize.com/blog/democratizing-automated-testing-in-a-down-economy",

        ]

        try:
            compare_url_1 = ReadUrlFromFile()
            # last_product_url = ''
        except FileNotFoundError:
            compare_url_1 = ''
            print('file not found')

        for product_url in url_link:
            print("product url:--", product_url)

            if product_url in compare_url_1:
                print(f"URL {product_url} already processed.")
                continue

            driver = Get_Driver_Urls(product_url)
            DownloadImages(driver)
            driver.quit()

            last_product_url = product_url
            file_path = 'lasturl.csv'
            header = 'URL'
            file_exists = os.path.exists(file_path)
            with open(file_path, 'a', newline='', encoding='utf-8') as save:
                if not file_exists:
                    save.write(f"{header}\n")
                save.write(f"{last_product_url}\n")
        print('Saved the last URL')



def main():
    run = RunFunctions()
    run.UsingList()
    ReadUrlFromFile()



if __name__ == '__main__':
    main()



#
# def ReadUrlFromFile():
#     try:
#         compare_url = pd.read_csv("lasturl.csv")['URL']
#         return list(compare_url)
#     except pd.errors.EmptyDataError:
#         print("The file 'lasturl.csv' is empty or doesn't have columns.")
#         return []
#
#
# class RunFunctions:
#     @staticmethod
#     def UsingList():
#         url_link = [
#             "https://stage.raptorsupplies.com/c/electrical-gloves",
#             "https://www.functionize.com/blog/big-data-potential-for-small-and-medium-businesses",
#             "https://www.functionize.com/blog/welcome-to-the-party-bizdevops",
#             "https://stage.raptorsupplies.com/c/adjustable-frequency-drive-accessories",
#             "https://www.functionize.com/blog/democratizing-automated-testing-in-a-down-economy",
#         ]
#
#         compare_url = ReadUrlFromFile()
#         last_processed_index = -1
#
#         for index, product_url in enumerate(url_link):
#             print("product url:--", product_url)
#
#             if product_url in compare_url:
#                 last_processed_index = compare_url.index(product_url)
#                 print(f"Resuming processing from {product_url}")
#                 continue
#
#             if index > last_processed_index:
#                 driver = Get_Driver_Urls(product_url)
#                 DownloadImages(driver)
#                 driver.quit()
#
#                 last_processed_index = index
#
#
#             with open('lasturl.csv', 'w', encoding='utf-8') as save:
#                 for url in url_link[last_processed_index + 1:]:
#                     save.write(f"{url}\n")
#
#             print('save last url')

