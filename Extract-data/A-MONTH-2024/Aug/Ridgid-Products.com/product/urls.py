import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd



# mylist_url = ['https://www.ridgid.com/us/en/drain-cleaning-tools']

file_path = r"P:\Web-scrapings\A-MONTH-2024\Aug\Ridgid-Products.com\product\product_url_ridgid3.csv"
my_url_lists = pd.read_csv(file_path)['URL']

base_url = 'https://www.ridgid.com'



def extract_url():
    product_urls = []

    start_url = 3
    for index, url in enumerate(my_url_lists[start_url:], start=start_url):
        ress = requests.get(url)
        soup = BeautifulSoup(ress.content, "lxml")
        print('product_url.....', index, url)

        for href_tag in soup.select("ul.grid a[itemprop='url']"):
            product_url = urljoin(base_url, href_tag.get('href'))
            product_urls.append(product_url)
            print(product_url)

    df = pd.DataFrame(product_urls, columns=['URL'])
    df.to_csv('product_url_ridgid4.csv', mode='a', header=not pd.io.common.file_exists('product_url_ridgid.csv'),index=False)
    print('save data in dataframe')



extract_url()