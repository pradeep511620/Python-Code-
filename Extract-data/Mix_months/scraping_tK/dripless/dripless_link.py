import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from typing import TextIO
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.headless = False
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
browser = webdriver.Chrome(r"/home/tajender/Downloads/chromedriver",options=opts)
l=[
'https://dripless.com/en/driplessecwidcom/#!/ETS-Caulking-Guns/c/44608161',
]

for li in l:
    r=requests.get(li)
    # time.sleep(5)
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # time.sleep(4)

    # r=browser.page_source
    soup=BeautifulSoup(r.text,'html.parser')
    print(soup)
    # li=browser.find_element(By.XPATH,'//*[@id="my-store-2442022"]/div[2]/div/div/div[2]/div/div[2]/div').find_elements(By.CLASS_NAME,'grid-product__title-hover')
    # for l in li:
    #     print(l.get('href'))





