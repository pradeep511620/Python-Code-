import requests
from lxml import html
from itertools import cycle
import time
from bs4 import BeautifulSoup
import ssl

def free_proxies():
    h1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    Proxy_res = requests.get('https://sslproxies.org/',headers = h1)
    #print(Proxy_res.status_code)
    extract_proxies = html.fromstring(Proxy_res.content)
    Proxies = set()
    proxies = extract_proxies.xpath('//tbody/tr')[:2000]
    for i in proxies:
     
        if i.xpath('.//td[7][contains(text(),"yes")]') :
            proxy = i.xpath('.//td[1]/text()')[0] + ':' + i.xpath('.//td[2]/text()')[0]
            Proxies.add(proxy)

    #print(Proxies)
    return Proxies

proxy_list = free_proxies()
proxy_pool = cycle(proxy_list)
print(len(proxy_list))
l=[]
for i in range(0,len(proxy_list)):
        proxy ="http://"+ next(proxy_pool)
        print(proxy)
        proxy = {
            "http": proxy,
            "https": proxy
        }
        try:
            Res = requests.get('https://www.raptorsupplies.com/',proxies=proxy)
        except:
            continue
        l.append(proxy)
        soup=BeautifulSoup(Res.text,'html.parser')
        print(soup.find('span',class_='catalogue-text').text)
        print(Res.status_code)

print(proxy)        