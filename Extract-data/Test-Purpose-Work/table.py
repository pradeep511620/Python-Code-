import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# List of URLs

base_url = "https://www.widia.com/"

file_path = r"P:\Web-scrapings\A-MONTH-2024\Aug\Widia.com\url\Product-url.csv"
urls = pd.read_csv(file_path)['URL']

# urls = [
#    'https://www.widia.com/us/en/products.html'
# ]

product_urls = []
start_url = 0
for url_count, url in enumerate(urls[start_url:1], start=start_url):
    ress = requests.get(url)
    soup = BeautifulSoup(ress.content, 'lxml')
    print(f'product-urls----: , {url} url-count-no. {url_count}')

    product = soup.select("tbody tr td.product-code")
    print(product)
    # if product:
    #     for products in soup.select("td.product-code a"):
    #         product_url = urljoin(base_url, products.get('href'))
    #         if 'products' in product_url:
    #             product_urls.append(product_url)
    #             print(product_url)
    #         else:
    #             with open('remaining.txt', 'a+', encoding='utf-8') as file_save:
    #                 file_save.write(f'{url}')
    # else:
    #     print('no')



    # df = pd.DataFrame(product_urls, columns=['URL'])
    # df.to_csv('widia4.csv', mode='a', header=not pd.io.common.file_exists('widia4.csv'), index=False)

