import json
import requests
from bs4 import BeautifulSoup
import json

import requests
from bs4 import BeautifulSoup

# url = 'https://www.brahelectric.com/Products/Bus-Plugs?page=1&pageSize=60'
# url = 'https://www.brahelectric.com/Products/Circuit-Breakers?page=1&pageSize=60'
url = 'https://www.brahelectric.com/Products/Motor-Controls?page=1&pageSize=60'


def get_url(self):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def pagination(soup):
    le = soup.find('p', class_="text-lg font-semibold text-center md:text-left").text.split(' ')[0]
    print('Total-Url', le)
    length = round(int(le) / 60)
    print("loop.... ", length)
    for i in range(1, length + 1):
        # url_pagination1 = f'https://www.brahelectric.com/Products/Bus-Plugs?page={i}&pageSize=60'
        # url_pagination1 = f'https://www.brahelectric.com/Products/Circuit-Breakers?page={i}&pageSize=60'
        url_pagination1 = f'https://www.brahelectric.com/Products/Motor-Controls?page={i}&pageSize=60'
        soup1 = get_url(url_pagination1)
        print(i)
        json_data = json.loads(soup1.find(id="__NEXT_DATA__", type='application/json').text)
        for data in json_data['props']['pageProps']['products']['data']:
            product_url = f"https://www.brahelectric.com/Products/{data['custom']['WebDisplayUrl']}"
            print("url..", product_url)
            save = open('brah-electric.csv', 'a+', encoding="utf-8")
            save.write("\n" + product_url)


def main():
    soup = get_url(url)
    pagination(soup)


main()
