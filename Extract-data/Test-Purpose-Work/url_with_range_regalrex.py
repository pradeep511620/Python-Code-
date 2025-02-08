import time
import pandas as pd
from selenium import webdriver
from selenium.common import JavascriptException
driver = webdriver.Chrome()
driver.maximize_window()

def Regalrexnord_url():
    product_urls = []
    for count in range(400, 449):  # 449
        i = count * 12

        # url = 'https://www.regalrexnord.com/products/electric-motors#f-brand=Genteq'
        url = f'https://www.regalrexnord.com/search#q=Fasco&firstResult={i}'
        driver.get(url)
        time.sleep(8)
        print(url)


        for i in range(1, 12 + 1):
            script = f'''
            return document.querySelector("#list-result-view")
            .shadowRoot
            .querySelector("div > div > atomic-result:nth-child({i})")
            .shadowRoot
            .querySelector("div > atomic-field-condition > div > div.result-details > div > atomic-result-link > a")
            .getAttribute("href")
            '''
            try:
                href_value = driver.execute_script(script)
                product_url = "https://www.regalrexnord.com" + href_value
                product_urls.append(product_url)
                print(product_url)

            except JavascriptException:
                href_value = None
        print('save data 1')

    # Save data to CSV using pandas
    df = pd.DataFrame(product_urls, columns=['URL'])
    df.to_csv('product_link_url1.csv', mode='a+', header=not pd.io.common.file_exists('product_link_url1'), index=False)
    print("Data saved to product_urls.csv")



Regalrexnord_url()
