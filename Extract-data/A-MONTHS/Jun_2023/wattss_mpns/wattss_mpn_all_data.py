import csv
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Chrome(options=chrome_options)

browser.maximize_window()

url = 'https://www.watts.com/'

browser.get(url)
print("Product_urls", url)
time.sleep(3)
with open("C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/wattss_mpns/watts_mpns.csv", 'r') as file:
    # with open("/var/www/html/webscr/source_dir/watts_mpn.csv", 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

for csv_link in range(6980, 6990):
    url = csv_list[csv_link][0].replace('ï»¿', '').replace('rp_', '')
    print("Product-Length...", csv_link)
    print("Urls......", url)
    time.sleep(1)
    browser.find_element(By.XPATH, "//button[@id='skiptosearchdesk']").click()
    print('click search button')
    time.sleep(2)

    browser.find_element(By.ID, "searchtermdesk").send_keys(url)
    print('enter mpns in search bar')
    time.sleep(1)
    #
    browser.find_element(By.XPATH, "//form[@aria-controls='skiptosearchdesk']//div[@class='js-search-bar__button search-bar__button']").click()
    print('click search button')
    time.sleep(5)

    try:
        browser.find_element(By.XPATH, "//div[@class='js-results-target results-target']//a[1]").click()
        print('click product')
    except NoSuchElementException:
        print('')

    get_current_urls = browser.current_url
    print("Current_Urls...", get_current_urls)

    try:
        browser.find_element(By.XPATH, "//p[@class='ean-ucc-code']")
        get_current_urls = browser.current_url
        print("Get_Current_Urls...", get_current_urls)
        save = open('product_current.txt', 'a+', encoding='utf-8')
        save.write('\n' + get_current_urls)
        print('save current urls')
    except NoSuchElementException:
        print('Exceptions')

    try:
        # browser.find_element(By.XPATH, "//div[@class='js-show-all-button-container show-all-button-container button__container']//a").click()
        browser.find_element(By.XPATH, "//a[normalize-space()='View all models']").click()
        time.sleep(3)
    except NoSuchElementException:
        print('unable to locate element')
    except ElementNotInteractableException:
        print('element not interactable')

        print('unable to locate')
    for product in browser.find_elements(By.XPATH, "//div[@class='js-results-target results-target']//a"):
        product_urls = product.get_attribute('href')
        save = open('product.txt', 'a+', encoding='utf-8')
        save.write('\n' + product_urls)
        print(product_urls)
