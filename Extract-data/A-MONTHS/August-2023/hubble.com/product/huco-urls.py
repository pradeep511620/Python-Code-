import csv
import time
import requests
from bs4 import BeautifulSoup

time.sleep(7)

with open("C:/Users/PK/Desktop/Web-Scrapping/August-2023/hubble.com/urls/hubbell-url.csv", 'r') as files:
    csv_reader = csv.reader(files)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

for csv_link in range(55, csv_length + 1):
    url = csv_list[csv_link][0] + "?ps=30&pg="
    print("Product-Length...", csv_link)
    print("Product-Urls......", url)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    #
    count = soup.find('div', class_="showing-amount").text.strip().replace('\n', ' ').split(' ')[-1]
    print("Total..", count)
    length = round(int(count) / 30)
    print("Loop..", length)

    for i in range(0, length + 1):
        urlss = f"{url}{i}"
        print(urlss)
        save = open('product-url-huco.txt', 'a+', encoding='utf-8')
        save.write('\n' + urlss)
