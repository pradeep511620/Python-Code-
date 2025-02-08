import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()

# file_path = "C:/Users/PK/Desktop/web-scrapping/Test-Purpose-Work/urlsss.csv"
# url_list = pd.read_csv(file_path)['URL']

url_list = [




    'https://osgtool.com/milling/holders-milling/extensions-milling/9911-mill/',

]
start = 0
for url_c, url in enumerate(url_list[start:], start=start):
    driver.get(url)
    time.sleep(2)
    print('product_url.....', url_c, url)
    print('current_url..........', driver.current_url)

    try:
        driver.find_element(By.CSS_SELECTOR, ".css-1wn42nw .css-a0j149").click()
        time.sleep(1)
    except NoSuchElementException:
        print('None')

    try:
        main_url = driver.find_elements(By.CSS_SELECTOR, ".custom-table-container tbody tr a")
        for main_urls in main_url:
            product_url = main_urls.get_attribute('href')
            print(product_url)
            with open('osgtool_url.txt', 'a+', encoding='utf-8') as url_save:
                url_save.write(f'\n{product_url}\n')
    except NoSuchElementException:
        print('Not found')

    # while True:
    #     try:
    #         load_more_button = driver.find_element(By.CSS_SELECTOR, ".pagination-link.pagination-link--next")
    #         load_more_button.click()
    #         time.sleep(2)
    #     except NoSuchElementException:
    #         print("No more 'Load More' button found, exiting loop.")
    #         break
    #
    #     try:
    #         main_url = driver.find_elements(By.CSS_SELECTOR, ".custom-table-container tbody tr a")
    #         for main_urls in main_url:
    #             product_url = main_urls.get_attribute('href')
    #             print(product_url)
    #             with open('osgtool_url.txt', 'a+', encoding='utf-8') as url_save:
    #                 url_save.write(f'\n{product_url}\n')
    #     except NoSuchElementException:
    #         print('Not found')

    # try:
    #     main_url = driver.find_elements(By.CSS_SELECTOR, ".part-link")
    #     for main_urls in main_url:
    #         product_url = main_urls.get_attribute('href')
    #         # print(product_url)
    #         with open('saginawcontrol_url.txt', 'a+', encoding='utf-8') as url_save:
    #             url_save.write(f'\n{product_url}\n')
    # except NoSuchElementException:
    #     print('Not found')

driver.close()
driver.quit()
