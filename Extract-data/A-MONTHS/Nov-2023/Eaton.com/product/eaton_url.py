import time
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
# browser = webdriver.Chrome(options=opts)
browser = webdriver.Chrome()
browser.maximize_window()
#

website_url = 'https://www.eaton.com/us/en-us/site-search.html.searchTerm$SVX125A2-5A4N1.tabs$all.html'
browser.get(website_url)
time.sleep(3)
print("Product_urls", website_url)

url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Nov-2023/eaton.com/url/eaton_mpn.csv")['MPN']
print(len(url_link))
i = 0
for url_count, url in enumerate(url_link[i:5], start=i):
    # browser.get(url)
    # time.sleep(2)
    print("Product-Urls......", url_count, url)
    try:
        browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
        print("click accept all cookies")
    except NoSuchElementException:
        print("Not Found accept all cookies")

    browser.find_element(By.XPATH, "//div[@class='header-utility-nav__toggle-selector search__utility']//textarea[@id='site-search-box']").clear()
    print('clear')
    browser.find_element(By.XPATH, "//*[@id='site-search-box']").send_keys(url)
    print('send url')
    time.sleep(2)
    browser.find_element(By.XPATH, "//div[@class='header-utility-nav__toggle-selector search__utility']//button[@type='submit']").click()
    print('click')
    time.sleep(1)
    browser.find_element(By.XPATH, "//div[@class='header-utility-nav__toggle-selector search__utility']//textarea[@id='site-search-box']").clear()
    print('clear')
    time.sleep(1)


    product_url = browser.find_element(By.XPATH, "(//h4[@class='results-list-submodule__name b-heading-h5'])[1]//a")
    product_href = product_url.get_attribute('href')
    print('product_href.....', product_href)
    with open('product_url_weg.txt', 'a+', encoding='utf-8') as save:
        save.write('\n' + product_href)
    print('save 1')
