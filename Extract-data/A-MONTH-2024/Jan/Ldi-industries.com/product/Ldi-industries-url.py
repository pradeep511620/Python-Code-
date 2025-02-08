import os
import time

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()


def ReadChromeDriver(product_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(6)

    return driver



def FetchProductUrl(driver):

    # driver.execute_script('return document.querySelector("path")').click()
    # time.sleep(3)
    # print('click...')
    # # try:
    # #     driver.find_element(By.XPATH, "(//*[name()='circle'])[1]").click()
    # #     time.sleep(4)
    # # except NoSuchElementException:
    # #     print('nn')
    #
    # try:
    #     driver.find_element(By.XPATH, "//button[@id='close']").click()
    #     time.sleep(2)
    #     print('click 1')
    # except NoSuchElementException:
    #     print('not interact elements')
    #
    # try:
    #     driver.find_element(By.XPATH, "(//header[@class='modal-header'])[3]//button").click()
    #     time.sleep(2)
    #     print('click 2')
    # except NoSuchElementException:
    #     print('not interact elements')
    #
    #
    #
    # try:
    #     option = driver.find_element(By.ID, "limiter-top").find_elements(By.TAG_NAME, "option")
    # except NoSuchElementException:
    #     option = ''
    # for opn in option:
    #     clk = opn.text.strip()
    #     print(clk)
    #     if clk == "All Items":
    #         opn.click()
    #         time.sleep(2)
    #         break

    try:
        for product in driver.find_elements(By.XPATH, "(//div[@class='item'])//a"):
            product_url_main = product.get_attribute('href')

            print(product_url_main)
            with open("prod.txt", 'a+', encoding="utf-8") as file_save:
                file_save.write(f"{product_url_main}\n")
        print('')
    except NoSuchElementException:
        print('//')





def ReadUrlFromFile():
    compare_product_url = []
    compare_url = pd.read_csv('already-scrape-url.csv')['URL']
    for compare_urls in compare_url:
        compare_product_url.append(compare_urls.strip())
    return compare_product_url





def ReadFromListUrl():

    # url_lists = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Globescientific.com/url/Globescientific-product-url.csv")["URL"]

    url_list = [

        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/AirOil-Reservoirs.htm',
        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/Centralized-Lubrication-Systems.htm',
        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/Chain-Oilers--Applicators.htm',
        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/Flow-Sights.htm',
        'https://www.ldi-industries.com/Catalog/lubrication-equipment/Inline-Filter---Liquid/Inline-Filter---Liquid.htm',
        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/Lubricators-and-Dispensers.htm',
        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/Metering--Shut-Off-Valves.htm',
        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/Pressure-Vacuum-Relief-Vents.htm',
        'https://www.ldi-industries.com/Catalog/lubrication-equipment/Sampling-Valve.htm',
        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/Sight-Plugs_LE.htm',
        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/Vented-Oil-Gages.htm',
        'https://www.ldi-industries.com/LDI/Lubrication-Equipment/Vents.htm',
        'https://www.ldi-industries.com/LDI/Specialty-Fittings--Valves/Self-Flare-Fittings.htm',
        'https://www.ldi-industries.com/LDI/Specialty-Fittings--Valves/LDI-Port-Connections.htm',
        'https://www.ldi-industries.com/LDI/Specialty-Fittings--Valves/CheckRelief-Valves.htm',
        'https://www.ldi-industries.com/LDI/Specialty-Fittings--Valves/Filter-Fittings.htm',
        'https://www.ldi-industries.com/LDI/Specialty-Fittings--Valves/Pressure-Vacuum-Relief-Vents.htm',
        'https://www.ldi-industries.com/LDI/Specialty-Fittings--Valves/CheckRelief-Valve-Design-Request-/Custom-Configurations.htm',
        'https://www.ldi-industries.com/LDI/Specialty-Fittings--Valves/CheckRelief-Valve-Design-Request-.htm',
        'https://www.ldi-industries.com/LDI/Specialty-Fittings--Valves/Filter-Fitting-Design-Request-Form.htm',
        'https://www.ldi-industries.com/LDI/Reservoirs-Tanks/JIC-Type-Reservoirs.htm',
        'https://www.ldi-industries.com/LDI/Reservoirs-Tanks/Reservoirs-with-Integrated-Skid.htm',
        'https://www.ldi-industries.com/LDI/Reservoirs-Tanks/Horizontal-Reservoirs.htm',
        'https://www.ldi-industries.com/LDI/Reservoirs-Tanks/Vertical-Reservoirs.htm',
        'https://www.ldi-industries.com/LDI/Reservoirs-Tanks/DIN-Type-Reservoirs.htm',
        'https://www.ldi-industries.com/LDI/Reservoirs-Tanks/Cylindrical-Reservoirs.htm',
        'https://www.ldi-industries.com/LDI/Reservoirs-Tanks/Custom-Reservoirs.htm',
        'https://www.ldi-industries.com/LDI/Reservoirs-Tanks/EZMOD-Program.htm',

    ]

    # Read url from file to compare url
    try:
        compare_product_url = ReadUrlFromFile()
    except FileNotFoundError:
        compare_product_url = ''
        print('file not found')

    # Read url one by one using list
    i = 0
    for N0, product_url in enumerate(url_list[i:], start=i):
        print("Product --", N0, product_url)


        # compare url in already exist file
        if product_url in compare_product_url:
            print(f"Skipped this {product_url} Url Because It Is Already Done")
            continue

        # colling function
        # FetchProductUrl()

        driver = ReadChromeDriver(product_url)
        try:
            FetchProductUrl(driver)
        finally:
            driver.quit()

        # save running url
        last_product_url = product_url
        file_path = 'already-scrape-url.csv'
        header = 'URL'
        file_exists = os.path.exists(file_path)
        with open(file_path, 'a', newline='', encoding='utf-8') as save:
            if not file_exists:
                save.write(f"{header}\n")
            save.write(f"{last_product_url}\n")
    print('Saved Url')


def main():
    ReadFromListUrl()


if __name__ == "__main__":
    main()
