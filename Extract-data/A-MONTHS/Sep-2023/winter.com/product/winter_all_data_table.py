# import mysql.connector
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate
from selenium import webdriver
from selenium.common import NoSuchElementException, MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/winter.com/data/winter-all-data.csv", 'a',
                  encoding='utf-8')


def Get_Soup_Url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def Get_Driver_Urls(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    # driver = webdriver.Chrome()
    # driver = webdriver.Chrome(options=opts)
    driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    return driver


def product_detail(url, driver):
    # print(driver)
    actions = ActionChains(driver)
    driver.execute_script('return document.querySelector("body > app-root > app-cookies-banner > div > div.dir-row.sub-content > div.dir-row.btn-space > button.red-btn")').click()
    time.sleep(1)

    try:
        product_title = driver.find_element(By.XPATH, "//h1[@class='rto title-product left web-only']").text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute ... product_title')
    except NoSuchElementException:
        print('')
    #

    # try:
    #     driver.execute_script(f"window.scrollBy(0, {600});")
    #     time.sleep(2)
    # except NoSuchElementException:
    #     print('nnnnnnnnnnnnnnnnnnnnnnn')

    # try:
    #     slk = driver.find_element(By.XPATH, "//button[normalize-space()='SEE MORE']")
    #     actions = ActionChains(driver)
    #     actions.move_to_element(slk).click().perform()
    #     time.sleep(5)
    # except Exception as e:
    #     print("An error occurred:", str(e))

    try:
        slk = driver.find_element(By.XPATH, "//button[normalize-space()='SEE MORE']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", slk)
        wait = WebDriverWait(driver, 10)
        slk = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='SEE MORE']")))
        actions = ActionChains(driver)
        driver.execute_script("arguments[0].click();", slk)
        actions.move_to_element(slk).click().perform()
        driver.execute_script("arguments[0].click();", slk)
    except MoveTargetOutOfBoundsException:
        time.sleep(1)
        print("An error occurred:")
        count = 0
        d = []
        attr_name = []
        attr_value = []
        table = driver.find_elements(By.XPATH, "//div[@class='tabs-space specs-space ng-star-inserted']//table//td")
        for tr in table:
            tab = tr.text.strip()
            if tab:
                d.append(tab)
        for td in d:
            count += 1
            if count % 2 != 0:
                attr_name.append(td)
            else:
                attr_value.append(td.replace('\n', '<<'))
        for a, b in zip(attr_name, attr_value):
            print(a, "...", b)
        # save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/winter.com/data/winter_specs1.txt", 'a+', encoding='utf-8')
        # save.write('\n' + url + " \t" + product_title + "\t" + a + "\t" + b)
        # print('save data into table files ................1')



def main():
    url_link_count = 0
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/winter.com/url/winter_product_url.csv")['url']
    for url in url_link[0:]:
        url_link_count += 1
        print("Product-Length...", url_link_count)
        print("Product-Urls......", url)
        # soup = Get_Soup_Url(url)
        # product_title = product_detail(url, soup)
        # get_specs(url, soup, product_title)

        # selenium calling here
        driver = Get_Driver_Urls(url)
        product_detail(url, driver)
        # get_specs(url, driver)
    print('loop End')


if __name__ == "__main__":
    main()









