import requests
from bs4 import BeautifulSoup
import pandas as pd

url_list = [
    'https://dealerselectric.com/custompages/sitemaps/sitemap_products.xml',

]

def SiteMapUrl():
    start_url = 0
    for url_count, url in enumerate(url_list[start_url:1], start=start_url):
        product_urls = []
        session_store = requests.Session()
        url_store = session_store.get(url)
        print(url_store, url_count)

        soup = BeautifulSoup(url_store.content, 'lxml-xml')
        url_tags = soup.find_all('loc')

        urls = [url.text for url in url_tags]
        # print(urls)

        for product_url in urls:
            if 'asp' in product_url:
                product_urls.append(product_url)
                print(product_url)

        df = pd.DataFrame(product_urls, columns=['URL'])
        df.to_csv('dealer.csv', index=False)

    print("Data saved to dealer.csv")



SiteMapUrl()
