import time
from typing import TextIO

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

myresult = [
            # 'https://www.championbuilt.com/cht2416st.html',
            # 'https://www.championbuilt.com/cht7215.html',
            # 'https://www.championbuilt.com/cht2417tdr.html',
            # 'https://www.championbuilt.com/cht2415tdr.html',
            # 'https://www.championbuilt.com/cht1814sw.html',
            # 'https://www.championbuilt.com/cht36tb.html',
            # 'https://www.championbuilt.com/chttc2d.html',
            # 'https://www.championbuilt.com/cht4815.html',
            # 'https://www.championbuilt.com/cht2402.html',
            # 'https://www.championbuilt.com/chtr9620.html',
            # 'https://www.championbuilt.com/cht1214cav.html',
            # 'https://www.championbuilt.com/cht4804.html',
            # 'https://www.championbuilt.com/cht4816.html',
            # 'https://www.championbuilt.com/cht6015.html',
            # 'https://www.championbuilt.com/chtr3620.html',
            # 'https://www.championbuilt.com/chttc.html',
            # 'https://www.championbuilt.com/cht2416nd.html',
            # 'https://www.championbuilt.com/chtr10820.html',
            # 'https://www.championbuilt.com/cht3078.html',
            # 'https://www.championbuilt.com/cht3056.html',
            # 'https://www.championbuilt.com/cht60tb.html',
            # 'https://www.championbuilt.com/cht3616st.html',
            # 'https://www.championbuilt.com/cht5416st.html',
            # 'https://www.championbuilt.com/chtr7220.html',
            # 'https://www.championbuilt.com/cht5416.html',
            # 'https://www.championbuilt.com/cht2417.html',
            # 'https://www.championbuilt.com/chtr12020.html',
            # 'https://www.championbuilt.com/chtr2420.html',
            # 'https://www.championbuilt.com/cht6016.html',
            # 'https://www.championbuilt.com/cht3616.html',
            # 'https://www.championbuilt.com/cht2416.html',
            # 'https://www.championbuilt.com/cht1214c.html',
            # 'https://www.championbuilt.com/cht2415.html',
            # 'https://www.championbuilt.com/cht3615.html',
            # 'https://www.championbuilt.com/chtr6020.html',
            # 'https://www.championbuilt.com/cht3078rol.html',
            # 'https://www.championbuilt.com/cht6016st.html',
            # 'https://www.championbuilt.com/cht1214ri.html',
            # 'https://www.championbuilt.com/cht72tb.html',
            # 'https://www.championbuilt.com/cht4816st.html',
            # 'https://www.championbuilt.com/cht1214rm.html',
            # 'https://www.championbuilt.com/chtr5420.html',
            # 'https://www.championbuilt.com/chtr4820.html',
            # 'https://www.championbuilt.com/cht48tb.html',
            'https://www.championbuilt.com/cts15pc.html',
            'https://www.championbuilt.com/cts2pc.html',
            'https://www.championbuilt.com/cts3tr.html', ]


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
        driver.get(product_url)
        print(product_url)

        # ========================================= part Number ========================================================
        print("*********************************** Part Number: *************************************")
        h2 = soup.find("h2", class_="wsite-content-title").text.strip()
        h2_d = h2
        print("Part N == ", h2_d)
        print()
        # ========================================= Description =========================================================
        print("*********************************** Description : *************************************")
        product = soup.find("div", class_="paragraph").text.strip()
        product_d = product
        print("Description == ", product_d)
        print()
        #
        # # ============================================ Features =========================================================
        print("*********************************** Features: *************************************")
        f = soup.find("div", class_="tabbed-box-content tab-0")
        f_d = f.text.strip()
        print("Features == ", f_d)
        print()

        # ============================================ Specifications ===================================================
        print("***********************************  Specifications: *************************************")
        s = soup.find("div", class_="tabbed-box-content tab-1").text.strip()
        s_d = s
        print("Specifications = ", s_d)
        print()

        # ============================================ Options  =========================================================
        print("***********************************  Options: *************************************")
        op = soup.find("div", class_="tabbed-box-content tab-2").text.strip()
        op_d = op
        print("Options == ", op_d)
        print()

        # ============================================ Images =========================================================
        print("*********************************** Images: *************************************")
        image = soup.find("img", alt="Picture")
        image_d = image
        print("image_d", image_d.get('src'))
        print()
        save_details: TextIO = open("champion_section3.txt", "a+", encoding="utf-8")
        save_details.write("\n" + product_url + "\t" + h2_d + "\t" + product_d + "\t" + f_d + "\t" + s_d + "\t" + op_d + "\t" + str(image_d))
        print("End")
        save_details.close()
        print("\n ***** Record stored into champion_section_2 . *****")
        print()

        #============================================= color =========================================================
        # print("*********************************** color: *************************************")
        # co = soup.find("div", class_="wsite-section wsite-body-section wsite-background-365").find_all("div", class_="paragraph")
        # color_d = ""
        # for i in co:
        #     color_d = i.text
        #     print("color_d == ", color_d)
        #     print()
        #     save_details: TextIO = open("champion_section3.txt", "a+", encoding="utf-8")
        #     save_details.write("\n" + color_d)
        #     print("End")
        #     save_details.close()
        #     print("\n ***** Record stored into champion_section_2 . *****")
        #     # print
        # ============================================ color image =========================================================
        # print("*********************************** color image: *************************************")
        # image1 = soup.find_all("div", class_="wsite-section-wrap")[2].find_all_next('img')
        # for x in image1:
        #     image2 = x.get('src')
        #     print("image2 == ", image2)


    except Exception as e:
        print(e)
        # pass
        save_details: TextIO = open("samples.txt", "a+", encoding="utf-8")
        save_details.write("\n" + product_url)
        save_details.close()
        print("\n**Record stored into txt file.**")



