from typing import TextIO
import requests
from bs4 import BeautifulSoup
import selenium

myresult = [
    'https://www.besttliebco.com/product/polyester-nylon-blend-short-angle/',
            # 'https://www.besttliebco.com/product/deck-scrub-brush/',
            # 'https://www.besttliebco.com/product/black-china-blend-trim-and-angle/',
            # 'https://www.besttliebco.com/product/minwax-polycrylic/',
            # 'https://www.besttliebco.com/product/polyester-nylon-blend-brush-2-pack/',
            # 'https://www.besttliebco.com/product/semi-oval-brush/',
            # 'https://www.besttliebco.com/product/polyester-nylon-blend-short-angle/',
            # 'https://www.besttliebco.com/product/minwax-polyurethane/',
            # 'https://www.besttliebco.com/product/polyester-blend-trim-and-angle/',
            # 'https://www.besttliebco.com/product/polyester-nylon-blend-trim-and-angle/',
            # 'https://www.besttliebco.com/product/minwax-wood-finish/',
            # 'https://www.besttliebco.com/product/502480700/',
            # 'https://www.besttliebco.com/product/996620030/',
            # 'https://www.besttliebco.com/product/bestt-liebco-polyester-bristle-blend/',
            # 'https://www.besttliebco.com/product/bestt-liebco-100-white-china-bristle/',
            # 'https://www.besttliebco.com/product/bestt-liebco-bestt-trim-stainer/',
            # 'https://www.besttliebco.com/product/bestt-liebco-first-mate/',
            # 'https://www.besttliebco.com/product/tru-pro-piedmont/',
            # 'https://www.besttliebco.com/product/tru-pro-palmer/',
            # 'https://www.besttliebco.com/product/tru-pro-peoria/',
            # 'https://www.besttliebco.com/product/tru-pro-pacifica/',
            # 'https://www.besttliebco.com/product/tru-pro-2535/',
            # 'https://www.besttliebco.com/product/tru-pro-cape-may/',
            # 'https://www.besttliebco.com/product/tru-pro-colorado/',
            # 'https://www.besttliebco.com/product/tru-pro-bridgeport/',
            # 'https://www.besttliebco.com/product/tru-pro-brisbane/',
            # 'https://www.besttliebco.com/product/tru-pro-bristol/',
            # 'https://www.besttliebco.com/product/tru-pro-mechanic/',
            # 'https://www.besttliebco.com/product/tru-pro-white-skipper/',
            # 'https://www.besttliebco.com/product/tru-pro-white-tampa/',
            # 'https://www.besttliebco.com/product/deck-scrub-brush/',
            # 'https://www.besttliebco.com/product/black-china-blend-trim-and-angle/',
            # 'https://www.besttliebco.com/product/semi-oval-brush/',
            # 'https://www.besttliebco.com/product/polyester-nylon-blend-short-angle/',
            # 'https://www.besttliebco.com/product/polyester-blend-trim-and-angle/',
            # 'https://www.besttliebco.com/product/polyester-nylon-blend-trim-and-angle/',
            # 'https://www.besttliebco.com/product/502480700/',
            # 'https://www.besttliebco.com/product/master-angle-sash/',
            # 'https://www.besttliebco.com/product/master-thin-angle-sash/',
            # 'https://www.besttliebco.com/product/master-trim/',
            # 'https://www.besttliebco.com/product/master-brush-3-pack/',
            # 'https://www.besttliebco.com/product/master-angle-sash-2/',
            # 'https://www.besttliebco.com/product/master-trim-2/',
            # 'https://www.besttliebco.com/product/100-white-china-bristle-trim-and-angle/',
            # 'https://www.besttliebco.com/product/master-stain-brush/',
            # 'https://www.besttliebco.com/product/earth-tones-angle-sash-brush/',
            # 'https://www.besttliebco.com/product/earth-tones-trim-wall-brush/',
            # 'https://www.besttliebco.com/product/earth-tones-brush-2pk/',
            # 'https://www.besttliebco.com/product/996620030/',
            # 'https://www.besttliebco.com/product/one-coat-white-china-2/',
            # 'https://www.besttliebco.com/product/one-coat-white-china/',
            # 'https://www.besttliebco.com/product/one-coat-100-polyester-3/',
            # 'https://www.besttliebco.com/product/one-coat-100-polyester-2/',
            # 'https://www.besttliebco.com/product/perfect-touch-100-polyester/',
            # 'https://www.besttliebco.com/product/weekender-white-gold-poly-2/',
            # 'https://www.besttliebco.com/product/weekender-white-gold-poly/',
            # 'https://www.besttliebco.com/product/weekender-china-bristle-2/',
            # 'https://www.besttliebco.com/product/weekender-china-bristle/',
            # 'https://www.besttliebco.com/product/hand-craft-stain-varnish-brushes-2/',
            # 'https://www.besttliebco.com/product/stain-varnish-brushes-trim/',
            # 'https://www.besttliebco.com/product/perfect-touch-100-polyester-3/',
            # 'https://www.besttliebco.com/product/perfect-touch-white-china-bristle-2/',
            # 'https://www.besttliebco.com/product/perfect-touch-white-china-bristle/',
            # 'https://www.besttliebco.com/product/perfect-touch-100-polyester-2/',
            # 'https://www.besttliebco.com/product/perfect-touch-100-polyester/',
            # 'https://www.besttliebco.com/product/minwax-polycrylic/',
            # 'https://www.besttliebco.com/product/minwax-polyurethane/',
            # 'https://www.besttliebco.com/product/minwax-wood-finish/',
            # 'https://www.besttliebco.com/product/extra-rough-surfaces/',
            # 'https://www.besttliebco.com/product/semi-rough-surfaces/',
            # 'https://www.besttliebco.com/product/semi-smooth-surfaces/',
            # 'https://www.besttliebco.com/product/smooth-surfaces/',
            # 'https://www.besttliebco.com/product/very-smooth-surfaces/',
            # 'https://www.besttliebco.com/product/tru-pro-salmon-woven/',
            # 'https://www.besttliebco.com/product/tru-pro-white-woven/',
            # 'https://www.besttliebco.com/product/tru-pro-nylon-polyester/',
            # 'https://www.besttliebco.com/product/tru-pro-triple-a-lambskin/',
            # 'https://www.besttliebco.com/product/tru-pro-mohair/',
            # 'https://www.besttliebco.com/product/tru-pro-frieze/',
            # 'https://www.besttliebco.com/product/tru-pro-hi-solvent/',
            # 'https://www.besttliebco.com/product/tru-pro-decotex/',
            # 'https://www.besttliebco.com/product/tru-pro-polypropylene-core/',
            # 'https://www.besttliebco.com/product/weekender-polyester-knit/',
            # 'https://www.besttliebco.com/product/polyester-knit-multi-packs-2pk/',
            # 'https://www.besttliebco.com/product/tru-pro-salmon-woven/',
            # 'https://www.besttliebco.com/product/tru-pro-white-woven/',
            # 'https://www.besttliebco.com/product/tru-pro-nylon-polyester/',
            # 'https://www.besttliebco.com/product/tru-pro-triple-a-lambskin/',
            # 'https://www.besttliebco.com/product/tru-pro-mohair/',
            # 'https://www.besttliebco.com/product/tru-pro-frieze/',
            # 'https://www.besttliebco.com/product/tru-pro-hi-solvent/',
            # 'https://www.besttliebco.com/product/tru-pro-decotex/',
            # 'https://www.besttliebco.com/product/tru-pro-polypropylene-core/',
            # 'https://www.besttliebco.com/product/earth-tones-100-recycled-materials/',
            # 'https://www.besttliebco.com/product/perfect-touch-polyester-knit/',
            # 'https://www.besttliebco.com/product/one-coat-single-rollers/',
            # 'https://www.besttliebco.com/product/one-coat-multi-packs/',
            # 'https://www.besttliebco.com/product/extra-rough-surfaces/',
            # 'https://www.besttliebco.com/product/semi-rough-surfaces/',
            # 'https://www.besttliebco.com/product/semi-smooth-surfaces/',
            # 'https://www.besttliebco.com/product/smooth-surfaces/',
            # 'https://www.besttliebco.com/product/very-smooth-surfaces/',
            # 'https://www.besttliebco.com/product/weekender-polyester-knit/',
            # 'https://www.besttliebco.com/product/polyester-knit-multi-packs-2pk/',
            # 'https://www.besttliebco.com/product/weekender-polyester-knit-multi-packs/',
            # 'https://www.besttliebco.com/product/blue-stripe-4/',
            # 'https://www.besttliebco.com/product/blue-stripe-4-cover-and-frame-combo/',
            # 'https://www.besttliebco.com/product/blue-stripe-6/',
            # 'https://www.besttliebco.com/product/mini-roller-grid/',
            # 'https://www.besttliebco.com/product/__trashed-2/',
            # 'https://www.besttliebco.com/product/bestt-liebco-mini-roller-tray/',
            # 'https://www.besttliebco.com/product/bestt-liebco-928/',
            # 'https://www.besttliebco.com/product/master-short-john/',
            # 'https://www.besttliebco.com/product/master-long-john-complete-6-12/',
            # 'https://www.besttliebco.com/product/master-little-john-complete-4/',
            # 'https://www.besttliebco.com/product/master-non-bubbling-4/',
            # 'https://www.besttliebco.com/product/master-non-bubbling-6-12/',
            # 'https://www.besttliebco.com/product/master-mohair-6-12/',
            # 'https://www.besttliebco.com/product/foam-4/',
            # 'https://www.besttliebco.com/product/foam-6/',
            # 'https://www.besttliebco.com/product/master-enameler-6-12/',
            # 'https://www.besttliebco.com/product/blue-stripe-4/',
            # 'https://www.besttliebco.com/product/blue-stripe-4-cover-and-frame-combo/',
            # 'https://www.besttliebco.com/product/blue-stripe-6/',
            # 'https://www.besttliebco.com/product/mini-roller-grid/',
            # 'https://www.besttliebco.com/product/__trashed-2/',
            # 'https://www.besttliebco.com/product/bestt-liebco-mini-roller-tray/',
            # 'https://www.besttliebco.com/product/bestt-liebco-928/',
            # 'https://www.besttliebco.com/product/master-long-john-complete-6-12/',
            # 'https://www.besttliebco.com/product/master-little-john-complete-4/',
            # 'https://www.besttliebco.com/product/master-non-bubbling-4/',
            # 'https://www.besttliebco.com/product/master-non-bubbling-6-12/',
            # 'https://www.besttliebco.com/product/master-mohair-6-12/',
            # 'https://www.besttliebco.com/product/foam-4/',
            # 'https://www.besttliebco.com/product/foam-6/',
            # 'https://www.besttliebco.com/product/master-enameler-6-12/',
            # 'https://www.besttliebco.com/product/master-all-purpose-4/',
            # 'https://www.besttliebco.com/product/mini-roller-grid/',
            # 'https://www.besttliebco.com/product/__trashed-2/',
            # 'https://www.besttliebco.com/product/bestt-liebco-mini-roller-tray/',
            # 'https://www.besttliebco.com/product/lambskin-s-mitts/',
            # 'https://www.besttliebco.com/product/bestt-liebco-polyester-bristle-blend/',
            # 'https://www.besttliebco.com/product/bestt-liebco-100-white-china-bristle/',
            # 'https://www.besttliebco.com/product/bestt-liebco-bestt-trim-stainer/',
            # 'https://www.besttliebco.com/product/bestt-liebco-first-mate/',
            # 'https://www.besttliebco.com/product/bestt-liebco-ruff-rider/',
            # 'https://www.besttliebco.com/product/bestt-liebco-masonry/',
            # 'https://www.besttliebco.com/product/bestt-liebco-hockey-stick/',
            # 'https://www.besttliebco.com/product/bestt-liebco-bent-radiator/',
            # 'https://www.besttliebco.com/product/bestt-liebco-928/',
            # 'https://www.besttliebco.com/product/bestt-liebco-888/',
            # 'https://www.besttliebco.com/product/bestt-liebco-fox/',
            # 'https://www.besttliebco.com/product/bestt-liebco-birch/',
            # 'https://www.besttliebco.com/product/bestt-liebco-2561/',
            # 'https://www.besttliebco.com/product/bestt-liebco-2560/',
            # 'https://www.besttliebco.com/product/master-stain-brush-2/',
            # 'https://www.besttliebco.com/product/master-stain-brush/',
            # 'https://www.besttliebco.com/product/bestt-liebco-lambskin-pieces/',
            # 'https://www.besttliebco.com/product/bestt-liebco-triple-a-lambskin-stain-pads/',
            # 'https://www.besttliebco.com/product/bestt-liebco-floor-applicators/',
            # 'https://www.besttliebco.com/product/lambskin-floor-applicator-pads/',
            # 'https://www.besttliebco.com/product/bestt-liebco-water-based-floor-applicator/',
            # 'https://www.besttliebco.com/product/water-based-floor-applicator-pads/',
            # 'https://www.besttliebco.com/product/bestt-liebco-polyester-bristle-blend/',
            # 'https://www.besttliebco.com/product/bestt-liebco-100-white-china-bristle/',
            # 'https://www.besttliebco.com/product/bestt-liebco-bestt-trim-stainer/',
            # 'https://www.besttliebco.com/product/bestt-liebco-first-mate/',
            # 'https://www.besttliebco.com/product/bestt-liebco-ruff-rider/',
            # 'https://www.besttliebco.com/product/bestt-liebco-masonry/',
            # 'https://www.besttliebco.com/product/bestt-liebco-hockey-stick/',
            # 'https://www.besttliebco.com/product/bestt-liebco-bent-radiator/',
            # 'https://www.besttliebco.com/product/bestt-liebco-888/',
            # 'https://www.besttliebco.com/product/bestt-liebco-fox/',
            # 'https://www.besttliebco.com/product/bestt-liebco-birch/',
            # 'https://www.besttliebco.com/product/bestt-liebco-2561/',
            # 'https://www.besttliebco.com/product/bestt-liebco-2560/',
            # 'https://www.besttliebco.com/product/master-stain-brush-2/',
            # 'https://www.besttliebco.com/product/master-stain-brush/',
            # 'https://www.besttliebco.com/product/lambskin-s-mitts/',
            # 'https://www.besttliebco.com/product/bestt-liebco-lambskin-pieces/',
            # 'https://www.besttliebco.com/product/bestt-liebco-triple-a-lambskin-stain-pads/',
            # 'https://www.besttliebco.com/product/bestt-liebco-floor-applicators/',
            # 'https://www.besttliebco.com/product/lambskin-floor-applicator-pads/',
            # 'https://www.besttliebco.com/product/bestt-liebco-water-based-floor-applicator/',
            # 'https://www.besttliebco.com/product/water-based-floor-applicator-pads/',
            # 'https://www.besttliebco.com/product/12-18-adjustable-frame/',
            # 'https://www.besttliebco.com/product/18-value-line-frame/',
            # 'https://www.besttliebco.com/product/3-utility-rollers/',
            # 'https://www.besttliebco.com/product/consumer-3-4-cage-frames/',
            # 'https://www.besttliebco.com/product/consumer-5-wire-frame/',
            # 'https://www.besttliebco.com/product/ec-30-end-caps/',
            # 'https://www.besttliebco.com/product/economy-prep-tools/',
            # 'https://www.besttliebco.com/product/heavy-duty-5-wire-4-frame/',
            # 'https://www.besttliebco.com/product/heavy-duty-5-wire-frames/',
            # 'https://www.besttliebco.com/product/long-handle-wire-brush/',
            # 'https://www.besttliebco.com/product/master-5-piece-kit-2/',
            # 'https://www.besttliebco.com/product/master-pin-lock-extension-poles/',
            # 'https://www.besttliebco.com/product/mini-roller-grid/',
            # 'https://www.besttliebco.com/product/pro-wood-handle-frame/',
            # 'https://www.besttliebco.com/product/tack-cloth/',
            # 'https://www.besttliebco.com/product/wire-brush-with-scraper/',
            # 'https://www.besttliebco.com/product/bestt-liebco-plated-metal-bucket-grids/',
            # 'https://www.besttliebco.com/product/master-5-piece-kit-2/',
            # 'https://www.besttliebco.com/product/earth-tones-4-piece-kit/',
            # 'https://www.besttliebco.com/product/master-5-piece-kit/',
            # 'https://www.besttliebco.com/product/one-coat-one-coat-kits/',
            # 'https://www.besttliebco.com/product/mini-roller-grid/',
            # 'https://www.besttliebco.com/product/one-coat-one-coat-kits/',
            # 'https://www.besttliebco.com/product/bestt-liebco-toughee-18-tray/',
            # 'https://www.besttliebco.com/product/bestt-liebco-551-metal-tray/',
            # 'https://www.besttliebco.com/product/bestt-liebco-4-quart-heavy-duty-tray/',
            # 'https://www.besttliebco.com/product/bestt-liebco-deepwell-plastic-tray/',
            # 'https://www.besttliebco.com/product/economy-tray/',
            # 'https://www.besttliebco.com/product/general-purpose-plastic-tray/',
            # 'https://www.besttliebco.com/product/__trashed-2/',
            # 'https://www.besttliebco.com/product/bestt-liebco-mini-roller-tray/',
            # 'https://www.besttliebco.com/product/bestt-liebco-pro1-metal-tray/',
            # 'https://www.besttliebco.com/product/bestt-liebco-standard-duty-metal-tray/',
            # 'https://www.besttliebco.com/product/12-18-adjustable-frame/',
            # 'https://www.besttliebco.com/product/18-value-line-frame/',
            # 'https://www.besttliebco.com/product/3-utility-rollers/',
            # 'https://www.besttliebco.com/product/consumer-3-4-cage-frames/',
            # 'https://www.besttliebco.com/product/consumer-5-wire-frame/',
            # 'https://www.besttliebco.com/product/ec-30-end-caps/',
            # 'https://www.besttliebco.com/product/heavy-duty-5-wire-4-frame/',
            # 'https://www.besttliebco.com/product/heavy-duty-5-wire-frames/',
            # 'https://www.besttliebco.com/product/pro-wood-handle-frame/',
            # 'https://www.besttliebco.com/product/bestt-liebco-kwik-change-frame/',
            # 'https://www.besttliebco.com/product/bestt-liebco-pipe-painters/',
            # 'https://www.besttliebco.com/product/bestt-liebco-rigid-yoke-18-frame/',
            # 'https://www.besttliebco.com/product/bestt-liebco-12-to-18-adjustable-frame/',
            # 'https://www.besttliebco.com/product/bestt-liebco-big-mike/',
            # 'https://www.besttliebco.com/product/master-pin-lock-extension-poles/',
            # 'https://www.besttliebco.com/product/bestt-liebco-wood-pole-with-threaded-tip/',
            # 'https://www.besttliebco.com/product/bestt-liebco-consumer-extension-pole/',
            # 'https://www.besttliebco.com/product/bestt-liebco-metal-pole-with-threaded-tip/',
            # 'https://www.besttliebco.com/product/bestt-liebco-klamp-tite-adaptor/',


]

