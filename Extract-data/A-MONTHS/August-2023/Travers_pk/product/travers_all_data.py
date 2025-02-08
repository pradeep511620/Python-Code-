import time

import requests
from bs4 import BeautifulSoup

mylst = [

    'https://www.travers.com/product/akuma-070100125-round-insert-indexable-endmill-22-600-040',
    # 'https://www.travers.com/product/vermont-gage-901100400-pin-gage-set-57-062-923',
]

for url in mylst:
    r = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(r.content, 'html.parser')
    print("product Urls", url)
    breadcrumb = soup.find(class_='page-wrapper').find_all('script')
    print(breadcrumb)

    print("***********************************  Title : **************************************")
    title = soup.find('h1', {"class": "page-title"})
    title_d = title.text.strip()
    # print("title = ", title_d)

    print("************************************* sku : ****************************************")
    try:
        print("************************************* sku : ****************************************")
        sku = soup.find('div', {"itemprop": "sku"})
        sku_d = sku.text
        print("sku = ", sku_d)
    except:
        sku_d = "Not Found"
        print("Not Found", sku_d)

    print("************************************* images : ****************************************")
    image = soup.find('div', {"class": "gallery-placeholder"}).find('img')
    images = image.get('src')
    print("images...", images)

    print("************************************* price : ****************************************")
    price = soup.find('span', {"class": "price"}).text
    each = soup.find('span', {"class": "uom"}).text.strip()
    prices = price + "" + each
    # print("price...", prices)

    print("************************************* table : ****************************************")
    attr_name = []
    attr_value = []
    table = soup.find('tbody', class_='attribute_body')
    for th in table.find_all('th'):
        attr_name.append(th.text.strip())
    for td in table.find_all('td'):
        attr_value.append("rp_"+td.text)
    for a, b in zip(attr_name, attr_value):
        pass
        # print(a, ".......", b)
    print("************************************* all details : ****************************************")
    details_all = soup.find('div', {"id": "description"}).text
    # print('details_all', details_all)

    print("************************************* pdf : ****************************************")
    pdf = soup.find('div', {"class": 'product-social-links'}).find('a')
    datasheet = pdf.get('href')
    # print('datasheet', datasheet)
