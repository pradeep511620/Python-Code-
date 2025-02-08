# import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# opts = Options()
# opts.headless = False
# driver = webdriver.Chrome()
# driver.maximize_window()


mylst = [
    'https://deadontools.com/products/16-oz-graphite-hammer',
]

# for url in mylst:


def request_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    save_datas(url)
    return soup


def get_data(soup):
    try:
        print("********** Meta-Title : **********")
        meta_title = soup.find('title').string
        print("Title...", meta_title)
    except:
        meta_title = "Not Found"
        print("Not Found")

    try:
        print("********** Meta-Description : **********")
        meta_description = soup.find("meta", {"name": "description"}).get('content').strip()
        print("Meta_description......", meta_description)
    except:
        meta_description = "Not Found"
        print("Not Found")

    title = soup.find("h1", {"class": "#hero-heading heading-font"}).text.strip()
    print("Title...", title)

    sku = soup.find('span', {"class": "product-meta-sku-value"}).text.strip()
    print("sku...", sku)

    price = soup.find("span", {"class": "#price-value"}).text.strip()
    print("Price...", price)

    desc = soup.find("div", {"class": "#product-description-expand-content"}).find('p').text
    print(desc)

    desc1 = soup.find("div", {"class": "#product-description-expand-content"}).find('ul').text.replace('\n', '')
    print(desc1)
    save_datas(meta_title, meta_description, title, sku, price, desc, desc1)


def save_datas(url='', meta_title='', meta_description='', title='', sku='', price='', desc='', desc1='', images='', shopping='', about=''):
    save_data: TextIO = open('dead-on-tools', 'a+', encoding='utf-8')
    save_data.write(url + "\t" + meta_title + "\t" + meta_description + "\t" + title + "\t" + sku + "\t" + price + "\t" + desc + "\t" + desc1 + "\t" + images + "\t" + shopping + "\t" + about)
    # save_data.write('\n' + url + meta_title + meta_description + title + sku + price + desc + desc1 + images + shopping + about)
    print('data save into images files and all data')


def extract_image(soup):
    for img in soup.find('div', class_="#slideshow-thumbnails-scroller").find_all('img'):
        images = "https://deadontools.com" + img['src']
        print('Images...', images)
        save_datas(images, '\n')


def extract_shopping_about(soup):
    full = []
    about_shopping = soup.find_all('div', class_="#product-meta-collapse-body")
    for abo in about_shopping:
        full.append(abo.text.strip())
    shopping = full[0]
    print('sopping...', shopping)
    about = full[1]
    print('about...', about)
    save_datas(shopping, about)


def main():
    for url in mylst:
        soup = request_url(url)
        get_data(soup)
        extract_image(soup)
        extract_shopping_about(soup)


main()
