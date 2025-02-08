import requests
from bs4 import BeautifulSoup
from typing import TextIO
import pandas as pd
import threading
import time

file_lock = threading.Lock()


def main_multi(url):
    count = 40
    for row in url[count:]:
        count += 1
        print("url :", count, " ", row)
        Url41 = row
        try:
            proxy_url = f"https://spo3cndgqr:A7lgg1Uesqms3XvyQ9@gate.smartproxy.com:7000"

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 "
                              "GTB7.1 (.NET CLR 3.5.30729)", "Referer": "http://example.com"}

            proxies = {
                "http": proxy_url,
                "https": proxy_url,
            }

            result = requests.get(Url41, proxies=proxies, headers=headers)
            soup = BeautifulSoup(result.content, 'html.parser')

            image_tags = soup.find(class_='vJXKUW').find_all('img')

            image_urls = []

            for img in image_tags:
                img_url = img.get('src')
                if img_url:
                    image_urls.append(img_url)
            # print(image_urls)
            with file_lock:
                save_details: TextIO = open("01_image.txt", "a+", encoding="utf-8")
                save_details.write('\n' + Url41 + "\t" + ','.join(image_urls))
                save_details.close()
        except:
            print("\n**End.**")


def multi_threads():
    product_urls = pd.read_excel('grainger_url_for_image_rem.xlsx')['URLS']
    urls = []

    # Append url in list
    for url in product_urls[75000:100000]:
        urls.append(url)

    # Define the number of threads
    num_threads = 10
    # Calculate the chunk size
    chunk_size = len(urls) // num_threads

    # Create and start threads
    threads = []
    for i in range(num_threads):
        # Calculate the start and end indices for the chunk
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(urls)

        # Get the chunk of URLs for the thread
        chunk_urls = urls[start:end]

        # Create and start the thread
        thread = threading.Thread(target=main_multi, args=(chunk_urls,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


multi_threads()
