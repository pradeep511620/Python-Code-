import requests
from bs4 import BeautifulSoup

URL = "https://www.raptorsupplies.com/b/morse-drum"
r = requests.get(URL)
print(r)
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.text)

list_pro =soup.find('div', {'class': 'all-pro-inner'})

data = soup.findAll(class_='tab-content-inner catItem')
# for title in data:
#     print(title.find('span').contents[0])

# title = soup.find('span', class_="brand-title")
# print(title.contents[0])
# for i in title:
#     print(title)
# print(list_pro)
# for l3 in list_pro:
#     image = (l3.find('img')['src'])
#     # title = (l3.find('img')['alt'])
#     title = (l3.find('img')['alt'])
#     count = (l3.find('p').find_all('span')[-1].text)
#     print( image,'--', title,'--', count)