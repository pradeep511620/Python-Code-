from select import select

import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
l = 0
Result = [
    # 'https://www.packardonline.com/products/prcfd4575a/',
    # 'https://www.packardonline.com/products/prcfd555a/',
    # 'https://www.packardonline.com/products/pocf25b/',
    # 'https://www.packardonline.com/products/pocd1010a/',
    # 'https://www.packardonline.com/products/poc5a/',
    # 'https://www.packardonline.com/products/prcfd2510a/',
    # 'https://www.packardonline.com/products/poc20a/',
    # 'https://www.packardonline.com/products/pocd204a/',
    # 'https://www.packardonline.com/products/poc40a/',
    # 'https://www.packardonline.com/products/pocfd353a/',
    # 'https://www.packardonline.com/products/pocd3575a/',
    # 'https://www.packardonline.com/products/prcd503a/',
    # 'https://www.packardonline.com/products/pocfd355a/',
    # 'https://www.packardonline.com/products/prcd304a/',
    'https://www.packardonline.com/products/prcfd5010a/',
    'https://www.packardonline.com/products/poc60a/',
    'https://www.packardonline.com/products/prcd6010a/',
    'https://www.packardonline.com/products/pocd205a/',
    'https://www.packardonline.com/products/pocfd2575a/',
    'https://www.packardonline.com/products/prcfd403a/',
    'https://www.packardonline.com/products/prcfd8075a/',
    'https://www.packardonline.com/products/prcfd355a/',
    'https://www.packardonline.com/products/pocf40a/',
    'https://www.packardonline.com/products/pocd55a/',
    'https://www.packardonline.com/products/pocfd3075a/',
    'https://www.packardonline.com/products/poc15a/',
    'https://www.packardonline.com/products/prcd303a/',
    'https://www.packardonline.com/products/pocd4515a/',
    'https://www.packardonline.com/products/prcf40a/',
    'https://www.packardonline.com/products/pocfd3010a/',
    'https://www.packardonline.com/products/pocf30a/',
    'https://www.packardonline.com/products/prcf80a/',
    'https://www.packardonline.com/products/pocf10a/',
    'https://www.packardonline.com/products/pocd253a/',
    'https://www.packardonline.com/products/pocfd2015a/',
    'https://www.packardonline.com/products/prcfd6010a/',
    'https://www.packardonline.com/products/pocfd154a/',
    'https://www.packardonline.com/products/prcd5510a/',
    'https://www.packardonline.com/products/pocd354a/',
    'https://www.packardonline.com/products/prcd455a/',
    'https://www.packardonline.com/products/prc7-5a/',
    'https://www.packardonline.com/products/pocfd305a/',
    'https://www.packardonline.com/products/prcf12-5a/',
    'https://www.packardonline.com/products/prc5a/',
    'https://www.packardonline.com/products/prcd5575a/',
    'https://www.packardonline.com/products/prcd8010a/',
    'https://www.packardonline.com/products/prcd404a/',
    'https://www.packardonline.com/products/prcf25a/',
    'https://www.packardonline.com/products/prc35a/',
    'https://www.packardonline.com/products/pocfd304a/',
    'https://www.packardonline.com/products/pocd154a/',
    'https://www.packardonline.com/products/prc60a/',
    'https://www.packardonline.com/products/tm44450a/',
    'https://www.packardonline.com/products/prcf45a/',
    'https://www.packardonline.com/products/pocfd4010a/',
    'https://www.packardonline.com/products/pocfd105a/',
    'https://www.packardonline.com/products/prcfd2515a/',
    'https://www.packardonline.com/products/prcd8075a/',
    'https://www.packardonline.com/products/pocd605a/',
    'https://www.packardonline.com/products/pocd505a/',
    'https://www.packardonline.com/products/prcfd4010a/',
    'https://www.packardonline.com/products/pocfd354a/',
    'https://www.packardonline.com/products/prcd353a/',
    'https://www.packardonline.com/products/prc12-5a/',
    'https://www.packardonline.com/products/prcd4510a/',
    'https://www.packardonline.com/products/tf40224a/',
    'https://www.packardonline.com/products/prcf50a/',
    'https://www.packardonline.com/products/tm52460a/',
    'https://www.packardonline.com/products/pocf3a/',
    'https://www.packardonline.com/products/prcd403a/',
    'https://www.packardonline.com/products/pocfd4075a/',
    'https://www.packardonline.com/products/tf52475a/',
    'https://www.packardonline.com/products/prcd453a/',
    'https://www.packardonline.com/products/pocfd4575a/',
    'https://www.packardonline.com/products/tf12440a/',
    'https://www.packardonline.com/products/pocf20a/',
    'https://www.packardonline.com/products/prc10a/',
    'https://www.packardonline.com/products/poc25a/',
    'https://www.packardonline.com/products/prcd4575a/',
    'https://www.packardonline.com/products/prcf15a/',
    'https://www.packardonline.com/products/prc15a/',
    'https://www.packardonline.com/products/prcfd705a/',
    'https://www.packardonline.com/products/prcfd5075a/',
    'https://www.packardonline.com/products/prcfd453a/',
    'https://www.packardonline.com/products/pocd4575a/',
    'https://www.packardonline.com/products/prcfd2015a/',
    'https://www.packardonline.com/products/pocf6a/',
    'https://www.packardonline.com/products/poc4a/',
    'https://www.packardonline.com/products/prcd80125a/',
    'https://www.packardonline.com/products/pocd153a/',
    'https://www.packardonline.com/products/pocd255a/',
    'https://www.packardonline.com/products/pocf15a/',
    'https://www.packardonline.com/products/prc40a/',
    'https://www.packardonline.com/products/prcfd406a/',
    'https://www.packardonline.com/products/tf22440a/',
    'https://www.packardonline.com/products/prcfd455a/',
    'https://www.packardonline.com/products/prcfd8010a/',
    'https://www.packardonline.com/products/poc12-5a/',
    'https://www.packardonline.com/products/pocfd205a/',
    'https://www.packardonline.com/products/prcd505a/',
    'https://www.packardonline.com/products/pocd2015a/',
    'https://www.packardonline.com/products/prcd253a/',
    'https://www.packardonline.com/products/poc55a/',
    'https://www.packardonline.com/products/prcfd6510a/',
    'https://www.packardonline.com/products/pocd4010a/',
    'https://www.packardonline.com/products/prcf30a/',
    'https://www.packardonline.com/products/tf40350a/',
    'https://www.packardonline.com/products/pocfd805a/',
    'https://www.packardonline.com/products/pocd305a/',
    'https://www.packardonline.com/products/pocd2515a/',
    'https://www.packardonline.com/products/prcf17-5a/',
    'https://www.packardonline.com/products/prc80a/',
    'https://www.packardonline.com/products/prcf90a/',
    'https://www.packardonline.com/products/prcf10a/',
    'https://www.packardonline.com/products/prcd6075a/',
    'https://www.packardonline.com/products/pocd4510a/',
    'https://www.packardonline.com/products/prcfd356a/',
    'https://www.packardonline.com/products/prcd305a/',
    'https://www.packardonline.com/products/pocfd3510a/',
    'https://www.packardonline.com/products/tf42440a/',
    'https://www.packardonline.com/products/pocf55a/',
    'https://www.packardonline.com/products/prcfd6075a/',
    'https://www.packardonline.com/products/pocd2575a/',
    'https://www.packardonline.com/products/pocfd555a/',
    'https://www.packardonline.com/products/prcd555a/',
    'https://www.packardonline.com/products/pocd5575a/',
    'https://www.packardonline.com/products/prc20a/',
    'https://www.packardonline.com/products/prcd3575a/',
    'https://www.packardonline.com/products/prc30a/',
    'https://www.packardonline.com/products/prcfd405a/',
    'https://www.packardonline.com/products/prcd5010a/',
    'https://www.packardonline.com/products/prcf55a/',
    'https://www.packardonline.com/products/pocfd1510a/',
    'https://www.packardonline.com/products/pocd2510a/',
    'https://www.packardonline.com/products/prcfd4075a/',
    'https://www.packardonline.com/products/pocd404a/',
    'https://www.packardonline.com/products/pocfd5075a/',
    'https://www.packardonline.com/products/pocf12-5a/',
    'https://www.packardonline.com/products/pocfd5510a/',
    'https://www.packardonline.com/products/prcfd3075a/',
    'https://www.packardonline.com/products/pocf70a/',
    'https://www.packardonline.com/products/prcfd2575a/',
    'https://www.packardonline.com/products/prcd4075a/',
    'https://www.packardonline.com/products/prcf7-5a/',
    'https://www.packardonline.com/products/prcfd5510a/',
    'https://www.packardonline.com/products/pocd254a/',
    'https://www.packardonline.com/products/pocfd6510a/',
    'https://www.packardonline.com/products/prcfd304a/',
    'https://www.packardonline.com/products/prcfd303a/',
    'https://www.packardonline.com/products/pocf50a/',
    'https://www.packardonline.com/products/prcfd805a/',
    'https://www.packardonline.com/products/pocd1510a/',
    'https://www.packardonline.com/products/pocd353a/',
    'https://www.packardonline.com/products/pocfd505a/',
    'https://www.packardonline.com/products/pocd1755a/',
    'https://www.packardonline.com/products/prcfd404a/',
    'https://www.packardonline.com/products/prcfd5575a/',
    'https://www.packardonline.com/products/poc70a/',
    'https://www.packardonline.com/products/prc55a/',
    'https://www.packardonline.com/products/pocd455a/',
    'https://www.packardonline.com/products/prcfd253a/',
    'https://www.packardonline.com/products/prc17-5a/',
    'https://www.packardonline.com/products/poc17-5a/',
    'https://www.packardonline.com/products/prcfd4510a/',
    'https://www.packardonline.com/products/prc25a/',
    'https://www.packardonline.com/products/pocfd255a/',
    'https://www.packardonline.com/products/poc50a/',
    'https://www.packardonline.com/products/prcfd255a/',
    'https://www.packardonline.com/products/pocfd155a/',
    'https://www.packardonline.com/products/prcf70a/',
    'https://www.packardonline.com/products/prcd3010a/',
    'https://www.packardonline.com/products/pocf80a/',
    'https://www.packardonline.com/products/prcf60a/',
    'https://www.packardonline.com/products/poc10a/',
    'https://www.packardonline.com/products/prcf20a/',
    'https://www.packardonline.com/products/prcfd7010a/',
    'https://www.packardonline.com/products/prcd3075a/',
    'https://www.packardonline.com/products/poc6a/',
    'https://www.packardonline.com/products/prcd5075a/',
    'https://www.packardonline.com/products/pocd405a/',
    'https://www.packardonline.com/products/prcf75a/',
    'https://www.packardonline.com/products/pocd6075a/',
    'https://www.packardonline.com/products/tf4031oema/',
    'https://www.packardonline.com/products/poc2a/',
    'https://www.packardonline.com/products/pocfd405a/',
    'https://www.packardonline.com/products/pocfd8075a/',
    'https://www.packardonline.com/products/pocfd403a/',
    'https://www.packardonline.com/products/pocd2010a/',
    'https://www.packardonline.com/products/prc100a/',
    'https://www.packardonline.com/products/pocf2a/',
    'https://www.packardonline.com/products/tm12440a/',
    'https://www.packardonline.com/products/prcfd605a/',
    'https://www.packardonline.com/products/pocd403a/',
    'https://www.packardonline.com/products/pocf60a/',
    'https://www.packardonline.com/products/pocd6010a/',
    'https://www.packardonline.com/products/prc50a/',
    'https://www.packardonline.com/products/pocfd2510a/',
    'https://www.packardonline.com/products/prcfd7075a/',
    'https://www.packardonline.com/products/pocd3510a/',
    'https://www.packardonline.com/products/prcfd3510a/',
    'https://www.packardonline.com/products/pocf17-5a/',
    'https://www.packardonline.com/products/poc35a/',
    'https://www.packardonline.com/products/prcd405a/',
    'https://www.packardonline.com/products/prcd255a/',
    'https://www.packardonline.com/products/pocf7-5a/',
    'https://www.packardonline.com/products/prcfd3575a/',
    'https://www.packardonline.com/products/pocfd3575a/',
    'https://www.packardonline.com/products/pocd258a/',
    'https://www.packardonline.com/products/tf42450a/',
    'https://www.packardonline.com/products/prcfd354a/',
    'https://www.packardonline.com/products/prcd355a/',
    'https://www.packardonline.com/products/prc31-5a/',
    'https://www.packardonline.com/products/pocd3075a/',
    'https://www.packardonline.com/products/pocd355a/',
    'https://www.packardonline.com/products/pocf5a/',
    'https://www.packardonline.com/products/prcd805a/',
    'https://www.packardonline.com/products/pocd555a/',
    'https://www.packardonline.com/products/prcd605a/',
    'https://www.packardonline.com/products/prcf35a/',
    'https://www.packardonline.com/products/pocd155a/',
    'https://www.packardonline.com/products/prcf65a/',
    'https://www.packardonline.com/products/pocd3010a/',
    'https://www.packardonline.com/products/poc45a/',
    'https://www.packardonline.com/products/prcd254a/',
    'https://www.packardonline.com/products/prcf5a/',
    'https://www.packardonline.com/products/pocf45a/',
    'https://www.packardonline.com/products/pocd303a/',
    'https://www.packardonline.com/products/poc30a/',
    'https://www.packardonline.com/products/prcd3510a/',
    'https://www.packardonline.com/products/prcfd353a/',
    'https://www.packardonline.com/products/prcd354a/',
    'https://www.packardonline.com/products/prcfd105a/',
    'https://www.packardonline.com/products/prcfd305a/',
    'https://www.packardonline.com/products/prcfd205a/',
    'https://www.packardonline.com/products/tm32440a/',
    'https://www.packardonline.com/products/prcd4010a/',
    'https://www.packardonline.com/products/poc80a/',
    'https://www.packardonline.com/products/prcfd456a/',
    'https://www.packardonline.com/products/pocf4a/',
    'https://www.packardonline.com/products/prcfd505a/',
    'https://www.packardonline.com/products/pocfd2515a/',
    'https://www.packardonline.com/products/prcfd60125a/',
    'https://www.packardonline.com/products/poc3a/',
    'https://www.packardonline.com/products/pocf2-5a/',
    'https://www.packardonline.com/products/pocfd605a/',
    'https://www.packardonline.com/products/prc70a/',
    'https://www.packardonline.com/products/pocf35a/',
    'https://www.packardonline.com/products/tm524100a/',
    'https://www.packardonline.com/products/pocd4075a/',
    'https://www.packardonline.com/products/poc7-5a/',
    'https://www.packardonline.com/products/prc45a/',
    'https://www.packardonline.com/products/pocfd455a/',

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

        print("Products urls == : ", l, url)
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
            lists.append(x.text.strip().replace("\n", ' '))
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
                save_details: TextIO = open("titanhd.xlsx", "a+", encoding="utf-8")
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
            feature_d = (feature.text.replace("\n", ''))
            print("feature", feature_d)
        except:
            feature_d = "Not Found"
            print(feature_d)
        #
        try:
            print("************************** pdf ***********************************")
            pdf = driver.find_element(by=By.XPATH,value='//*[@id="Contentplaceholder1_C022_Col00"]/div[2]').find_elements(by=By.TAG_NAME, value='a')
            for pddf in pdf:
                pdf_d = pddf.get_attribute('href')
                save_details: TextIO = open("titanhd.xlsx", "a+", encoding="utf-8")
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
            save_details: TextIO = open("titanhd.xlsx", "a+", encoding="utf-8")
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
                save_details: TextIO = open("titanhd_table.xlsx", "a+", encoding="utf-8")
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
                save_details: TextIO = open("titanhd_table1.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + url + "\t" + y + "\t" + "rp_"+u)
                print("End")
                save_details.close()
                print("\n ***** Record stored into titan table section 2  files. *****")
        except Exception as e:
            print("Not Found")
            print(e)

    except Exception as e:
        print(e)
