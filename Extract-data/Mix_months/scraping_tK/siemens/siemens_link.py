import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from typing import TextIO
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#
opts = Options()
opts.headless = False
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
browser = webdriver.Chrome(r"/home/tajender/Downloads/chromedriver",options=opts)

l=[
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/A7B82500006691',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/3VL98604TJ01',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/5SP41926',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/5SP42926',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/5SP43926',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/8PQ91584AA54',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/8PQ91584AA55',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/3VL61802KN300AA0',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/5SY41207',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/5SY41638',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/3RT10566AF363PA0',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/3RU21160AB0',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/3RU21160CB0',
'https://mall.industry.siemens.com/mall/en/us/Catalog/Product/6EP13321LD10',

]

for li in l:

    browser.get(li)
    time.sleep(6)
    try:
        d = browser.execute_script(
        "return document.querySelector('#usercentrics-root').shadowRoot.querySelector('#uc-center-container  div.sc-iAEawV.jKNlvn  div  div  div  button:nth-child(1)')").click()
    except:
        pass
    try:


    # to=browser.find_element(By.XPATH,'//*[@id="searchArea"]/div[1]/div[7]/ul/li[1]/span/a').text
    # count=int(to.split('(')[1].replace(')',''))
    # co=int(round(count/20+2,0))
    # print(co)
        lin=[]
        # for ij in range(1,co):
        cl=browser.find_element(By.XPATH,'//*[@id="RelatedProductsKoRegion"]/div/div[1]/div/div/div[2]').click()
        c =browser.find_element(By.XPATH,'//*[@id="RelatedProductsKoRegion"]/div/div[1]/div/div/div[2]/a').text
        count = int(c.split('(')[1].replace(')', ''))
        co=int(round(count/4,0))
        print(co)


        for jh in range(0,co):
            links = browser.find_element(By.XPATH, '//*[@id="ProductDisplay"]').find_elements(By.TAG_NAME, 'a')
            for link in links:
                v=link.get_attribute('href')

                if v is not None and "login" not in v and "javascript" not in v :
                    lin.append(link.get_attribute('href'))
                    print(link.get_attribute('href'))
            try:
                browser.find_element(By.XPATH,'//*[@id="RelatedProductsCarousel"]/div/div[3]').click()
                time.sleep(4)
            except:
                pass

    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(2)
    # browser.find_element(By.XPATH,'//*[@id="RelatedProductsCarousel"]/div/div[3]').click()
    # time.sleep(2)
            result=[]
            [result.append(x) for x in lin if x not in result]

            print(result)
            for jg in result:
                save_details: TextIO = open("SIEMENS_LINK.txt", "a+", encoding="utf-8")
                save_details.write(
                    "\n" + "'" + jg + "',")
                print("End")

                save_details.close()
    except:
        pass



