import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from typing.io import TextIO
from webdriver_manager.chrome import ChromeDriverManager

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
l = 0
Result = [
    'https://www.se.com/in/en/product/GVSUPS10KB4HS/galaxy-vs-ups-10kw-400v-1-internal-9ah-smart-modular-battery-string-expandable-to-4-startup-5x8/?range=65772-galaxy-vs&selected-node-id=27602447535',
    # 'https://www.se.com/in/en/product/E3MUPS80KHS/easy-ups-3m-80kva-400v-33-ups-for-external-batteries-startup-5x8/?parent-subcategory-id=8030&range=66001-easy-ups-3m&filter=business-3-critical-power-cooling-and-racks&selected-node-id=27590330530',
    # 'https://www.se.com/in/en/product/E3MUPS120KHS/easy-ups-3m-120kva-400v-33-ups-for-external-batteries-startup-5x8/?parent-subcategory-id=8030&range=66001-easy-ups-3m&filter=business-3-critical-power-cooling-and-racks&selected-node-id=27590330530',
    #
    # 'https://www.se.com/ww/en/product/18889/switchdisconnector-ng125na-3-poles-63-a/?%3Frange=1729-acti9-ng125-na&parent-subcategory-id=1610&selected-node-id=12367704277',

]

for url in Result:
    l = l + 1
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        # print(soup.prettify())
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        # opts = Options()
        # opts.headless = True
        # driver = webdriver.Chrome(r"/home/pradeep/Downloads/chromedriver_linux64/chromedriver", options=opts)
        # driver.get(url)
        # time.sleep(5)
        print("Products urls", l, url)
        bread = ''
        title_d = ''
        unic_d = ''
        image = ''
        pdf_d = ''
        try:
            print("************************************* Meta Description : ****************************************")
            meta_description = soup.find("meta", attrs={"name": "description"}).get("content").strip().replace("\n", "->")
            print("Meta_description......", meta_description)
        except:
            meta_description = "Not Found"
            print("Not Found")
        try:
            print("************************************* Meta Title : ****************************************")
            meta_title = soup.find('title').string.strip()
            print("Meta_title .....", meta_title)
        except:
            meta_title = "Not Found"
            print("Not Found")

        lists = []
        print("**************** BREADCRUMB ********************")
        sku = soup.find_all('div', {"class": "breadcrumb-container"})
        for x in sku:
            lists.append(x.text.replace("\n", ' '))
        bread = lists
        print("Breadcrumb...", bread)

        print("**************** TITLE  ********************")
        title = soup.find("h1", {"class": "main-product-info__description sc-pes-main-product-info"})
        title_d = title.text
        print("title...", title_d)

        try:
            print("**************** ITEM NUMBER ********************")
            unic = soup.find("h2", {"class": "main-product-info__bottom-item"})
            unic_d = unic.text
            print("unic...", unic_d)
        except:
            unic_d = "Not Found"
            print("Not Found")

        #
        try:
            for img in soup.find('div', class_="desktop-media sc-pes-media-gallery").find_all("img"):
                image = img['src']
                print("image...", image)
                save_details: TextIO = open("se_files.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + url + "\t" + meta_description + "\t" + meta_title + "\t" + "".join(bread) + "\t" + title_d + "\t" + unic_d + "\t" + image.strip())
                save_details.close()
            print("\n ***** Record stored into electric  files. *****")
        except:
            pass

        try:
            print("**************** PDF ********************")
            pdf = soup.find_all('a', {"class": "document-item"})
            for pd in pdf:
                pdf_d = (pd.get('href'))
                print("pdf = ", pdf_d)
                save_details: TextIO = open("se_files.xlsx", "a+", encoding="utf-8")
                save_details.write("\n" + url + "\t" + meta_description + "\t" + meta_title + "\t" + "".join(bread) + "\t" + title_d + "\t" + unic_d + "\t" + image + "\t" + pdf_d.strip())
                save_details.close()
            print("\n ***** Record stored into electric  files. *****")
        except:
            pdf_d = "Not Found"
            print("Not Found")

        # ================================ table=======================================
        print("******************** Table ********************")
        attr_name = []
        attr_value = []
        table = soup.find('div', {"class": "specifications specifications__view-more-content-wrapper"})
        th = table.find_all('th')
        td = table.find_all('td')
        for thh in th:
            attr_name.append(thh.text)
        for tdd in td:
            attr_value.append(tdd.text)
        for data1, data2 in zip(attr_name, attr_value):
            print(data1, "........", data2)
            save_details: TextIO = open("vollrath.xlsx", "a+", encoding="utf-8")
            save_details.write("\n" + url + "\t" + unic_d + "\t" + data1 + "\t" + data2)
            save_details.close()
        print("\n ***** Record stored into table  files. *****")

    except Exception as e:
        print(e)
