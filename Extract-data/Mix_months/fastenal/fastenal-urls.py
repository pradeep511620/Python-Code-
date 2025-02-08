import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# mylist = [
#     'https://www.fastenal.com/fast/supplier-partners'
# ]
#
# for url in mylist:
#     driver.get(url)
#     time.sleep(2)
#     for u in driver.find_elements(By.XPATH, "//body/div/div[@class='App']/div[@class='feco-container-fix feco-container-inner']/div[@class='row']/div[@class='col-xs-12 col-sm-12 feco-container-fix flex-grow-1']/div[@class='container-static']/div[@class='cms-panel-container']/div/div[4]/div[2]//div//ul//li//a"):
#         url_links = u.get_attribute('href')
#         save = open("fastenal-urls.txt", "a+", encoding="utf-8")
#         save.write('\n' + "'" + url_links + "',")
#         print('sava list into txt files')
#         print(url_links)


#
mylist = [

    'https://www.mscdirect.com/corporate/industrial-suppliers-line-card'
]

for url in mylist:
    driver.get(url)
    time.sleep(3)
    u = driver.find_elements(By.XPATH, "//div[contains(@class,'h-20 w-auto mt-1 mb-7 sticky-wrapper')]//li")
    for j in u:
        j.click()
        print(j.is_selected())
        time.sleep(2)
        for urs in driver.find_elements(By.XPATH, "//ul[@class='filterLi']//li//a"):
            url_linkss = urs.get_attribute('href')
            url_text = urs.text

            save = open("msc-urls.txt", "a+", encoding="utf-8")
            save.write('\n' + url_text + '\t' + url_linkss)
            print('sava list into txt files')
            print(url_text, url_linkss)

#
# mylist = [
#
#     'https://www.fastenal.com/product/all'
#
#     ]
#
# for url in mylist:
#     driver.get(url)
#     time.sleep(5)
#
#     le = driver.find_elements(By.XPATH, "//body/div/div[@class='App']/main[@role='main']/div[@class='row flex-nowrap flex-column flex-lg-row ie-width-full feco-mx-sm-0']/div[@class='col-xs-12 col-sm-12 col-md-12 feco-left-aggr ie-left-aggr feco-px-sm-0']/div[@class='fixed-aggregations mt-3']/div[@class='accordion mt-2']/div[2]/div[1]/div[2]/div[2]/div//input")
#     length = len(le)
#     print(length)
#     # u = driver.find_elements(By.XPATH, "//body[1]/div[1]/div[1]/main[1]/div[5]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]//div")
#     u = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/main[1]/div[5]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]")
#     ur = u.find_elements(By.XPATH, "/html/body/div[1]/div/main/div[5]/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div")
#     print(len(ur))
#     cont=0
#     for j in range(0,500):
#         cont+=1
#         time.sleep(3)
#         k='document.querySelector("#scroll_1 > div:nth-child('+str(cont)+') > div")'
#         print(k)
#         f=driver.execute_script('return document.querySelector("#scroll_1 > div:nth-child('+str(cont)+') > div")')

