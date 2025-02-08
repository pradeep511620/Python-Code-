import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

mylst = [
    # 'https://www.usnetting.com/barrier-netting/ez-barrier-nets/'
    'https://www.usnetting.com/all-purpose-netting/knotless-netting/sbn-4045/',
    'https://www.usnetting.com/all-purpose-netting/knotless-netting/sbn-5100/',
    'https://www.usnetting.com/all-purpose-netting/knotless-netting/sbn-s800/',

]
l = 0

for url in mylst:
    l += 1
    driver.get(url)
    time.sleep(2)
    print("Product-url...", l, url)

    meta_title = driver.find_element(By.XPATH, '/html/head/title').get_attribute("innerHTML")
    print("meta_title...", meta_title)

    print("********** Breadcrumb : **********")
    bread = driver.find_element(By.CLASS_NAME, "breadcrumbs").text.replace('\n', '>>')
    print('bread...', bread)

    print("********** Title : **********")
    title = driver.find_element(By.TAG_NAME, 'h1').text.strip()
    print('Title...', title)
# Double click options  =============================== fist Option
    #   Length of First option
    count = driver.find_element(By.XPATH, "//div[contains(@class,'option-description js-active opening-size radio-img-container')] and //div[@class='option-description js-active radio-img-container border-style']").find_elements(By.CLASS_NAME, "radio-img")
    length = len(count)
    for ln in count:
        ln.click()
        # print("value-of-first-click", ln.text)
        time.sleep(3)

        #  Length of Second option
        color = (driver.find_element(By.XPATH, "//div[@class='option-description js-active radio-img-container colors']").find_elements(By.TAG_NAME, "img"))
        print(len(color))
        for ln1 in color:
            ln1.click()
            # print("value-of-second-click..", ln1.text)
            time.sleep(2)

            #   Get Price Here
            print("********** Price : **********")
            price = driver.find_element(By.XPATH, "//div[@class=' cargo-netting-product-price']").text.strip()
            print("Price...", price)

            #   Get Images Here
            for img in driver.find_element(By.XPATH, "//div[@class='product-photos col-xs-12 col-sm-7']").find_elements(By.TAG_NAME, "img"):
                images = img.get_attribute('src')
                print("Images...", images)

    print("********** Description : **********")
    try:
        description = driver.find_element(By.CLASS_NAME, "description").find_element(By.TAG_NAME, 'p').text.strip()
        print('description...', description)
    except:
        print("Not Found")

#
    print("********** Table : **********")
    try:
        name = []
        value = []
        for desc in driver.find_elements(By.XPATH, "//div[@class='description']//li"):
            table = desc.text.split(':')
            name.append(table[0].strip())
            value.append(table[1].strip())
        for a, b, in zip(name, value):
            print(a, "......", b)
    except:
        print("Not Found")
