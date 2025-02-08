import time
from typing import TextIO

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

mylst = [

            # 'https://www.usnetting.com/cargo-netting/cargo-nets/1-inch-webbing-cargo-nets/snap-hooks/',
            # 'https://www.usnetting.com/cargo-netting/cargo-nets/1-inch-webbing-cargo-nets/loops/',
            # 'https://www.usnetting.com/cargo-netting/cargo-nets/1-inch-webbing-cargo-nets/rings/',
            # 'https://www.usnetting.com/cargo-netting/cargo-nets/1-inch-webbing-cargo-nets/snap-hooks/',
            # 'https://www.usnetting.com/cargo-netting/cargo-nets/2-inch-webbing-cargo-nets/grommets/',
            # 'https://www.usnetting.com/cargo-netting/cargo-nets/2-inch-webbing-cargo-nets/loops/',
            # 'https://www.usnetting.com/cargo-netting/cargo-nets/2-inch-webbing-cargo-nets/rings/',
            # 'https://www.usnetting.com/cargo-netting/cargo-nets/2-inch-webbing-cargo-nets/snap-hooks/',

            # three click images


]
l = 0

for url in mylst:
    l += 1
    driver.get(url)
    time.sleep(8)
    print("Product-url...", l, url)

    desc = ''
    images = ''
    price = ''
    meta_title = driver.find_element(By.XPATH, '/html/head/title').get_attribute("innerHTML")
    print("meta_title...", meta_title)

    print("********** Breadcrumb : **********")
    bread = driver.find_element(By.CLASS_NAME, "breadcrumbs").text.replace('\n', '>>')
    print('bread...', bread)

    print("********** Title : **********")
    title = driver.find_element(By.TAG_NAME, 'h1').text.strip()
    print('Title...', title)
    # Triple click options

    # try:
    #   Length of First option
    count = driver.find_element(By.XPATH, "//div[@class='option-description js-active material']").find_elements(By.NAME, "Material")
    length = len(count)
    for ln in count:
        time.sleep(2)
        ln.click()
        # time.sleep(2)

        #   Length of Second option
        count1 = driver.find_element(By.XPATH, "//div[contains(@class,'option-description js-active opening-size radio-img-container')]").find_elements(By.CLASS_NAME, "radio-img")
        for ln1 in count1:
            time.sleep(2)
            ln1.click()
            # time.sleep(2)

            # #  Length of Third option
            color2 = (driver.find_element(By.XPATH, "//div[@class='option-description js-active radio-img-container colors']").find_elements(By.TAG_NAME, "img"))
            for ln2 in color2:
                time.sleep(2)
                ln2.click()
                print(ln2.text)
                # time.sleep(2)

                #   Get Price Here
                try:
                    print("********** Price : **********")
                    price = driver.find_element(By.XPATH, "//div[@class=' cargo-netting-product-price']").text.strip()
                    print("Price...", price)
                except:
                    price = 'Not Found'
                    print("Not Found Price")

                #   Get Images Here
                for img in driver.find_element(By.XPATH, "//div[@class='product-photos col-xs-12 col-sm-5']").find_elements(By.TAG_NAME, "img"):
                    images = img.get_attribute('src')
                    print("Images...", images)
                    save_d: TextIO = open('three.txt', 'a+', encoding="utf-8")
                    save_d.write('\n' + url + "\t" + meta_title + "\t" + bread + "\t" + title + "\t" + price + "\t" + images)
                print('images and all data save into files')
    print("********** Description : **********")
    try:
        dess = []
        for description in driver.find_element(By.CLASS_NAME, "description").find_elements(By.TAG_NAME, 'li'):
            dess.append(description.text.strip())
        print('description...', dess)
    except:
        print("Not Found")

#
    print("********** Table : **********")
    try:
        name = []
        value = []
        i = 0
        for desc in driver.find_elements(By.XPATH, "//div[@class='materials']/table//tr/td"):
            i += 1
            if i % 2 != 0:
                name.append(desc.text.strip())
            else:
                value.append(desc.text.strip())
        for a, b, in zip(name, value):
            print(a, "......", b)
            save_d: TextIO = open('three.txt', 'a+', encoding="utf-8")
            save_d.write('\n' + url + "\t" + meta_title + "\t" + bread + "\t" + title + "\t" + price + "\t" + images + "\t" + str(desc) + "\t" + a + "\t" + b)
            print('table data')
    except Exception as e:
        print(e)
        print("Not Found")
