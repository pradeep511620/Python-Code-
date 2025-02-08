from typing import TextIO
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

#

mylst = [

    'https://deadontools.com/products/3-in-oil-tan-belt',
    'https://deadontools.com/products/ballistic-framers-tool-belt-with-suspenders',
    'https://deadontools.com/products/carpenters-tool-belt-with-suspenders',
    'https://deadontools.com/products/electricians-tool-belt-with-suspenders',
    'https://deadontools.com/products/framers-tool-belt-with-suspenders',
    'https://deadontools.com/products/journeymans-tool-belt-with-suspenders',
    'https://deadontools.com/products/leather-hybrid-tool-belt-with-suspenders',
    'https://deadontools.com/products/workwear-shirt-black',
    'https://deadontools.com/products/workwear-shirt-gray',
    'https://deadontools.com/products/workwear-shirt-safety-green',
    'https://deadontools.com/products/trucker-hat',
    'https://deadontools.com/products/trucker-hat?variant=43444944011479',
    'https://deadontools.com/products/trucker-hat?variant=43444944044247',
    'https://deadontools.com/products/versatile-neck-gaiter',
    'https://deadontools.com/products/versatile-neck-gaiter?variant=42826019012823',
    'https://deadontools.com/products/versatile-neck-gaiter?variant=42826019045591',
    'https://deadontools.com/products/a1-general-purpose-work-gloves',
    'https://deadontools.com/products/a3-general-purpose-work-gloves',
    'https://deadontools.com/products/a3-demo-work-gloves',
    'https://deadontools.com/products/all-terrain-gel-knee-pads',
    'https://deadontools.com/products/eliminator-gel-knee-pads',
    'https://deadontools.com/products/flexible-gel-knee-pads',
    'https://deadontools.com/products/hard-cap-gel-knee-pads',
    'https://deadontools.com/products/heavy-duty-24-oz-canvas-work-apron-bib-style',
    'https://deadontools.com/products/heavy-duty-24-oz-canvas-work-apron-shop-style',
    'https://deadontools.com/products/no-rock-gel-knee-pads',
    'https://deadontools.com/products/14-in-flattop-weather-resistant-tool-bag',
    'https://deadontools.com/products/16-can-weather-resistant-backpack-cooler',
    'https://deadontools.com/products/18-in-flattop-weather-resistant-tool-bag',
    'https://deadontools.com/products/18-rolling-open-tool-tote',
    'https://deadontools.com/products/20-in-weather-resistant-duffel-bag',
    'https://deadontools.com/products/25-in-weather-resistant-duffel-bag',
    'https://deadontools.com/products/cell-phone-holder-large',
    'https://deadontools.com/products/cell-phone-holder-small',
    'https://deadontools.com/products/destroyer-tech-pack',
    'https://deadontools.com/products/electricians-pouch',
    'https://deadontools.com/products/heavy-duty-24-oz-canvas-large-wrench-roll',
    'https://deadontools.com/products/heavy-duty-24-oz-canvas-wrench-roll',
    'https://deadontools.com/products/heavy-duty-24-oz-canvas-zippered-tool-roll',
    'https://deadontools.com/products/parachute-bag',
    'https://deadontools.com/products/tape-measure-holder',
    'https://deadontools.com/products/utility-pouch',
    'https://deadontools.com/products/14-in-annihilator-wrecking-bar',
    'https://deadontools.com/products/16-oz-graphite-hammer',
    'https://deadontools.com/products/18-in-annihilator-wrecking-bar',
    'https://deadontools.com/products/21-oz-investment-cast-wood-hammer-curved-handle',
    'https://deadontools.com/products/21-oz-investment-cast-wood-hammer-straight-handle',
    'https://deadontools.com/products/22-oz-steel-hammer-milled-face',
    'https://deadontools.com/products/22-oz-steel-hammer-smooth-face',
    'https://deadontools.com/products/22-oz-steel-hammer-smooth-face-16-inch-handle',
    'https://deadontools.com/products/24-oz-forged-wood-hammer',
    'https://deadontools.com/products/classic-exhumer-nail-puller',
    'https://deadontools.com/products/exhumer-8-nail-puller',
    'https://deadontools.com/products/exhumer-9-nail-puller',
    'https://deadontools.com/products/nail-gun-hook',
]

for url in mylst:
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        images = ''
        shopping = ''
        about = ''

        try:
            print("********** Meta-Title : **********")
            meta_title = soup.find('title').string
            print("Title...", meta_title)
        except:
            meta_title = "Not Found"
            print("Not Found")

        try:
            print("********** Meta-Description : **********")
            meta_description = soup.find("meta", {"name": "description"}).get('content').strip()
            print("Meta_description......", meta_description)
        except:
            meta_description = "Not Found"
            print("Not Found")

        print('********** Title : **********')
        title = soup.find("h1", {"class": "#hero-heading heading-font"}).text.strip()
        print("Title...", title)

        print('********** sku : **********')
        sku = soup.find('span', {"class": "product-meta-sku-value"}).text.strip()
        print("sku...", sku)

        print('********** Price : **********')
        price = soup.find("span", {"class": "#price-value"}).text.strip()
        print("Price...", price)

        print('********** Description : **********')
        desc = soup.find("div", {"class": "#product-description-expand-content"}).find('p').text
        print(desc)

        print('********** Description1 : **********')
        desc1 = soup.find("div", {"class": "#product-description-expand-content"}).find('ul').text.replace('\n', '')
        print(desc1)

        print('********** Shopping-About : **********')
        full = []
        about_shopping = soup.find_all('div', class_="#product-meta-collapse-body")
        for abo in about_shopping:
            full.append(abo.text.strip())
        shopping = full[0]
        print('sopping...', shopping)
        about = full[1]
        print('about...', about)
        save_data: TextIO = open('dead-on-tools', 'a+', encoding='utf-8')
        save_data.write(
            "\n" + url + "\t" + meta_title + "\t" + meta_description + "\t" + title + "\t" + sku + "\t" + price + "\t" + desc + "\t" + desc1 + "\t" + shopping + "\t" + about.strip())
        print('data save into files and all data')

        print('********** Images : **********')
        for img in soup.find('div', class_="#slideshow-thumbnails-scroller").find_all('img'):
            images = "https://deadontools.com" + img['src']
            print('Images...', images)
            save_data: TextIO = open('dead-on-tools', 'a+', encoding='utf-8')
            save_data.write("\n" + url + "\t" + meta_title + "\t" + meta_description + "\t" + title + "\t" + sku + "\t" + price + "\t" + desc + "\t" + desc1 + "\t" + shopping + "\t" + about + "\t" + images)
        print('data save into images files and all data')

    except Exception as e:
        save_data: TextIO = open('remain', 'a+', encoding='utf-8')
        save_data.write("\n" + url)
        print('data save into remaining files')
        print("Error", e)
