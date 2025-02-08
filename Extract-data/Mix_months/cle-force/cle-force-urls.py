import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)


# first options to get urls
# find pagination value
def get_url():
    for change in range(1, 27 + 1):
        Result = [
            f'https://www.cmtindustrial.com/cat.php?nb%5BBrandName%5D%5B0%5D=Cle-Force&nameblock=noname&paginate%5Bpage%5D={change}&paginate%5Bitems_per_page%5D=15',
        ]
        for url in Result:
            # try:
            requests.get(url, headers=headers)
            driver.get(url)
            time.sleep(5)
            print("Products Urls", url)
            # click 45 option only
            driver.find_element(By.XPATH,
                                "//body[1]/div[6]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div[3]/div[1]/div[1]/button[3]").click()
            time.sleep(3)
            # find url and a tag after that get herf
            links = driver.find_element(By.XPATH,
                                        "//div[@class='ng-scope uk-flex uk-flex-middle uk-grid-small uk-grid']").find_elements(
                By.TAG_NAME, 'a')
            print(len(links))
            for x in links:
                url_links = (x.get_attribute('href'))
                data_urls = url_links
                print(data_urls)
                # save_details: url_links = open("cle-force_urls.txt", "a+", encoding="utf-8")
                # save_details.write("\n" + "'" + data_urls + "',")
                # print("\n ***** Record stored into urls  files. *****")


# call the function of get url and printed it
get_url()
