
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.sprayon.com/products/page/1/'


def request_func(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup


def product_link(url):
    """find all the product links and save as csv file"""
    soup = request_func(url)
    product_links = soup.find('ul', class_="products columns-3").find_all('li')
    for link in product_links:
        # product_urls.append(link.find('a')['href'])
        product_urls = link.find('a')['href']
        print(product_urls)
        save = open('sprayon-url.csv', 'a+', encoding='utf-8')
        save.write('\n' + product_urls)


for i in range(1, 10):
    url = f'https://www.sprayon.com/products/page/{i}/'
    # print(url)
    product_link(url)
