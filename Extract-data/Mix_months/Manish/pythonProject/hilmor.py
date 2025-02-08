import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

base_url = 'https://www.hilmor.com/'

product_urls = [
    'https://www.hilmor.com/products/family/adjustable-wrenches',
    'https://www.hilmor.com/products/family/bending-tools',
    'https://www.hilmor.com/products/family/driving-tools',
    'https://www.hilmor.com/products/family/electronic-tools',
    'https://www.hilmor.com/products/family/flaring-tools',
    'https://www.hilmor.com/products/family/gauges',
    'https://www.hilmor.com/products/family/hoses',
    'https://www.hilmor.com/products/family/kit',
    'https://www.hilmor.com/products/family/leak-detector',
    'https://www.hilmor.com/products/family/manifolds',
    'https://www.hilmor.com/products/family/pliers-wrenches-wire-strippers',
    'https://www.hilmor.com/products/family/recovery-machine',
    'https://www.hilmor.com/products/family/refrigerant-scale',
    'https://www.hilmor.com/products/family/service-tools',
    'https://www.hilmor.com/products/family/sheet-metal-and-duct-tools',
    'https://www.hilmor.com/products/family/stainless-steel-evacuation-hoses',
    'https://www.hilmor.com/products/family/swaging-tools',
    'https://www.hilmor.com/products/family/tool-storage',
    'https://www.hilmor.com/products/family/tubing-cutters',
    'https://www.hilmor.com/products/family/copper-metal-tubing-cutters',
    'https://www.hilmor.com/products/family/plastic-tubing-cutters',
    'https://www.hilmor.com/products/family/utility-knives',
    'https://www.hilmor.com/products/family/vacuum-gauge',
    'https://www.hilmor.com/products/family/vacuum-pump-oil',
    'https://www.hilmor.com/products/family/vacuum-pumps',
    'https://www.hilmor.com/products/family/valve-core-removal-tools',
    'https://www.hilmor.com/products/family/work-lights',
    'https://www.hilmor.com/products/family/worksite-storage',
    'https://www.hilmor.com/products/family/bending-tools',
    'https://www.hilmor.com/products/compact-benders',
    # 'https://www.hilmor.com/products/spring-benders',
    'https://www.hilmor.com/products/tri-tube-bender-3-16-1-4-3-8-1-2',
    'https://www.hilmor.com/products/tri-tube-bender-3-16-1-4-5-16-3-8',
    'https://www.hilmor.com/products/family/adjustable-wrenches',
    # 'https://www.hilmor.com/products/digital-adjustable-torque-wrench',
    'https://www.hilmor.com/products/family/driving-tools',
    'https://www.hilmor.com/products/1-1-2-shaft-magnetic-nut-drivers',
    'https://www.hilmor.com/products/18-shaft-magnetic-nut-drivers',
    'https://www.hilmor.com/products/3-shaft-magnetic-nut-drivers',
    'https://www.hilmor.com/products/6-in-1-stubby-multi-tool',
    'https://www.hilmor.com/products/6-shaft-magnetic-nut-drivers',
    'https://www.hilmor.com/products/9-in-1-multi-tool',
    'https://www.hilmor.com/products/cabinet-tip-screwdrivers',
    'https://www.hilmor.com/products/fast-connect-bit-extension',
    'https://www.hilmor.com/products/fast-connect-magnetic-nut-driver-set',
    'https://www.hilmor.com/products/fast-connect-screwdriver-bit-set',
    'https://www.hilmor.com/products/impact-fastener-bits',
    'https://www.hilmor.com/products/keystone-tip-demolition-screwdrivers1',
    'https://www.hilmor.com/products/keystone-tip-screwdrivers',
    'https://www.hilmor.com/products/magnetic-nutsetters',
    'https://www.hilmor.com/products/phillips-tip-screwdrivers',
    'https://www.hilmor.com/products/precision-screwdriver-set',
    'https://www.hilmor.com/products/quick-change-magnetic-nut-drivers',
    'https://www.hilmor.com/products/ratcheting-9-in-1-multi-tool',
    'https://www.hilmor.com/products/reversible-magnetic-nut-driver',
    'https://www.hilmor.com/products/screwdriver-sets',
    'https://www.hilmor.com/products/terminal-block-screwdriver',
    'https://www.hilmor.com/products/family/electronic-tools',
    'https://www.hilmor.com/products/dual-readout-thermometer',
    'https://www.hilmor.com/products/thermocouple-clamp',
    'https://www.hilmor.com/products/family/flaring-tools',
    'https://www.hilmor.com/products/basic-flare-swage-kit',
    'https://www.hilmor.com/products/basic-flares',
    'https://www.hilmor.com/products/flare-swage',
    'https://www.hilmor.com/products/orbital-flare',
    'https://www.hilmor.com/products/orbital-flare-kit',
    'https://www.hilmor.com/products/quick-engage-flare-swage',
    'https://www.hilmor.com/products/family/gauges',
    'https://www.hilmor.com/products/analog-gauges',
    'https://www.hilmor.com/products/family/hoses',
    'https://www.hilmor.com/products/ball-valve-adapters',
    'https://www.hilmor.com/products/hoses',
    'https://www.hilmor.com/products/refrigeration-hoses-with-ball-valve-adapters',
    'https://www.hilmor.com/products/ball-valve-end-hoses',
    'https://www.hilmor.com/products/ball-valve-extension-hoses',
    'https://www.hilmor.com/products/set-of-3-ball-valve-ends',
    'https://www.hilmor.com/products/family/kit',
    'https://www.hilmor.com/products/starter-kit',
    'https://www.hilmor.com/products/family/leak-detector',
    'https://www.hilmor.com/products/heated-diode-refrigerant-leak-detector',
    'https://www.hilmor.com/products/infrared-refrigerant-leak-detector',
    'https://www.hilmor.com/products/family/Manifolds',
    'https://www.hilmor.com/products/2-valve-aluminum-manifold',
    'https://www.hilmor.com/products/2-valve-basic-manifold-with-60-hoses',
    'https://www.hilmor.com/products/4-valve-aluminum-manifold',
    'https://www.hilmor.com/products/4-valve-aluminum-manifold-set',
    'https://www.hilmor.com/products/family/pliers-wrenches-wire-strippers',
    'https://www.hilmor.com/products/adjustable-wrenches',
    'https://www.hilmor.com/products/crimping-tool',
    'https://www.hilmor.com/products/diagonal-cutting-pliers',
    'https://www.hilmor.com/products/linemans-pliers',
    'https://www.hilmor.com/products/long-nose-pliers',
    'https://www.hilmor.com/products/multi-function-pliers',
    'https://www.hilmor.com/products/quick-adjusting-tongue-groove-pliers',
    'https://www.hilmor.com/products/self-adjusting-wire-stripper',
    'https://www.hilmor.com/products/tongue-groove-pliers',
    'https://www.hilmor.com/products/wire-strippers',
    'https://www.hilmor.com/products/family/recovery-machine',
    'https://www.hilmor.com/products/lightweight-brushless-dc-refrigerant-recovery-machine',
    'https://www.hilmor.com/products/family/refrigerant-scale',
    'https://www.hilmor.com/products/refrigerant-scale',
    'https://www.hilmor.com/products/wireless-refrigerant-scale',
    'https://www.hilmor.com/products/family/sheet-metal-and-duct-tools',
    'https://www.hilmor.com/products/aluminum-handle-snip',
    'https://www.hilmor.com/products/aviation-snips',
    'https://www.hilmor.com/products/cable-tie-tensioning-tool',
    'https://www.hilmor.com/products/duct-knife',
    'https://www.hilmor.com/products/duct-slitting-tool',
    'https://www.hilmor.com/products/duct-stretcher',
    'https://www.hilmor.com/products/folding-tools',
    'https://www.hilmor.com/products/hand-crimpers',
    'https://www.hilmor.com/products/hand-seamers',
    'https://www.hilmor.com/products/hole-cutters',
    'https://www.hilmor.com/products/offset-aviation-snips',
    'https://www.hilmor.com/products/pipe-duct-cutter',
    'https://www.hilmor.com/products/pocket-brake',
    'https://www.hilmor.com/products/snap-lock-punch',
    'https://www.hilmor.com/products/tinner-snips',
    'https://www.hilmor.com/products/v-notcher',
    'https://www.hilmor.com/products/family/stainless-steel-evacuation-hoses',
    'https://www.hilmor.com/products/stainless-steel-hoses',
    'https://www.hilmor.com/products/family/swaging-tools',
    'https://www.hilmor.com/products/compact-swage-tool',
    'https://www.hilmor.com/products/deluxe-compact-swage-tool-kit',
    'https://www.hilmor.com/products/multi-swage-punch',
    'https://www.hilmor.com/products/punch-swage-set',
    'https://www.hilmor.com/products/family/copper-metal-tubing-cutters',
    'https://www.hilmor.com/products/large-diameter-tubing-cutters',
    'https://www.hilmor.com/products/small-diameter-tubing-cutters',
    'https://www.hilmor.com/products/family/plastic-tubing-cutters',
    'https://www.hilmor.com/products/plastic-tubing-cutter-1-5-16',
    'https://www.hilmor.com/products/ratcheting-plastic-tubing-cutter-1-58',
    'https://www.hilmor.com/products/ptc238-ratcheting-plastic-tubing-cutter',
    'https://www.hilmor.com/products/family/utility-knives',
    'https://www.hilmor.com/products/folding-utility-knife',
    'https://www.hilmor.com/products/retractable-utility-knife',
    'https://www.hilmor.com/products/family/vacuum-gauge',
    'https://www.hilmor.com/products/compact-vacuum-gauge',
    'https://www.hilmor.com/products/wireless-vacuum-gauge',
    'https://www.hilmor.com/products/family/vacuum-pumps',
    'https://www.hilmor.com/products/vacuum-pumps',
    'https://www.hilmor.com/products/family/vacuum-pump-oil',
    'https://www.hilmor.com/products/vacuum-pump-oil',
    'https://www.hilmor.com/products/family/service-tools',
    'https://www.hilmor.com/products/ball-end-hex-key-set',
    'https://www.hilmor.com/products/deburrers',
    'https://www.hilmor.com/products/fin-straightening-tools',
    'https://www.hilmor.com/products/folding-hex-key-sets',
    'https://www.hilmor.com/products/inspection-mirrors',
    'https://www.hilmor.com/products/lineset-cleaner',
    'https://www.hilmor.com/products/liquid-charger',
    'https://www.hilmor.com/products/locking-pliers-pinch-off-tool',
    'https://www.hilmor.com/products/nitrogen-purge-tool1',
    'https://www.hilmor.com/products/refrigerant-recovery-pliers',
    'https://www.hilmor.com/products/refrigerant-recovery-tool',
    'https://www.hilmor.com/products/service-wrenches',
    'https://www.hilmor.com/products/t-handle-hex-key-set',
    'https://www.hilmor.com/products/family/valve-core-removal-tools',
    'https://www.hilmor.com/products/valve-core-removal-tool',
    'https://www.hilmor.com/products/family/worksite-storage',
    'https://www.hilmor.com/products/backpack-bag',
    'https://www.hilmor.com/products/hvac-r-carrying-strap',
    'https://www.hilmor.com/products/hvac-r-general-purpose-gloves',
    'https://www.hilmor.com/products/hvac-r-refrigerant-tank-utility-backpack',
    'https://www.hilmor.com/products/hvac-r-sheet-metal-gloves',
    'https://www.hilmor.com/products/hvac-r-tote',
    'https://www.hilmor.com/products/tool-center-bag',
    'https://www.hilmor.com/products/zipper-pouch',
    'https://www.hilmor.com/products/family/work-lights',
    'https://www.hilmor.com/products/compact-work-light',
    'https://www.hilmor.com/products/mini-work-light',
    'https://www.hilmor.com/products/pivoting-work-light',
    'https://www.hilmor.com/products/pocket-work-light',
    'https://www.hilmor.com/products/portable-work-light',
    'https://www.hilmor.com/products/work-light'
]


