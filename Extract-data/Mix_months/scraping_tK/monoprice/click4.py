

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from typing import TextIO

browser = webdriver.Chrome(r"/home/tajender/Downloads/chromedriver")
l =[
'https://www.monoprice.com/product?p_id=16086'

]

for url in l:
    browser.get(url)
    first_click = browser.find_elements(By.XPATH,'//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span')
    second_click = browser.find_elements(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[2]/div/span')
    third_click = browser.find_elements(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[3]/div/span')
    fourth_click = browser.find_elements(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[4]/div/span')
    # import pdb;
    #
    # pdb.set_trace()
    r = []
    s3 = []
    op=[]
    first_loop = (len(first_click) + 1)
    second_loop = (len(second_click) + 1)
    third_loop = (len(third_click) )
    fourth_loop = (len(third_click)+1)
    print(third_loop)
    # try:
    # if len(click_count) == 1:
    #     save_details: TextIO = open("1.txt", "a+", encoding="utf-8")
    #     save_details.write(
    #         "\n" + "'" + i + "'" + "\t" + "1")
    #     print("End")
    #     save_details.close()
    for entry1 in range(1, first_loop):
            first_click = browser.find_element(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span[' + str(entry1) + ']').click()
            time.sleep(4)
            try:
                c = browser.find_element(By.XPATH, '//*[@id="ltkpopup-close-button"]').click()

            except:
                pass
            f = browser.find_element(By.XPATH,'//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span[' + str(entry1) + ']')
            f = f.text
    # print(data)
            for entry2 in range(1, second_loop):
                second_click = browser.find_element(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[2]/div/span[' + str(entry2) + ']').click()
                time.sleep(4)
                f_r = browser.find_element(By.XPATH,
                                           '//*[@id="addCart"]/div[2]/div[1]/form[1]/span/span[2]')
                f2 = f_r.text
                f_r1 = browser.find_element(By.XPATH,
                                           '//*[@id="addCart"]/div[2]/div[1]/form[2]/span/span[2]')
                f4 = f_r1.text
                if f not in f2:
                    first_click = browser.find_element(By.XPATH,'//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span[' + str(entry1) + ']').click()
                    time.sleep(4)
                    continue

                for entry3 in range(1, third_loop):
                    third_click = browser.find_element(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[3]/div/span[' + str(entry3) + ']').click()
                    time.sleep(4)
                    try:
                        c = browser.find_element(By.XPATH, '//*[@id="ltkpopup-close-button"]').click()

                    except:
                        pass

                    f_r1 = browser.find_element(By.XPATH,
                                               '//*[@id="addCart"]/div[2]/div[1]/form[2]/span/span[2]')
                    f_r4 = browser.find_element(By.XPATH,
                                                '//*[@id="addCart"]/div[2]/div[1]/form[2]/span/span[2]')
                    f3 = f_r1.text
                    f5=f_r4.text
                    if f4 not in f3:
                        second_click = browser.find_element(By.XPATH,'//*[@id="addCart"]/div[2]/div[1]/form[2]/div/span[' + str(entry2) + ']').click()


                        time.sleep(4)
                        continue

                    for entry4 in range(1, fourth_loop):
                        fourth_click = browser.find_element(By.XPATH,'//*[@id="addCart"]/div[2]/div[1]/form[4]/div/span[' + str(entry4) + ']').click()
                        time.sleep(4)
                        try:
                            c = browser.find_element(By.XPATH, '//*[@id="ltkpopup-close-button"]').click()

                        except:
                            pass
                        f_r3 = browser.find_element(By.XPATH,
                                                    '//*[@id="addCart"]/div[2]/div[1]/form[3]/span/span[2]')
                        f6 = f_r3.text
                        if f5 not in f6:
                            third_click = browser.find_element(By.XPATH,'//*[@id="addCart"]/div[2]/div[1]/form[3]/div/span[' + str(entry3) + ']').click()

                            time.sleep(4)
                            continue
                        data = browser.page_source
                        soup = BeautifulSoup(data, 'html.parser')
                        l = soup.find('div', class_='prod-breadcrumb').find_all('a')
                        Breadcrumb = []
                        for i in l:
                            Breadcrumb.append(i.text)
                        print(Breadcrumb)

                        title = soup.find('div', class_='product-name').text
                        print(title)

                        item_no = soup.find('div', class_='product-code').text
                        print(item_no)

                        UPC = soup.find('div', class_='product-barcode').text
                        print(UPC)

                        price = soup.find('span', class_='sale-price').text.strip()
                        print(price)

                        try:
                            images = soup.find('div', class_='lightbox-gallerylist').find_all('a')
                            im = []
                            for ie in images:
                                im.append(ie.get('href'))
                            print(im)
                        except:
                            pass

                        value = soup.find_all('span', class_="mp-prod-attrform-label")
                        op = []
                        for i in value:
                            c = i.text.split('\n')
                            op.append(c)
                            print(c[1], c[2])

                        # for d in op:
                        #     print(d)
                        #     save_details: TextIO = open("monopriceclick2.txt", "a+", encoding="utf-8")
                        #     save_details.write(
                        #         "\n" + url + "\t" + item_no + "\t" + UPC + "\t" + '->'.join(Breadcrumb) + "\t" + ".".join(
                        #             im) + "\t" + price + "\t" + d[1].replace(':', '') + "\t" + d[2])
                        #     save_details.close()
                        #     print("End")
                        #     print("***********************************************************************************")
