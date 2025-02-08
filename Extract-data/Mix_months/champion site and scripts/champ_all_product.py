import time
from typing import TextIO

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

myresult = [
    'https://www.championbuilt.com/store/p11/Drawer_Cabinet_NW600-0201ILC.html',
    'https://www.championbuilt.com/store/p11/Drawer_Cabinet_NW600-0201ILC.html',
    'https://www.championbuilt.com/store/p14/Drawer_Cabinet_NW600-0202ILC.html',
    'https://www.championbuilt.com/store/p14/Drawer_Cabinet_NW600-0202ILC.html',
    'https://www.championbuilt.com/store/p43/Drawer_Cabinet_NW600-0301ILC.html',
    'https://www.championbuilt.com/store/p43/Drawer_Cabinet_NW600-0301ILC.html',
    'https://www.championbuilt.com/store/p44/Drawer_Cabinet_NW600-0401ILC.html',
    'https://www.championbuilt.com/store/p44/Drawer_Cabinet_NW600-0401ILC.html',
    'https://www.championbuilt.com/store/p45/Drawer_Cabinet_NW1200-0301ILC-FTB.html',
    'https://www.championbuilt.com/store/p45/Drawer_Cabinet_NW1200-0301ILC-FTB.html',
    'https://www.championbuilt.com/store/p46/Drawer_Cabinet_NW1200-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p46/Drawer_Cabinet_NW1200-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p47/Drawer_Cabinet_NW1200-0402ILC-FTB.html',
    'https://www.championbuilt.com/store/p47/Drawer_Cabinet_NW1200-0402ILC-FTB.html',
    'https://www.championbuilt.com/store/p48/Drawer_Cabinet_NW1200-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p48/Drawer_Cabinet_NW1200-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p49/Drawer_Cabinet_NW1200-0502ILC-FTB.html',
    'https://www.championbuilt.com/store/p49/Drawer_Cabinet_NW1200-0502ILC-FTB.html',
    'https://www.championbuilt.com/store/p50/Drawer_Cabinet_NW1200-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p50/Drawer_Cabinet_NW1200-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p51/Drawer_Cabinet_NW1200-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p51/Drawer_Cabinet_NW1200-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p52/Drawer_Cabinet_NW1500-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p52/Drawer_Cabinet_NW1500-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p53/Drawer_Cabinet_NW1500-0402ILC-FTB.html',
    'https://www.championbuilt.com/store/p53/Drawer_Cabinet_NW1500-0402ILC-FTB.html',
    'https://www.championbuilt.com/store/p54/Drawer_Cabinet_NW1500-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p54/Drawer_Cabinet_NW1500-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p55/Drawer_Cabinet_NW1500-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p55/Drawer_Cabinet_NW1500-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p56/Drawer_Cabinet_NW1500-0602ILC-FTB.html',
    'https://www.championbuilt.com/store/p56/Drawer_Cabinet_NW1500-0602ILC-FTB.html',
    'https://www.championbuilt.com/store/p57/Drawer_Cabinet_NW1500-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p57/Drawer_Cabinet_NW1500-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p58/Drawer_Cabinet_NW1500-0702ILC-FTB.html',
    'https://www.championbuilt.com/store/p59/Drawer_Cabinet_NW1800-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p59/Drawer_Cabinet_NW1800-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p60/Drawer_Cabinet_NW1800-0502ILC-FTB.html',
    'https://www.championbuilt.com/store/p60/Drawer_Cabinet_NW1800-0502ILC-FTB.html',
    'https://www.championbuilt.com/store/p61/Drawer_Cabinet_NW1800-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p61/Drawer_Cabinet_NW1800-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p62/Drawer_Cabinet_NW1800-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p62/Drawer_Cabinet_NW1800-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p63/Drawer_Cabinet_NW1800-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p63/Drawer_Cabinet_NW1800-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p64/Drawer_Cabinet_NW1800-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p64/Drawer_Cabinet_NW1800-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p66/Drawer_Cabinet_SW1500-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p66/Drawer_Cabinet_SW1500-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p99/Drawer_Cabinet_SW1500-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p99/Drawer_Cabinet_SW1500-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p100/Drawer_Cabinet_SW1500-0702ILC-FTB.html',
    'https://www.championbuilt.com/store/p100/Drawer_Cabinet_SW1500-0702ILC-FTB.html',
    'https://www.championbuilt.com/store/p101/Drawer_Cabinet_SW1500-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p101/Drawer_Cabinet_SW1500-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p102/Drawer_Cabinet_SW1800-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p102/Drawer_Cabinet_SW1800-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p103/Drawer_Cabinet_SW1800-0402ILC-FTB.html',
    'https://www.championbuilt.com/store/p103/Drawer_Cabinet_SW1800-0402ILC-FTB.html',
    'https://www.championbuilt.com/store/p104/Drawer_Cabinet_SW1800-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p104/Drawer_Cabinet_SW1800-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p105/Drawer_Cabinet_SW1800-0502ILC-FTB.html',
    'https://www.championbuilt.com/store/p105/Drawer_Cabinet_SW1800-0502ILC-FTB.html',
    'https://www.championbuilt.com/store/p106/Drawer_Cabinet_SW1800-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p106/Drawer_Cabinet_SW1800-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p107/Drawer_Cabinet_SW1800-0602ILC-FTB.html',
    'https://www.championbuilt.com/store/p107/Drawer_Cabinet_SW1800-0602ILC-FTB.html',
    'https://www.championbuilt.com/store/p108/Drawer_Cabinet_SW1800-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p108/Drawer_Cabinet_SW1800-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p109/Drawer_Cabinet_SW1800-0702ILC-FTB.html',
    'https://www.championbuilt.com/store/p109/Drawer_Cabinet_SW1800-0702ILC-FTB.html',
    'https://www.championbuilt.com/store/p110/Drawer_Cabinet_SW1800-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p110/Drawer_Cabinet_SW1800-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p111/Drawer_Cabinet_SW1800-0802ILC-FTB.html',
    'https://www.championbuilt.com/store/p111/Drawer_Cabinet_SW1800-0802ILC-FTB.html',
    'https://www.championbuilt.com/store/p112/Drawer_Cabinet_SW1800-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p112/Drawer_Cabinet_SW1800-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p113/Drawer_Cabinet_SW1800-0902ILC-FTB.html',
    'https://www.championbuilt.com/store/p113/Drawer_Cabinet_SW1800-0902ILC-FTB.html',
    'https://www.championbuilt.com/store/p114/Drawer_Cabinet_SW1800-1001ILC-FTB.html',
    'https://www.championbuilt.com/store/p114/Drawer_Cabinet_SW1800-1001ILC-FTB.html',
    'https://www.championbuilt.com/store/p115/Drawer_Cabinet_SW2700-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p115/Drawer_Cabinet_SW2700-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p116/Drawer_Cabinet_SW2700-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p116/Drawer_Cabinet_SW2700-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p117/Drawer_Cabinet_SW2700-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p117/Drawer_Cabinet_SW2700-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p118/Drawer_Cabinet_SW2700-0702ILC-FTB.html',
    'https://www.championbuilt.com/store/p118/Drawer_Cabinet_SW2700-0702ILC-FTB.html',
    'https://www.championbuilt.com/store/p119/Drawer_Cabinet_SW2700-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p119/Drawer_Cabinet_SW2700-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p120/Drawer_Cabinet_SW2700-0802ILC-FTB.html',
    'https://www.championbuilt.com/store/p120/Drawer_Cabinet_SW2700-0802ILC-FTB.html',
    'https://www.championbuilt.com/store/p121/Drawer_Cabinet_SW2700-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p121/Drawer_Cabinet_SW2700-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p122/Drawer_Cabinet_SW2700-1001ILC-FTB.html',
    'https://www.championbuilt.com/store/p122/Drawer_Cabinet_SW2700-1001ILC-FTB.html',
    'https://www.championbuilt.com/store/p123/Drawer_Cabinet_SW2700-1002ILC-FTB.html',
    'https://www.championbuilt.com/store/p123/Drawer_Cabinet_SW2700-1002ILC-FTB.html',
    'https://www.championbuilt.com/store/p124/Drawer_Cabinet_SW2700-1101ILC-FTB.html',
    'https://www.championbuilt.com/store/p124/Drawer_Cabinet_SW2700-1101ILC-FTB.html',
    'https://www.championbuilt.com/store/p125/Drawer_Cabinet_SW2700-1201ILC-FTB.html',
    'https://www.championbuilt.com/store/p125/Drawer_Cabinet_SW2700-1201ILC-FTB.html',
    'https://www.championbuilt.com/store/p126/Drawer_Cabinet_SW2700-1202ILC-FTB.html',
    'https://www.championbuilt.com/store/p126/Drawer_Cabinet_SW2700-1202ILC-FTB.html',
    'https://www.championbuilt.com/store/p127/Drawer_Cabinet_SW2700-1301ILC-FTB.html',
    'https://www.championbuilt.com/store/p127/Drawer_Cabinet_SW2700-1301ILC-FTB.html',
    'https://www.championbuilt.com/store/p128/Drawer_Cabinet_SW2700-1501ILC-FTB.html',
    'https://www.championbuilt.com/store/p128/Drawer_Cabinet_SW2700-1501ILC-FTB.html',
    'https://www.championbuilt.com/store/p129/Drawer_Cabinet_SW2700-1601ILC-FTB.html',
    'https://www.championbuilt.com/store/p129/Drawer_Cabinet_SW2700-1601ILC-FTB.html',
    'https://www.championbuilt.com/store/p130/Drawer_Cabinet_EW1500-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p130/Drawer_Cabinet_EW1500-0401ILC-FTB.html',
    'https://www.championbuilt.com/store/p131/Drawer_Cabinet_EW1500-0402ILC-FTB.html',
    'https://www.championbuilt.com/store/p131/Drawer_Cabinet_EW1500-0402ILC-FTB.html',
    'https://www.championbuilt.com/store/p132/Drawer_Cabinet_EW1500-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p132/Drawer_Cabinet_EW1500-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p133/Drawer_Cabinet_EW1500-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p133/Drawer_Cabinet_EW1500-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p134/Drawer_Cabinet_EW1500-0602ILC-FTB.html',
    'https://www.championbuilt.com/store/p134/Drawer_Cabinet_EW1500-0602ILC-FTB.html',
    'https://www.championbuilt.com/store/p135/Drawer_Cabinet_EW1500-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p135/Drawer_Cabinet_EW1500-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p136/Drawer_Cabinet_EW1500-0802ILC-FTB.html',
    'https://www.championbuilt.com/store/p136/Drawer_Cabinet_EW1500-0802ILC-FTB.html',
    'https://www.championbuilt.com/store/p137/Drawer_Cabinet_EW1800-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p137/Drawer_Cabinet_EW1800-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p138/Drawer_Cabinet_EW1800-0502ILC-FTB.html',
    'https://www.championbuilt.com/store/p138/Drawer_Cabinet_EW1800-0502ILC-FTB.html',
    'https://www.championbuilt.com/store/p139/Drawer_Cabinet_EW1800-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p139/Drawer_Cabinet_EW1800-0601ILC-FTB.html',
    'https://www.championbuilt.com/store/p140/Drawer_Cabinet_EW1800-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p140/Drawer_Cabinet_EW1800-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p141/Drawer_Cabinet_EW1800-0702ILC-FTB.html',
    'https://www.championbuilt.com/store/p141/Drawer_Cabinet_EW1800-0702ILC-FTB.html',
    'https://www.championbuilt.com/store/p142/Drawer_Cabinet_EW1800-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p142/Drawer_Cabinet_EW1800-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p143/Drawer_Cabinet_EW1800-0902ILC-FTB.html',
    'https://www.championbuilt.com/store/p143/Drawer_Cabinet_EW1800-0902ILC-FTB.html',
    'https://www.championbuilt.com/store/p144/Drawer_Cabinet_EW2700-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p144/Drawer_Cabinet_EW2700-0501ILC-FTB.html',
    'https://www.championbuilt.com/store/p145/Drawer_Cabinet_EW2700-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p145/Drawer_Cabinet_EW2700-0701ILC-FTB.html',
    'https://www.championbuilt.com/store/p146/Drawer_Cabinet_EW2700-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p146/Drawer_Cabinet_EW2700-0801ILC-FTB.html',
    'https://www.championbuilt.com/store/p147/Drawer_Cabinet_EW2700-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p147/Drawer_Cabinet_EW2700-0901ILC-FTB.html',
    'https://www.championbuilt.com/store/p148/Drawer_Cabinet_EW2700-1101ILC-FTB.html',
    'https://www.championbuilt.com/store/p148/Drawer_Cabinet_EW2700-1101ILC-FTB.html',
    'https://www.championbuilt.com/store/p149/Drawer_Cabinet_EW2700-1201ILC-FTB.html',
    'https://www.championbuilt.com/store/p149/Drawer_Cabinet_EW2700-1201ILC-FTB.html',
    'https://www.championbuilt.com/store/p150/Drawer_Cabinet_EW2700-1401ILC-FTB.html',
    'https://www.championbuilt.com/store/p150/Drawer_Cabinet_EW2700-1401ILC-FTB.html',
    'https://www.championbuilt.com/store/p151/Drawer_Cabinet_DW1500-0401ILC.html',
    'https://www.championbuilt.com/store/p151/Drawer_Cabinet_DW1500-0401ILC.html',
    'https://www.championbuilt.com/store/p152/Drawer_Cabinet_DW1500-0601ILC.html',
    'https://www.championbuilt.com/store/p152/Drawer_Cabinet_DW1500-0601ILC.html',
    'https://www.championbuilt.com/store/p153/Drawer_Cabinet_DW1500-0801ILC.html',
    'https://www.championbuilt.com/store/p153/Drawer_Cabinet_DW1500-0801ILC.html',
    'https://www.championbuilt.com/store/p154/Drawer_Cabinet_DW1800-0501ILC.html',
    'https://www.championbuilt.com/store/p154/Drawer_Cabinet_DW1800-0501ILC.html',
    'https://www.championbuilt.com/store/p155/Drawer_Cabinet_DW1800-0701ILC.html',
    'https://www.championbuilt.com/store/p155/Drawer_Cabinet_DW1800-0701ILC.html',
    'https://www.championbuilt.com/store/p156/Drawer_Cabinet_DW1800-0901ILC.html',
    'https://www.championbuilt.com/store/p156/Drawer_Cabinet_DW1800-0901ILC.html',
    'https://www.championbuilt.com/store/p157/Drawer_Cabinet_DW2700-0501ILC.html',
    'https://www.championbuilt.com/store/p157/Drawer_Cabinet_DW2700-0501ILC.html',
    'https://www.championbuilt.com/store/p158/Drawer_Cabinet_DW2700-0601ILC.html',
    'https://www.championbuilt.com/store/p158/Drawer_Cabinet_DW2700-0601ILC.html',
    'https://www.championbuilt.com/store/p159/Drawer_Cabinet_DW2700-0701ILC.html',
    'https://www.championbuilt.com/store/p159/Drawer_Cabinet_DW2700-0701ILC.html',
    'https://www.championbuilt.com/store/p160/Drawer_Cabinet_DW2700-0901ILC.html',
    'https://www.championbuilt.com/store/p160/Drawer_Cabinet_DW2700-0901ILC.html',
    'https://www.championbuilt.com/store/p161/Drawer_Cabinet_DW2700-1001ILC.html',
    'https://www.championbuilt.com/store/p161/Drawer_Cabinet_DW2700-1001ILC.html',
    'https://www.championbuilt.com/store/p162/Drawer_Cabinet_DW2700-1201ILC.html',
    'https://www.championbuilt.com/store/p162/Drawer_Cabinet_DW2700-1201ILC.html',
    'https://www.championbuilt.com/store/p163/Drawer_Cabinet_DW2700-1501ILC.html',
    'https://www.championbuilt.com/store/p163/Drawer_Cabinet_DW2700-1501ILC.html',]

