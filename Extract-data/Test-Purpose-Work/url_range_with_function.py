import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def Get_driver():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def Request_url(driver):
    urls = []
    for num in range(1, 3):
        url = f'https://www.govets.com/isaac/search/result/?qty_inc=2&q=regal&v=1716791168&page={num}'
        driver.get(url)
        time.sleep(30)
        urls.append(url)
    return urls

def Get_Url(driver, urls):
    with open('Regal.txt', 'a+', encoding='utf-8') as file_save:
        for url in urls:
            driver.get(url)
            time.sleep(30)
            for product_cate in driver.find_elements(By.CSS_SELECTOR, ".product-item-link"):
                product_url = product_cate.get_attribute('href')
                file_save.write(f"{product_url}\n")
                print(product_url)
            print("current_url....................", driver.current_url)
    driver.quit()

def main():
    driver = Get_driver()
    urls = Request_url(driver)
    Get_Url(driver, urls)


if __name__ == "__main__":
    main()
