import time
from typing import TextIO
from selenium import webdriver
from selenium.webdriver.common.by import By

l = 0
options = webdriver.FirefoxOptions()

browser = webdriver.Chrome()
browser.maximize_window()

url = 'https://www.rpmbearings.com/product/251-sgs-tool-company/477073-31251/sgs-tool-company-31251'

l = l + 1
browser.get(url)
print("Product_urls", l, url)
time.sleep(4)
lst = [
    'rp_B1512S',
    'rp_B1516',
    'rp_B1516S',
    'rp_B1524S',

]


for i in lst:
    # try:
        rp = i.replace("rp_", "")
        print("running_mpns....", rp)
        title = ''
        upc_d = ''
        browser.find_element(By.XPATH, "//input[@id='search_q']").send_keys(rp)
        time.sleep(3)

        try:
            browser.find_element(By.XPATH, "//button[@class='uk-search-icon-flip uk-icon uk-search-icon']").click()
            time.sleep(3)
        except:
            print('mmm')

        try:
            browser.find_element(By.XPATH, "//input[@id='search_q']").clear()
            time.sleep(2)
        except:
            pass
        #
        # get_url = browser.current_url
        # print("current.....", get_url)

        # try:
        #     for j in browser.find_element(By.XPATH, "//div[@class='search-product row small-gutters']").find_elements(By.TAG_NAME, "a"):
        #         j.click()
        #         time.sleep(6)
        #         print("for click")
        #         get_url1 = browser.current_url
        #         print("current1.....", get_url1)
        # except:
        #     get_url1 = ''
        #     pass

    #     sku = browser.find_element(By.CLASS_NAME, "mt-n1").text
    #     print(sku)
    #     browser.refresh()
    #
    #     try:
    #         title = browser.find_element(By.XPATH, "//span[@itemprop='name']").text
    #         print("Title.....", title)
    #     except:
    #         pass
    #     # time.sleep(5)
    #     try:
    #         upc = browser.find_element(By.ID, "product_description").text.replace('\n', '').split('UPC:')
    #         U = upc[1]
    #         ss = U.split('Average')
    #         upc_d = ss[0]
    #         print("upc...", upc_d)
    #         save_data: TextIO = open("altronix.txt", "a+", encoding="utf-8")
    #         save_data.write("\n" + url + "\t" + get_url1 + "\t" + title + "\t" + "rp_" + upc_d)
    #         print("\n ***** Record stored into upc  files. *****")
    #     except:
    #         save_data: TextIO = open("altronix.txt", "a+", encoding="utf-8")
    #         save_data.write("\n" + url + "\t" + get_url1 + "\t" + title + "\t" + "rp_" + upc_d)
    #         print("\n ***** Record stored into upc  files. *****")
    #         upc_d = "Not Found"
    #         print('Not Found')
    #
    #     browser.back()
    #     browser.find_element(By.XPATH, "//div[@id='search']//input[@placeholder='Search JMAC']").clear()
    #     print("clear3")
    #     time.sleep(5)
    #
    # except Exception as e:
    #     save_data: TextIO = open("remaining.txt", "a+", encoding="utf-8")
    #     save_data.write("\n" + url + "\t" + get_url1)
    #     print("\n ***** Record stored into upc  files. *****")
    #     print(e)
