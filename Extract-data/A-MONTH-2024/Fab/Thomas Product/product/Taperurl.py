
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
ress = requests.session()
base_url = 'https://catalog.taperline.com/'
mylist = [
    'https://catalog.taperline.com/viewitems/all-categories/cylinder-rod-eyes-and-cylinder-rod-clevises',
    'https://catalog.taperline.com/viewitems/all-categories/locking-alignment-couplers',
    'https://catalog.taperline.com/viewitems/hex-nuts-1/face-lock-hex-nuts',
    'https://catalog.taperline.com/viewitems/hex-nuts-1/peripheral-lock-hex-nuts',
    'https://catalog.taperline.com/viewitems/special-and-custom-made-locknuts/special-custom-made-facelock-locknuts',
    'https://catalog.taperline.com/viewitems/special-and-custom-made-locknuts/special-custom-made-peripheral-locknuts',
    'https://catalog.taperline.com/viewitems/heavy-duty-metric-locknuts/heavy-duty-metric-spindle-peripheral-locknuts',
    'https://catalog.taperline.com/viewitems/heavy-duty-metric-locknuts/heavy-duty-metric-spindle-facelock-locknuts',
    'https://catalog.taperline.com/viewitems/heavy-duty-locknuts/heavy-duty-inch-spindle-locknuts-with-ball-screws',
    'https://catalog.taperline.com/viewitems/heavy-duty-locknuts/heavy-duty-inch-spindle-peripheral-locknuts',
    'https://catalog.taperline.com/viewitems/metric-bearing-locknuts/metric-bearing-facelock-locknuts',
    'https://catalog.taperline.com/viewitems/metric-bearing-locknuts/metric-bearing-peripheral-locknuts',
    'https://catalog.taperline.com/viewitems/inch-bearing-locknuts/inch-bearing-facelock-locknuts',
    'https://catalog.taperline.com/viewitems/inch-bearing-locknuts/inch-bearing-peripheral-locknuts',
]

for url in mylist:
    res = ress.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    for product in soup.find_all(class_="plp-itemlink"):
        get_href_tag = product['href']
        relative_url = urljoin(base_url,get_href_tag)
        with open('taper line.txt', 'a+', encoding='utf-8') as file_save:
            file_save.write(f"{relative_url}\n")
    print("save all data in file")
