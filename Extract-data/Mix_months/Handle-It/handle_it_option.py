import csv
import time
from typing import TextIO

import requests
from bs4 import BeautifulSoup

sess = requests.Session()
with open('handle_it_product_urls.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

# displaying the contents of the CSV file
for url_Links in range(2054, csv_length):
    urls = csv_list[url_Links]
    url = urls[0]
    r = sess.get(url)
    time.sleep(1)
    soup = BeautifulSoup(r.content, "html.parser")
    print("Product-Length...", url_Links)
    print("Product-Urls......", url)

    title = soup.find("h1", {"class": "product-single__title header-flavour"}).text.strip().replace('\n', "").replace("                          ", "").replace("          ", "")
    print("Title...", title)

    print("************************************* Table UPC : ****************************************")
    data = []
    th = []

    table = soup.find("table", class_="handleit-table")
    td = table.find_all('tr')
    # print(td)
    for dd in td:
        ss = dd.find_all('th')
        # print(dd.text)

        if not ss:
            print('null')
        else:
            save_details: TextIO = open("handle-it-option.xlsx", "a+", encoding="utf-8")
            save_details.write('\n' + url + "\t" + title)
            print("\n ***** Record stored into Handle it urls files. *****")

            for f1 in ss:
                save_details.write("\t" + f1.text)
                continue

        s = dd.find_all('td')
        if not s:
            continue

        save_details: TextIO = open("handle-it-option.xlsx", "a+", encoding="utf-8")
        save_details.write('\n' + url + "\t" + title)
        for f in s:
            # print(f)
            save_details.write('\t' + f.text)
            # save_details.write('\t' + "rp_" + f.text)
        print("\n ***** Record stored into Handle it  tables  files. *****")
