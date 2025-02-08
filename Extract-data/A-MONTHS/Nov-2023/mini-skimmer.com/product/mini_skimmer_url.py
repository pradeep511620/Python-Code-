import time

import pandas as pd
from selenium import webdriver
from selenium.common import ElementNotInteractableException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()
#

mylist = [
    # 'https://mini-skimmer.com/product/mini-skimmer-r-s/',
    'https://mini-skimmer.com/product/ts/',
    # 'https://www.midea.com/global/search?search=midea&page=3',
    # 'https://www.midea.com/global/search?search=midea&page=4',

]

for url in mylist:
    browser.get(url)
    time.sleep(4)
    print("Product_urls", url)

    l3_name = browser.find_element(By.XPATH, "//nav[@class='woocommerce-breadcrumb']").text.strip()
    print('l3_name.....', l3_name)


    product_title = browser.find_element(By.XPATH, "//div[@class='summary entry-summary']//h1").text.strip()
    print('product_title.....', product_title)

    price = browser.find_element(By.XPATH, "//p[@class='price']").text.strip()
    print('price.....', price)


    short_description = browser.find_element(By.XPATH, "//div[@class='woocommerce-product-details__short-description']").text.strip().replace("\n", ">>")
    print('short_description.....', short_description)

    description = []
    for des in browser.find_elements(By.XPATH, "//div[@id='tab-description']//p"):
        des_1 = des.text.strip()
        description.append(des_1)
    print('description.....', description)

    try:
        image = []
        img_1 = browser.find_element(By.XPATH, "//div[@class='woocommerce-product-gallery woocommerce-product-gallery--with-images woocommerce-product-gallery--columns-4 images']")
        image_tag = img_1.find_elements(By.TAG_NAME, "a")
        for img_3 in image_tag:
            image_href = img_3.get_attribute('href')
            image.append(image_href)

        while len(image) < 5:
            image.append('')

        print('image.....', image)
    except Exception as e:
        image = ['N/A'] * 5
        print('object has no attribute ... image')




    related_url = []
    for relat in browser.find_elements(By.XPATH, "//section[@class='related products']//li//a"):
        related = relat.get_attribute('href')
        related_url.append(related)
    print('related_url.....', related_url)


"""
    option = browser.find_element(By.XPATH, "//select[@id='reach']")
    clickable = option.find_elements(By.XPATH, '//*[@id="reach"]/option')
    for i in range(1, len(clickable) + 1):
        option = browser.find_element(By.XPATH, "//select[@id='reach']")
        clickable = option.find_elements(By.XPATH, '//*[@id="reach"]/option')
        clk = clickable[i - 1]
        if "Choose an option" not in clk.text:
            clk.click()
            time.sleep(2)

            option_2 = browser.find_element(By.XPATH, "//select[@id='motor-speed']")
            clickable_2 = option_2.find_elements(By.XPATH, '(//select[@id="motor-speed"])//option')
            for i_2 in range(1, len(clickable_2) + 1):
                option_2 = browser.find_element(By.XPATH, "//select[@id='motor-speed']")
                clickable_2 = option_2.find_elements(By.XPATH, '(//select[@id="motor-speed"])//option')
                clk = clickable_2[i_2 - 1]
                if "Choose an option" not in clk.text:
                    clk.click()
                    time.sleep(2)

                    price = browser.find_element(By.XPATH, "//div[@class='woocommerce-variation-price']//span").text.strip()
                    print('price.....', price)

                    sku = browser.find_element(By.XPATH, "//div[@class='product_meta']//span[1]").text.strip()
                    print('sku.....', sku)
                    
                    category = browser.find_element(By.XPATH, "//div[@class='product_meta']//span[2]").text.strip()
                    print('category.....', category)


"""


















    # option = browser.find_element(By.XPATH, "//select[@id='reach']")
    # clickable = option.find_elements(By.XPATH, '//*[@id="reach"]/option')
    # for i, clk in enumerate(clickable, start=1):
    #     if "Choose an option" not in clk.text:
    #         click_value = option.find_element(By.XPATH, f'//*[@id="reach"]/option[{i}]')
    #         click_value.click()
    #         time.sleep(2)

        # option_2 = browser.find_element(By.XPATH, "//select[@id='motor-speed']")
        # clickable_2 = option_2.find_elements(By.XPATH, '(//select[@id="motor-speed"])//option')
        # for i_2, clk_2 in enumerate(clickable_2, start=1):
        #     click_value_2 = option_2.find_element(By.XPATH, f'(//select[@id="motor-speed"])//option[{i_2}]')
        #     click_value_2.click()
        #     time.sleep(2)


