import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from typing import TextIO
from selenium.webdriver.chrome.options import Options
import csv

opts = Options()
opts.headless = False
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")

file = open('book1.csv', 'r')
csvreader = csv.reader(file)
c=list(csvreader)

browser = webdriver.Chrome(options=opts)

for j in range(462,5000):
    s=c[j]
    print(j)
    print(s[0])

    f='https://www.upcitemdb.com/query?s='+s[0].replace('rp_','')+"&type=2"
    browser.get(f)
    time.sleep(4)

    print("------------------------------------",s[0])
    try:
        for j in  browser.find_element(By.XPATH,'/html/body/div/div/div/div[3]/div').find_elements(By.TAG_NAME,'a'):
            j.click()
            for dj in browser.find_element(By.XPATH,'/html/body/div/div/div/div[1]/ul').find_elements(By.TAG_NAME,'li'):
                if ''!=dj.text:
                    d=dj.text.strip().split('\n')
                    print(d)
                    save_details: TextIO = open("upc_csv.txt", "a+", encoding="utf-8")
                    save_details.write("\n" + s[0]+"\t"+ "rp_" + d[0] + "\t" + "rp_" + d[1])
                    print("End")

                    save_details.close()
    except:
        try:
            for dj in browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/ul').find_elements(By.TAG_NAME, 'li'):
                if '' != dj.text:
                    d = dj.text.strip().split('\n')
                    print(d)
                    save_details: TextIO = open("upc_csv.txt", "a+", encoding="utf-8")
                    save_details.write("\n" + s[0]+"\t"+ "rp_" + d[0] + "\t" + "rp_" + d[1])
                    print("End")

                    save_details.close()
        except:
            pass
        pass














