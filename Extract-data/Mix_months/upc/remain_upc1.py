import requests
from bs4 import BeautifulSoup
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from typing.io import TextIO

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
l = 0
mylist = [


    'https://www.zoro.com/search?q=panduit%20METS3-X',
    'https://www.zoro.com/search?q=panduit%20METS4-X',
    'https://www.zoro.com/search?q=panduit%20MLT2EH-LP',
    'https://www.zoro.com/search?q=panduit%20MLT4EH-LP',
    'https://www.zoro.com/search?q=panduit%20MLT4SH-LP',
    'https://www.zoro.com/search?q=panduit%20MLT6SH-LP',
    'https://www.zoro.com/search?q=panduit%20MLTFC2H-LP316',
    'https://www.zoro.com/search?q=panduit%20MLTFC2H-LP316RD',
    'https://www.zoro.com/search?q=panduit%20MLTFC4H-LP316',
    'https://www.zoro.com/search?q=panduit%20MLTFC4H-LP316BU',
    'https://www.zoro.com/search?q=panduit%20MLTFC4H-LP316GR',
    'https://www.zoro.com/search?q=panduit%20MLTFC4H-LP316RD',
    'https://www.zoro.com/search?q=panduit%20MLTFC4H-LP316WH',
    'https://www.zoro.com/search?q=panduit%20MLTFC4H-LP316YL',
    'https://www.zoro.com/search?q=panduit%20MMP172-C',
    'https://www.zoro.com/search?q=panduit%20MMP172-C316',
    'https://www.zoro.com/search?q=panduit%20MT150D-Q',
    'https://www.zoro.com/search?q=panduit%20MT1D-Q',
    'https://www.zoro.com/search?q=panduit%20MT350-C',
    'https://www.zoro.com/search?q=panduit%20MT350-C316',
    'https://www.zoro.com/search?q=panduit%20MTB150D-Q',
    'https://www.zoro.com/search?q=panduit%20MTB1D-Q',
    'https://www.zoro.com/search?q=panduit%20PBTMT',
    'https://www.zoro.com/search?q=panduit%20RGTBSG-C',
    'https://www.zoro.com/search?q=panduit%20GB2B0304TPI-1',
    'https://www.zoro.com/search?q=panduit%20GB2B0312TPI-1',
    'https://www.zoro.com/search?q=panduit%20GB4B0612TPI-1',
    'https://www.zoro.com/search?q=panduit%20GB4B0624TPI-1',
    'https://www.zoro.com/search?q=panduit%20RGRB19CN',
    'https://www.zoro.com/search?q=panduit%20RGRB19U',
    'https://www.zoro.com/search?q=panduit%20GACB-1',
    'https://www.zoro.com/search?q=panduit%20GPQC07-1/0',
    'https://www.zoro.com/search?q=panduit%20GPQC10-1/0',
    'https://www.zoro.com/search?q=panduit%20GPQC12-1/0',
    'https://www.zoro.com/search?q=panduit%20GPQC15-1/0',
    'https://www.zoro.com/search?q=panduit%20GCC6X6250-1/0',
    'https://www.zoro.com/search?q=panduit%20GCC6X6500-250',
    'https://www.zoro.com/search?q=panduit%20GCE1/0-1/0',
    'https://www.zoro.com/search?q=panduit%20GCE250-1/0',
    'https://www.zoro.com/search?q=panduit%20GCE250-250',
    'https://www.zoro.com/search?q=panduit%20GCE500-250',
    'https://www.zoro.com/search?q=panduit%20CGK630U',
    'https://www.zoro.com/search?q=panduit%20CGK630UA',
    'https://www.zoro.com/search?q=panduit%20ACG24K',
    'https://www.zoro.com/search?q=panduit%20CGR630U',
    'https://www.zoro.com/search?q=panduit%20RGS134-10-1Y',
    'https://www.zoro.com/search?q=panduit%20RGS134-1Y',
    'https://www.zoro.com/search?q=panduit%20RGS134B-1',
    'https://www.zoro.com/search?q=panduit%20HTCT2-2-1',
    'https://www.zoro.com/search?q=panduit%20HTWC2-2-1',
    'https://www.zoro.com/search?q=panduit%20RGCBNJ660P22',
    'https://www.zoro.com/search?q=panduit%20RGCBNJ660PY',
    'https://www.zoro.com/search?q=panduit%20RGEJ657PFY',
    'https://www.zoro.com/search?q=panduit%20RGREJ696Y',
    'https://www.zoro.com/search?q=panduit%20RGRKCBNJY',
    'https://www.zoro.com/search?q=panduit%20CNB4K',
    'https://www.zoro.com/search?q=panduit%20CNBK',
    'https://www.zoro.com/search?q=panduit%20CT-1550',
    'https://www.zoro.com/search?q=panduit%20CT-1525',
    'https://www.zoro.com/search?q=panduit%20CT-1570',
    'https://www.zoro.com/search?q=panduit%20CT-1700',
    'https://www.zoro.com/search?q=panduit%20CT-1002',
    'https://www.zoro.com/search?q=panduit%20CT-1003',
    'https://www.zoro.com/search?q=panduit%20CT-1123',
    'https://www.zoro.com/search?q=panduit%20CT-1000',
    'https://www.zoro.com/search?q=panduit%20F80-10-M',
    'https://www.zoro.com/search?q=panduit%20F84-12-TL',
    'https://www.zoro.com/search?q=panduit%20F87-25-C',
    'https://www.zoro.com/search?q=panduit%20FSD81-12-C',
    'https://www.zoro.com/search?q=panduit%20BS10-D',
    'https://www.zoro.com/search?q=panduit%20BS14-M',
    'https://www.zoro.com/search?q=panduit%20BS18-C',
    'https://www.zoro.com/search?q=panduit%20BSH10-E',
    'https://www.zoro.com/search?q=panduit%20BSH14-Q',
    'https://www.zoro.com/search?q=panduit%20BSN14-M',
    'https://www.zoro.com/search?q=panduit%20BSN18-C',
    'https://www.zoro.com/search?q=panduit%20BSN18-M',
    'https://www.zoro.com/search?q=panduit%20BSV10X-D',
    'https://www.zoro.com/search?q=panduit%20BSV14X-L',
    'https://www.zoro.com/search?q=panduit%20BSV18X-LY',
    'https://www.zoro.com/search?q=panduit%20D10-250-D',
    'https://www.zoro.com/search?q=panduit%20D14-250-M',
    'https://www.zoro.com/search?q=panduit%20DNF10-250FI-D',
    'https://www.zoro.com/search?q=panduit%20DNF10-250FIMB-D',
    'https://www.zoro.com/search?q=panduit%20DNF14-250FI-L',
    'https://www.zoro.com/search?q=panduit%20DNF18-250FIM-M',
    'https://www.zoro.com/search?q=panduit%20DNF18-250-M',
    'https://www.zoro.com/search?q=panduit%20DNFR14-250FIB-M',
    'https://www.zoro.com/search?q=panduit%20DNFR18-250FIB-M',
    'https://www.zoro.com/search?q=panduit%20DR14-250-M',
    'https://www.zoro.com/search?q=panduit%20DV10-250-D',
    'https://www.zoro.com/search?q=panduit%20DV10-250-L',
    'https://www.zoro.com/search?q=panduit%20DV10-250M-L',
    'https://www.zoro.com/search?q=panduit%20DV14-250B-C',
    'https://www.zoro.com/search?q=panduit%20DV14-250MB-C',
    'https://www.zoro.com/search?q=panduit%20DV18-250B-CY',
    'https://www.zoro.com/search?q=panduit%20DV18-250B-MY',
    'https://www.zoro.com/search?q=panduit%20DV18-250MB-CY',
    'https://www.zoro.com/search?q=panduit%20P10-14R-D',
    'https://www.zoro.com/search?q=panduit%20P10-38R-D',
    'https://www.zoro.com/search?q=panduit%20P10-6R-D',
    'https://www.zoro.com/search?q=panduit%20P10-8F-L',

]


