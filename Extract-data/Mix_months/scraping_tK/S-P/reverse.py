import requests
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

proxies = [
    "http://115.96.208.124:8080",
    'http://20.69.79.158:8443',
    'http://146.70.76.146:3128',
    'http://104.223.135.178:10000',
    'http://157.245.27.9:3128',
    'http://20.69.79.158:8443',

]

urls = [
    'https://www.grainger.com/product/INSIZE-Digital-Microscope-Digital-55VP03',
    'https://www.grainger.com/product/INSIZE-Digital-Auto-Focus-Microscope-55VP01',

]


for url in reversed(urls):
    print(url)
    urls.pop()

print(urls)