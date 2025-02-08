from typing import TextIO

import requests
from bs4 import BeautifulSoup

mylist = [
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/aluminet/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/black/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/blue/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/green/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/red/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/tan/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/white/',
    # 'https://www.usnetting.com/shade-cloth/rectangular-shade-cloth-netting/',
    'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/black/',
    'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/blue/',
    'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/green/',
    'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/red/',
    'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/tan/',
    'https://www.usnetting.com/shade-cloth/triangular-shade-cloth-netting/white/',

]
for url in mylist:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    # print(soup)
    print("Product-url...", url)
    try:
        print("************************************* Meta Description : ****************************************")
        meta_description = soup.find("meta", attrs={"name": "description"}).get("content").strip()
        print("Meta_description......", meta_description)
    except:
        meta_description = "Not Found"
        print("Not Found")
    try:
        print("************************************* Meta Title : ****************************************")
        meta_title = soup.find('title').string.strip()
        print("Meta_title .....", meta_title)
    except:
        meta_title = "Not Found"
        print("Not Found")

    # title = soup.find("div", {"class": "breadcrumb-wrap"}).find('h2').text.strip()
    title = soup.find('h2').text.strip()
    print("Title...", title)
    descs = []
    for desc in soup.find('div', class_="description").find('ul').find_all('li'):
        descs.append(desc.text.strip())
    print(descs)
    try:
        price = soup.find("div", class_="cargo-netting-product-price").text.strip()
        print(price)
    except:
        price = "Not Found"
        print("Not Found")

    for img in soup.find('div', class_='col-xs-12 col-sm-5').find_all('img'):
        # print(img)
        images = "https://www.usnetting.com/"+img.get("src")
        print(images)
        save_d: TextIO = open('us-netting-shade.txt', 'a+', encoding="utf-8")
        save_d.write('\n' + url + "\t" + meta_description + "\t" + meta_title + "\t" + "".join(descs) + "\t" + images)
