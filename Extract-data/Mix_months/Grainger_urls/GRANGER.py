from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = False
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")

driver = webdriver.Chrome()
driver.maximize_window()

mylist = [

    'https://www.grainger.com/category/motors/ac-motors/general-purpose-ac-motors/3-phase-nema-frame-general-purpose-ac-motors'

    ]

c = 0
for url in mylist:
    c = c + 1
    driver.get(url)
    time.sleep(3)
    print('Product-url', c, url)
    for i in range(0, 10):
        driver.execute_script("window.scrollBy(0, 700)", "")
        time.sleep(1)
        print(i)

        table = driver.find_elements(By.XPATH, "//div[@class='J5ihJT']//table//td")
        print(len(table))
        for a in table:
            time.sleep(2)
            link = a.find_elements(By.TAG_NAME, "a")
            for l in link:
                url_links = l.get_attribute('href')
                print(url_links)
        #         save = open("Motors.txt", 'a+', encoding="utf-8")
        #         save.write('\n' + url + '\t' + "'" + url_links + "',")
        # print('save urls into text files')




