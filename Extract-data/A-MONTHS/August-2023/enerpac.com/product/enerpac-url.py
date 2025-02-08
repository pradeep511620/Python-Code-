import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()


url = 'https://www.enerpac.com/en-us/'

browser.get(url)
print("Product_urls", url)
time.sleep(2)

with open("C:/Users/PK/Desktop/Python_project/scrape/Web-Scrapping/August-2023/enerpac.com/url/Hand_Tools_ENERPAC_request.csv",'r') as file:
    # with open("/var/www/html/webscr/source_dir/url/Vermont_gage_Product1.csv", 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)
    print(csv_length)

for csv_link in range(1, csv_length):
    url = csv_list[csv_link][0]
    print("Product-Length...", csv_link)
    print("Urls......", url)


    try:
        browser.execute_script('return document.querySelector("#regionDropdownModal > div > div.modal-body > div > div:nth-child(1) > div.col.col-sm-4.pointer")').click()
        print('click')
    except AttributeError:
        print('Not click pop up')

    browser.find_element(By.XPATH, "//input[@id='theSearch']").send_keys(url)
    time.sleep(1)

    browser.find_element(By.XPATH, "//button[@jason='desktop']//*[name()='svg']").click()
    time.sleep(1)
    get_current_url = browser.current_url
    print('get_current_url.....1', get_current_url)
    save = open('enerpac_product_url.txt', 'a+', encoding='utf-8')
    save.write('\n' + get_current_url)

    try:    # click product page
        browser.find_element(By.XPATH, "//div[@class='row EnerpacDynamicProductList__Table EnerpacDynamicProductList__Table--Desktop ']//img[1]").click()
        time.sleep(1)
        get_current_url = browser.current_url
        print('get_current_url.....2', get_current_url)
        save = open('enerpac_product_url.txt', 'a+', encoding='utf-8')
        save.write('\n' + get_current_url)
    except:
        print("not click product page")
