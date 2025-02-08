import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
# driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome()

driver.maximize_window()
l = 0
Result = [
    # 'https://www.se.com/ww/en/product-range/45435153-acti9-active-afdd/?parent-subcategory-id=45435076',
    # 'https://www.se.com/ww/en/product-range/45435131-acti9-active-vigiarc/?parent-subcategory-id=45435076',
    # 'https://www.se.com/ww/en/product-range/64155-resi9-db60/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/61364-resi9-protection/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/64211-resi9-cx-enclosures/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/62107-wiser-energy/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/65817-easy9-devices/?parent-subcategory-id=1665',
    # 'https://www.se.com/ww/en/product-range/61956-easy9-mp-enclosures/?parent-subcategory-id=1665',

    # 'https://www.se.com/in/en/product-range/8297102-easy-ups-3l/?parent-subcategory-id=8030',
    'https://www.se.com/in/en/product-range/61909-symmetra-px/?parent-subcategory-id=8030',



]
for url in Result:
    try:
        l = l + 1
        driver.get(url)
        r = driver.page_source
        soup = BeautifulSoup(r, "html.parser")
        # print(soup)
        time.sleep(15)
        print("products urls", l, url)
        # first urls printed here
        for j in range(1, 12 + 1):
            k = driver.execute_script('return document.querySelector("pes-tabs se-container.pes-tabs-content.centered-content.relative.ct-bg-standard.row-dir.flex-display.hydrated div:nth-child(1) pes-range-products-tab")\
            .shadowRoot.querySelector("se-container div.range-products-tab__main-block-container se-block product-cards-wrapper")\
            .shadowRoot.querySelector("div ul li:nth-child(' + str(j) + ') product-card")\
            .shadowRoot.querySelector("article div div.body product-card-main-info").shadowRoot.querySelector("div pes-router-link a")')
            u1 = k.get_attribute('href')
            print("data1...", u1)

        counts = driver.execute_script('return document.querySelector("pes-tabs se-container.pes-tabs-content.centered-content.relative.ct-bg-standard.row-dir.flex-display.hydrated div:nth-child(1) pes-range-products-tab").shadowRoot.querySelector("se-container div.range-products-tab__main-block-container se-block product-cards-wrapper").shadowRoot.querySelector("div div pdp-switch-card-view").shadowRoot.querySelector("span")')
        count = counts.text.split()[-2]
        print("count...", count)
        length = round(int(count) / 12 + 1)
        print("division...", length)
        for j in range(1, length):
            inc = j * 12
            print(inc)
            adds = '&No=' + str(inc) + '&Nrpp=12'
            add_urls = url + adds
            print(add_urls)
            # driver.get(add_urls)
            # time.sleep(10)
            # for m in range(1, 12 + 1):
            #     k = driver.execute_script('return document.querySelector("pes-tabs se-container.pes-tabs-content.centered-content.relative.ct-bg-standard.row-dir.flex-display.hydrated div:nth-child(1) pes-range-products-tab")\
            #     .shadowRoot.querySelector("se-container div.range-products-tab__main-block-container se-block product-cards-wrapper")\
            #     .shadowRoot.querySelector("div ul li:nth-child(' + str(m) + ') product-card")\
            #     .shadowRoot.querySelector("article div div.body product-card-main-info").shadowRoot.querySelector("div pes-router-link a")')
            #     uu = k.get_attribute('href')
            #     print("data2..", uu)

    except:
        print("Not Found")
