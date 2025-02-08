import csv

import requests
from bs4 import BeautifulSoup
with open('handle_it_product_urls.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

# displaying the contents of the CSV file
for url_Links in range(2054, csv_length):
    urls = csv_list[url_Links]
    url = urls[0]
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    print("Product-Length...", url_Links)
    print("Product-Urls......", url)

    title = soup.find("h1", {"class": "product-single__title header-flavour"}).text.strip().replace('\n', "").replace("                          ", "").replace("          ", "")
    print("Title...", title)
    try:
        i = 0
        name = []
        value = []
        table = soup.find('div', {"id": "specification"})
        td = table.find_all('td')
        for t in td:
            i += 1

            if i % 2 != 0:
                name.append(t.text.strip().replace("\n", ''))
            else:
                value.append(t.text.strip().replace("\n", ''))
        for a, b in zip(name, value):
            print(a, ".....", b)
            save = open('handle-it-tables.txt', 'a+', encoding="utf-8")
            save.write('\n' + url + "\t" + title + "\t" + a + "\t" + b)
        print('save into tables')
    except Exception as e:
        print(e)

