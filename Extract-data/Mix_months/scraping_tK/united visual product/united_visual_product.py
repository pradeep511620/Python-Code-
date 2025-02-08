import requests
from bs4 import BeautifulSoup
from typing import TextIO
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import time
from typing import TextIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
opts = Options()
opts.headless = True
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")

file = open('united_visual_product_link.csv', 'r')
csvreader = csv.reader(file)
c=list(csvreader)
#
# opts = Options()
# opts.headless = False
# opts.add_argument(
#     "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
# browser = webdriver.Chrome(options=opts)

for j in range(1,len(c)+1):
    s=c[j]
    print(s[0])
    r=requests.get(s[0])
    soup=BeautifulSoup(r.text,'html.parser')
    images=[]
    for im in soup.find('div',class_='product-image-gallery').find_all('img'):
        images.append(im.get('src'))
    # print(images)
    Breadcrumb=soup.find('div',class_='breadcrumbs').text.replace('\n','').replace(' /',' ->')
    # print(Breadcrumb)
    title=soup.find('div',class_='product-name secondary').text.strip()
    # print(title)
    Pcode=soup.find('span',class_='sku-number').text
    # print(Pcode)
    spec=[]
    for sp in soup.find('table',id='product-attribute-specs-table').find_all('tr'):
        spec.append(sp.text.strip().split('\n'))
    desc=[]
    description=soup.find('dl',id='collateral-tabs').find('dt').text
    description_cont = soup.find('dl', id='collateral-tabs').find('dd').text
    desc.append(description)
    desc.append(description_cont.strip())
    spec.append(desc)
    # print(spec)
    for j in spec:
        save_details: TextIO = open("united_visual_product.txt", "a+", encoding="utf-8")
        save_details.write(
            "\n" +s[0]+"\t"+Breadcrumb+"\t"+' , '.join(images)+"\t"+title+"\t"+"rp_"+Pcode+"\t"+j[0]+"\t"+"rp_"+j[1] )
        save_details.close()





    # to get product link
    # browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # time.sleep(2)
    # try:
    #     l=len(browser.find_element(By.XPATH,'//*[@id="top"]/body/div[1]/div[6]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div[2]').find_elements(By.TAG_NAME,'li'))
    #     print(l)
    # except:
    #     fd = browser.find_element(By.CLASS_NAME, 'category-products').find_elements(By.CLASS_NAME,
    #                                                                                 'product-image-container')
    #     for h in fd:
    #         # print(h.find_element(By.TAG_NAME, 'a').get_attribute('href'))
    #         save_details: TextIO = open("united_visual_product_link.txt", "a+", encoding="utf-8")
    #         save_details.write(
    #             "\n" + "''" + h.find_element(By.TAG_NAME, 'a').get_attribute('href') + "'',")
    #         save_details.close()
    #     continue
    # for d in range(1,int(l)):
    #     fd=browser.find_element(By.CLASS_NAME,'category-products').find_elements(By.CLASS_NAME,'product-image-container')
    #     for h in fd:
    #         # print(h.find_element(By.TAG_NAME,'a').get_attribute('href'))
    #         save_details: TextIO = open("united_visual_product_link.txt", "a+", encoding="utf-8")
    #         save_details.write(
    #             "\n" +"''"+h.find_element(By.TAG_NAME,'a').get_attribute('href')+"'',")
    #
    #         save_details.close()
    #     f=j.split('?')[0]+"?p="+str(d+1)
    #     browser.get(f)



    # page = requests.get(j)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # To get main-link
    # link=soup.find_all('a',class_='catagory-level1')
    # for l in link:
    #     print("'https://www.uvpinc.com/"+l.get('href')+"',")




