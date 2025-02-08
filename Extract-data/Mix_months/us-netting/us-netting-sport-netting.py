from typing import TextIO

import requests
from bs4 import BeautifulSoup

mylist = [
    # 'https://www.usnetting.com/sports-netting/camo-netting/desert/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/flyway/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/greenbrown/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/killer/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/night/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/realtree/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/snow/',
    # 'https://www.usnetting.com/sports-netting/camo-netting/urban/',
    'https://www.usnetting.com/sports-netting/camo-netting/woodland/',
    # 'https://www.usnetting.com/sports-netting/custom-sports-netting/',
    # 'https://www.usnetting.com/sports-netting/golf-netting/golf-cages/',

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
    bread_d = []
    for bread in soup.find("ol", {"class": "breadcrumbs"}).find_all('li'):
        bread_d.append(bread.text.strip().replace("+ Categories", ""))
    print(bread_d)
    try:
        title = soup.find('h1', class_="text-center").text.strip()
        print("Title...", title)
    except:
        pass
    product = soup.find('p').text
    print('product...', product)
    try:
        feature = []
        for data in soup.find('div', class_="col-xs-10 col-sm-12 col-xs-offset-1").find_all('li'):
            feature.append(data.text.strip().replace('\n', ''))
        print(feature)
    except:
        pass

    #
    try:
        for img in soup.find('div', class_='col-sm-6 col-xs-12').find_all('img'):
            # print(img)
            # images = "https://www.usnetting.com/"+img.get("src")
            images = img.get("src")
            print(images)
            save_d: TextIO = open('us-netting-sport.txt', 'a+', encoding="utf-8")
            save_d.write('\n' + url + "\t" + meta_description + "\t" + meta_title + "\t" + "".join(bread_d) + "\t" + title + "\t" + product + "\t" + "".join(feature) + "\t" + images)
        print('data save')
    except:
        pass