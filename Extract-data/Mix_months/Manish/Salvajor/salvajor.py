import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

sess = requests.Session()

base_url = 'https://www.singerequipment.com/store/salvajor/?mpp=250'

product_urls = []
product_url = open("salvajor_product_urls.csv", 'a', encoding='utf-8')
product_data = open("salvajor_product_data.csv", 'a', encoding='utf-8')


def request_func(url):
    """Send Requests and Get Response from webpage and return Soup"""
    res = sess.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    return soup


def urljoin_func(url):
    """function takes a relative url and convert it into absolute url and returns"""
    return urljoin(base_url, url)


def product_link(url):
    """find all the product links and save as csv file"""
    soup = request_func(url)
    product_links = soup.findAll(class_="itemImageWrapper itemLink")
    for link in product_links:
        product_urls.append(urljoin_func(link['href']))


def product_details(url):
    """Get product details(Respective Product url, title, breadcrumb, item no, image url
    video url, pdf url, product details, product specifications) and call data save function(file as txt or csv)"""

    cols = ["url", "breadCrumb", "title", "item_num", "description", "images", "pdfs", "attr_name", "attr_value"]

    row = []

    soup = request_func(url)
    bread_crumb = soup.find(class_="breadcrumbs").text.replace('\n', '')
    # print("bread_crumb >>> ", bread_crumb)
    title = soup.h1.text
    # print("title >>> ", title)
    item_num = soup.find(class_="itemSku").text.replace('\n', '').replace('#', '')
    # print("item_num >>> ", item_num)
    description = soup.find(class_='se-seeMore-Wrapper').text.replace('\n', '').replace('See More', ' ')
    # print("description >>> ", description)
    images = soup.find(class_="w-100 se-productImage-group").findAll('img')
    image_list = []
    for image in images:
        image_list.append(urljoin_func(image['src']))

    pdf_list = []
    try:
        pdfs = soup.find(class_="product-documents-list").findAll('a')
        for pdf in pdfs:
            print(pdf['href'])
            pdf_list.append(urljoin_func(pdf['href']))
        # print("pdf >>> ", urljoin_func(pdfs['href']))
    except AttributeError:
        pass

    table_content = soup.findAll(class_='prod-spec-each')
    attr_name = []
    attr_value = []
    for item in table_content:
        attr_name.append(item.find(class_='label').text)
        attr_value.append(item.find(class_='content').text)

    row.append({
        "url": url,
        "breadCrumb": bread_crumb,
        "title": title,
        "item_num": item_num,
        "description": description.strip(),
        "images": image_list,
        "pdfs": pdf_list,
        "attr_name": attr_name,
        "attr_value": attr_value,
    })

    data_save(row, cols)


def data_save(row, cols):
    """function takes row and columns convert into dataframe and filter out and save data into the file"""
    df = pd.DataFrame(row, columns=cols)
    df = df.explode(['attr_name', 'attr_value'])
    df = df.explode(["images"])
    df = df.explode(['pdfs'])
    # df = df.drop('index', axis=1)
    print(df)
    # df.to_csv(product_data, index=False, lineterminator='\n', header=False)
    df.to_csv("test.csv")


def main():
    product_link(base_url)
    i = 165
    """using i indexing product url default i value is 0"""
    for url in product_urls[i:]:
        print(i, ">>>>>>>>>>>>>", url)
        product_details(url)
        i += 1


main()

"""testing call"""
# product_details('https://www.singerequipment.com/products/salvajor-200-ca-18-mss/10055225/')
