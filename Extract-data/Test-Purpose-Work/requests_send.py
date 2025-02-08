import requests
from bs4 import BeautifulSoup

ress = requests.Session()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

mylist = [
    'https://www.widia.com/us/en/products/fam.series-sf-round-nose-tree-aluminum-cut-burs-inch.100074259.html',
]
for url in mylist:
    res_s = ress.get(url, headers=headers)
    soup = BeautifulSoup(res_s.content, "lxml")
    try:
        for product_cate in soup.select(".product-code a"):
            product_url = product_cate.get_attribute("href")
            print(product_url)
            with open('product_link_widia1.txt', 'a+', encoding='utf-8') as file_save:
                file_save.write(f"{product_url}\n")
    except AttributeError:
        print("Not Found")
