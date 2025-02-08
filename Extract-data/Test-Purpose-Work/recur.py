from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
base_urls = 'https://www.arrowpneumatics.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


def scrape_urls_recursive(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Successfully fetched URL-----: {url} with status code-----: {response.status_code}")
        soup = BeautifulSoup(response.content, 'html.parser')
        sub_urls = []

        # Extract URLs from the current page and append to urls list

        for url_href in soup.select(".product-archive-wrap ul li a"):
            print(url_href)
            for link in url_href.find_all('a', href=True):
                product_url = urljoin(base_urls, link['href'])
                print(product_url)
                sub_urls.append(product_url)
                # with open('scraped_urlssss.txt', 'a+', encoding='utf-8') as file_save:
                #     file_save.write(f"{product_url}\n


        # Recursive call for each extracted URL
        for new_url in sub_urls:
            scrape_urls_recursive(new_url)


    else:
        print(f"Failed to fetch URL: {url} with status code: {response.status_code}")


start_url = 'https://www.saginawcontrol.com/product_lines/?lines=759'
scrape_urls_recursive(start_url)


