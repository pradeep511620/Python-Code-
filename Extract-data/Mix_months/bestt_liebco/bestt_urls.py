import requests
from bs4 import BeautifulSoup


myurl = [
    'https://www.besttliebco.com/product-category/brushes/',
    'https://www.besttliebco.com/product-category/brushes/tru-pro-brushes/',
    'https://www.besttliebco.com/product-category/brushes/master-brushes/',
    'https://www.besttliebco.com/product-category/brushes/earth-tones-brushes/',
    'https://www.besttliebco.com/product-category/brushes/one-coat-brushes/',
    'https://www.besttliebco.com/product-category/brushes/weekender-brushes/',
    'https://www.besttliebco.com/product-category/brushes/hand-craft-brushes/',
    'https://www.besttliebco.com/product-category/brushes/perfect-touch-brushes/',
    'https://www.besttliebco.com/product-category/brushes/minwax-brushes/',

    'https://www.besttliebco.com/product-category/roller-covers/',
    'https://www.besttliebco.com/product-category/roller-covers/tru-pro-roller-covers/',
    'https://www.besttliebco.com/product-category/roller-covers/earth-tones-roller-covers/',
    'https://www.besttliebco.com/product-category/roller-covers/Perfect-Touch-roller-covers/',
    'https://www.besttliebco.com/product-category/roller-covers/One-Coat-roller-covers/',
    'https://www.besttliebco.com/product-category/roller-covers/weekender-roller-covers/',

    'https://www.besttliebco.com/product-category/mini-rollers/',
    'https://www.besttliebco.com/product-category/mini-rollers/master-mini-rollers/',
    'https://www.besttliebco.com/product-category/mini-rollers/mini-trays/',

    'https://www.besttliebco.com/product-tag/specialty/',
    'https://www.besttliebco.com/product-category/brushes/specialty-applicators/specialty-applicators-brushes/',
    'https://www.besttliebco.com/product-category/specialty-applicators/pads-mitts/',

    'https://www.besttliebco.com/product-category/accessories/',
    'https://www.besttliebco.com/product-category/accessories/buckets-grids/',
    'https://www.besttliebco.com/product-category/accessories/kits/',
    'https://www.besttliebco.com/product-category/accessories/trays/',
    'https://www.besttliebco.com/product-category/accessories/frames/',
    'https://www.besttliebco.com/product-category/accessories/poles/',


]
for url in myurl:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')


#
    link = soup.find_all('a', {"class": "woocommerce-LoopProduct-link woocommerce-loop-product__link"})
    print("lenght..", len(link))
    for u_link in link:
        url_link = u_link.get('href')
        save_details: u_link = open("bestt_urls.xlsx", "a+", encoding="utf-8")
        save_details.write('\n' + "'"+url_link+"',")
    print("\n ***** urls stored into files. *****")
