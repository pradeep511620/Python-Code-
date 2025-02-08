import time

from selenium import webdriver

from selenium .webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


for i in range(0, 11 + 1):
    mylist = [

        f'https://zebra-scratch-and-dent-sale.myshopify.com/collections/all?page={i}'
    ]
    for url in mylist:
        driver.get(url)
        time.sleep(2)

        for u in driver.find_elements(By.XPATH, "//body/div[@class='page-container drawer-page-content']/main[@role='main']/div[@class='shopify-section']/div[@data-section-id='collection-template']/div[1]//a"):
            url_links = u.get_attribute('href')
            if "page" not in url_links:
                print(url_links)
                # save = open("zebra-url.txt", "a+", encoding="utf-8")
                # save.write('\n' + url)
            print()
        print()
    print()
