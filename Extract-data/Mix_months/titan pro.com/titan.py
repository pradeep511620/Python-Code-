from select import select

import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
l = 0
Result = [

    # 'https://www.packardonline.com/products/trcf50/',
    # 'https://www.packardonline.com/products/trcf35/',
    # 'https://www.packardonline.com/products/trcfd505/',
    # 'https://www.packardonline.com/products/toc175/',
    # 'https://www.packardonline.com/products/tocf5/',
    # 'https://www.packardonline.com/products/tocf15/',
    # 'https://www.packardonline.com/products/trcfd2515/',
    # 'https://www.packardonline.com/products/trc5/',
    # 'https://www.packardonline.com/products/tocfd2575/',
    # 'https://www.packardonline.com/products/tocfd353/',
    # 'https://www.packardonline.com/products/tocf20/',
    # 'https://www.packardonline.com/products/trcd3075/',
    # 'https://www.packardonline.com/products/toc5b/',
    # 'https://www.packardonline.com/products/tocf65/',
    # 'https://www.packardonline.com/products/trcd1010/',
    # 'https://www.packardonline.com/products/trc30/',
    # 'https://www.packardonline.com/products/trcfd553/',
    'https://www.packardonline.com/products/tocf25a/',
    'https://www.packardonline.com/products/trcfd4075/',
    'https://www.packardonline.com/products/trcf12-5/',
    'https://www.packardonline.com/products/tocfd305/',
    'https://www.packardonline.com/products/trcd5010/',
    'https://www.packardonline.com/products/trc70/',
    'https://www.packardonline.com/products/tocfd405/',
    'https://www.packardonline.com/products/tocf17-5/',
    'https://www.packardonline.com/products/trcd355/',
    'https://www.packardonline.com/products/toc75/',
    'https://www.packardonline.com/products/tocf12-5/',
    'https://www.packardonline.com/products/tocf2-5/',
    'https://www.packardonline.com/products/trcd253/',
    'https://www.packardonline.com/products/trcfd805/',
    'https://www.packardonline.com/products/tocfd505/',
    'https://www.packardonline.com/products/trcfd3075/',
    'https://www.packardonline.com/products/tocfd255/',
    'https://www.packardonline.com/products/tocd305/',
    'https://www.packardonline.com/products/trc17-5/',
    'https://www.packardonline.com/products/trcd3575/',
    'https://www.packardonline.com/products/tocd455/',
    'https://www.packardonline.com/products/trcfd2575/',
    'https://www.packardonline.com/products/trcf6/',
    'https://www.packardonline.com/products/trcfd6010/',
    'https://www.packardonline.com/products/trcfd3575/',
    'https://www.packardonline.com/products/trcfd2015/',
    'https://www.packardonline.com/products/toc40/',
    'https://www.packardonline.com/products/tocf50/',
    'https://www.packardonline.com/products/trc55/',
    'https://www.packardonline.com/products/toc60/',
    'https://www.packardonline.com/products/trcd254/',
    'https://www.packardonline.com/products/trcd304/',
    'https://www.packardonline.com/products/tocfd3575/',
    'https://www.packardonline.com/products/toc125/',
    'https://www.packardonline.com/products/tocd153/',
    'https://www.packardonline.com/products/trcf30/',
    'https://www.packardonline.com/products/trcd505/',
    'https://www.packardonline.com/products/tocf60/',
    'https://www.packardonline.com/products/trcd353/',
    'https://www.packardonline.com/products/trcd4575/',
    'https://www.packardonline.com/products/trcd6075/',
    'https://www.packardonline.com/products/trcf10/',
    'https://www.packardonline.com/products/tocfd605/',
    'https://www.packardonline.com/products/trcf5/',
    'https://www.packardonline.com/products/trcd405/',
    'https://www.packardonline.com/products/trcd4075/',
    'https://www.packardonline.com/products/trcfd4575/',
    'https://www.packardonline.com/products/toc10b/',
    'https://www.packardonline.com/products/tocf7-5/',
    'https://www.packardonline.com/products/trcd154/',
    'https://www.packardonline.com/products/trcfd353/',
    'https://www.packardonline.com/products/tocf40/',
    'https://www.packardonline.com/products/trcfd605/',
    'https://www.packardonline.com/products/tocfd2510/',
    'https://www.packardonline.com/products/tocf35/',
    'https://www.packardonline.com/products/trcd255/',
    'https://www.packardonline.com/products/toc45/',
    'https://www.packardonline.com/products/trc60/',
    'https://www.packardonline.com/products/tocfd155/',
    'https://www.packardonline.com/products/trcd303/',
    'https://www.packardonline.com/products/trcfd6075/',
    'https://www.packardonline.com/products/toc30/',
    'https://www.packardonline.com/products/tocfd304/',
    'https://www.packardonline.com/products/trcd305/',
    'https://www.packardonline.com/products/trcfd403/',
    'https://www.packardonline.com/products/tocf10/',
    'https://www.packardonline.com/products/trcd205/',
    'ttps://www.packardonline.com/products/trc65/',
   ' https://www.packardonline.com/products/tocd355/',
    'https://www.packardonline.com/products/trcf80/',
    'https://www.packardonline.com/products/trc7-5/',
   ' https://www.packardonline.com/products/tocfd455/',
    'https://www.packardonline.com/products/trcfd453/',
    'https://www.packardonline.com/products/tocd1010/',
    'https://www.packardonline.com/products/trcf70/',
    'https://www.packardonline.com/products/tocf2/',
    'https://www.packardonline.com/products/trcf40/',
    'https://www.packardonline.com/products/trc100/',
    'https://www.packardonline.com/products/trcf75/',
    'https://www.packardonline.com/products/tocf30/',
    'https://www.packardonline.com/products/tocf4/',
    'https://www.packardonline.com/products/toc3/',
    'https://www.packardonline.com/products/trcd5075/',
    'https://www.packardonline.com/products/trcf15/',
    'https://www.packardonline.com/products/tocfd555/',
    'https://www.packardonline.com/products/toc2/',
    'https://www.packardonline.com/products/trcfd405/',
    'https://www.packardonline.com/products/trcd7010/',
    'https://www.packardonline.com/products/trcfd7075/',
    'https://www.packardonline.com/products/trcfd355/',
    'https://www.packardonline.com/products/trcfd5075/',
    'https://www.packardonline.com/products/toc80/',
    'https://www.packardonline.com/products/trcf3/',
    'https://www.packardonline.com/products/tocf45/',
    'https://www.packardonline.com/products/trcd155/',
    'https://www.packardonline.com/products/trcfd705/',
   ' https://www.packardonline.com/products/trcf55/',
   ' https://www.packardonline.com/products/trcfd255/',
   ' https://www.packardonline.com/products/trcf25/',
    'https://www.packardonline.com/products/trcd8075/',
    'https://www.packardonline.com/products/toc5/',
    'https://www.packardonline.com/products/toc35/',
    'https://www.packardonline.com/products/trcd403/',
    'https://www.packardonline.com/products/toc75b/',
    'https://www.packardonline.com/products/trcfd5575/',
    'https://www.packardonline.com/products/tocfd5510/',
    'https://www.packardonline.com/products/tocf55/',
    'https://www.packardonline.com/products/trc20/',
    'https://www.packardonline.com/products/toc6/',
    'https://www.packardonline.com/products/trcf100/',
    'https://www.packardonline.com/products/trc50/',
    'https://www.packardonline.com/products/trcd805/',
    'https://www.packardonline.com/products/trcfd8075/',
    'https://www.packardonline.com/products/tocd255/',
    'https://www.packardonline.com/products/trc10/',
    'https://www.packardonline.com/products/trcf20/',
    'https://www.packardonline.com/products/trcf60/',
    'https://www.packardonline.com/products/trcfd354/',
    'https://www.packardonline.com/products/trc25/',
    'https://www.packardonline.com/products/trcf45/',
    'https://www.packardonline.com/products/toc10/',
    'https://www.packardonline.com/products/toc55/',
    'https://www.packardonline.com/products/trcfd555/',
    'https://www.packardonline.com/products/trcd7075/',
    'https://www.packardonline.com/products/trcfd603/',
    'https://www.packardonline.com/products/toc20/',
    'https://www.packardonline.com/products/trcfd4510/',
    'https://www.packardonline.com/products/tocfd354/',
    'https://www.packardonline.com/products/tocfd154/',
    'https://www.packardonline.com/products/trcfd503/',
    'https://www.packardonline.com/products/toc15/',
    'https://www.packardonline.com/products/tocfd2015/',
    'https://www.packardonline.com/products/trcd455/',
    'https://www.packardonline.com/products/tocf25/',
    'https://www.packardonline.com/products/trc12-5/',
    'https://www.packardonline.com/products/trcd555/',
    'https://www.packardonline.com/products/trcfd303/',
    'https://www.packardonline.com/products/tocd353/',
    'https://www.packardonline.com/products/trcfd205/',
    'https://www.packardonline.com/products/trcfd50125/',
    'https://www.packardonline.com/products/trcfd305/',
    'https://www.packardonline.com/products/toc4/',
    'https://www.packardonline.com/products/trcf17-5/',
    'https://www.packardonline.com/products/trc80/',
    'https://www.packardonline.com/products/trcd5575/',
    'https://www.packardonline.com/products/trcd705/',
    'https://www.packardonline.com/products/trc35/',
    'https://www.packardonline.com/products/tocfd3075/',
    'https://www.packardonline.com/products/toc70/',
    'https://www.packardonline.com/products/tocfd355/',
    'https://www.packardonline.com/products/trcd605/',
    'https://www.packardonline.com/products/tocd405/',
    'https://www.packardonline.com/products/toc50/',
    'https://www.packardonline.com/products/toc25/',
    'https://www.packardonline.com/products/trc15/',
    'https://www.packardonline.com/products/tocd55/',
    'https://www.packardonline.com/products/trcd8010/',
    'https://www.packardonline.com/products/trc40/',
    'https://www.packardonline.com/products/tocf6/',
    'https://www.packardonline.com/products/tocd155/',
    'https://www.packardonline.com/products/trc45/',
    'https://www.packardonline.com/products/tocfd4075/',
    'https://www.packardonline.com/products/trcfd8010/',
    'https://www.packardonline.com/products/tocf3/',
    'https://www.packardonline.com/products/trcfd455/',


]

