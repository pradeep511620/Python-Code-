import time
from typing import TextIO

from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector
import requests
import html
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.headless = True
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")

"""mydb = mysql.connector.connect(
    host="development-com.c5tedj3txtxy.eu-west-1.rds.amazonaws.com",
    user="raptoradmin",
    password="Raptorpwa2020",
    database="raptor_data"
)
cur = mydb.cursor(buffered=True)

cur.execute('select barcode_url,model_no,id from `upc_barcode_lookup` where status is null and id BETWEEN 18001 AND 20000')
myresult = cur.fetchall()
"""
import csv
file = open('/home/tajender/barcode_url_csv_file.csv', 'r')
csvreader = csv.reader(file)
c=list(csvreader)
print(len(c))
for j in range(1,5000):

    fetch=c[j]
    print(fetch)
    url = fetch[4]
    model_no =fetch[1]
    id = fetch[0]
    driver = webdriver.Chrome(options=opts)
    print(id)
    driver.get(url)
    time.sleep(3)
    li = []
    b = 0
    fl = 1
    try:
        n = driver.find_element(By.ID, 'product-search-results')
        f = driver.find_element(By.XPATH, '//*[@id="product-search-body"]/section[2]/div/div/div/div/nav').find_elements(
        By.TAG_NAME, 'li')


        for x in n.find_elements(By.TAG_NAME, 'li'):
            for z in x.find_elements(By.TAG_NAME, 'p'):
                if fl == 1:
                    li.append(z.text)
                    continue
                li.append(z.text.split(':')[-1])
            print(li)
            if len(li)==3:
                save_details: TextIO = open("test_upc.txt", "a+", encoding="utf-8")
                save_details.write(
                    "\n" + driver.current_url + "\t" + li[0] + "\t" + "rp_" + li[1] + "\t" + "rp_" + li[2] )
                save_details.close()
            else:
                save_details: TextIO = open("test_upc.txt", "a+", encoding="utf-8")
                save_details.write(
                    "\n" + driver.current_url + "\t" + li[0] + "\t" + "rp_" + li[1] + "\t" + "rp_" + li[
                        2] + "\t" + "rp_" + li[3])
                save_details.close()
            li.clear()

    except:
        save_details: TextIO = open("test_upcnot_found.txt", "a+", encoding="utf-8")
        save_details.write("\n" + url)
        save_details.close()
        pass