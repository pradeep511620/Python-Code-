import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import TextIO

base_url = 'https://www.liftnbuddy.com/'

sess = requests.Session()

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

product_urls = [

    "https://www.liftnbuddy.com/products/lnb-2",
    "https://www.liftnbuddy.com/products/pail-lifter",
    "https://www.liftnbuddy.com/products/lnb-keg-lifter",
    "https://www.liftnbuddy.com/products/lnb-series4"

]


def request_fun(url):
    response = sess.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup


def product_url(url):
    soup = request_fun(url)
    # print(soup)
    nav = soup.find(class_="uk-navbar").find(class_='uk-dropdown-navbar').find(class_='uk-grid').findAll('a')
    for product_link in nav:
        print(urljoin(base_url, product_link['href']))


def product_details(url):
    img_l = ''
    soup = request_fun(url)
    title = soup.h1.text
    description = soup.find(class_='element element-textarea last').text
    desc = description.strip().replace('\n', ' ').replace('Description', 'Description ')
    pdf_link = soup.find(class_='pos-media media-right').find('a')
    if pdf_link is not None:
        pdf = pdf_link['href']
    else:
        pdf = "not available"
    video_link = soup.find(class_='element element-mediapro last')
    if video_link is not None:
        v_link = video_link.find('iframe')['src']
    else:
        v_link = "not available"

    image = soup.find(class_="zoo-gallery-wall clearfix nav margin").findAll('img')
    img_link = []
    for imgs in image:
        img_link.append(imgs['src'])

    for img_l in img_link:
        save_d: TextIO = open('liftnbuddy.txt', 'a+', encoding='utf-8')
        save_d.write("\n" + url + "\t" + title + "\t" + desc + "\t" + pdf + "\t" + v_link + "\t" + img_l.strip())
    print('\n', "save data into image and all file")

    specification = soup.find('table').findAll('tr')
    attr_name = []
    attr_value = []

    for spec in specification:
        spec_list = spec.text.replace('\n', '\t').replace('\xa0', '').split('\t')
        print(spec_list)
        attr_name.append(spec_list[1])
        attr_value.append(spec_list[2])

    for a, b in zip(attr_name, attr_value):
        save_d: TextIO = open('liftnbuddy.txt', 'a+', encoding='utf-8')
        save_d.write("\n" + url + "\t" + title + "\t" + desc + "\t" + pdf + "\t" + v_link + "\t" + img_l + "\t" + a + "\t" + b.strip())
    print('\n', "save data into image and all file")


def main():
    i = 0
    for url in product_urls:
        print(i)
        print(url)
        product_details(url)
        i += 1


main()

# product_details('https://www.liftnbuddy.com/products/lnb-2')
# product_url(base_url)
