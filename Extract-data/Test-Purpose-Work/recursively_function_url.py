import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



base_urls = 'https://www.widia.com/us/en'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


def scrape_urls_recursive(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser')
        urls = []
        # Extract URLs from the current page here and append to urls list
        for url_href in soup.find_all('div', class_='category-tile-wrapper'):
            for urls in url_href.find_all('a'):
                product_url = urljoin(base_urls, urls['href'])
                print(product_url)
                urls.append(product_url)



        # Recursive call for each extracted URL
        for url in urls:
            scrape_urls_recursive(url)
    else:
        print(f"Failed to fetch URL: {url}")


start_url = 'https://www.widia.com/us/en/products.html'
scrape_urls_recursive(start_url)

