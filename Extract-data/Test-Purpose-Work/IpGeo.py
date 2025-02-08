import time
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

url = "https://www.raptorsupplies.com/"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(5)


def GetIpGeoDetails():
    ipgeo_list = []
    for entry in driver.execute_script("return window.performance.getEntries();"):
        ipgeo = entry['name']
        if "ipgeo.php" in ipgeo:
            ipgeo_list.append(ipgeo)
    print("Product_url_of_Ipgeo.....", ipgeo_list)

    for url in ipgeo_list:
        ress = requests.get(url, headers=header)
        soup = BeautifulSoup(ress.content, 'lxml')
        if ress.status_code == 200:
            ipgeo = soup.find('p')
            ipgeo_details = ipgeo.text.strip()
            data = ipgeo_details
            ipgeo_tag = json.loads(data)

            for key, value in ipgeo_tag.items():
                print(f"{key}: {value}")
        else:
            print(ress.status_code)



GetIpGeoDetails()


driver.quit()













"""
import requests
import json
from bs4 import BeautifulSoup
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
mylist = [
    
    # "https://www.raptorsupplies.com/ipgeo/ipgeo.php?addr=119.82.85.90&api=%27ngBm.F2E3ihqc%27&_=17",

]
for url in mylist:
    ress = requests.get(url, headers=header)
    soup = BeautifulSoup(ress.content, 'lxml')
    if ress.status_code == 200:
        ipgeo = soup.find('p')
        ipgeo_details = ipgeo.text.strip()
        data = ipgeo_details
        ipgeo_tag = json.loads(data)

        for key, value in ipgeo_tag.items():
            print(f"{key}: {value}")
    else:
        print(ress.status_code)
"""
