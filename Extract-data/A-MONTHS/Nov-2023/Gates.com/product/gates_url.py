import time
import pandas as pd
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--enable-javascript")
options.add_argument("--headless")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

# browser = Chrome(options=options)
with Chrome(options=options) as browser:
    url_link = pd.read_csv("Gates_product_url.csv")['URL']
    print(len(url_link))

    i = 0
    for url_count, url in enumerate(url_link[i:], start=i):
        try:
            browser.get(url)
            time.sleep(5)
            print("Product-Urls......", url_count, url)
        except Exception as e:
            print(f"Error accessing URL: {url}")
            print(f"Error details: {e}")

        for product_url in browser.find_elements(By.XPATH, "//*[@class='card-link']"):
            product_href = product_url.get_attribute('href')
            print(product_href)
            with open('product_url_gets.txt', 'a+', encoding='utf-8') as save:
                save.write('\n' + product_href)
        print('save 1')

    browser.quit()





"""

base_url = 'https://www.motion.com/products/brands/Gates;pageNo={};numItems=96'

for i in range(460):
    url = base_url.format(i)
    browser.get(url)
    time.sleep(1)
    print("Product_urls", url)

    with open('product_url_gates.txt', 'a+', encoding='utf-8') as save:
            save.write('\n' + url)
"""