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
    'https://www.championbuilt.com/store/p163/Drawer_Cabinet_DW2700-1501ILC.html', ]

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
        time.sleep(5)
        driver.get(product_url)
        print(product_url)

        # ============================================= DRAWER COMPARTMENTS ========================================
        print("*********************************** Technical Specifications: *************************************")
        try:
            draw_detail = ""
            draw = soup.find("tr", class_="wsite-multicol-tr").find_all("strong")
            draw1 = soup.find("tr", class_="wsite-multicol-tr").find_all("span")
            draw_details = []
            for drawer, dra in zip(draw, draw1):
                draw_details = drawer.text
                print(draw_details)
                draw_detail = dra.text
                print(draw_detail)

                images = soup.find_all("img", alt="Picture")
                for draw_image in images:
                    draw_image1 = draw_image['src']
                    print(draw_image1)
                    save_details: TextIO = open("data.txt", "a+", encoding="utf-8")
                    save_details.write("\n" + draw_details + "\t" + draw_detail + "\t" + draw_image1)
                    print("End")
                    save_details.close()
                    print("\n ***** Record stored into Table Specifications . *****")
                    print()
        except:
           pass
    except:
        save_details: TextIO = open("samples.txt", "a+", encoding="utf-8")
        save_details.write("\n" + product_url)
        save_details.close()
        print("\n**Record stored into txt file.**")
