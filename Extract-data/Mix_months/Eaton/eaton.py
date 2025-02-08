import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from typing.io import TextIO
from webdriver_manager.chrome import ChromeDriverManager

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = True
# driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

l = 0
url = 'https://www.drivetrainamerica.com/eaton-weatherhead-fj3055-05-1010s-female-o-ring-a-c-ez-fitting/'

l = l + 1
driver.get(url)
print("Product_urls", l, url)
time.sleep(2)

lst = [

    'GH493-8',
    'GH493-12',
    # 'GH493-16',
    # 'GH493-20',
    # '1BA8MP8',
    # '1BA12MP12',
    # '1BA16MP16',
    # '1BA20MP20',
    # '1BA12FJA12',

]

for i in lst:
    print("running_mpns....", i)

    part = ''
    rs = ''
    upc = ''

    driver.find_element(By.XPATH, "//div[@id='quickSearch']//input[@id='search_query']").send_keys(i)
    driver.find_element(By.XPATH, "//div[@id='quickSearch']//input[@value='Search']").click()
    time.sleep(1)
    current = driver.current_url
    print("Current_urls", current)

    #
    #
    #     # close the clear button and clear search bar
    #     try:
    #         driver.find_element(By.XPATH, "//img[@alt='Clear Search']").click()
    #         time.sleep(1)
    #     except:
    #         pass
    #
    #     #
    #
    #     try:
    #         part = driver.find_element(By.XPATH, "//strong[@class='manufacturer-part-number']").text
    #         print("part....", part)
    #     except:
    #         part = "Not Found"
    #         print("Not Found")
    #
    #     #
    #
    #     try:
    #         rs = driver.find_element(By.XPATH, "//span[@class='allied-stock-number']").text
    #         print("rs....", rs)
    #     except:
    #         rs = "Not Found"
    #         print("Not Found")
    #
    #     #
    #
    #     try:
    #         upc = driver.find_element(By.XPATH,
    #                                   "//div[@id='attribute-16435']//div[@class='product-specifications-data value']").text
    #         print("upc....", upc)
    #         save_details: TextIO = open("kipp.txt", "a+", encoding="utf-8")
    #         save_details.write("\n" + url + "\t" + current + "\t" + part + "\t" + rs + "\t" + "rp_" + upc)
    #         save_details.close()
    #         print("\n ***** Record stored into upc  files. *****")
    #     except:
    #         save_details: TextIO = open("kipp.txt", "a+", encoding="utf-8")
    #         save_details.write("\n" + url + "\t" + current + "\t" + part + "\t" + rs + "\t" + "rp_" + upc)
    #         save_details.close()
    #         print("\n ***** Record stored into upc  files. *****")
    #         upc = "Not Found"
    #         print("Not Found")
    # except:
    #     save_details: TextIO = open("remain.txt", "a+", encoding="utf-8")
    #     save_details.write("\n" + url + "\t" + current)
    #     save_details.close()
    #     print("\n ***** Record stored into upc  files. *****")
    #     pass
