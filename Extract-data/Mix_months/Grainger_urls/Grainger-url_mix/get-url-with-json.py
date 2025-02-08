import requests
from urllib.parse import urljoin

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

data = {
    "categoryIndex": 1
}

base_url = 'https://www.grainger.com/category/motors/'

res = requests.get('https://www.grainger.com/experience/pub/api/products/collection/26947?categoryId=15346', headers=header)

t = res.json()
print(len(t))

for i in range(1, 53):
    url_links = urljoin(base_url, t[i]['productDetailUrl'])
    print(url_links)
