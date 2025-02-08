import time
import requests
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
# driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = uc.Chrome()

driver.maximize_window()
l = 0
mylist = [
    'https://lovejoy-inc.com/products/quick-flex-couplings/',
    'https://lovejoy-inc.com/products/hercuflex-gear-couplings/',
    'https://lovejoy-inc.com/products/s-flex-couplings/',
    'https://lovejoy-inc.com/products/runright-rubber-suspension/',
    'https://www.lovejoy-inc.com/products/jaw-type-couplings/',
    'https://lovejoy-inc.com/products/grid-couplings/',
    'https://lovejoy-inc.com/products/torsional-couplings/',
    'https://lovejoy-inc.com/products/disc-couplings/',
    'https://lovejoy-inc.com/products/jaw-in-shear-type-couplings/',
    'https://lovejoy-inc.com/products/curved-jaw-couplings/',
    'https://lovejoy-inc.com/products/lovejoy-sier-bath-gear-type-couplings/',
    'https://lovejoy-inc.com/products/high-performance-gear-couplings/',
    'https://lovejoy-inc.com/products/universal-joints/',
    'https://www.lovejoy-inc.com/products/curtis-universal-joints/',
    'https://www.lovejoy-inc.com/products/rigid-compression-couplings/',
    'https://lovejoy-inc.com/products/motion-control-couplings/',
    'https://lovejoy-inc.com/products/specialty-products/',
    'https://lovejoy-inc.com/products/variable-speed-drives/',
    'https://lovejoy-inc.com/products/shaft-locking-devices/',
    'https://lovejoy-inc.com/products/hydraulic-components/',
    'https://lovejoy-inc.com/products/engineering-data/',
]

for url in mylist:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    driver.get(url)
    time.sleep(2)
    print("Product Urls", l, url)
    lk = driver.find_element(By.XPATH, "//div[@class='textwidget']")
    lks = lk.find_elements(By.TAG_NAME, "a")
    for ul in lks:
        data = (ul.get_attribute('href'))
        print("'"+data+"',")










#

    # breadcrumb = []
    # bread = driver.find_element(By.XPATH, "//ul[@class='breadcrumbs']").find_elements(By.TAG_NAME, "li")
    # for bread_d in bread:
    #     breadcrumb.append(bread_d.text.replace("\n", ""))
    # print(breadcrumb)
    #
    # title = driver.find_element(By.XPATH, "//span[@class='product__name h2']").text
    # print(title)
    #
    # item = driver.find_element(By.XPATH, "//div[@class='customer-part-number']").text
    # print(item)
    #
    # price = driver.find_element(By.XPATH, "//span[@class='price']").text
    # print(price)
    # #
    # pr = []
    # pro = driver.find_element(By.XPATH, "//div[@class='short-description']").find_elements(By.TAG_NAME, "li")
    # for pro_d in pro:
    #     pr.append(pro_d.text)
    # print(pr)

    # desc = driver.find_element(By.XPATH, "//li[contains(text(),'This coupling offers standard shaft-to-shaft conne')]").text
    # print(desc)
    # all = []
    # f = driver.find_element(By.XPATH, "//div[@class='features']").text
    # all.append(f.split('FEATURES'))
    # s = all[0]
    # description = s[0].replace("\n", "")
    # print("desc...", description)
    # feature = s[1].replace("\n", "")
    # print("feature...", feature)

    # breadcrumb = []
    # bread = driver.find_element(By.XPATH, "//ul[@class='breadcrumbs']").find_elements(By.TAG_NAME, "li")
    # for bread_d in bread:
    #     breadcrumb.append(bread_d.text.replace("\n", ""))
    # print(breadcrumb)