for url in Result:
    try:
        l = l + 1
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        opts = Options()
        opts.headless = True
        driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
        driver.get(url)
        time.sleep(3)

        print("Products urls == : ", l,  url)
        print()
        u = ''
        u1 = ''
        pdf_d = ''
        try:
            print("*********************************** Mete Title : **************************************")
            meta_title = soup.title.string.strip()
            print("Meta Title = ", meta_title)
        except:
            meta_title = "Not Found"
            print("Not Found")
        #
        print("************************** BreadCrumb ***********************************")
        lists = []
        sku = soup.find_all('div', {"class": "breadcrumbs"})
        for x in sku:
            lists.append(x.text.replace("\n", ' '))
        bread = lists
        print("Breadcrumb = ", bread)

        print("************************** Title ***********************************")
        title = soup.find("h1", {"class": "title titleProduct"})
        title_d = title.text
        print("title = ", title_d)

        print("************************** Item Number ***********************************")
        unic = soup.find("div", {"class": "itemSku"})
        unic_d = unic.text
        print("unic = ", unic_d)

        try:
            print("********************** sales ***************************")
            sale = driver.find_element(by=By.XPATH, value='//*[@id="Contentplaceholder1_C022_Col00"]/div[2]')
            sales = sale.find_element(by=By.TAG_NAME, value='ul').find_elements(by=By.TAG_NAME, value='span')
            for each in sales:
                unit = each.text
                u = unit.split(": ")[0]
                u1 = unit.split(": ")[1]
                print(u, "=====", u1)
                save_details: TextIO = open("titan.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + url + "\t" + meta_title + "\t" + "".join(bread) + "\t" + title_d + "\t" + unic_d + "\t" + u + "\t" + u1)
                print("End")
                save_details.close()
                print("\n ***** Record stored into titan  1  files. *****")
        except:
            pdf_d = "Not Found"
            print("Not Found")

        try:
            print("************************** Feature ***********************************")
            feature = soup.find("div", {"id": "product-tab-0"})
            feature_d = (feature.text.strip())
            print("feature", feature_d)
        except:
            feature_d = "Not Found"
            print(feature_d)
        #
        try:
            pdf = driver.find_element(by=By.XPATH, value='//*[@id="Contentplaceholder1_C022_Col00"]/div[2]').find_elements(by=By.TAG_NAME, value='a')
            for pddf in pdf:
                pdf_d = pddf.get_attribute('href')
                save_details: TextIO = open("titan.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + url + "\t" + meta_title + "\t" + "".join(bread) + "\t" + title_d + "\t" + unic_d + "\t" + u + "\t" + u1 + "\t" + feature_d + "\t" + pdf_d)
                print("End")
                save_details.close()
                print("\n ***** Record stored into titan 2  files. *****")
        except:
            pdf_d = "Not Found"
            print("Not Found")

        # # ========================= image with soup =============================
        print("************************** Image ***********************************")
        image = soup.find('ul', {"class": "altViews"}).find_all('img')
        for img in image:
            image_d = (img.get('src'))
            print("image = ", image_d)
            save_details: TextIO = open("titan.xlsx", "a+", encoding="utf-8")
            save_details.write("\n" + url + "\t" + meta_title + "\t" + "".join(bread) + "\t" + title_d + "\t" + unic_d + "\t" + u + "\t" + u1 + "\t" + feature_d + "\t" + pdf_d + "\t" + image_d)
            print("End")
            save_details.close()
            print("\n ***** Record stored into titan 3  files. *****")


    # ========================= image with selenium =============================
    #     image = driver.find_element(by=By.CLASS_NAME, value='altViews').find_elements(by=By.TAG_NAME,value='img')
    #     for img in image:
    #         image_d = (img.get_attribute('src'))
    #         print("image = ", image_d)


    #   ================================ table ==================================
        try:
            print("********************** TABLE 1 SECTION ***************************")
            attr_name_d = []
            attr_value_d = []
            table = soup.find("table", {"class": "table-responsive-simple"})
            attr_name = table.find_all('th')
            attr_value = table.find_all('td')
            for th in attr_name:
                attr_name_d.append(th.text)
            for td in attr_value:
                attr_value_d.append(td.text)
                # print("attr_value", attr_value_d)
            for g, h, in zip(attr_name_d, attr_value_d):
                print(g, "====", h)
                save_details: TextIO = open("titan_table.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + url + "\t" + g + "\t" + "rp_"+h)
                print("End")
                save_details.close()
                print("\n ***** Record stored into titan table section 1  files. *****")
        except:
            print("Not Found")

    #    ==========================table2 ==================================
        try:
            print("********************** TABLE 2 SECTION ***************************")
            attr_name_d1 = []
            attr_value_d1 = []
            table2 = soup.find("div", {"id": "product-tab-2"})
            attr_name1 = table2.find_all('th')
            attr_value1 = table2.find_all('td')
            for th in attr_name1:
                attr_name_d1.append(th.text)
            for td in attr_value1:
                attr_value_d1.append(td.text)
            for y, u, in zip(attr_name_d1, attr_value_d1):
                print(y, "=======", u)
                save_details: TextIO = open("titan_table1.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + url + "\t" + y + "\t" + "rp_"+u)
                print("End")
                save_details.close()
                print("\n ***** Record stored into titan table section 2  files. *****")
        except Exception as e:
            print("Not Found")
            print(e)

    except Exception as e:
        print(e)










