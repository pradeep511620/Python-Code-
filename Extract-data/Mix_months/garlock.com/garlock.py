import time
from typing import TextIO

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = True

mylst = [

    # 'https://garlockequipment.com/no-30-dump-box-for-workhorse-300443.html',
    # 'https://garlockequipment.com/enforcer-sp-twin-saw-300591.html',
    # 'https://garlockequipment.com/9-hp-honda-ultra-cutter-300632.html',
    # 'https://garlockequipment.com/ultra-cutter-dust-saw-04-300635.html',
    # 'https://garlockequipment.com/forklift-for-r800-300763.html',
    # 'https://garlockequipment.com/gs-36-sweeper-301242.html',
    # 'https://garlockequipment.com/no-12-scratcher-400001.html',
    # 'https://garlockequipment.com/rotary-planer-400017.html',
    # 'https://garlockequipment.com/gravel-spreader-attachment-36-400025.html',
    # 'https://garlockequipment.com/ultra-cutter-mini-saw-301293.html',
    # 'https://garlockequipment.com/ultra-cutter-pro-13-hp-pull-start-301295.html',
    # 'https://garlockequipment.com/high-lift-fork-overall-assembly-407698.html',
    # 'https://garlockequipment.com/mustang-flat-free-g2-301467.html',
    # 'https://garlockequipment.com/mustang-pneumatic-tire-g2-301468.html',
    # 'https://garlockequipment.com/r800-g2-carefree-tires-301470.html',
    # 'https://garlockequipment.com/r800-g2-air-tires-301471.html',
    # 'https://garlockequipment.com/tuff-tray-with-pivot-frame-409459.html',
    # 'https://garlockequipment.com/g12-generator-skid-301477.html',
    # 'https://garlockequipment.com/rolling-kit-g12-generator-409730.html',
    # 'https://garlockequipment.com/sound-reduction-kit-g12-generator-409731.html',
    # 'https://garlockequipment.com/generator-trailer-mount-409789.html',
    # 'https://garlockequipment.com/g12-generator-with-rolling-kit-301524.html',
    # 'https://garlockequipment.com/roof-warrior-g5-210-001-909.html',
    # 'https://garlockequipment.com/tine-bar-complete-3-5-153947.html',
    # 'https://garlockequipment.com/trash-chute-support-system-300108.html',
    # 'https://garlockequipment.com/lgt-2-trailer-300118.html',
    # 'https://garlockequipment.com/air-conditioner-jack-complete-300228.html',
    # 'https://garlockequipment.com/30-cu-ft-dumper-300377.html',
    # 'https://garlockequipment.com/power-jack-material-mover-300531.html',
    # 'https://garlockequipment.com/pallet-packer-f-lite-tires-300556.html',
    # 'https://garlockequipment.com/packer-pal-carefree-tires-300557.html',
    # 'https://garlockequipment.com/big-giant-trailer-with-carefree-300565.html',
    # 'https://garlockequipment.com/super-tearoff-bar-400009.html',
    # 'https://garlockequipment.com/li-l-giant-trailer-w-featherlites-400016.html',
    # 'https://garlockequipment.com/trash-chute-hopper-400128.html',
    # 'https://garlockequipment.com/super-shingle-bar-400287.html',
    # 'https://garlockequipment.com/trash-tray-hoist-400794.html',
    # 'https://garlockequipment.com/insulation-fork-w-dual-wheels-400847.html',
    # 'https://garlockequipment.com/wheelbarrow-boxed-301286.html',
    # 'https://garlockequipment.com/cast-chute-assembly-408961.html',
    # 'https://garlockequipment.com/square-trash-chute-hoist-301443.html',
    # 'https://garlockequipment.com/chute-pallet-weld-garlock-green-408962green.html',
    # 'https://garlockequipment.com/pick-box-weld-garlock-green-408964green.html',
    # 'https://garlockequipment.com/square-trash-chute-system-301445.html',
    # 'https://garlockequipment.com/tuff-tray-twin-301473.html',
    # 'https://garlockequipment.com/smart-cart-w-tuff-tray-301474.html',
    # 'https://garlockequipment.com/trash-chute-support-pro-garlock-green-301386green.html',
    # 'https://garlockequipment.com/hopper-assembly-pro-garlock-green-408859green.html',
    # 'https://garlockequipment.com/hopper-pallet-weld-p-coat-green-408963green.html',
    # 'https://garlockequipment.com/5-extension-3-in-e-z-roll-carrier-409601.html',
    # 'https://garlockequipment.com/easy-roll-carrier-3-in-w-flat-free-301495.html',
    # 'https://garlockequipment.com/easy-roll-carrier-3-in-tubeless-tires-301496.html',
    # 'https://garlockequipment.com/parapet-adapter-square-chute-system-409587.html',
    # 'https://garlockequipment.com/pallet-packer-two-wheel-fork-dolly-with-flat-air-tires.html',
    # 'https://garlockequipment.com/obs-2022-150-gsx-301431.html',
    # 'https://garlockequipment.com/230-gsx-301432.html',
    # 'https://garlockequipment.com/ram-60-310-002-004.html',
    # 'https://garlockequipment.com/m1-a-ram-311-006-902.html',
    # 'https://garlockequipment.com/m2-a-ram-311-024-902.html',
    # 'https://garlockequipment.com/cyclone-standard-wand-301340.html',
    # 'https://garlockequipment.com/515-extruder-single-speed-301513.html',
    # 'https://garlockequipment.com/515-extruder-2-speed-301546.html',
    # 'https://garlockequipment.com/warning-line-flag-100-ft-5ft-153810.html',
    # 'https://garlockequipment.com/base-4-post-guardrail-galv-155159.html',
    # 'https://garlockequipment.com/base-4-post-guardrail-pcoat-yellow-155160.html',
    # 'https://garlockequipment.com/pin-lynch-38-x-2-50-155278.html',
    # 'https://garlockequipment.com/everlast-3-base-yellow-plastic-warn-line-300975.html',
    # 'https://garlockequipment.com/skydome-a-29-b-29-c-14-301097-2929s.html',
    # 'https://garlockequipment.com/skydome-a-36-b-36-c-18-301097-3636s.html',
    # 'https://garlockequipment.com/skydome-a-36-b-60-c-18-301097-3660s.html',
    # 'https://garlockequipment.com/skydome-a-48-b-48-c-20-301097-4848s.html',
    # 'https://garlockequipment.com/obs-2023-skydome-60-x-60-pcoat-301097-6060s.html',
    # 'https://garlockequipment.com/perimeter-clamp-box-of-4-garlock-301282.html',
    # 'https://garlockequipment.com/railguard-10-ft-std-hgt-pcoat-yellow-402335s.html',
    # 'https://garlockequipment.com/railguard-5-ft-std-hgt-pcoat-yellow-402337s.html',
    # 'https://garlockequipment.com/railguard-10-ft-std-hgt-galv-404654g.html',
    # 'https://garlockequipment.com/railguard-5-ft-std-hgt-galv-404656g.html',
    # 'https://garlockequipment.com/railguard-8-ft-std-hgt-404977s.html',
    # 'https://garlockequipment.com/railguard-8-ft-std-hgt-galv-406930g.html',
    # 'https://garlockequipment.com/screen-guard-24-x-24-301314-2424.html',
    # 'https://garlockequipment.com/screen-guard-28-x-28-301314-2828.html',
    # 'https://garlockequipment.com/screen-guard-28-x-36-301314-2836.html',
    # 'https://garlockequipment.com/screen-guard-36-x-36-301314-3636.html',
    # 'https://garlockequipment.com/screen-guard-36-x-52-301314-3652.html',
    # 'https://garlockequipment.com/screen-guard-42-x-42-301314-4242.html',
    # 'https://garlockequipment.com/screen-guard-52-x-52-301314-5252.html',
    # 'https://garlockequipment.com/base-4-post-yellow-w-pads-407723.html',
    # 'https://garlockequipment.com/base-4-post-galv-w-pads-407724.html',
    # 'https://garlockequipment.com/screen-guard-52-x-100-301314-52100.html',
    # 'https://garlockequipment.com/slab-clamp-301355.html',
    # 'https://garlockequipment.com/lifepoint-duo-concrete-wgts-301384.html',
    # 'https://garlockequipment.com/lifepoint-duo-steel-wgts-301385.html',
    # 'https://garlockequipment.com/railguard-gc-10-ft-std-hgt-yellow-409269s.html',
    # 'https://garlockequipment.com/railguard-gc-7-5-ft-std-hgt-yellow-409270s.html',
    # 'https://garlockequipment.com/railguard-gc-5-ft-std-hgt-yellow-409271s.html',
    # 'https://garlockequipment.com/base-2-post-gc-complete-409277.html',
    # 'https://garlockequipment.com/multi-man-cobra-cart-standard-g2-301463.html',
    # 'https://garlockequipment.com/life-point-transport-cart-complete-301511.html',
    # 'https://garlockequipment.com/life-point-tie-off-anchor-complete-301512.html',
    # 'https://garlockequipment.com/multi-man-cobra-cart-deluxe-g2-301528.html',
    # 'https://garlockequipment.com/warning-line-cone-156281.html',
    # 'https://garlockequipment.com/warning-line-base-156282.html',
    # 'https://garlockequipment.com/screen-guard-53-x-53-301314-5353.html',
    # 'https://garlockequipment.com/lifepoint-duo-cover-156315.html',
    # 'https://garlockequipment.com/everlast-wl-galv-bases-plastic-flags-301548.html',
    # 'https://garlockequipment.com/hatch-prot-30-36-x-36-54-galv-452-010-600.html',
    # 'https://garlockequipment.com/skyguard-36-60-w-to-36-60-l-galvanized-443-002-600.html',
    # 'https://garlockequipment.com/skyguard-36-60-w-to-36-60-l-yellow-443-003-001.html',
    # 'https://garlockequipment.com/skyguard-36-110-w-to-36-110-l-galv-443-004-600.html',
    # 'https://garlockequipment.com/skyguard-36-110-w-to-36-110-l-yellow-443-005-001.html',
    # 'https://garlockequipment.com/hatch-prot-30-36-x-36-54-yellow-452-010-001.html',
    # 'https://garlockequipment.com/hatch-prot-30-36-x-96-114-yellow-452-011-001.html',
    # 'https://garlockequipment.com/hatch-prot-30-36-x-96-114-galv-452-011-600.html',
    # 'https://garlockequipment.com/hatch-prot-32-48-x-42-60-yellow-452-012-001.html',
    'https://garlockequipment.com/hatch-prot-32-48-x-42-60-galv-452-012-600.html',

]


