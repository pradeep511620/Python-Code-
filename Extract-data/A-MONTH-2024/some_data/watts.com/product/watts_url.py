import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import ChromeOptions


def ReadChromeDriver(product_url):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(5)

    return driver


def ReadSoupUrl(product_url):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    ress = requests.get(product_url, headers=header)
    soup = BeautifulSoup(ress.content, "html.parser")

    return soup


def FetchProductUrl(driver):

    try:
        option = driver.find_element(By.ID, "SelectResultCount").find_elements(By.TAG_NAME, "option")
    except NoSuchElementException:
        option = ''
    for opn in option:
        clk = opn.text.strip()
        if clk == "60":
            print("count......................", clk)
            opn.click()
            time.sleep(4)
            break
    # try:
    #     driver.execute_script(f"window.scrollBy(0, {5500});")
    # except:
    #     driver.execute_script(f"window.scrollBy(0, {5500});")

    for product in driver.find_elements(By.XPATH, "//div[@class='js-results-target results-target']//a"):
        product_url_main = product.get_attribute('href')
        print(product_url_main)
        with open("prod1.txt", 'a+', encoding="utf-8") as file_save:
            file_save.write(f"{product_url_main}\n")


    url_length = driver.find_element(By.XPATH, "//div[@id='divsort']//h2").text.strip().split(" ")[0]
    length = round(int(url_length) / 60 + 1)
    print(length)

    for i in range(1, length):
        try:
            next_page_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='>']")))
            driver.execute_script("arguments[0].scrollIntoView();", next_page_link)
            next_page_link.click()
            time.sleep(4)
        except:
            try:
                next_page_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='>']")))
                driver.execute_script("arguments[0].scrollIntoView();", next_page_link)
                next_page_link.click()
                time.sleep(4)
            except Exception as e:
                print(f"Error processing {driver.current_url}: {e}")

            for product in driver.find_elements(By.XPATH, "//div[@class='js-results-target results-target']//a"):
                product_url_main = product.get_attribute('href')
                print(product_url_main)
                with open("prod1.txt", 'a+', encoding="utf-8") as file_save:
                    file_save.write(f"{product_url_main}\n")

        for product in driver.find_elements(By.XPATH, "//div[@class='js-results-target results-target']//a"):
            product_url_main = product.get_attribute('href')
            print(product_url_main)
            with open("prod1.txt", 'a+', encoding="utf-8") as file_save:
                file_save.write(f"{product_url_main}\n")
    print('')


def ReadFromListUrl():
    # file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Knapeandvogt.com/url/Product-url.csv"
    # url_lists = pd.read_csv(file_path)["URL"]

    url_list = [

        # 'https://www.watts.com/products/water-quality-rainwater-harvesting-solutions',
        'https://www.watts.com/products/plumbing-flow-control-solutions',
        'https://www.watts.com/products/drainage-solutions',
        'https://www.watts.com/products/hvac-hot-water-solutions',
    ]

    # Read url from file to compare url

    i = 0
    for N0, product_url in enumerate(url_list[i:], start=i):
        print("Product --", N0, product_url)

        # soup = ReadSoupUrl(product_url)
        # FetchProductUrl(soup)

        driver = ReadChromeDriver(product_url)
        try:
            FetchProductUrl(driver)
        except Exception as e:
            print(f"Error processing {product_url}: {e}")
        finally:
            driver.quit()

    print('Saved Url')


def main():
    ReadFromListUrl()


if __name__ == "__main__":
    main()
