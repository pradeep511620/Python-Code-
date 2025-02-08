import undetected_chromedriver.v2 as uc
import time
from typing import TextIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType


def main(url):
 py = '125.63.100.243'
 options = webdriver.ChromeOptions()
 options.add_argument('--proxy-server=%s' % py)
 #options.headless = True
 driver = webdriver.Chrome(r"/home/tajender/Downloads/chromedriver",options=options)
 driver.get(url)
 driver.delete_all_cookies()
 time.sleep(5)
 data=driver.page_source
 #print(data)
 soup = BeautifulSoup(data, 'html.parser')
 title = soup.find("h3", class_="header-primary--pd")
 aa = (title.text.strip() if title else "not given")
 print(aa)



if __name__ == '__main__':
    list=['https://whatismyipaddress.com']
    for x in range(0,len(list)):
     print(x)
     print(list[x])
     main(list[x])