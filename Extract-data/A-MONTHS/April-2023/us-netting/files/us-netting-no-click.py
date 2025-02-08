import time
from typing import TextIO

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
opts = Options()
opts.headless = False
opts.add_argument("--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")

mylst = [
    # 'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-12-175/',
    # 'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-120-350/',
    # 'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-21-075/',
    # 'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-21-175/',
    # 'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-30-400/',
    # 'https://www.usnetting.com/all-purpose-netting/knotted-netting/sbn-84-200/',
    'https://www.usnetting.com/fence/deer-fence/standard-duty-plastic-deer-fence/',
]
l = 0

for url in mylst:
    l += 1
    driver.get(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    time.sleep(2)
    print("Product-url...", l, url)
    description = ''
    images = ''

    meta_title = driver.find_element(By.XPATH, '/html/head/title').get_attribute("innerHTML")
    print("meta_title...", meta_title)

    print("********** Breadcrumb : **********")
    bread = driver.find_element(By.CLASS_NAME, "breadcrumb-wrap").text.replace('\n', '>>')
    print('bread...', bread)

    print("********** Title : **********")
    title = driver.find_element(By.TAG_NAME, 'h1').text.strip()
    print('Title...', title)

    #   Get Price Here
    print("********** Price : **********")
    price = driver.find_element(By.XPATH, "//div[@class=' cargo-netting-product-price']").text.strip()
    print("Price...", price)

    # #   Get Images Here
    for img in driver.find_element(By.XPATH, "//div[@class='product-photos col-xs-12 col-sm-5']").find_elements(By.TAG_NAME, "img"):
        images = img.get_attribute('src')
        print("Images...", images)
        save_d: TextIO = open("us-netting-no-click.txt", "a+", encoding="utf-8")
        save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + price + '\t' + images + "\t" + images.strip())
    print('data save into files in images')

    print("********** Description : **********")
    try:
        description = driver.find_element(By.ID, "desc").find_element(By.TAG_NAME, 'p').text.strip()
        print('description...', description)
    except:
        print("Not Found")
    #     print("********** Table : **********")
    # try:
    name = []
    value = []
    table = soup.find('div', {"id": "specs"}).find('ul').find_all('li')
    for td in table:
        tables = td.text.split('\n')
        for tab in tables:
            if ":" in tab:
                tabless = tab.split(':')
                name.append(tabless[0].strip())
                value.append(tabless[1].strip())
    for a, b, in zip(name, value):
        print(a, "......", b)
        save_d: TextIO = open("us-netting-no-click.txt", "a+", encoding="utf-8")
        save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + price + "\t" + images + "\t" + description + "\t" + a + "\t" + b)
    print('data save into files in tables')

# try:
#        print("********** Table : **********")
#        table1 = []
#        table2 = []
#        table = []
#        name = []
#        value = []
#        for desc in driver.find_elements(By.CLASS_NAME, "single-product__description__list"):
#            table = desc.text.strip().split('\n')
#            for tab in table:
#                if ":" in tab:
#                    table = tab.split(':')
#                    name.append(table[0].strip())
#                    value.append(table[1].strip())
#                else:
#                    table2.append('name')
#
#                    table1.append(tab.strip())
#        for a, b in zip(name, value):
#            print(a, ".....", b)
#            save_d: TextIO = open("oneclik_num.txt", "a+", encoding="utf-8")
#            save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + num + '\t' + price + "\t" + images + "\t" + description + "\t" + a + "\t" + b)
#            print('tabel data 1')
#
#            pass
#        for j, h in zip(table2, table1):
#            print(j, ".....", h)
#            save_d: TextIO = open("oneclik_num.txt", "a+", encoding="utf-8")
#            save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + num + '\t' + price + "\t" + images + "\t" + description + "\t" + a + "\t" + b + "\t" + j + "\t" + h)
#            print('tabel data 2')
#            pass
#    except:
#        print("Not Found")
