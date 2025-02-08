import os
import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def Get_Driver_Urls(product_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(2)
    return driver


def DownloadImages(driver, folder_path):
    try:
        img = []
        images = driver.find_elements(By.TAG_NAME, 'img')
        image_urls = [img.get_attribute('src') for img in images]
        for url_1 in image_urls:
            if url_1 is not None and any(ext in url_1.lower() for ext in [".jpg", ".svg", ".webp", ".png", ".gif"]):
                img.append(url_1)
    except AttributeError:
        print('href tag......')
        img = []
        images = driver.find_elements(By.TAG_NAME, 'a')
        image_urls = [img.get_attribute('href') for img in images]
        for url_1 in image_urls:
            if url_1 is not None and any(ext in url_1.lower() for ext in [".jpg", ".svg", ".webp", ".png", ".gif"]):
                img.append(url_1)



    for data in img:
        print(data)
        save = open("images.csv", "a+", encoding="utf-8")
        save.write(f"{data}\n")


    os.makedirs(folder_path, exist_ok=True)

    for images_name, data in enumerate(img):
        response = requests.get(data)
        if response.status_code == 200:
            image_name = str(data).replace('/', 'tick').replace('\\', 'tick').split("tick")[-1].split(".")[0]
            file_name = f"{image_name}.png"
            file_path = os.path.join(folder_path, file_name)
            try:
                os.makedirs(folder_path, exist_ok=True)
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"Image downloaded: {file_name}")
            except OSError as e:
                print(f"Error downloading image: {e}")
        else:
            print(f"Failed to download image: {data}")





def ReadUrlFromFileToCompare():
    compare_product_url = []
    try:
        compare_url = pd.read_csv('Already-Scrape-Url.csv')['URL']
        for compare_urls in compare_url:
            compare_product_url.append(compare_urls.strip())
    except FileNotFoundError:
        print('File not found for comparison')
    return compare_product_url


class ReadUrl:

    def __init__(self):
        pass



    def UsingList(self):
        url_list = [
            "https://www.functionize.com/blog/are-your-engineers-testing-think-again",
            "https://www.functionize.com/blog/ai-augmented-testing",
            "https://www.functionize.com/blog/welcome-to-the-party-bizdevops",
            "https://www.functionize.com/blog/democratizing-automated-testing-in-a-down-economy",
            "https://www.functionize.com/blog/big-data-potential-for-small-and-medium-businesses",
        ]
        compare_product_url = ReadUrlFromFileToCompare()

        for product_url in url_list:
            print("product url:--", product_url)

            if product_url in compare_product_url:
                print(f"URL {product_url} already processed.")
                continue

            driver = Get_Driver_Urls(product_url)
            DownloadImages(driver, 'image_folder')
            driver.quit()

            last_product_url = product_url
            file_path = 'already-scrape-url.csv'
            header = 'URL'
            file_exists = os.path.exists(file_path)
            with open(file_path, 'a', newline='', encoding='utf-8') as save:
                if not file_exists:
                    save.write(f"{header}\n")
                save.write(f"{last_product_url}\n")
        print('Saved Url')


    def ReadCsvUsingPandas(self):

        compare_product_url = ReadUrlFromFileToCompare()

        file_path = 'Book.csv'
        if os.path.exists(file_path):
            url_link = pd.read_csv(file_path)['URL']
            for url_count, product_url in enumerate(url_link, start=1):
                print("Url-No...", url_count)
                print("product url:--", product_url)

                if product_url in compare_product_url:
                    print(f"URL {product_url} already processed.")
                    continue

                driver = Get_Driver_Urls(product_url)
                DownloadImages(driver, 'image_folder')
                driver.quit()

                last_product_url = product_url
                already_scraped_path = 'already-scrape-url.csv'
                header = 'URL'
                file_exists = os.path.exists(already_scraped_path)
                with open(already_scraped_path, 'a', newline='', encoding='utf-8') as save:
                    if not file_exists:
                        save.write(f"{header}\n")
                    save.write(f"{last_product_url}\n")
            print('Saved Url')


    def GoogleShareDrive(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/PK/Downloads/credentials.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1jTgsmpuqeKTeaikevOlfPo6w_9M0eE7uD4zhzg56rEI/edit#gid=0').sheet1
        url_link = sheet.col_values(1)  # Fetching all values from the first column
        compare_product_url = ReadUrlFromFileToCompare()

        for url_count, product_url_3 in enumerate(url_link, start=1):
            print("Url-No...", url_count)
            print("Product-Urls......", product_url_3)

            if product_url_3 in compare_product_url:
                print(f"URL {product_url_3} already processed.")
                continue

            driver = Get_Driver_Urls(product_url_3)
            DownloadImages(driver, 'image_folder')
            driver.quit()

            last_product_url = product_url_3
            already_scraped_path = 'already-scrape-url.csv'
            header = 'URL'
            file_exists = os.path.exists(already_scraped_path)
            with open(already_scraped_path, 'a', newline='', encoding='utf-8') as save:
                if not file_exists:
                    save.write(f"{header}\n")
                save.write(f"{last_product_url}\n")
        print('Saved Url')


def main():

    URL = ReadUrl()

    URL.UsingList()
    URL.GoogleShareDrive()
    URL.GoogleShareDrive()


if __name__ == '__main__':
    main()
