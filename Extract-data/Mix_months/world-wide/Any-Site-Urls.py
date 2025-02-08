from urllib.parse import urljoin

# import pandas as pd
import requests
from bs4 import BeautifulSoup


base_url = 'https://worldwideelectric.com/products/'


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
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # print(soup)
            # try:
            product_links = soup.find(class_="product__grid").findAll(class_='product__image')
            # except AttributeError:
            #     product_links = soup.find(id="pg-w62a786bed04f5-1").findAll(class_='textwidget custom-html-widget')
            for link in product_links:
                next_url = urljoin(base_url, link.find('a')['href'])
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
                urls = urls.union(extract_urls_recursive(url+next_page_link))
            print('next_page_link')
        print('response')

    except Exception as e:
        print(e)
    return urls


product_urls = extract_urls_recursive(base_url)
print(product_urls)
print(len(product_urls))
# save = open('urls-world-wide1.csv', "a+", encoding="utf-8")
# df = pd.DataFrame(product_urls)
# df.to_csv(save, lineterminator='\n')
