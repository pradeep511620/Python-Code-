import time

from selenium import webdriver
from selenium.common import NoSuchElementException, JavascriptException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import undetected_chromedriver as uc

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
# driver = webdriver.Chrome()
driver = uc.Chrome(options=opts)

driver.maximize_window()


url_list = [

# 'https://www.regalrexnord.com/products/mechanical-power-transmission-components/tighteners-idlers/sprocket-idlers',
    # 'https://www.regalrexnord.com/products/mechanical-power-transmission-components/tighteners-idlers/tightener-shafts',
    'https://www.regalrexnord.com/products/mechanical-power-transmission-components/tighteners-idlers/v-belt-idlers',




]
for url in url_list:
    try:
        driver.get(url)
        time.sleep(4)
        print("Product - url : -----", url)
        # res = requests.get(url)
        # soup = BeautifulSoup(res.content, "html.parser")
        save = open('url.txt', "a+", encoding='utf-8')

        try:
            driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
            time.sleep(5)
        except NoSuchElementException:
            print('Not interact')

        for i in range(1, 12 + 1):
            script = f'return document.querySelector("#list-result-view").shadowRoot.querySelector("div > div > atomic-result:nth-child({i})").shadowRoot.querySelector("div > atomic-field-condition > div > div.result-details > div > atomic-result-link > a").getAttribute("href")'
            try:
                href_value = driver.execute_script(script)
                product_url = "https://www.regalrexnord.com" + href_value
                print(product_url)
                save.write(f"{product_url}\n")
            except JavascriptException:
                href_value = 'nnnn'
        print('save data 1')

        total_url_count = driver.find_element(By.XPATH, "//atomic-query-summary[@class='hydrated']").text.strip().split(" ")[-1]
        length = round(int(total_url_count) / 12 + 1)
        print('length.....', length)
        for count in range(1, length):
            multi = count * 12
            adds = '#firstResult=' + str(multi)
            add_urls = url + adds
            print(add_urls)
            driver.get(add_urls)
            time.sleep(5)
            for i_1 in range(1, 12 + 1):
                script = f'return document.querySelector("#list-result-view").shadowRoot.querySelector("div > div > atomic-result:nth-child({i_1})").shadowRoot.querySelector("div > atomic-field-condition > div > div.result-details > div > atomic-result-link > a").getAttribute("href")'
                try:
                    href_value = driver.execute_script(script)
                    product_url = "https://www.regalrexnord.com" + href_value
                    print(product_url)
                    save.write(f"{product_url}\n")
                except JavascriptException:
                    href_value = 'nnn'
            print('save data 2')

    except Exception as e:
        save = open('remaining_url.txt', "a+", encoding='utf-8')
        save.write(f"{url}\n")


    driver.quit()
