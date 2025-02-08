import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-plugins")
chrome_options.add_argument("--headless")
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

for i in range(69, 115):

    url_list = [
    f"https://www.motion.com/products/brands/Thomson;pageNo={i};numItems=96"


    ]
    for url in url_list:
        driver.get(url)
        time.sleep(4)
        print("Product - url : -----", url)
        save = open('Thomson_urls.txt', "a+", encoding='utf-8')

        for product_cate in driver.find_elements(By.XPATH, "//*[@class='card-link']"):
            product_tag = product_cate.get_attribute("href")
            if "#" not in product_tag and "=" not in product_tag:
                print(product_tag)
                save.write(f"{product_tag}\n")
driver.quit()

