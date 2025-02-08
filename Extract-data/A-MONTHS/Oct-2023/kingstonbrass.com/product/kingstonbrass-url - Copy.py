import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import numpy as np


sess = requests.Session()

header = {
    "accept-language": "en-US,en;q=0.9,pl;q=0.8",
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}


base_url = 'https://www.kingstonbrass.com/'

product_urls = [
    # "https://www.kingstonbrass.com/sitemap_products_1.xml?from=6840484397098&to=6841226330154",
    # "https://www.kingstonbrass.com/sitemap_products_2.xml?from=6841226428458&to=6841367068714",
    # "https://www.kingstonbrass.com/sitemap_products_3.xml?from=6841367101482&to=6841470124074",
    # "https://www.kingstonbrass.com/sitemap_products_4.xml?from=6841470156842&to=6841790890026",
    # "https://www.kingstonbrass.com/sitemap_products_5.xml?from=6841790922794&to=6841910591530",
    # "https://www.kingstonbrass.com/sitemap_products_6.xml?from=6841910657066&to=6842121977898",
    # "https://www.kingstonbrass.com/sitemap_products_7.xml?from=6842122010666&to=6849392803882",
    # "https://www.kingstonbrass.com/sitemap_products_8.xml?from=6849392902186&to=6849568931882",
    # "https://www.kingstonbrass.com/sitemap_products_9.xml?from=6849569030186&to=6849727692842",
    # "https://www.kingstonbrass.com/sitemap_products_10.xml?from=6849727758378&to=6891662377002",
    # "https://www.kingstonbrass.com/sitemap_products_11.xml?from=6891662409770&to=6967870390314",

    "https://www.kingstonbrass.com/en-ca/sitemap_products_1.xml?from=6840484397098&to=6841226330154",
    "https://www.kingstonbrass.com/en-ca/sitemap_products_2.xml?from=6841226428458&to=6841367068714",
    "https://www.kingstonbrass.com/en-ca/sitemap_products_3.xml?from=6841367101482&to=6841470124074",
    "https://www.kingstonbrass.com/en-ca/sitemap_products_4.xml?from=6841470156842&to=6841790890026",
    "https://www.kingstonbrass.com/en-ca/sitemap_products_5.xml?from=6841790922794&to=6841910591530",
    "https://www.kingstonbrass.com/en-ca/sitemap_products_6.xml?from=6841910657066&to=6842121977898",
    "https://www.kingstonbrass.com/en-ca/sitemap_products_7.xml?from=6842122010666&to=6849392803882",
    "https://www.kingstonbrass.com/en-ca/sitemap_products_8.xml?from=6849392902186&to=6849568931882",
    "https://www.kingstonbrass.com/en-ca/sitemap_products_9.xml?from=6849569030186&to=6849727692842",
    "https://www.kingstonbrass.com/en-ca/sitemap_products_10.xml?from=6849727758378&to=6891662377002",



]

product_url_file = open('kingstonbrass.csv', 'a', encoding='utf-8')
pro_url = []


def urljoin_func(url):
    """function takes a relative url and convert it into absolute url and returns"""
    return urljoin(base_url, url)


def request_func(url):
    """Send Requests and Get Response from webpage and return Soup"""
    res = sess.get(url, headers=header)
    soup = BeautifulSoup(res.content, features='xml')
    return soup


def product_link(url):
    """find all the product links and save as csv file"""
    soup = request_func(url)
    product_links = soup.findAll("loc")
    save = open('kingstonbrass.txt', 'a+', encoding='utf-8')
    for link in product_links:
        absolute_url = urljoin_func(link.text)
        save.write("\n" + url + "\t" + absolute_url)
    print('save data into files')


for i, urls in enumerate(product_urls[:]):
    print(i, ">>>>>>>>>>>>>Working Url >>>>>>>>>>>>>", urls)
    product_link(urls)
    # df = pd.DataFrame(product_urls)
    # df.to_csv(product_url_file, lineterminator='\n', header=False, index=False)

# df = pd.DataFrame(product_urls)
# df.to_csv(product_url_file, lineterminator='\n', header=False, index=False)