import time
from typing import TextIO

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

mylst = [

        # 'https://www.usnetting.com/safety-solutions/wall-mounted-safety-nets/72-inch-tall-loading-dock-safety-net/',
        # 'https://www.usnetting.com/safety-solutions/above-ground-safety-nets/',
        # 'https://www.usnetting.com/fence/safety-fence/guardrail-safety-netting/',
        # 'https://www.usnetting.com/safety-netting/conveyor-netting/light-duty-conveyor-netting/',
        # 'https://www.usnetting.com/safety-netting/conveyor-netting/heavy-duty-conveyor-netting/',
        # 'https://www.usnetting.com/safety-netting/conveyor-netting/heavy-duty-conveyor-netting-w-debris-liner/',

        # 'https://www.usnetting.com/metal-netting/decorative-steel-netting/heavy-duty-decorative-steel-netting/',
        # 'https://www.usnetting.com/metal-netting/decorative-steel-netting/light-duty-decorative-steel-netting/',
        # 'https://www.usnetting.com/metal-netting/decorative-steel-netting/medium-duty-decorative-steel-netting/',

        'https://www.usnetting.com/fence/snow-fence/studded-steel-t-post/',
        'https://www.usnetting.com/safety-netting/guardrail-netting/',
        'https://www.usnetting.com/safety-solutions/wall-mounted-safety-nets/48-inch-tall-loading-dock-safety-net-with-debris-liner/',
        'https://www.usnetting.com/safety-solutions/wall-mounted-safety-nets/48-inch-tall-loading-dock-safety-net/',


]
l = 0

for url in mylst:
    l += 1
    driver.get(url)
    time.sleep(2)
    print("Product-url...", l, url)
    images = ''
    a = ''
    b = ''
    price = ''
    num = ''
    description = ''

    print("********** Meta-Title : **********")
    meta_title = driver.find_element(By.XPATH, '/html/head/title').get_attribute("innerHTML")
    print("meta_title...", meta_title)

    print("********** Breadcrumb : **********")
    bread = driver.find_element(By.CLASS_NAME, "breadcrumbs").text.replace('\n', '>>')
    print('bread...', bread)

    print("********** Title : **********")
    title = driver.find_element(By.TAG_NAME, 'h1').text.strip()
    print('Title...', title)

#    Single click options ================================================================================
    #  Length of First option
    count = driver.find_element(By.XPATH, "//div[@class='option-description']").find_elements(By.TAG_NAME, "option")
    length = len(count)
    for ln in count:
        ln.click()
        num = ln.text
        print(num)
        time.sleep(3)

        #   Get Price Here
        print("********** Price : **********")
        price = driver.find_element(By.CLASS_NAME, "single-product__price").text.strip()
        print("Price...", price)
        save_d: TextIO = open("oneclik_num.txt", "a+", encoding="utf-8")
        save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + num + '\t' + price)
    print('save data into files price')



    #   Get Images Here
    for img in driver.find_element(By.CLASS_NAME, "img-slider-container").find_elements(By.TAG_NAME, "img"):
        images = img.get_attribute('src')
        # print("Images...", images)
        save_d: TextIO = open("oneclik_num.txt", "a+", encoding="utf-8")
        save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + num + '\t' + price + "\t" + images)
    print('save data into files Images')

    print("********** Description : **********")
    try:
        description = driver.find_element(By.XPATH, "//div[@class='product-info']//p").text.strip()
        print('description...', description)
    except:
        print("Not Found")

#
    try:
        print("********** Table : **********")
        table1 = []
        table2 = []
        table = []
        name = []
        value = []
        for desc in driver.find_elements(By.CLASS_NAME, "single-product__description__list"):
            table = desc.text.strip().split('\n')
            for tab in table:
                if ":" in tab:
                    table = tab.split(':')
                    name.append(table[0].strip())
                    value.append(table[1].strip())
                else:
                    table2.append('name')

                    table1.append(tab.strip())
        for a, b in zip(name, value):
            print(a, ".....", b)
            save_d: TextIO = open("oneclik_num.txt", "a+", encoding="utf-8")
            save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + num + '\t' + price + "\t" + images + "\t" + description + "\t" + a + "\t" + b)
            print('tabel data 1')

            pass
        for j, h in zip(table2, table1):
            print(j, ".....", h)
            save_d: TextIO = open("oneclik_num.txt", "a+", encoding="utf-8")
            save_d.write('\n' + url + '\t' + meta_title + '\t' + bread + '\t' + title + '\t' + num + '\t' + price + "\t" + images + "\t" + description + "\t" + a + "\t" + b + "\t" + j + "\t" + h)
            print('tabel data 2')
            pass
    except:
        print("Not Found")
