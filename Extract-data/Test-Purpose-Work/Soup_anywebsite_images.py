
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

url = 'https://www.mscdirect.com/product/details/05416334'
ress = requests.Session()
ress1 = ress.get(url, headers=headers)
print(ress1.status_code)

soup = BeautifulSoup(ress1.content, 'lxml')
tit = soup.find_all('h1')
print(tit)

