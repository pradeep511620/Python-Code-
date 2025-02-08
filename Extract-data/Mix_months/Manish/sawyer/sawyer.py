import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

sess = requests.Session()

base_url = 'https://sawyermfg.com/equipment/'

product_urls = []
product_url = open("sawyer_product_urls.csv", 'a', encoding='utf-8')
product_data = open("sawyer_product_data.csv", 'a', encoding='utf-8')


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
    product_links = soup.findAll(class_="fl-post-image")
    for link in product_links:
        product_urls.append(urljoin_func(link.find('a')['href']))
    # df = pd.DataFrame(product_urls)
    # df.to_csv(product_url, lineterminator='\n')


def product_details(url):
    """Get product details(Respective Product url, title, breadcrumb, item no, image url
    video url, pdf url, product details, product specifications) and call data save function(file as txt or csv)"""

    cols = ["url", "title", "sub_title", "description", "features", "video_link", "images", "pdfs", "attr_name", "attr_value"]

    row = []

    soup = request_func(url)
    title = soup.h1.text
    # print("title >>> ", title)
    try:
        sub_title = soup.find(id="product-sub-title").text.replace('\n', '')
    except AttributeError:
        sub_title = ''
    # print("sub_title >>> ", sub_title)
    description = soup.find(class_='fl-col fl-node-5de5596a3f8c7 fl-col-small').text.replace('\n', ' ')
    # print("description >>> ", description)
    features = soup.find(class_='fl-module fl-module-html fl-node-5dc990dba352b features-list').text.replace('\n', ' ')
    # print("features >>> ", features)
    try:
        video_link = soup.find(class_="fl-col fl-node-5de5596a3f8c7 fl-col-small").findAll('p')[-1].find('iframe')['src']
        # print("Video >>>>>>>", video_link)
    except TypeError:
        video_link = ''
    images = soup.find(class_="fl-module fl-module-fl-woo-product-images fl-node-5f6235c4284db").findAll('a')
    image_list = []
    for image in images:
        image_list.append(urljoin_func(image['href']))
    # print(image_list)

    pdf_list = []
    try:
        pdfs = soup.find(id="downloads-section").findAll('a')
        for pdf in pdfs:
            # print(pdf['href'])
            pdf_list.append(urljoin_func(pdf['href']))
        # print("pdf >>> ", pdf_list)
    except AttributeError:
        pass

    attr_name = []
    attr_value = []
    try:
        table_content = soup.findAll(class_='main-point-inner')
        for item in table_content:
            attr_name.append(item.h2.text.replace('-', ''))
            attr_value.append(item.find('p').text)
        # print(attr_name, ">>>>>>", attr_value)
    except AttributeError:
        pass

    row.append({
        "url": url,
        "title": title,
        "sub_title": sub_title,
        "description": description.strip(),
        "features": features.strip(),
        "video_link": video_link,
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
    df.to_csv(product_data, index=False, lineterminator='\n', header=False)
    # df.to_csv("test.csv")


def main():
    product_link(base_url)
    i = 0
    """using i indexing product url default i value is 0"""
    for url in product_urls[i:]:
        print(i, ">>>>>>>>>>>>>", url)
        product_details(url)
        i += 1


main()

"""testing call"""
# product_details('https://sawyermfg.com/equipment/band-beveling/')
# print(len(product_urls))

