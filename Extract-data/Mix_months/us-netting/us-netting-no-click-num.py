import time
from typing import TextIO

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

mylst = [

    # 'https://www.usnetting.com/safety-netting/construction/temporary-fence/standard-duty-folded-temporary-fence/',
    # 'https://www.usnetting.com/safety-netting/construction/temporary-fence/heavy-duty-temporary-fence/',
    # 'https://www.usnetting.com/fence/snow-fence/fence-post-driver/',
    # 'https://www.usnetting.com/fence/snow-fence/sod-staples/',
    # 'https://www.usnetting.com/fence/snow-fence/t-post-puller/',
    # 'https://www.usnetting.com/fence/snow-fence/wooden-snow-fence/',
    # 'https://www.usnetting.com/hardware/bungee-clips/',
    # 'https://www.usnetting.com/hardware/hook-and-barrel-bungee-cord/',
    # 'https://www.usnetting.com/hardware/scaffold-clips/',
    # 'https://www.usnetting.com/hardware/secure-clips/',
    # 'https://www.usnetting.com/hardware/snaphooks/',
    # 'https://www.usnetting.com/hardware/stainless-steel-zip-ties/',


]
l = 0

for url in mylst:

    # def extract_data(url):
    l += 1
    driver.get(url)
    time.sleep(2)
    print("Product-url...", l, url)
    images = ''
    bread = ''
    a = ''
    b = ''
    num = ''
    description = ''

    print("********** Meta-Title : **********")
    meta_title = driver.find_element(By.XPATH, '/html/head/title').get_attribute("innerHTML")
    print("meta_title...", meta_title)
    try:
        print("********** Breadcrumb : **********")
        bread = driver.find_element(By.CLASS_NAME, "breadcrumbs").text.replace('\n', '>>')
        print('bread...', bread)
    except:
        pass

    print("********** Title : **********")
    title = driver.find_element(By.TAG_NAME, 'h2').text.strip()
    print('Title...', title)

    print("********** Price : **********")
    price = driver.find_element(By.CLASS_NAME, "price").text.strip()
    print("Price...", price)

    print("********** Description : **********")
    try:
        description = driver.find_element(By.XPATH, "//div[@class='single-product-description']").text.strip()
        print('description...', description)
        save_d: TextIO = open("no-clik_num.txt", "a+", encoding="utf-8")
        save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + price + '\t' + description.strip())
        print('save data into files price')
    except:
        # save_d: TextIO = open("no-clik_num.txt", "a+", encoding="utf-8")
        # save_d.write(
        #     '\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + price + '\t' + description.strip())
        # print('save data into files price')
        print("Not Found")

    name = []
    value = []
    # for desc in driver.find_elements(By.CLASS_NAME, "single-product__description__list"):
    for desc in driver.find_elements(By.XPATH, "//ul[@class='single-product__description__list']"):
        value.append(desc.text.split('\n'))
        name.append('name')
    # print(name)
    for a, b in zip(name, value):
        print(a, ".....", b)
        save_d: TextIO = open("no-clik_num.txt", "a+", encoding="utf-8")
        save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + price + '\t' + description + '\t' + a + '\t' + "".join(b))
    print('save data into files price')


# def main():
#     extract_data(url)

