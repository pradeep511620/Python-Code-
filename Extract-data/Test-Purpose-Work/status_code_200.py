import requests

url = 'https://eldonjames.com/product/lslr-pp-b-qc/'

sess = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


res = sess.get(url, headers=headers)

if res.status_code == 200:
    print('You can do anything')
else:
    print("can't do anything")


