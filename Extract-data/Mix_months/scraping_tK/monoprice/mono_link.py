import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from typing import TextIO
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
d = uc.Chrome(options=chrome_options)
# opts.headless = True
# opts.add_argument("--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
# d = uc.Chrome(chrome_options=opts.headless)

g=[
'https://a183607.sitemaphosting.com/4119210/sitemap.xml',

]

for li in g:

    d.get(li)

    data = d.page_source
    # print(data)
    time.sleep(4)
    soup = BeautifulSoup(data, 'html.parser')
    l=soup.find_all('div',class_='tdmain')
    for link in l:
        print("'"+link.find('a').get('href')+"',")