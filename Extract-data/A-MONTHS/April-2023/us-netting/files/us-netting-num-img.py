import time
from typing import TextIO

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

mylst = [
    # 'https://www.usnetting.com/fence/safety-fence/economy-plastic-safety-fence/',
    # 'https://www.usnetting.com/fence/safety-fence/heavy-duty-plastic-safety-fence/',
    # 'https://www.usnetting.com/fence/safety-fence/privacy-screen/',
    # 'https://www.usnetting.com/fence/snow-fence/heavy-duty-plastic-snow-fence/',
    # 'https://www.usnetting.com/fence/snow-fence/economy-plastic-snow-fence/',
    'https://www.usnetting.com/safety-netting/debris-netting/heavy-duty-debris-netting-panels/',
    'https://www.usnetting.com/safety-netting/debris-netting/standard-duty-debris-netting-panels/',
]
l = 0

for url in mylst:
    l += 1
    driver.get(url)
    time.sleep(4)
    print("Product-url...", l, url)
    number = ''
    price = ''
    description = ''
    images = ''

    meta_title = driver.find_element(By.XPATH, '/html/head/title').get_attribute("innerHTML")
    print("meta_title...", meta_title)

    print("********** Breadcrumb : **********")
    bread = driver.find_element(By.CLASS_NAME, "breadcrumbs").text.replace('\n', '>>')
    print('bread...', bread)

    print("********** Title : **********")
    title = driver.find_element(By.TAG_NAME, 'h1').text.strip()
    print('Title...', title)

    # Length of First option
    count = driver.find_element(By.XPATH, "//select[@name='sizes']").find_elements(By.TAG_NAME, "option")
    length = len(count)
    print(length)
    for ln in count:
        ln.click()
        number = ln.text
        print(number)
        time.sleep(3)

        # Length of Second option
        color = (driver.find_element(By.XPATH, "//div[@class='product-info']//form/div[6]").find_elements(By.TAG_NAME, "img"))
        for ln1 in color:
            ln1.click()
            # print("value-of-second-click..", ln1.text)
            time.sleep(3)
        #
        #     #   Get Price Here
            print("********** Price : **********")
            price = driver.find_element(By.XPATH, "//div[@class='single-product__price']").text.strip()
            print("Price...", price)
        #     #
        #     # #   Get Images Here
            for img in driver.find_element(By.XPATH, "//div[@class='col-xs-12 col-sm-6 product-photos']").find_elements(By.TAG_NAME, "img"):
                images = img.get_attribute('src')
                print("Images...", images)
                save_d: TextIO = open("us-netting-num-img2.txt", 'a+', encoding="utf-8")
                save_d.write('\n' + url + "\t" + meta_title + "\t" + bread + "\t" + title + "\t" + number + "\t" + price + "\t" + images.strip())
            print('data save into files')

    print("********** Description : **********")
    try:
        description = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div[3]/form/div[8]/ul').text.strip().replace("\n", ">>")#.find_element(By.TAG_NAME, 'p').text.strip()
        print('description...', description)
    except:
        print("Not Found")

        print("********** Feature : **********")
    try:
        feature = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[2]/div[3]/form/div[7]/ul').text.strip().replace("\n", ">>")#.find_element(By.TAG_NAME, 'p').text.strip()
        print('Feature...', feature)
        save_d: TextIO = open("us-netting-num-img2.txt", 'a+', encoding="utf-8")
        save_d.write('\n' + url + "\t" + meta_title + "\t" + bread + "\t" + title + "\t" + number + "\t" + price + "\t" + images + "\t" + description + "\t" + feature.strip())
        print('data save into files')
    except:
        print("Not Found")
