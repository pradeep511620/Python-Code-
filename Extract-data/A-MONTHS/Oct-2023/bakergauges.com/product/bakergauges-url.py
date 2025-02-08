import time
from selenium import webdriver
from selenium.common import NoSuchElementException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()

mylist = [
    'https://www.airvise.com/pneumatic-vise-cnc-vise-workholding-s/141.htm',
    'https://www.airvise.com/vise-jaws-soft-table-vise-jaws-self-centering-s/148.htm',
    'https://www.airvise.com/workholding-automation-UR-robot-cobot-s/146.htm',
    'https://www.airvise.com/vise-operations-kit-manual-robot-operation-kit-s/147.htm',
    'https://www.airvise.com/workholding-cnc-grippers-vise-grip-s/150.htm',
    'https://www.airvise.com/Air-Vise-Fittings-s/171.htm',
    'https://www.airvise.com/Air-Vise-Jaw-Accessories-s/174.htm',
    'https://www.airvise.com/Air-Vise-Pneumatics-s/165.htm',
    'https://www.airvise.com/Air-Vise-Tubing-s/170.htm',
    'https://www.airvise.com/category-s/172.htm',
    'https://www.airvise.com/category-s/199.htm',


]

for url in mylist:
    browser.get(url)
    print("Product_urls", url)
    time.sleep(2)

    for product in browser.find_elements(By.XPATH, "//div[@class='v-product-grid']//a"):
        product_url = product.get_attribute('href')
        if 'ShoppingCart' not in product_url:
            print(product_url)
            save = open("url1.txt", "a+", encoding="utf-8")
            save.write(f"\n {product_url}")
    print('save url ...........1')

    # count_of_total_url_number = browser.find_element(By.XPATH, "//p[@class='woocommerce-result-count']").text.strip().split(' ')[-2]
    # print('count_of_total_url_number.....', count_of_total_url_number)
    # length = round(int(count_of_total_url_number) / 80 + 1)
    # print(length)
    # for i in range(1, length):
    #     try:
    #         browser.find_element(By.XPATH, "//a[contains(text(),'→')]").click()
    #         time.sleep(3)
    #         print(i)
    #     except NoSuchElementException:
    #         print('Unable to locate element')
    #
    #     for product in browser.find_elements(By.XPATH, "//ul[@class='products columns-5']//li//a"):
    #         product_url = product.get_attribute('href')
    #         print(product_url)
    #         save = open("url1.txt", "a+", encoding="utf-8")
    #         save.write(f"\n {product_url}")
    # print('save url ...........2')
