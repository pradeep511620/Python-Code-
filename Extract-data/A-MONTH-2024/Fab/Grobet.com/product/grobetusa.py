import threading

import pandas as pd
import requests
from bs4 import BeautifulSoup
import concurrent.futures

urls = []
csv_lock = threading.Lock()
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Grobet.com/data/grobetssss.csv", "a+", encoding="utf-8")

file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Grobet.com/url/Product_url.csv"
url_link = pd.read_csv(file_path)['URL']
i = 2000
for url_count, url in enumerate(url_link[i:], start=i):
    urls.append(url)
    print('product-url---:', url_count, url)


def transform(urls):
    res = requests.get(str(urls))
    soup = BeautifulSoup(res.content, 'html.parser')
    try:
        l3_name = []
        for bread in soup.find("div", {"id": "ProductBreadcrumb"}).find_all("li"):
            l3 = bread.text.strip()
            l3_name.append(l3)
        print(l3_name[2])
        l3_names = "## ".join(l3_name)
        print('l3_name.....', l3_names)
    except AttributeError:
        l3_name = ''
        l3_names = 'N/A'
        print('l3_name.....', l3_names)

    try:
        product_title = soup.find('title').string
        print('product_title.....', product_title)
    except AttributeError:
        product_title = 'N/A'
        print('product_title.....', product_title)

    try:
        mpn = soup.find("span", {"class": "VariationProductSKU"}).text.strip()
        mpn = {"SKU": mpn}
        print('mpn.....', mpn)
    except AttributeError:
        mpn = 'N/A'
        print('mpn.....', mpn)

    try:
        description_dict = {}
        description_des = soup.find(class_="ProductDescriptionContainer").find_all('p')
        for index, tag in enumerate(description_des, start=1):
            des_text = tag.text.strip()
            if des_text:
                key = f'p{index}'
                description_dict[key] = des_text
        description_1 = ["desc" + str(description_dict)]
        print('description_1.....', description_1)
    except AttributeError:
        description_1 = 'N/A'
        print('description_1.....', description_1)

    try:
        description_2 = []
        for des_2 in soup.find(class_="ProductDescriptionContainer").find('ul').find_all('li'):
            description_2.append(des_2.text.strip())
        print('description_2.....', description_2)
    except AttributeError:
        description_2 = 'N/A'
        print('description_2.....', description_2)

    img_tag = ''
    alt_tag_1 = ''
    for img_1 in soup.find_all("img", {"itemprop": "image"}):
        img_tag = img_1.get('src')
        # print(img_tag)

    for alt_1 in soup.find_all("img", {"itemprop": "image"}):
        alt_tag = alt_1.get('alt')
        alt_tag_1 = {"alt": alt_tag}
        # print(alt_tag_1)

    images = img_tag, alt_tag_1
    print('images.....', images)

    try:
        video_links = []
        for video in soup.find(class_="ProductDescriptionContainer").find_all('iframe'):
            video_tag = video.get('src')
            video_links.append(video_tag)
        print("video.....", video_links)
    except AttributeError:
        video_links = "N/A"
        print("video.....", video_links)

    print(l3_name[2], l3_name[3])
    mylist = [
        "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
        "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
        "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
        "scraped_by"
    ]
    raw_data = [{
        "brand": "Grobet", "catlvl1": l3_name[2], "catlvl2": l3_name[3], "catlvl3": l3_name[4], "url": urls,
        "title": product_title, "price_value": "N/A", "unit": "N/A", "shipping_weight": "N/A", "breadscrumbs": l3_names,
        "image_urls": images, "mpn": mpn, "specification_1": description_1, "specification_2": description_2,
        "datasheets": "N/A", "product_description_1": "N/A", "product_description_2": "N/A", "accessories": "N/A",
        "video_links": video_links, "miscellaneous": "N/A", "scraped_by": "Pradeep Kumar",
    }]

    Data_Save(raw_data, mylist)


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(transform, urls)

# print(len(titles))
# df = pd.DataFrame(urls, l3_name, titles)
# df.to_csv('concurrent-titles.csv', index=False)
# print('Complete.')
