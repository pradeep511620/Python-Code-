

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from typing import TextIO
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = True
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
browser = webdriver.Chrome(r"/home/tajender/Downloads/chromedriver",chrome_options=opts)
l =[
#
# 'https://www.monoprice.com/product?p_id=38913',
# 'https://www.monoprice.com/product?p_id=41021',
# 'https://www.monoprice.com/product?p_id=30762',
# 'https://www.monoprice.com/product?p_id=4982',
# 'https://www.monoprice.com/product?p_id=13779',
# 'https://www.monoprice.com/product?p_id=24187',
# 'https://www.monoprice.com/product?p_id=13586',
# 'https://www.monoprice.com/product?p_id=39477',
# 'https://www.monoprice.com/product?p_id=31231',
# 'https://www.monoprice.com/product?p_id=15648',
# 'https://www.monoprice.com/product?p_id=13760',
# 'https://www.monoprice.com/product?p_id=12584',
# 'https://www.monoprice.com/product?p_id=42682',
# 'https://www.monoprice.com/product?p_id=13758',
# 'https://www.monoprice.com/product?p_id=42674',
# 'https://www.monoprice.com/product?p_id=13775',
# 'https://www.monoprice.com/product?p_id=42077',
# 'https://www.monoprice.com/product?p_id=13578',
# 'https://www.monoprice.com/product?p_id=13589',
# 'https://www.monoprice.com/product?p_id=3341',
# 'https://www.monoprice.com/product?p_id=42964',
# 'https://www.monoprice.com/product?p_id=13656',
# 'https://www.monoprice.com/product?p_id=36230',
# 'https://www.monoprice.com/product?p_id=13533',
# 'https://www.monoprice.com/product?p_id=13129',
# 'https://www.monoprice.com/product?p_id=40879',
# 'https://www.monoprice.com/product?p_id=9548',
# 'https://www.monoprice.com/product?p_id=5012',
'https://www.monoprice.com/product?p_id=24346',
'https://www.monoprice.com/product?p_id=2379',
'https://www.monoprice.com/product?p_id=288',
'https://www.monoprice.com/product?p_id=6989',
'https://www.monoprice.com/product?p_id=34227',
'https://www.monoprice.com/product?p_id=13410',
'https://www.monoprice.com/product?p_id=14774',
'https://www.monoprice.com/product?p_id=13561',
'https://www.monoprice.com/product?p_id=8106',
'https://www.monoprice.com/product?p_id=39075',
'https://www.monoprice.com/product?p_id=2270',
'https://www.monoprice.com/product?p_id=877',
'https://www.monoprice.com/product?p_id=886',
'https://www.monoprice.com/product?p_id=21794',
'https://www.monoprice.com/product?p_id=43702',
'https://www.monoprice.com/product?p_id=12757',
'https://www.monoprice.com/product?p_id=12797',
'https://www.monoprice.com/product?p_id=8182',
'https://www.monoprice.com/product?p_id=33',
'https://www.monoprice.com/product?p_id=545',
'https://www.monoprice.com/product?p_id=42993',
'https://www.monoprice.com/product?p_id=41278',
'https://www.monoprice.com/product?p_id=6015',
'https://www.monoprice.com/product?p_id=6019',
'https://www.monoprice.com/product?p_id=5999',
'https://www.monoprice.com/product?p_id=6002',
'https://www.monoprice.com/product?p_id=40783',
'https://www.monoprice.com/product?p_id=2404',
'https://www.monoprice.com/product?p_id=2810',
'https://www.monoprice.com/product?p_id=2218',
'https://www.monoprice.com/product?p_id=3030',
'https://www.monoprice.com/product?p_id=38394',
'https://www.monoprice.com/product?p_id=38384',
'https://www.monoprice.com/product?p_id=12843',
'https://www.monoprice.com/product?p_id=31190',
'https://www.monoprice.com/product?p_id=31195',
'https://www.monoprice.com/product?p_id=39631',
'https://www.monoprice.com/product?p_id=39241',
'https://www.monoprice.com/product?p_id=41940',
'https://www.monoprice.com/product?p_id=24283',
'https://www.monoprice.com/product?p_id=27926',
'https://www.monoprice.com/product?p_id=41939',
'https://www.monoprice.com/product?p_id=12857',
'https://www.monoprice.com/product?p_id=5137',
'https://www.monoprice.com/product?p_id=13919',
'https://www.monoprice.com/product?p_id=5447',
'https://www.monoprice.com/product?p_id=5443',
'https://www.monoprice.com/product?p_id=43177',
'https://www.monoprice.com/product?p_id=7671',
'https://www.monoprice.com/product?p_id=43193',
'https://www.monoprice.com/product?p_id=5309',
'https://www.monoprice.com/product?p_id=5284',
'https://www.monoprice.com/product?p_id=7679',
'https://www.monoprice.com/product?p_id=38785',
'https://www.monoprice.com/product?p_id=7684',
'https://www.monoprice.com/product?p_id=7675',
'https://www.monoprice.com/product?p_id=13823',
'https://www.monoprice.com/product?p_id=13833',
'https://www.monoprice.com/product?p_id=41771',
'https://www.monoprice.com/product?p_id=44317',
'https://www.monoprice.com/product?p_id=1303',
'https://www.monoprice.com/product?p_id=35133',
'https://www.monoprice.com/product?p_id=33642',
'https://www.monoprice.com/product?p_id=5586',
'https://www.monoprice.com/product?p_id=5346',
'https://www.monoprice.com/product?p_id=11502',
'https://www.monoprice.com/product?p_id=14916',
'https://www.monoprice.com/product?p_id=9768',
'https://www.monoprice.com/product?p_id=5576',
'https://www.monoprice.com/product?p_id=2747',
'https://www.monoprice.com/product?p_id=9764',
'https://www.monoprice.com/product?p_id=644',
'https://www.monoprice.com/product?p_id=5597',
'https://www.monoprice.com/product?p_id=653',
'https://www.monoprice.com/product?p_id=2009',
'https://www.monoprice.com/product?p_id=658',
'https://www.monoprice.com/product?p_id=38450',
'https://www.monoprice.com/product?p_id=6386',
'https://www.monoprice.com/product?p_id=5220',
'https://www.monoprice.com/product?p_id=2605',
'https://www.monoprice.com/product?p_id=6843',
'https://www.monoprice.com/product?p_id=11854',
'https://www.monoprice.com/product?p_id=11830',
'https://www.monoprice.com/product?p_id=11797',
'https://www.monoprice.com/product?p_id=2626',
'https://www.monoprice.com/product?p_id=42643',
'https://www.monoprice.com/product?p_id=8240',
'https://www.monoprice.com/product?p_id=5761',
'https://www.monoprice.com/product?p_id=6457',
'https://www.monoprice.com/product?p_id=7028',
'https://www.monoprice.com/product?p_id=21887',
'https://www.monoprice.com/product?p_id=6483',
'https://www.monoprice.com/product?p_id=40365',
'https://www.monoprice.com/product?p_id=24506',
'https://www.monoprice.com/product?p_id=27548',
'https://www.monoprice.com/product?p_id=7260',
'https://www.monoprice.com/product?p_id=8631',
'https://www.monoprice.com/product?p_id=42358',
'https://www.monoprice.com/product?p_id=4100',
'https://www.monoprice.com/product?p_id=4103',
'https://www.monoprice.com/product?p_id=18587',
'https://www.monoprice.com/product?p_id=16094',
'https://www.monoprice.com/product?p_id=33085',
'https://www.monoprice.com/product?p_id=10546',
'https://www.monoprice.com/product?p_id=39605',
'https://www.monoprice.com/product?p_id=13518',
'https://www.monoprice.com/product?p_id=2132',
'https://www.monoprice.com/product?p_id=43077',
'https://www.monoprice.com/product?p_id=5900',
'https://www.monoprice.com/product?p_id=36210',
'https://www.monoprice.com/product?p_id=3375',
'https://www.monoprice.com/product?p_id=24360',
'https://www.monoprice.com/product?p_id=13661',
'https://www.monoprice.com/product?p_id=13538',
'https://www.monoprice.com/product?p_id=8103',
'https://www.monoprice.com/product?p_id=43701',
'https://www.monoprice.com/product?p_id=880',
'https://www.monoprice.com/product?p_id=42959',
'https://www.monoprice.com/product?p_id=13672',
'https://www.monoprice.com/product?p_id=8108',
'https://www.monoprice.com/product?p_id=41007',
'https://www.monoprice.com/product?p_id=6201',
'https://www.monoprice.com/product?p_id=6262',
'https://www.monoprice.com/product?p_id=2602',
'https://www.monoprice.com/product?p_id=40371',
'https://www.monoprice.com/product?p_id=35113',
'https://www.monoprice.com/product?p_id=5296',
'https://www.monoprice.com/product?p_id=1302',
'https://www.monoprice.com/product?p_id=40129',
'https://www.monoprice.com/product?p_id=5308',
'https://www.monoprice.com/product?p_id=3342',
'https://www.monoprice.com/product?p_id=13784',
'https://www.monoprice.com/product?p_id=42675',
'https://www.monoprice.com/product?p_id=2749',
'https://www.monoprice.com/product?p_id=5300',
'https://www.monoprice.com/product?p_id=5301',
'https://www.monoprice.com/product?p_id=24193',
'https://www.monoprice.com/product?p_id=13592',
'https://www.monoprice.com/product?p_id=24183',
'https://www.monoprice.com/product?p_id=24188',
'https://www.monoprice.com/product?p_id=42079',
'https://www.monoprice.com/product?p_id=42683',
'https://www.monoprice.com/product?p_id=42688',
'https://www.monoprice.com/product?p_id=2661',
'https://www.monoprice.com/product?p_id=43083',
'https://www.monoprice.com/product?p_id=5298',
'https://www.monoprice.com/product?p_id=38788',
'https://www.monoprice.com/product?p_id=41280',
'https://www.monoprice.com/product?p_id=43073',
'https://www.monoprice.com/product?p_id=43079',
'https://www.monoprice.com/product?p_id=42985',
'https://www.monoprice.com/product?p_id=24362',
'https://www.monoprice.com/product?p_id=14788',
'https://www.monoprice.com/product?p_id=13521',
'https://www.monoprice.com/product?p_id=24192',
'https://www.monoprice.com/product?p_id=35057',
'https://www.monoprice.com/product?p_id=24375',
'https://www.monoprice.com/product?p_id=31363',
'https://www.monoprice.com/product?p_id=24407',
'https://www.monoprice.com/product?p_id=24411',
'https://www.monoprice.com/product?p_id=31373',
'https://www.monoprice.com/product?p_id=13562',
'https://www.monoprice.com/product?p_id=2165',
'https://www.monoprice.com/product?p_id=2330',
'https://www.monoprice.com/product?p_id=2331',
'https://www.monoprice.com/product?p_id=14309',
'https://www.monoprice.com/product?p_id=24419',
'https://www.monoprice.com/product?p_id=31384',
'https://www.monoprice.com/product?p_id=31380',
'https://www.monoprice.com/product?p_id=8630',
'https://www.monoprice.com/product?p_id=38378',
'https://www.monoprice.com/product?p_id=12859',
'https://www.monoprice.com/product?p_id=31192',
'https://www.monoprice.com/product?p_id=31188',
'https://www.monoprice.com/product?p_id=38301',
'https://www.monoprice.com/product?p_id=38303',
'https://www.monoprice.com/product?p_id=38305',
'https://www.monoprice.com/product?p_id=12858',
'https://www.monoprice.com/product?p_id=12840',
'https://www.monoprice.com/product?p_id=30771',
'https://www.monoprice.com/product?p_id=30767',
'https://www.monoprice.com/product?p_id=30770',
'https://www.monoprice.com/product?p_id=38914',
'https://www.monoprice.com/product?p_id=38904',
'https://www.monoprice.com/product?p_id=27919',
'https://www.monoprice.com/product?p_id=38333',
'https://www.monoprice.com/product?p_id=41943',
'https://www.monoprice.com/product?p_id=41942',
'https://www.monoprice.com/product?p_id=41944',
'https://www.monoprice.com/product?p_id=39905',
'https://www.monoprice.com/product?p_id=5138',
'https://www.monoprice.com/product?p_id=12298',
'https://www.monoprice.com/product?p_id=11040',
'https://www.monoprice.com/product?p_id=5902',
'https://www.monoprice.com/product?p_id=16092',
'https://www.monoprice.com/product?p_id=31189',
'https://www.monoprice.com/product?p_id=3997',
'https://www.monoprice.com/product?p_id=27923',
'https://www.monoprice.com/product?p_id=27932',
'https://www.monoprice.com/product?p_id=8102',
'https://www.monoprice.com/product?p_id=42678',
'https://www.monoprice.com/product?p_id=39481',
'https://www.monoprice.com/product?p_id=24285',
'https://www.monoprice.com/product?p_id=34221',
'https://www.monoprice.com/product?p_id=13135',
'https://www.monoprice.com/product?p_id=40880',
'https://www.monoprice.com/product?p_id=16091',
'https://www.monoprice.com/product?p_id=30766',
'https://www.monoprice.com/product?p_id=12839',
'https://www.monoprice.com/product?p_id=36213',
'https://www.monoprice.com/product?p_id=7672',
'https://www.monoprice.com/product?p_id=6003',
'https://www.monoprice.com/product?p_id=6020',
'https://www.monoprice.com/product?p_id=40370',
'https://www.monoprice.com/product?p_id=12955',
'https://www.monoprice.com/product?p_id=13929',
'https://www.monoprice.com/product?p_id=13928',

]

