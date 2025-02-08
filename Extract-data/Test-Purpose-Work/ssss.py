
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.devtools.v85.page import print_to_pdf

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
'dnt': '1',
'priority':'u=0, i',
'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform':"Windows",
'sec-fetch-dest':'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site':'none',
'sec-fetch-user':'?1',
'upgrade-insecure-requests': '1'
           }
cookies = {
    "gr_1_deviceId": "4bd1f4de-bbf1-456a-843d-cca953aa8bf0",
    # "city": "Diu",
    # "__cf_bm": "Fyrs6cmt2LVPnQI8Uk05N.DNKdgYDEMLKZQIK8EamaE-1735835863-1.0.1.1-teF2bfV83ictAr5BMuQQD6oAYbqXWkbjmXZH8CscmKWYQdod5f0taIkHtyGKPEcXkH8Welj3wgxhb1pUvyM8Ng",
    "_cfuvid": "5HTmn92lrCNR7RAEx4eI54SP12GzG6WS5A6xTeXNBIU-1735835863308-0.0.1.1-604800000",
    "__cfruid": "22510faf33a39a306f73d0126bffd0be1740b05c-1735835904",
    # "gr_1_lat": "28.4554726",
    # "gr_1_lon": "77.0219019",
    # "gr_1_locality": "Gurugram",
    # "gr_1_landmark": "undefined",
}
url_list = [
    # 'https://blinkit.com/prn/amul-masti-pouch-curd/prid/45533'
    'https://blinkit.com/cn/chicken/cid/4/1362'
    # 'https://www.zeptonow.com/pn/relish-peri-peri-chicken-wings/pvid/13dcbd39-5b05-4cc3-8297-52276371c1de'
    # 'https://www.bigbasket.com/pc/foodgrains-oil-masala/edible-oils-ghee/ghee-vanaspati/',
    # 'https://www.bigbasket.com/pc/beverages/tea/'
    # 'https://www.bigbasket.com/pd/20000911/fresho-kiwi-green-3-pcs/?nc=l2category&t_pos_sec=1&t_pos_item=4&t_s=Kiwi+-+Green',
    # 'https://www.bigbasket.com/pd/10000149/fresho-onion-2-kg/?nc=Frequently+Bought+Together&t_pos_sec=4&t_pos_item=3&t_s=Onion+%2528Loose%2529',
    # 'https://www.bigbasket.com/pd/10000273/fresho-mushrooms-button-1-pack/?nc=l2category&t_pos_sec=1&t_pos_item=2&t_s=Mushrooms+-+Button'
    ]
for idx, url in enumerate(url_list):

    response_data = requests.Session()
    ress = response_data.post(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(ress.content, 'lxml')
    print(ress.status_code)
    # print(soup.select_one('h1.text-xl').text.strip())
    # upc = soup.select_one('h1.Description___StyledH-sc-82a36a-2.bofYPK').text.strip()
    # print(upc)
    #
    # images = [img.get('src') for img in soup.select('section.Image___StyledSection-sc-1nc1erg-0 img') if img.get('src') and 'jpg' in img.get('src')]
    # print(images)
    # price_list = [price.text.strip() for price in soup.select('.Pricing___StyledLabel-sc-pldi2d-1')]
    # print(price_list)
    # title_list = [title.text.strip() for title in soup.select('div.break-words.h-10.w-full')]
    # print(title_list)