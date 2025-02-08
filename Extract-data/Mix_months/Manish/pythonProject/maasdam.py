import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = 'https://www.maasdam.com/products.html'

sess = requests.Session()

url_list = [
    'https://www.maasdam.com/144s-6.html',
    'https://www.maasdam.com/144sb-6.html',
    'https://www.maasdam.com/144c-6.html',
    'https://www.maasdam.com/264s-5.html',
    'https://www.maasdam.com/6000s.html',
    'https://www.maasdam.com/8000sb.html',
    # 'https://www.maasdam.com/cable-pullers.html',
    'https://www.maasdam.com/a-0.html',
    'https://www.maasdam.com/a-20.html',
    'https://www.maasdam.com/a-50.html',
    'https://www.maasdam.com/a-100.html',
    # 'https://www.maasdam.com/rope-pullers.html',
    'https://www.maasdam.com/ws-1.html',
    'https://www.maasdam.com/ws-2.html',
    'https://www.maasdam.com/ws-25.html',
    # 'https://www.maasdam.com/strap-pullers.html'
]
# url_list = []

file = open("maasdam_data.csv", "a", encoding='utf-8')


def request_webpage(page_url):
    response = sess.get(page_url)
    soup = BeautifulSoup(response.content, 'lxml')
    next_page = soup.findAll(class_='wsite-image wsite-image-border-none')
    for page in next_page:
        try:
            page_link = urljoin(base_url, page.find('a')['href'])
            request_webpage(page_link)
            url_list.append(page_link)
        except KeyError:
            pass


def data_func(url):
    row = []
    response = sess.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    title = soup.find(class_='wsite-content-title')
    img = soup.find(class_='wsite-image wsite-image-border-none')
    details = soup.find(class_='paragraph')
    # print(details.text.split('\n'))
    element_list = []
    for d in details:
        data = d.text.split('\n')
        if data[0] != '':
            if data[0] != ' ':
                element_list.append(data)
    print(element_list)

    features = details.findAll('ul')
    weight = element_list[0][0].split(': ')[1]
    strap_length = element_list[1][0].split(': ')[1]
    strap_lift = element_list[2][0].split(': ')[1]
    strap_diameter = element_list[3][0].split(': ')[1]
    leverage = element_list[4][0].split(': ')[1]
    feature = features[0].text
    if len(features) > 1:
        suggest = features[1].text
    else:
        suggest = "not available"

    row.append({
        "product_name": title.text,
        "img_url": img.find('img')['src'],
        "weight": weight,
        "strap_length": strap_length,
        "strap_lift": strap_lift,
        "strap_diameter": strap_diameter,
        "leverage": f"rp_{leverage}",
        "feature": feature,
        "suggestion": suggest,
        "url": url
    })

    df = pd.DataFrame(row)
    df.to_csv(file, lineterminator='\n', index=False, header=False)


def main():
    x = 0
    for x, page_url in enumerate(url_list[x:], x):
        data_func(page_url)
        print("========", x)
        print(page_url)


# main()
# data_func('https://www.maasdam.com/144s-6.html')
# request_webpage(base_url)
# print(url_list)
