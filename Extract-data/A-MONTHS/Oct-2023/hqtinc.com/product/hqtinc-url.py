import time

from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()
# for i in range(489):
mylist = [

    'https://hqtinc.com/prestashop/index.php?id_category=4&controller=category&page=1',
    # 'https://hqtinc.com/prestashop/index.php?id_category=11&controller=category',

]

for url in mylist:
    browser.get(url)
    time.sleep(3)
    print("Product_urls", url)
    for product in browser.find_elements(By.XPATH, "//div[@id='js-product-list']//a"):
        product_link = product.get_attribute('href')
        if "#" not in product_link:
            print("'" + product_link + "',")
            save = open('url1.txt', 'a+', encoding='utf-8')
            save.write(f"{product_link}\n")


    # count = browser.find_element(By.XPATH, "//div[@class='col-md-4']").text.strip().split(' ')[-2]
    # lengths_count = len(count)
    # print('lengths', lengths_count)
    # length_c = round(int(lengths_count) / 20 + 1)
    # print('length', length_c)
    #
    # time.sleep(1)
    # print('time')
    for i in range(1, 3 + 1):
        browser.find_element(By.XPATH, "//a[@class='next js-search-link']").click()
        time.sleep(5)
        get_current_urls = browser.current_url
        # print(get_current_urls)
        print("Product_urls", url)
        save = open('url.txt', 'a+', encoding='utf-8')
        save .write(f"{get_current_urls}\n")
        # print(i)
    #     Result = [
    #         f"{url}/{'page'}/{i}"
    #     ]
    #     for pagination_link in Result:
    #         print("'" + pagination_link + "',")


        for product in browser.find_elements(By.XPATH, "//div[@id='js-product-list']//a"):
            product_link = product.get_attribute('href')
            if "#" not in product_link:
                print("'" + product_link + "',")
                save = open('url1.txt', 'a+', encoding='utf-8')
                save.write(f"{product_link}\n")

# url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/sourceasi.com/url/bakergauges_product_url - Copy.csv")['URL']
# url_length = 602
# for url_count, url in enumerate(url_link[url_length:], start=url_length):
#     browser.get(url)
#     time.sleep(1)
#     print("Product-Urls......", url)
#