for row in myresult:
    try:
        product_url = row
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
        result = requests.get(product_url, headers=headers)
        soup = BeautifulSoup(result.content, 'html.parser')
        opts = Options()
        opts.headless = True
        driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
        driver.implicitly_wait(15)
        time.sleep(5)
        driver.get(product_url)
        print(product_url)
        # ============================================== Find Breadcrumb =============================================
        print('******************************************* Breadcrumb **********************************************')
        list1 = ""
        try:
            bread = soup.find('ul', id='wsite-com-breadcrumbs').find_all("span")  # ("h6", {'itemprop': "name"})
            list1 = []
            for b in bread:
                list1.append(b.text.strip() if b else "Not Found")
            print(list1)
            print()
        except:
            list1 = "Not Found"
        # =============================================== Find Title =================================================
        print('**************************************** Product Title **********************************************')
        title_details = ""
        try:
            title1 = soup.find("h2", itemprop="name")
            title_details = (title1.text.strip() if title1 else "Not Found")
            print(title_details)
            print()
        except:
            title1 = "Not Found"

        # =============================================== Find price =================================================
        print('**************************************** Product Price **********************************************')
        price_details = ""
        try:
            price = soup.find("span", class_="wsite-com-product-price-amount")
            price_details = (price.text.strip() if price else "Not Found")
            print(price_details)
            print()
        except:
            price_details = "Not Found"

        # ======================================== Product Description ===============================================
        print('*************************************** Product Description *****************************************')
        Description = ""
        try:
            desc1 = soup.find("div", id="wsite-com-product-short-description")
            Description = (desc1.text.strip().replace("\n", "") if desc1 else "Not Found")
            print(Description)
            print()
        except:
            desc = "Not Found"
        # ============================================= Product Features ===========================================
        print('***************************************** Product Features ******************************************')
        Product_d = ""
        try:
            feature = soup.find("div", id="wsite-com-product-tab").find("div", class_="paragraph").find_all("span")
            Product_d = ""
            for feature_details in feature:
                Product_d = Product_d + feature_details.text.strip().replace("/n", "")
            print(Product_d)
            print()
        except:
            feature_details = "Not Found"

        # ======================================== DRAWER COMPARTMENTS ===============================================
        print('************************************* DRAWER COMPARTMENTS *******************************************')
        draw_details = ""
        try:
            draw = soup.find("tbody", class_="wsite-multicol-tbody").find_all("span")
            for drawer in draw:
                draw_details = drawer.text
            print(draw_details)
        except:
            draw_details = "Not Found"
        draw_image1 = []
        try:
            images = soup.find_all("img", alt="Picture")
            for draw_image in images:
                draw_image1.append(draw_image['src'])
            print(draw_image1)
            print()

        except:
            draw_image1 = "not found"

        # ======================================== Table Specifications =========================================
        print("*********************************** Technical Specifications: *************************************")
        table1 = ""
        table2 = ""
        prod1 = soup.find_all('td', class_='cell')
        prod = [p1.text.strip() for p1 in prod1 if p1 is not None]
        prod_i = []
        spec_i = []
        for i in range(0, len(prod)):
            if i % 2:
                spec_i.append(prod[i])
            else:
                prod_i.append(prod[i])
        i = 0
        # print(prod_i)
        # print(spec_i)
        data1 = ""
        while i < len(prod_i):
            j = 0
            while j < len(spec_i):
                table1 = (prod_i[i] if prod_i else "Not Found")
                # print(table1)
                i += 1
                table2 = (spec_i[j] if spec_i else "Not Found")
                # print(table2)
                j += 1
                # save_details: TextIO = open("Table_Specifications.txt", "a+", encoding="utf-8")
                # save_details.write("\n" + product_url + "\t" + table1 + "\t" + table2)
                # print("End")
                # save_details.close()
                # print("\n ***** Record stored into Table Specifications . *****")
                # print()

        # ======================================== sku and images find  =============================================
        print("************************************ Sku Numbers And Images ****************************************")
        sku_details = []
        clickable = driver.find_elements(By.CLASS_NAME, "wsite-com-product-option-color-container")
        for clicks in clickable:
            s = clicks.click()
            unic = driver.find_elements(By.ID, "pdp_prodInfo-price product_price")
            for sku in unic:
                sku_details.append(sku.text)
                print(sku_details)
        all_img = []
        images = soup.find("div", id="wsite-com-product-images").find_all("img")
        for image_details in images:
            all_img.append(image_details['src'])
        # print("===image===",all_img)
        i = 0
        while i < len(sku_details):
            j = 0
            while j < len(all_img):
                data_sku = (sku_details[i] if sku_details else "Not Found")
                # print("data_sku:--", data_sku)
                i += 1
                data_image = (all_img[j] if all_img else "Not Found")
                # print("data_image:--", data_image)
                j += 1
                # save_details: TextIO = open("sample_files.txt", "a+", encoding="utf-8")
                # save_details.write("\n" + product_url + "\t" + ",".join(
                #     list1) + "\t" + title_details + "\t" + price_details + "\t" + Description + "\t" + data_sku + "\t" + data_image + "\t" + Product_d + "\t" + draw_details + "\t" + ",".join(
                #     draw_image1))
                # print("End")
                # save_details.close()
                # print("\n**Record stored into txt file.**")
    except Exception as e:
        # print(e)
        pass
        # save_details: TextIO = open("samples.txt", "a+", encoding="utf-8")
        # save_details.write("\n" + product_url)
        # save_details.close()
        # print("\n**Record stored into txt file.**")