for url in mylist:
    try:
        l = l + 1
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        driver.get(url)
        driver.get(driver.current_url)
        # time.sleep(3)
        get_url = driver.current_url
        print("current = ", get_url)
        print("Products Urls", l, url)
        all_data = []
        all = driver.find_element(By.XPATH, "//ul[@class='product-identifiers pl-0 pb-2 product-specifications__identifiers my-4 pl-4']")
        data = all.find_elements(By.TAG_NAME, "li")
        for da in data:
            all_data.append(da.text)
        try:
            zoro = all_data[0]
        except:
            zoro = "Not Found"
            print("Not Found")
        try:
            mfr = all_data[1]
        except:
            mfr = "Not Found"
            print("Not Found")
        try:
            upc = all_data[2]
        except:
            upc = "Not Found"
            print("Not Found")

        print("zoro = ", zoro)
        print("mfr = ", mfr)
        print("upc = ", upc)
        save_details: TextIO = open("1u.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + url + "\t" + get_url + "\t" + zoro + "\t" + mfr + "\t" + upc)
        save_details.close()
        print("\n ***** Record stored into upc  files. *****")

    except:
        save_details: TextIO = open("1remaining_urlsu.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + url)
        save_details.close()
        print("\n ***** Record stored into upc  files. *****")
        print("Not Found")
