from urllib.parse import urljoin
import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
base_url = 'https://www.grainger.com/'


def url_join_func(url):
    return urljoin(base_url, url)


def extract_urls_recursive(url, visited=None):
    """
    Extracts all URLs from a webpage and any pages it links to, recursively.
    param url: the URL of the starting page
    param visited: a set of URLs that have already been visited
    return: a set of all unique URLs found on the pages
    """
    if visited is None:
        visited = set()
    urls = set()
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            print(soup)

            try:
                product_links = soup.find_all('a', class_='route categories__link')
                print("......................", product_links)
                for links in product_links:
                    absolute_url = url_join_func(links.find('a')['href'])
                    print(absolute_url)
            except AttributeError:
                product_links = soup.find('li', class_="_3dXDpA l-hSkF").find_all("a")
            for link in product_links:
                next_url = urljoin(base_url, link['href'])
                if next_url not in visited:
                    visited.add(next_url)
                    urls.add(next_url)
                    print(next_url)
                    urls = urls.union(extract_urls_recursive(next_url, visited))
                print('url')
            print("Link")

            next_page_url = soup.find(class_="pager__item pager__item--next")
            if next_page_url is not None:
                next_page_link = next_page_url.find('a')['href']
                print(urljoin(base_url, next_page_link))
                urls = urls.union(extract_urls_recursive(url + next_page_link))
            print('next_page_link')
        print('response')

    except Exception as e:
        print(e)

    return urls


cat_url = 'https://www.grainger.com/category/brand/Ge/'

product_urls = extract_urls_recursive(cat_url)
print(product_urls)
print(len(product_urls))
save = open('spc industries.csv', "a+", encoding="utf-8")
df = pd.DataFrame(product_urls)
df.to_csv(save, lineterminator='\n')
