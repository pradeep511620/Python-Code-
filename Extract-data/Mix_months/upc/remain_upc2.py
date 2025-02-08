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

    'https://www.zoro.com/search?q=panduit%20P10-8R-D',
    'https://www.zoro.com/search?q=panduit%20P14-14R-M',
    'https://www.zoro.com/search?q=panduit%20P14-6F-C',
    'https://www.zoro.com/search?q=panduit%20P14-6R-M',
    'https://www.zoro.com/search?q=panduit%20P14-8F-C',
    'https://www.zoro.com/search?q=panduit%20P14-8F-M',
    'https://www.zoro.com/search?q=panduit%20P14-8R-M',
    'https://www.zoro.com/search?q=panduit%20P18-10R-M',
    'https://www.zoro.com/search?q=panduit%20P18-6F-M',
    'https://www.zoro.com/search?q=panduit%20P18-6R-M',
    'https://www.zoro.com/search?q=panduit%20P4-14R-T',
    'https://www.zoro.com/search?q=panduit%20P4-38R-T',
    'https://www.zoro.com/search?q=panduit%20P4-56R-T',
    'https://www.zoro.com/search?q=panduit%20P6-38R-T',
    'https://www.zoro.com/search?q=panduit%20PH14-6R-Q',
    'https://www.zoro.com/search?q=panduit%20PN10-8F-D',
    'https://www.zoro.com/search?q=panduit%20PN14-14R-M',
    'https://www.zoro.com/search?q=panduit%20PN14-6R-M',
    'https://www.zoro.com/search?q=panduit%20PN14-8F-C',
    'https://www.zoro.com/search?q=panduit%20PN18-10R-M',
    'https://www.zoro.com/search?q=panduit%20PN18-6F-M',
    'https://www.zoro.com/search?q=panduit%20PN18-6R-C',
    'https://www.zoro.com/search?q=panduit%20PN18-6R-M',
    'https://www.zoro.com/search?q=panduit%20PN18-8R-M',
    'https://www.zoro.com/search?q=panduit%20PV10-10F-D',
    'https://www.zoro.com/search?q=panduit%20PV10-10F-E',
    'https://www.zoro.com/search?q=panduit%20PV10-10F-L',
    'https://www.zoro.com/search?q=panduit%20PV10-10R-D',
    'https://www.zoro.com/search?q=panduit%20PV10-10R-L',
    'https://www.zoro.com/search?q=panduit%20PV10-12R-Q',
    'https://www.zoro.com/search?q=panduit%20PV10-14F-L',
    'https://www.zoro.com/search?q=panduit%20PV10-14R-D',
    'https://www.zoro.com/search?q=panduit%20PV10-14R-L',
    'https://www.zoro.com/search?q=panduit%20PV10-38R-D',
    'https://www.zoro.com/search?q=panduit%20PV10-38R-L',
    'https://www.zoro.com/search?q=panduit%20PV10-56R-D',
    'https://www.zoro.com/search?q=panduit%20PV10-56R-L',
    'https://www.zoro.com/search?q=panduit%20PV10-6F-L',
    'https://www.zoro.com/search?q=panduit%20PV10-6R-D',
    'https://www.zoro.com/search?q=panduit%20PV10-6R-L',
    'https://www.zoro.com/search?q=panduit%20PV10-8F-D',
    'https://www.zoro.com/search?q=panduit%20PV10-8F-L',
    'https://www.zoro.com/search?q=panduit%20PV10-8R-D',
    'https://www.zoro.com/search?q=panduit%20PV10-8R-L',
    'https://www.zoro.com/search?q=panduit%20PV10-P55-DY',
    'https://www.zoro.com/search?q=panduit%20PV14-10F-C',
    'https://www.zoro.com/search?q=panduit%20PV14-10F-M',
    'https://www.zoro.com/search?q=panduit%20PV14-10R-C',
    'https://www.zoro.com/search?q=panduit%20PV14-10R-M',
    'https://www.zoro.com/search?q=panduit%20PV14-12R-L',
    'https://www.zoro.com/search?q=panduit%20PV14-14F-C',
    'https://www.zoro.com/search?q=panduit%20PV14-14R-C',
    'https://www.zoro.com/search?q=panduit%20PV14-38R-L',
    'https://www.zoro.com/search?q=panduit%20PV14-38R-M',
    'https://www.zoro.com/search?q=panduit%20PV14-56R-C',
    'https://www.zoro.com/search?q=panduit%20PV14-56R-M',
    'https://www.zoro.com/search?q=panduit%20PV14-6F-C',
    'https://www.zoro.com/search?q=panduit%20PV14-6F-M',
    'https://www.zoro.com/search?q=panduit%20PV14-6R-C',
    'https://www.zoro.com/search?q=panduit%20PV14-6R-M',
    'https://www.zoro.com/search?q=panduit%20PV14-8F-C',
    'https://www.zoro.com/search?q=panduit%20PV14-8F-M',
    'https://www.zoro.com/search?q=panduit%20PV14-8R-C',
    'https://www.zoro.com/search?q=panduit%20PV14-8R-M',
    'https://www.zoro.com/search?q=panduit%20PV14-P47-C',
    'https://www.zoro.com/search?q=panduit%20PV14-P47-M',
    'https://www.zoro.com/search?q=panduit%20PV18-10F-CY',
    'https://www.zoro.com/search?q=panduit%20PV18-10R-CY',
    'https://www.zoro.com/search?q=panduit%20PV18-10R-MY',
    'https://www.zoro.com/search?q=panduit%20PV18-14R-CY',
    'https://www.zoro.com/search?q=panduit%20PV18-14R-MY',
    'https://www.zoro.com/search?q=panduit%20PV18-6F-CY',
    'https://www.zoro.com/search?q=panduit%20PV18-6F-MY',
    'https://www.zoro.com/search?q=panduit%20PV18-6R-CY',
    'https://www.zoro.com/search?q=panduit%20PV18-6R-MY',
    'https://www.zoro.com/search?q=panduit%20PV18-8F-CY',
    'https://www.zoro.com/search?q=panduit%20PV18-8F-MY',
    'https://www.zoro.com/search?q=panduit%20PV18-8R-CY',
    'https://www.zoro.com/search?q=panduit%20PV18-8R-MY',
    'https://www.zoro.com/search?q=panduit%20PV18-P47-CY',
    'https://www.zoro.com/search?q=panduit%20PV6-10R-T',
    'https://www.zoro.com/search?q=panduit%20PV6-10R-X',
    'https://www.zoro.com/search?q=panduit%20PV6-14R-T',
    'https://www.zoro.com/search?q=panduit%20PV6-14R-X',
    'https://www.zoro.com/search?q=panduit%20PV8-10R-QY',
    'https://www.zoro.com/search?q=panduit%20PV8-10R-TY',
    'https://www.zoro.com/search?q=panduit%20PV8-12R-XY',
    'https://www.zoro.com/search?q=panduit%20PV8-14R-QY',
    'https://www.zoro.com/search?q=panduit%20PV8-14R-TY',
    'https://www.zoro.com/search?q=panduit%20PV8-38R-QY',
    'https://www.zoro.com/search?q=panduit%20PV8-38R-TY',
    'https://www.zoro.com/search?q=panduit%20PV8-56R-QY',
    'https://www.zoro.com/search?q=panduit%20PV8-56R-TY',
    'https://www.zoro.com/search?q=panduit%20KP-FSD2',
    'https://www.zoro.com/search?q=panduit%20KP-1075Y',
    'https://www.zoro.com/search?q=panduit%20KP-FSD1',
    'https://www.zoro.com/search?q=panduit%20KP-FSD3',
    'https://www.zoro.com/search?q=panduit%20KP-1165Y',
    'https://www.zoro.com/search?q=panduit%20GTS-E',
    'https://www.zoro.com/search?q=panduit%20K1-PNKIT',
    'https://www.zoro.com/search?q=panduit%20GTH-E',
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
        save_details: TextIO = open("2u.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + url + "\t" + get_url + "\t" + zoro + "\t" + mfr + "\t" + upc)
        save_details.close()
        print("\n ***** Record stored into upc  files. *****")

    except:
        save_details: TextIO = open("2remaining_urlsu.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + url)
        save_details.close()
        print("\n ***** Record stored into upc  files. *****")
        print("Not Found")
