import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# base_url = 'https://www.grainger.com/category?analytics=nav'
base_url = 'https://www.grainger.com/category/motors?categoryIndex=17'

data = {
    "categoryIndex": 17
}

header = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


def extract_urls_recursive(url, visited=None):
    """
    Extracts all URLs from a webpage and any pages it links to, recursively.
    :param url: the URL of the starting page
    :param visited: a set of URLs that have already been visited
    :return: a set of all unique URLs found on the pages
    """

    # print(url)
    if visited is None:
        visited = set()
    urls = set()

    try:
        response = requests.post(url, data=data, headers=header)
        print(response.text)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml")
            product_links = soup.findAll(class_="_3dXDpA")
            for link in product_links:
                next_url = urljoin(base_url, link.find('a')['href'])
                print(next_url)
                if next_url not in visited:
                        visited.add(next_url)
                        urls.add(next_url)
                        urls = urls.union(extract_urls_recursive(next_url, visited))
    except Exception as e:
        print(e)
    return urls


def tt(url):
    res = requests.get(url, data=data)
    print(res)


# tt(base_url)
urlss = extract_urls_recursive(base_url)
print(urlss)
df = pd.DataFrame(urlss)
df.to_csv("urls.csv")


