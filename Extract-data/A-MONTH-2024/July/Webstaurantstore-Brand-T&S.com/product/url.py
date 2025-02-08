import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

urk_list = [
    # 'https://www.webstaurantstore.com/59139/shop-all-t-s-brass-parts.html',
    # 'https://www.webstaurantstore.com/14985/pre-rinse-faucets-and-pre-rinse-spray-valves.html?vendor=T-S-Brass-and-Bronze-Works',
    # 'https://www.webstaurantstore.com/27957/wall-mount-faucets.html?vendor=T-S-Brass-and-Bronze-Works',
    # 'https://www.webstaurantstore.com/14077/glass-filler-faucets.html?vendor=T-S-Brass-and-Bronze-Works',
    # 'https://www.webstaurantstore.com/14959/mop-sink-faucets.html?vendor=T-S-Brass-and-Bronze-Works',
    # 'https://www.webstaurantstore.com/14963/hands-free-electronic-faucets.html?vendor=T-S-Brass-and-Bronze-Works',
]
def url_extracted():
    product_urls = []
    for url in urk_list:
        for i in range(1, 22):
            new_url = f"{url}?page={i}"
            driver.get(new_url)
            time.sleep(5)

            for href_tag in driver.find_elements(By.CSS_SELECTOR, "a[data-testid='itemLink']"):
                product_url = href_tag.get_attribute('href')
                print(product_url)
                product_urls.append(product_url)

    # save data into dataframe
    df = pd.DataFrame(product_urls, columns=['URL'])

    df.to_csv('product_urls.csv', mode='a', header=not pd.io.common.file_exists('3m_data1.csv'), index=False)


url_extracted()