def extract_all_details(url1):
    r = requests.get(url1)
    soup = BeautifulSoup(r.content, 'html.parser')
    driver = webdriver.Chrome()
    driver.get(url1)
    time.sleep(4)
    # print(soup)
    print('Product-urls...', url1)
    print()
    image_d = ''

    meta_title = soup.find('title').string.strip()
    print('meta_title...', meta_title)

    title = soup.find("h1", {"class": "page-title"}).text.strip()
    print('title...', title)

    sku = soup.find("div", {"itemprop": "sku"}).text
    print('sku...', sku)

    price = soup.find('span', {"class": "price"}).text.strip()
    print('price...', price)
    try:
        des = soup.find("div", {"itemprop": "description"}).find('p').text.replace("\n", "").strip()
        print('des...', des)
    except:
        des = "Not Found"
        print("Not Found")

    try:
        des1 = soup.find("div", {"itemprop": "description"}).find('ul').text.replace("\n", "").strip()
        print('des1...', des1)
    except:
        des1 = "Not Found"
        print("Not Found")

    try:
        details = soup.find('div', {"class": "product attribute description"}).text.strip().replace('\n', '')
        print('details...', details)
        save_u: TextIO = open('garlock.txt', 'a+', encoding='utf-8')
        save_u.write(
            '\n' + url1 + "\t" + meta_title + "\t" + title + "\t" + sku + "\t" + price + "\t" + des + "\t" + des1 + "\t" + details.strip())
        print('save data in all details files')
    except:
        details = "Not Found"
        print("Not Found")

    #
    try:
        image = driver.find_element(By.XPATH, "//div[@class='product media']")
        images = image.find_elements(By.TAG_NAME, "img")
        for img in images:
            image_d = img.get_attribute('src')
            print(image_d)
            save_u: TextIO = open('garlock.txt', 'a+', encoding='utf-8')
            save_u.write('\n' + url1 + "\t" + meta_title + "\t" + title + "\t" + sku + "\t" + price + "\t" + des + "\t" + des1 + "\t" + details + "\t" + image_d.strip())
        print('save data in images files')
    except:
        image_d = "Not Found"
        print("Not Found")

    #
    try:
        i = 0
        attr_name = []
        attr_value = []
        table = soup.find("table").find_all('td')
        for dt in table:
            i += 1
            # print(i)
            # print(dt.text)
            if i % 2 != 0:
                attr_name.append(dt.text.strip())
            else:
                attr_value.append(dt.text.strip())
        for a, b in zip(attr_name, attr_value):
            print(a, "........", b)
            save_u: TextIO = open('garlock.txt', 'a+', encoding='utf-8')
            save_u.write(
                '\n' + url1 + "\t" + meta_title + "\t" + title + "\t" + sku + "\t" + price + "\t" + des + "\t" + des1 + "\t" + details + "\t" + image_d + "\t" + a + "\t" + b)
        print('save data in table files')
    except:
        print("Not Found")


for url in mylst:
    extract_all_details(url)
