import csv
import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()

mylist = [
    'https://www.gradientlens.com/product/luxxor-ltc-camera/',
]
for url in mylist:
    browser.get(url)
    print("Product_urls", url)
    time.sleep(1)
    #
    browser.find_element(By.XPATH, "//a[@class='expand-purchase btn btn-primary']").click()
    print('click buy now')

    print('start loop')
    options_1 = browser.find_element(By.XPATH, "//select[@id='product-type']").find_elements(By.TAG_NAME, 'option')
    option = []
    for option_op in options_1:
        # print("options.....", option_op.text)
        if "Choose an option" not in option_op.text:
            option.append(option_op.text)
    print('list of options')
    dropdown1 = Select(browser.find_element(By.ID, 'product-type'))
    length1 = len(dropdown1.options)
    print("length of option.....1", length1)

    for option1, item1 in zip(option, range(1, length1)):
        dropdown1 = Select(browser.find_element(By.ID, 'product-type'))
        print("first loop.....", item1)
        try:
            dropdown1.select_by_index(item1)
            time.sleep(1)
        except NoSuchElementException:
            print('nooooo')
        option_d1 = option1
        print("options.....1", option_d1)
        print('loop finished')
        time.sleep(1)

    # -------------------------------------------------------------------------------------------------

        all_options = browser.find_element(By.XPATH, "//select[@id='product']").find_elements(By.TAG_NAME, 'option')
        op = []
        for o in all_options:
            # print("options = ", o.text)
            # if "Choose an option" not in o.text:
            op.append(o.text)
        # print('list of options')
        dropdown2 = Select(browser.find_element(By.XPATH, "//select[@id='product']"))
        length2 = len(dropdown2.options)
        print("length of option.....2", length2)
        for option2, item2 in zip(op, range(0, length2)):
            dropdown2 = Select(browser.find_element(By.XPATH, "//select[@id='product']"))
            print("first loop.....2", item2)
            dropdown2.select_by_index(item2)
            time.sleep(4)
            option_d2 = option2
            print("options.....2", option_d2)