# DESCRIPTION
#     try:
#         description = driver.find_element(By.XPATH, "//div[@class='features']/ul[1]").text.replace("\n", " ")
#         print("description...", description)
#     except:
#         description = "Not Found"
#         print("Not Found")
#     try:
#         feature = driver.find_element(By.XPATH, "//div[@class='features']/ul[2]").text.replace("\n", " ")
#         print("feature...", feature)
#     except:
#         feature = "Not Found"
#         print("Not Found")
#     try:
#         include = driver.find_element(By.XPATH, "//div[@class='features']/ul[3]").text.replace("\n", " ")
#         print("include...", include)
#     except:
#         include = "Not Found"
#         print("Not Found")


# ================================= Table =========================================
#     i = 0
#     attr_name = []
#     attr_value = []
#     table = driver.find_element(By.XPATH, "//section[@id='specifications']//div[@class='section__sub']")
#     td = table.find_elements(By.TAG_NAME, "td")
#     for ss in td:
#         i = i + 1
#         # print(i)
#         # print(ss.text)
#         if i % 2 != 0:
#             attr_name.append(ss.text)
#         else:
#             attr_value.append(ss.text)
#     # print(attr_name)
#     # print(attr_value)
#     for a, b in zip(attr_name, attr_value):
#         print(a, ".......", b)









#

    # breadcrumb = []
    # bread = driver.find_element(By.XPATH, "//ul[@class='breadcrumbs']").find_elements(By.TAG_NAME, "li")
    # for bread_d in bread:
    #     breadcrumb.append(bread_d.text.replace("\n", ""))
    # print(breadcrumb)
    #
    # title = driver.find_element(By.XPATH, "//span[@class='product__name h2']").text
    # print(title)
    #
    # item = driver.find_element(By.XPATH, "//div[@class='customer-part-number']").text
    # print(item)
    #
    # price = driver.find_element(By.XPATH, "//span[@class='price']").text
    # print(price)
    # #
    # pr = []
    # pro = driver.find_element(By.XPATH, "//div[@class='short-description']").find_elements(By.TAG_NAME, "li")
    # for pro_d in pro:
    #     pr.append(pro_d.text)
    # print(pr)

    # desc = driver.find_element(By.XPATH, "//li[contains(text(),'This coupling offers standard shaft-to-shaft conne')]").text
    # print(desc)
    # all = []
    # f = driver.find_element(By.XPATH, "//div[@class='features']").text
    # all.append(f.split('FEATURES'))
    # s = all[0]
    # description = s[0].replace("\n", "")
    # print("desc...", description)
    # feature = s[1].replace("\n", "")
    # print("feature...", feature)

    # breadcrumb = []
    # bread = driver.find_element(By.XPATH, "//ul[@class='breadcrumbs']").find_elements(By.TAG_NAME, "li")
    # for bread_d in bread:
    #     breadcrumb.append(bread_d.text.replace("\n", ""))
    # print(breadcrumb)

# DESCRIPTION
#     try:
#         description = driver.find_element(By.XPATH, "//div[@class='features']/ul[1]").text.replace("\n", " ")
#         print("description...", description)
#     except:
#         description = "Not Found"
#         print("Not Found")
#     try:
#         feature = driver.find_element(By.XPATH, "//div[@class='features']/ul[2]").text.replace("\n", " ")
#         print("feature...", feature)
#     except:
#         feature = "Not Found"
#         print("Not Found")
#     try:
#         include = driver.find_element(By.XPATH, "//div[@class='features']/ul[3]").text.replace("\n", " ")
#         print("include...", include)
#     except:
#         include = "Not Found"
#         print("Not Found")


# ================================= Table =========================================
#     i = 0
#     attr_name = []
#     attr_value = []
#     table = driver.find_element(By.XPATH, "//section[@id='specifications']//div[@class='section__sub']")
#     td = table.find_elements(By.TAG_NAME, "td")
#     for ss in td:
#         i = i + 1
#         # print(i)
#         # print(ss.text)
#         if i % 2 != 0:
#             attr_name.append(ss.text)
#         else:
#             attr_value.append(ss.text)
#     # print(attr_name)
#     # print(attr_value)
#     for a, b in zip(attr_name, attr_value):
#         print(a, ".......", b)
