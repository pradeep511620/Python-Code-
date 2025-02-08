import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# opts = Options()
# opts.headless = False
driver = webdriver.Chrome()
driver.maximize_window()

mylist = [

    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-xl',    # 2780
    # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-l', # 2202
    # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-htd-3mm',   # 1192
    # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-htd-5mm',#  2292

]
for url in mylist:
    driver.get(url)
    time.sleep(6)
    # Get length of urls
    le = driver.find_element(By.ID, "cds-product-controls-count")
    c = le.text.split(' ')[-2]
    print("count....", c)
    length = round(int(c) / 15 + 1)
    print('click...', length)
    for i in range(1, length + 1):
        try:
            driver.find_element(By.ID, "cds-show-more-products").click()
            time.sleep(3)
        except NoSuchElementException:
            print('unable to locate')
        print("click2", i)
    # Get urls here
    # url_links = driver.find_element(By.ID, "cds-product-list").find_elements(By.TAG_NAME, "a")
    # le = len(url_links)
    # print("Product-length", le)
    # for ur in url_links:
    #     urls_link = ur.get_attribute('href')
    #     print(urls_link)
    #     # Save urls here
    #     save = open("pulleys8mm792-2.txt", "a+", encoding="utf-8")
    #     save.write("\n" + "'"+urls_link+"',")
    # print('save data')
