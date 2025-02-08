from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.grainger.com/category/motors/'
url = "https://www.grainger.com/category/motors/ac-motors/pump-ac-motors/pool-spa-pump-ac-motors"

header = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

data = {
    "categoryIndex": 1
}


def extract_urls_recursive(url, visited=None):
    """
    Extracts all URLs from a webpage and any pages it links to, recursively.
    :param url: the URL of the starting page
    :param visited: a set of URLs that have already been visited
    :return: a set of all unique URLs found on the pages
    """
    if visited is None:
        visited = set()
    urls = set()
    try:
        response = requests.post(url, headers=header, data=data)
        if response.status_code == 200:
            # print(response.content)
            soup = BeautifulSoup(response.content, "html.parser")
            print(soup)
            product_links = soup.findAll(class_="cjpIYY")
            print(product_links)
            for link in product_links:
                next_url = urljoin(base_url, link.find('a')['href'])
                print(next_url)
                # if next_url not in visited:
                #     visited.add(next_url)
                #     urls.add(next_url)
                #     urls = urls.union(extract_urls_recursive(next_url, visited))
    except Exception as e:
        print(e)
    return urls


extract_urls_recursive(url)