def request_func(url):
    sess = requests.Session()
    response = sess.get(url)
    return response
    # print(response.text)


def selenium_fun(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(6)
    i = 0
    attr_name = []
    attr_value = []
    # table = driver.find_element(By.XPATH, "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[2]/table[1]")
    # table = driver.find_element(By.XPATH, "//body[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[2]/table[1]")
    table = driver.find_elements(By.XPATH, "//tbody//td")
    print(len(table))
    # print(table.text)
    for ta in table:
        print(ta.text)
    # print(table.text)
    th = table.find_elements(By.TAG_NAME, "td")
    for td in th:
        i += 1
        # print(i)
        print(td.text)
        if i % 2 != 0:
            attr_name.append(td.text.strip())
        else:
            attr_value.append(td.text.strip())
    for a, b, in zip(attr_name, attr_value):
        print(a, "....", b)
        # save_d:TextIO = open('table2.txt', 'a+', encoding='utf-8')
        # save_d.write("\n" + a + "\t" + b)
        # print('data save into file')


def product_url(url):
    response = request_func(url)
    soup = BeautifulSoup(response.content, 'lxml')

    # catalogue_links = soup.findAll(class_='dropdown-submenu')
    catalogue_links = soup.findAll(class_='nav')

    for catalogue_link in catalogue_links:
        for product_link in catalogue_link.find('li').findAll('a'):
            product_urls.append(product_link['href'])

    print(product_urls)


# def specification(table):


def product_details(url):
    response = request_func(url)
    soup = BeautifulSoup(response.content, 'lxml')

    pdfs_d = ''
    v_d = ''
    img_d = ''
    a=''
    b=''
    title = soup.find('h1').text
    print("title...", title)

    bread_crumb = ''
    for b in soup.find_all('ul', class_="breadcrumb"):
        dd = b.text.replace("\n", "").split(" ")
        for d in dd:
            if d != "":
                bread_crumb = f'{bread_crumb}{d}'

    description = soup.findAll(id='product-rating')
    product_description = description[1].text.replace('Download Instruction Sheet', '').replace('\n', ' ').strip()

    pdf_link = []
    for pdf in description:
        for pdf_url in pdf.findAll('a'):
            pdf_link.append(urljoin(base_url, pdf_url['href']))
    for pdfs in pdf_link:
        pdfs_d = pdfs
        print('pdf...', pdfs_d)
        save_d: TextIO = open('table_test.txt', 'a+', encoding='utf-8')
        save_d.write("\n" + url + "\t" + bread_crumb + "\t" + title + "\t" + product_description + "\t" + pdfs_d.strip())
    print('\n', "save data into pdf file")

    video_links = []
    videos = soup.findAll(class_="fancybox_video")
    for i in range(len(videos)):
        video_link = soup.find(id=f'video{i + 1}')
        video_links.append(video_link.find('source')['src'])
    # print(video_links)
    for v in video_links:
        v_d = v
        print("video_links...", v_d)
        save_d: TextIO = open('hilmor.txt', 'a+', encoding='utf-8')
        save_d.write("\n" + url + "\t" + bread_crumb + "\t" + title + "\t" + product_description + "\t" + pdfs_d + "\t" + v_d.strip())
    print('\n', "save data into video file")

    image_links = []
    try:
        image = soup.find(id="more-views").findAll('a')
        for image_link in image:
            image_links.append(urljoin(base_url, image_link['href']))
    except AttributeError:
        image = soup.find(id='product-share').find('a')['href']
        image_links.append(urljoin(base_url, image))
    for imgs in image_links:
        img_d = imgs
        print('images...', img_d)
        save_d: TextIO = open('hilmor.txt', 'a+', encoding='utf-8')
        save_d.write("\n" + url + "\t" + bread_crumb + "\t" + title + "\t" + product_description + "\t" + pdfs_d + "\t" + v_d + "\t" + img_d.strip())
    print('\n', "save data into images file")
    # print(image_links)

    i = 0
    attr_name = []
    attr_value = []
    attr_value2 = []

    for table in soup.find_all('table'):
        tds = table.findAll('tr')
        for tdss in tds[:-1]:
            if not tdss.find('table'):
                table_data = tdss.text.strip().replace('\n', '\t').split("\t")
                # print(table_data)
                i += 1
                # if i % 2 != 0:
                #     print(table_data[0])
                try:
                    attr_name.append(table_data[0])
                except IndexError:
                    pass
                try:
                    attr_value.append(table_data[1])
                except IndexError:
                    pass
                try:
                    attr_value2.append(table_data[2])
                except IndexError:
                    pass
        # t = table.findAll('table')
        # for d in t:
        #     print(d)

            # else:
            # print(tdss)
            # for inner_td in tds:
            #     print(inner_td.findAll('tr'))
            # print(inner_td.find('td').text.strip().replace('\n', '\t').split("\t"))
    # print(attr_value2)

    # print(attr_value)
    # print(attr_value2)
    # print(attr_name)

    for a, b, in zip(attr_name, attr_value):
        print(a, "....", b, "....")
        save_d: TextIO = open('hilmor.txt', 'a+', encoding='utf-8')
        save_d.write("\n" + url + "\t" + bread_crumb + "\t" + title + "\t" + product_description + "\t" + pdfs_d + "\t" + v_d + "\t" + img_d + "\t" + a + "\t" + b + "\t")
    print('\n', "save data into table file")


def main():
    for url in product_urls:
        if "family" not in url:
            # print(url)
            print(url)
            product_details(url)


# main()
# product_url(base_url)
# product_details('https://www.hilmor.com/products/compact-benders')
# product_details('https://www.hilmor.com/products/digital-adjustable-torque-wrench')
# product_details('https://www.hilmor.com/products/thermocouple-clamp')
# selenium_fun('https://www.hilmor.com/products/thermocouple-clamp')
