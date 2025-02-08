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
browser.maximize_window()
l=[
'https://lockesupply.com//Manufacturers/Category/468?catid=138&categoryName=Overloads',
'https://lockesupply.com//Manufacturers/Category/468?catid=54&categoryName=Safety%20%26%20Disconnect%20Switches',
'https://lockesupply.com//Manufacturers/Category/468?catid=82&categoryName=Enclosures',
'https://lockesupply.com//Manufacturers/Category/468?catid=45&categoryName=Circuit%20Breakers',
'https://lockesupply.com//Manufacturers/Category/468?catid=44&categoryName=Circuit%20Breaker%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=47&categoryName=Load%20Centers',
'https://lockesupply.com//Manufacturers/Category/468?catid=49&categoryName=Metering%20Equipment%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=209&categoryName=Transformer%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=50&categoryName=Panelboards%20%26%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=132&categoryName=Contactors',
'https://lockesupply.com//Manufacturers/Category/468?catid=137&categoryName=Motor%20Control%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=207&categoryName=Distribution%2C%20Dry-Type%20Transformers',
'https://lockesupply.com//Manufacturers/Category/468?catid=143&categoryName=Pushbuttons%20%26%20Pilot%20Lights',
'https://lockesupply.com//Manufacturers/Category/468?catid=147&categoryName=Starters',
'https://lockesupply.com//Manufacturers/Category/468?catid=146&categoryName=Selector%20Switches',
'https://lockesupply.com//Manufacturers/Category/468?catid=53&categoryName=Safety%20%26%20Disconnect%20Switch%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=830&categoryName=Supply%20%26%20Exhaust%20Fans%2FVentilators',
'https://lockesupply.com//Manufacturers/Category/468?catid=142&categoryName=Pushbutton%2C%20Pilot%20Light%20%26%20Switch%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=208&categoryName=Special%20Purpose%20Transformers',
'https://lockesupply.com//Manufacturers/Category/468?catid=46&categoryName=Load%20Center%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=189&categoryName=Generator%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=28&categoryName=Conduit%20Bodies',
'https://lockesupply.com//Manufacturers/Category/468?catid=52&categoryName=Power%20Outlet%20Panels',
'https://lockesupply.com//Manufacturers/Category/468?catid=828&categoryName=Motor%20Components%20%26%20Supplies',
'https://lockesupply.com//Manufacturers/Category/468?catid=133&categoryName=Control%20Stations%20%26%20Accessories',
'https://lockesupply.com//Manufacturers/Category/468?catid=234&categoryName=Compression%20Connectors%20%26%20Lugs',
'https://lockesupply.com//Manufacturers/Category/468?catid=211&categoryName=Surge%20Protective%20Devices',

]
c=0
for li in l:
    # r=requests.get(li)
    # soup=BeautifulSoup(r.text,'html.parser')
    # all=soup.find('div',class_='product-categories collection collection-underline').find_all('a')
    browser.get(li)
    c+=1
    print(c)
    print(li)
    time.sleep(6)
    r=browser.find_element(By.XPATH, '//*[@id="paged"]/div[4]/div[2]/div[1]').text.split(' ')
    print(r)
    print(int(int(r[5])/24))
    if int(int(r[5])/24)==0:
        all = browser.find_element(By.XPATH, '//*[@id="paged"]/div[5]').find_elements(By.CLASS_NAME, 'card-image')
        for a in all:
            print("'" + a.find_element(By.TAG_NAME, 'a').get_attribute('href') + "',")
            save_details: TextIO = open("LINK.txt", "a+", encoding="utf-8")
            save_details.write(
                "\n" + "'" + a.find_element(By.TAG_NAME, 'a').get_attribute('href') + "',")
            print("End")

            save_details.close()
    for i in range(0,int(int(r[5])/24)+1):

        all=browser.find_element(By.XPATH,'//*[@id="paged"]/div[5]').find_elements(By.CLASS_NAME,'card-image')
        for a in all:
            print("'"+a.find_element(By.TAG_NAME,'a').get_attribute('href')+"',")
            save_details: TextIO = open("LINK.txt", "a+", encoding="utf-8")
            save_details.write(
                "\n" + "'" + a.find_element(By.TAG_NAME,'a').get_attribute('href') + "',")
            print("End")

            save_details.close()
        try:
            browser.find_element(By.XPATH, '//*[@id="paged"]/div[6]/div/div/a[3]/i').click()
            time.sleep(10)
        except:
            pass






