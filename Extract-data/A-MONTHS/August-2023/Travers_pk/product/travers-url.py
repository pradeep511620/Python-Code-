import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome(options=opts)
browser.maximize_window()

with open("C:/Users/PK/Desktop/Python_project/scrape/Web-Scrapping/August-2023/Travers_pk/url/Vermont_gage_Product1.csv",'r') as file:
    # with open("/var/www/html/webscr/source_dir/url/Vermont_gage_Product1.csv", 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)
    print(csv_length)

for csv_link in range(20135, csv_length):
    url = csv_list[csv_link][0]
    print("Product-Length...", csv_link)
    print("Urls......", url)
    browser.get(url)
    time.sleep(3)
    #
    try:
        try:
            browser.find_element(By.XPATH, "//div[@class='list-and-flyout']//a[1]").click()
            time.sleep(1)
        except:
            print('not click')
        try:
            get_current_url = browser.current_url
            print('get_current_url...', get_current_url)
            save = open('traver_product_url20000.csv', 'a+', encoding='utf-8')
            save.write('\n' + get_current_url)
        except Exception as e:
            print(e)
    except Exception as e:
        get_current_url = browser.current_url
        print('get_current_url...', get_current_url)
        save = open('traver_product_url.csv', 'a+', encoding='utf-8')
        save.write('\n' + get_current_url)
        print()
