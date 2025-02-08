import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Create Firefox options
opts = Options()
# Set headless mode
opts.headless = True

opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")

# driver = webdriver.Chrome(options=opts)
driver = webdriver.Chrome()
driver.maximize_window()

mylist = pd.read_csv('granger_sub_product_urls1.csv')['url']


c = 492
for url in mylist[c:]:
    try:
        c = c + 1
        driver.get(url)
        time.sleep(4)
        print('Product-url', c, url)
        total_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
        # Execute JavaScript to get the current scroll position in the window
        scroll_position = driver.execute_script("return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")
        # Print the total height and current scroll position
        print("Total height of scrollable area:", total_height)
        for i in range(scroll_position, total_height - 800, 800):
            driver.execute_script("window.scrollBy(0, 700)", "")
            time.sleep(3)
            print(i)

            table = driver.find_elements(By.XPATH, "//div[@class='J5ihJT']//table//td")
            print(len(table))
            for a in table:
                element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, "a")))
                link = a.find_elements(By.TAG_NAME, "a")
                for product in link:
                    url_links = product.get_attribute('href')
                    # print(url_links)
                    save = open("granger_plumbing.txt", 'a+', encoding="utf-8")
                    save.write('\n' + "'" + url_links + "',")
            print('save urls into text files')
    except Exception as e:
        save_file = open("remains.txt", 'a+', encoding="utf-8")
        save_file.write('\n' + url)
        print('save urls into text files')
        print("Error.....", e)