for url in l:
    browser.get(url)
    first_click = browser.find_elements(By.XPATH,'//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span')
    second_click = browser.find_elements(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[2]/div/span')
    # third_click = browser.find_elements(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[3]/div/span')
    # import pdb;
    #
    # pdb.set_trace()
    r = []
    s3 = []
    op=[]
    first_loop = (len(first_click) + 1)
    second_loop = (len(second_click) + 1)
    # third_loop = (len(third_click) + 1)
    # try:
    # if len(click_count) == 1:
    #     save_details: TextIO = open("1.txt", "a+", encoding="utf-8")
    #     save_details.write(
    #         "\n" + "'" + i + "'" + "\t" + "1")
    #     print("End")
    #     save_details.close()
    for entry1 in range(1, first_loop):
        first_click = browser.find_element(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span['+str(entry1)+']').click()
        f = browser.find_element(By.XPATH,
                                           '//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span[' + str(entry1) + ']')
        f=f.text
        time.sleep(4)
        try:
            c=browser.find_element(By.XPATH,'//*[@id="ltkpopup-close-button"]').click()

        except:
            pass
        for entry2 in range(1, second_loop):
                second_click = browser.find_element(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[2]/div/span['+str(entry2)+']').click()

                time.sleep(4)
                # print("oooooo")
                try:
                    c = browser.find_element(By.XPATH, '//*[@id="ltkpopup-close-button"]').click()

                except:
                    pass
                f_r = browser.find_element(By.XPATH,
                                           '//*[@id="addCart"]/div[2]/div[1]/form[1]/span/span[2]')
                f2=f_r.text
                if f not in f2:
                    first_click = browser.find_element(By.XPATH, '//*[@id="addCart"]/div[2]/div[1]/form[1]/div/span['+str(entry1)+']').click()
                    time.sleep(4)
                    continue
        # print(data)
                data = browser.page_source
                soup = BeautifulSoup(data, 'html.parser')
                l=soup.find('div',class_='prod-breadcrumb').find_all('a')
                Breadcrumb=[]
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

                images = soup.find('div', class_='lightbox-gallerylist').find_all('a')
                im = []
                for ie in images:
                    im.append(ie.get('href'))
                print(im)
                value=soup.find_all('span',class_="mp-prod-attrform-label")
                op=[]
                for i in value:
                    c=i.text.split('\n')
                    op.append(c)
                    print(c[1],c[2])
                for d in op:
                    print(d)
                    save_details: TextIO = open("monopriceclick2.txt", "a+", encoding="utf-8")
                    save_details.write(
                        "\n" + url + "\t" + item_no + "\t" + UPC + "\t" + '->'.join(Breadcrumb) + "\t" + ".".join(
                            im) + "\t" + price + "\t" + d[1].replace(':', '') + "\t" + d[2])
                    save_details.close()
                    print("End")
                    print("***********************************************************************************")

