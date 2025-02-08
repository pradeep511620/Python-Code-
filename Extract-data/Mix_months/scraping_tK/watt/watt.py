import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
from typing import TextIO
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

l=[
    'https://www.watts.com/products/plumbing-flow-control-solutions/automatic-control-valves/commercial-markets/controls-and-accessories/lfcp15'
]

for j in l:
    s=requests.get(j)
    soup=BeautifulSoup(s.content, 'html.parser')
    print(soup)
    des = soup.find('p', {"class": "product__additional-details js-jump-links-target js-jump-links-default-label"})
    print(des)