l = 0
for url in myresult:
    l=l+1
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup)
    print('Product_urls', l, url)
    #

    a = ''
    b = ''
    image_d = ''
    f1 = ''

    """ 
    bread = soup.find("p", {"id": "breadcrumb"}).text.strip()
    bread_b = bread
    print("Bread...", bread_b)

    title = soup.find("h1", {"class": "page-title"}).text.strip()
    title_d = title
    print("Title...", title_d)

    para = soup.find("div", {"class": "summary entry-summary"}).find('p').text.replace('\n', '').strip()
    para_d = para
    print("paragraph...", para_d)

    try:
        attr_n = []
        attr_v = []
        table = soup.find("table", {"class": "shop_attributes"})
        th = table.find_all('th')
        td = table.find_all('td')
        for h in th:
            attr_n.append(h.text.strip())
        for t in td:
            attr_v.append(t.text.strip())
        # print(attr_n)
        # print(attr_v)
        for a, b in zip(attr_n, attr_v):
            print(a, "....", b)
            save_details: TextIO = open("bestt.xlsx", "a+", encoding="utf-8")
            save_details.write('\n' + url + "\t" + bread_b + "\t" + title_d + "\t" + para_d + "\t" + str(a) + "\t" + str(b).strip())
        print("\n ***** Record stored into  files. *****")
    except:
        save_details: TextIO = open("bestt.xlsx", "a+", encoding="utf-8")
        save_details.write('\n' + url + "\t" + bread_b + "\t" + title_d + "\t" + para_d + "\t" + str(a) + "\t" + str(b).strip())
        print("\n ***** Record stored into  files. *****")
        a = "Not Found"
        b = "Not Found"
        print("Not Found")

    try:
        image = soup.find('div', {"class": "images"}).find_all('img')
        for img in image:
            image_d = img.get('src')
            print("Image..", image_d)
            save_details: TextIO = open("bestt.xlsx", "a+", encoding="utf-8")
            save_details.write('\n' + url + "\t" + bread_b + "\t" + title_d + "\t" + para_d + "\t" + str(a) + "\t" + str(b).strip())
        print("\n ***** Images stored into  files. *****")
    except:
        image_d = "Not Found"
        print("Not Found Image")
    """

#

# =============================================== Table ======================================
    table = soup.find("table", {"class": "child-attributes hide-on-mobile"})
    tr = table.find_all('tr')
    for dd in tr:
        # find all th in table
        ss = dd.find_all('th')
        if not ss:
            print('null')
        else:
            pass
            save_details: TextIO = open("table.xlsx", "a+", encoding="utf-8")
            save_details.write('\n' + url)
            # print("\n ***** Record stored into files. *****")
            for f1 in ss:
                save_details.write('\t' + f1.text)
                continue

        #   find all td in table
        s = dd.find_all('td')
        if not s:
            continue
        # save_details: TextIO = open("table.xlsx", "a+", encoding="utf-8")
        # save_details.write('\n' + url)
        for f in s:
            print(f.text.replace('\n', ''))
            # print(f.text.strip().replace("\n", ""))
            pass
            # save_details.write('\t' + "rp_" + f.text)
        print("\n ***** Record stored into  files. *****")
