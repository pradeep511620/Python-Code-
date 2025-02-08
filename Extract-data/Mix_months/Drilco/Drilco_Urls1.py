import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
# driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver = uc.Chrome()

driver.maximize_window()

L = 0
Result = [
    'https://www.drillco-inc.com/products.php',

]

for url in Result:
    L = L + 1
    r = requests.get(url, headers=headers)
    driver.get(url)
    time.sleep(5)
    print("Products Urls", L, url)
    data_urls = ''
    url_links = ''
    try:
        links = driver.find_element(By.XPATH, "//body/div[@class='bg']/div/div[@class='productsContainer']/div[@class='ctCategorySidebar']/div[@class='ctCategorySidebarInner']/div[@class='ctSidebarContainer']/ul[1]").find_elements(By.TAG_NAME, 'a')
        print("Lenght", len(links))
        for x in links:
            url_links = (x.get_attribute('href'))
            data_urls = url_links
            print(data_urls)
        #     save_details: url_links = open("LoveJoy_urls.xlsx", "a+", encoding="utf-8")
        #     save_details.write("\n" + "'" + data_urls + "',")
        #     save_details.close()
        # print("\n ***** Record stored into urls  files. *****")
    except:
        pass
    #     save_details: url_links = open("remaining_urls.xlsx", "a+", encoding="utf-8")
    #     save_details.write("\n" + "'"+url+"',")
    #     save_details.close()
    # print("\n ***** Record stored into urls  files. *****")
