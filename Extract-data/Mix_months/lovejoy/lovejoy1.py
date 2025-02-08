import time

import requests
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from typing.io import TextIO

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
# driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = uc.Chrome()

driver.maximize_window()
l = 0
mylist = [
    # 'https://www.applied.com/brands/timken-company/lovejoy/c/Brand-985?q=:&override=true&isLevelUp=false&usePlp=&page=1',
    'https://www.applied.com/brands/timken-company/lovejoy/c/Brand-985?q=:&override=true&isLevelUp=false&usePlp=&page=2',


]

for url in mylist:
    l = l + 1
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    driver.get(url)
    time.sleep(5)
    print("Product Urls", l, url)
    images = ''

    links = driver.find_element(By.XPATH, "//div[@class='product-list']").find_elements(By.TAG_NAME, 'a')
    s = int(len(links))
    for ji in range(1, int(s/3+1)):

        unic = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div/div[2]/div[3]/div['+str(ji)+']/div/div[2]/div/div[1]/div[1]').text
        print("unic. ", unic)

        try:
            desc = driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div/div[2]/div[3]/div['+str(ji)+']/div/div[2]/div/div[1]/div[3]').text.replace("\n", "")
            print("desc. ", desc)
        except:
            desc = "Not Found"
            print("Not Found")

        driver.find_element(By.XPATH, '//*[@id="content"]/div[4]/div/div[2]/div[3]/div['+str(ji)+']/div/div[2]/div/div[1]/a').send_keys('\n')
        print("click")
        # driver.get(url)
        time.sleep(3)
        driver.get(driver.current_url)
        get_url = driver.current_url
        print("current = ", l,  get_url)

# ======================================== Breadcrumb =================================================================
        try:
            breadcrumb = []
            bread = driver.find_element(By.XPATH, "//ul[@class='breadcrumbs']").find_elements(By.TAG_NAME, "li")
            for bread_d in bread:
                breadcrumb.append(bread_d.text.replace("\n", ""))
            print("Breadcrumb..", breadcrumb)
        except:
            breadcrumb = "Not Found"
            print("Not Found")

        try:
            title = driver.find_element(By.XPATH, "//span[@class='product__name h2']").text
            print("title..", title)
        except:
            title = "Not Found"
            print("Not Found")

        try:
            item = driver.find_element(By.XPATH, "//div[@class='customer-part-number']").text
            print("item.. ", item)
        except:
            item = "Not Found"
            print("Not Found")

        try:
            price = driver.find_element(By.XPATH, "//span[@class='price']").text
            print("price.. ", price)
        except:
            price = "Not Found"
            print("Not Found")
            pass

        try:
            image = driver.find_element(By.CLASS_NAME, "js-pdp-lazy")
            images = image.get_attribute('src')
            print("images.. ", images)
        except:
            print("Not Found")
            pass
        # DESCRIPTION
        try:
            description = driver.find_element(By.XPATH, "//div[@class='features']/ul[1]").text.replace("\n", " ")
            print("description...", description)
        except:
            description = "Not Found"
            print("Not Found")
        try:
            feature = driver.find_element(By.XPATH, "//div[@class='features']/ul[2]").text.replace("\n", " ")
            print("feature...", feature)
        except:
            feature = "Not Found"
            print("Not Found")
        try:
            include = driver.find_element(By.XPATH, "//div[@class='features']/ul[3]").text.replace("\n", " ")
            print("include...", include)
            save_details: TextIO = open("lovejoy.xlsx", "a+", encoding="utf-8")
            save_details.write("\n" + get_url + "\t" + "".join(breadcrumb) + "\t" + title + "\t" + unic + "\t" + item + "\t" + price + "\t" + images + "\t" + desc + "\t" + description + "\t" + feature + "\t" + include.strip())
            save_details.close()
            print("\n ***** Record stored into watts  files. *****")
        except:
            include = "Not Found"
            print("Not Found")
#
#         # ================================= Table =========================================
        i = 0
        attr_name = []
        attr_value = []
        table = driver.find_element(By.XPATH, "//section[@id='specifications']//div[@class='section__sub']")
        td = table.find_elements(By.TAG_NAME, "td")
        for ss in td:
            i = i + 1
            # print(i)
            # print(ss.text)
            if i % 2 != 0:
                attr_name.append(ss.text)
            else:
                attr_value.append(ss.text)
        # print(attr_name)
        # print(attr_value)
        for a, b in zip(attr_name, attr_value):
            save_details: TextIO = open("lovejoy.xlsx", "a+", encoding="utf-8")
            save_details.write("\n" + get_url + "\t" + "".join(breadcrumb) + "\t" + title + "\t" + "rp"+unic + "\t" + item + "\t" + price + "\t" + images + "\t" + desc + "\t" + description + "\t" + feature + "\t" + include + "\t" + a + "\t" + "rp_"+b)
            save_details.close()
            print("\n ***** Record stored into watts  files. *****")
        print("tables..")
        # print(a, ".......", b)

        driver.back()
        # driver.get(url)
        # unic = driver.find_element(By.CLASS_NAME, "details").text
        # print("unic. ", unic)
