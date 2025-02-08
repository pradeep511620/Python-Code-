import time
from typing import TextIO

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

myresult = ['https://www.championbuilt.com/store/p11/Drawer_Cabinet_NW600-0201ILC.html',
            # 'https://www.championbuilt.com/store/p11/Drawer_Cabinet_NW600-0201ILC.html',
            # 'https://www.championbuilt.com/store/p14/Drawer_Cabinet_NW600-0202ILC.html',
            # 'https://www.championbuilt.com/store/p14/Drawer_Cabinet_NW600-0202ILC.html',
            # 'https://www.championbuilt.com/store/p43/Drawer_Cabinet_NW600-0301ILC.html',
            # 'https://www.championbuilt.com/store/p43/Drawer_Cabinet_NW600-0301ILC.html',
            # 'https://www.championbuilt.com/store/p44/Drawer_Cabinet_NW600-0401ILC.html',
            # 'https://www.championbuilt.com/store/p44/Drawer_Cabinet_NW600-0401ILC.html',
            # 'https://www.championbuilt.com/store/p45/Drawer_Cabinet_NW1200-0301ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p45/Drawer_Cabinet_NW1200-0301ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p46/Drawer_Cabinet_NW1200-0401ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p46/Drawer_Cabinet_NW1200-0401ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p47/Drawer_Cabinet_NW1200-0402ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p47/Drawer_Cabinet_NW1200-0402ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p48/Drawer_Cabinet_NW1200-0501ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p48/Drawer_Cabinet_NW1200-0501ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p49/Drawer_Cabinet_NW1200-0502ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p49/Drawer_Cabinet_NW1200-0502ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p50/Drawer_Cabinet_NW1200-0601ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p50/Drawer_Cabinet_NW1200-0601ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p51/Drawer_Cabinet_NW1200-0701ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p51/Drawer_Cabinet_NW1200-0701ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p52/Drawer_Cabinet_NW1500-0401ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p52/Drawer_Cabinet_NW1500-0401ILC-FTB.html',
            # 'https://www.championbuilt.com/store/p53/Drawer_Cabinet_NW1500-0402ILC-FTB.html',
            'https://www.championbuilt.com/store/p53/Drawer_Cabinet_NW1500-0402ILC-FTB.html', ]

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
        price_details = ""
        # =============================================== Find price =================================================
        print('**************************************** Product Price **********************************************')
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

        # ============================================= Product Features ===========================================
        print('************************************** Product Specs and SKU ****************************************')
        sku_details = []
        clickable = driver.find_elements(By.CLASS_NAME, "wsite-com-product-option-color-container")
        for clicks in clickable:
            s = clicks.click()
            unic = driver.find_elements(By.ID, "wsite-com-product-sku")
            for sku in unic:
                sku_details.append(sku.text) if unic else "Not Found"

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
        k = 0
        while k < len(sku_details):
            i = 0
            while i < len(prod_i):
                j = 0
                while j < len(spec_i):
                    x = sku_details[k] if sku_details else 'Not Found'
                    print(x)
                    k = k + 1

                    table1 = (prod_i[i] if prod_i else "Not Found")
                    print(table1)
                    i = i + 1

                    table2 = (spec_i[j] if spec_i else "Not Found")
                    print(table2)
                    j = j + 1
        print()
    except:
        pass

"""
        # ============================================ Images ======================================================
        print('**************************************** All Product  Image ****************************************')
        all_img = []
        try:
            images = soup.find("div", id="wsite-com-product-images").find_all("img")
            for image_details in images:
                all_img.append(image_details['src'] if images else "Not Found")
            # print(all_img)
            # print(len(all_img))
        except:
            image = "Not Found"        

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
                print(table1)
                i += 1
                table2 = (spec_i[j] if spec_i else "Not Found")
                print(table2)
                j += 1
                save_details: TextIO = open("Table_Specifications.txt", "a+", encoding="utf-8")
                save_details.write("\n" + product_url + "\t" + ",".join(data1) + "\t" + table1 + "\t" + table2)
                print("End")
                save_details.close()
                print("\n ***** Record stored into Table Specifications . *****")
                   # tables specs

        # ================================== specs and sku number ====================
        # sku_details = []
        # clickable = driver.find_elements(By.CLASS_NAME, "wsite-com-product-option-color-container")
        # for clicks in clickable:
        #     s = clicks.click()
        #     unic = driver.find_elements(By.ID, "wsite-com-product-sku")
        #     for sku in unic:
        #         sku_details.append(sku.text) if unic else "Not Found"
        #
        # table1 = ""
        # table2 = ""
        # prod1 = soup.find_all('td', class_='cell')
        # prod = [p1.text.strip() for p1 in prod1 if p1 is not None]
        # prod_i = []
        # spec_i = []
        #
        # for i in range(0, len(prod)):
        #     if i % 2:
        #         spec_i.append(prod[i])
        #     else:
        #         prod_i.append(prod[i])
        # i = 0
        # # print(prod_i)
        # # print(spec_i)
        # data1 = ""
        # while i < len(prod_i):
        #     j = 0
        #     while j < len(spec_i):
        #         k = 0
        #         while k < len(sku_details):
        #             x = sku_details[k] if sku_details else 'Not Found'
        #             print(x)
        #             k = k + 1
        #
        #             table1 = (prod_i[i] if prod_i else "Not Found")
        #             print(table1)
        #             i = i + 1
        #
        #             table2 = (spec_i[j] if spec_i else "Not Found")
        #             print(table2)
        #             j = j + 1
        #             save_details: TextIO = open("Table_Specifications_sku.txt", "a+", encoding="utf-8")
        #             save_details.write("\n" + product_url + "\t" + x + "\t" + table1 + "\t" + table2)
        #             print("End")
        #             save_details.close()
        #             print("\n ***** Record stored into Table Specifications . *****")

        # ======================================== sku and images find  =============================================
        sku_details = []
        clickable = driver.find_elements(By.CLASS_NAME, "wsite-com-product-option-color-container")
        for clicks in clickable:
            s = clicks.click()
            unic = driver.find_elements(By.ID, "wsite-com-product-sku")
            for sku in unic:
                sku_details.append(sku.text)
                # print(sku_details)
        all_img = []
        images = soup.find("div", id="wsite-com-product-images").find_all("img")
        for image_details in images:
            all_img.append(image_details['src'])
        # print(all_img)
        i = 0
        while i < len(sku_details):
            j = 0
            while j < len(all_img):
                data1 = (sku_details[i] if sku_details else "Not Found")
                print(data1)
                i += 1
                data2 = (all_img[j] if all_img else "Not Found")
                print(data2)
                j += 1
                save_details: TextIO = open("sample_files.txt", "a+", encoding="utf-8")
                save_details.write("\n" + product_url + "\t" + ",".join(list1) + "\t" + title_details + "\t" + price_details + "\t" + Description + "\t" + data1 + "\t" + data2 + "\t" + Product_d + "\t" + draw_details + "\t" + ",".join(draw_image1))
                print("End")
                save_details.close()
                print("\n**Record stored into txt file.**")
        except:
            # pass
            save_details: TextIO = open("samples.txt", "a+", encoding="utf-8")
            save_details.write("\n" + product_url)
            save_details.close()
            print("\n**Record stored into txt file.**)
"""

