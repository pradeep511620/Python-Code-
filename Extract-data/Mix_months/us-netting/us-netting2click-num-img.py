import time
from typing import TextIO

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

mylst = [

    # 'https://www.usnetting.com/safety-netting/debris-netting/rolls/heavy-duty-fire-retardant-debris-netting-roll/',
    # 'https://www.usnetting.com/safety-netting/debris-netting/rolls/standard-duty-fire-retardant-debris-netting-roll/',

]

l = 0

for url in mylst:
    l += 1
    driver.get(url)
    time.sleep(6)
    print("Product-url...", l, url)

    description = ''
    features = ''
    meta_title = driver.find_element(By.XPATH, '/html/head/title').get_attribute("innerHTML")
    print("meta_title...", meta_title)

    print("********** Breadcrumb : **********")
    bread = driver.find_element(By.CLASS_NAME, "breadcrumbs").text.replace('\n', '>>')
    print('bread...', bread)

    print("********** Title : **********")
    title = driver.find_element(By.TAG_NAME, 'h1').text.strip()
    print('Title...', title)
    print("********** Description : **********")


#    Single click options ================================================================================
    #  Length of First option
    count = driver.find_element(By.XPATH, "//div[@class='size-select-container']").find_elements(By.TAG_NAME, "option")
    length = len(count)
    for ln in count:
        if "Select Size" not in ln.text:
            ln.click()
            number = ln.text
            print(number)
            time.sleep(2)

            #  Length of Second option
            click2 = driver.find_element(By.XPATH, "//div[contains(@class,'option-description js-active radio-img-container colors')]").find_elements(By.CLASS_NAME, "radio-img")
            length = len(click2)
            for cl in click2:
                cl.click()
                color = cl.text
                print('color...', color)
                time.sleep(2)

                #   Get Price Here
                try:
                    print("********** Price : **********")
                    price = driver.find_element(By.CLASS_NAME, "cargo-netting-product-price").text.strip()
                    print("Price...", price)
                except:
                    price = "Not Found"
                    print("Not Found")

                #   Get Images Here
                for img in driver.find_element(By.XPATH, "//div[@class='product-photos col-xs-12 col-sm-5']").find_elements(By.TAG_NAME, "img"):
                    images = img.get_attribute('src')
                    print("Images...", images)
                    save_d: TextIO = open("us-netting-num-img2.txt", 'a+', encoding="utf-8")
                    save_d.write('\n' + url + "\t" + meta_title + "\t" + bread + "\t" + title + "\t" + number + "\t" + color + "\t" + price + "\t" + images + "\t" + features + "\t" + description)
                print('data save into files')
            print('for loop 2')
        print("if condition")
    print("for loop1")

    try:
        description = driver.find_element(By.XPATH, "//div[@class='product-info']//p").text.strip()
        print('description...', description)
    except:
        print("Not Found")

    print("********** Description : **********")
    try:
        features = []
        for feature in driver.find_elements(By.XPATH, "//body/div[contains(@class,'main-section single-product')]/div[contains(@class,'container')]/div[@id='cargo-netting-products']/div/div[contains(@class,'row')]/div[contains(@class,'col-xs-12')]/div[contains(@class,'product-box')]/div[contains(@class,'col-xs-12 col-sm-7')]/div[contains(@class,'product-info')]/div/ul/li"):
            features.append(feature.text)
        print('description...', features)
        save_d: TextIO = open("us-netting-num-img2.txt", 'a+', encoding="utf-8")
        save_d.write('\n' + url + "\t" + meta_title + "\t" + bread + "\t" + title + "\t" + number + "\t" + color + "\t" + price + "\t" + images + "\t" + "".join(features) + "\t" + description)
        print('data save into files')
    except:
        print("Not Found")
