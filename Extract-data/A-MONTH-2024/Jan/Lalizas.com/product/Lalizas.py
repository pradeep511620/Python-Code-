import os
import time

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


def ReadChromeDriver(product_url):
    headless_mode = True
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    if headless_mode:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(2)

    return driver



def FetchProductUrl(driver):

    try:
        option = driver.find_element(By.ID, "limit").find_elements(By.TAG_NAME, "option")
    except NoSuchElementException:
        option = ''
    for opn in option:
        clk = opn.text.strip()
        if clk == "All Products":
            opn.click()
            time.sleep(4)
            break


    for product in driver.find_elements(By.XPATH, "//div[@class='span9']//a"):
        product_url_main = product.get_attribute('href')
        print("'"+product_url_main+"',")
        with open("prod.txt", 'a+', encoding="utf-8") as file_save:
            file_save.write(f"{product_url_main}\n")
    print('')





def ReadUrlFromFile():
    compare_product_url = []
    compare_url = pd.read_csv('already-scrape-url.csv')['URL']
    for compare_urls in compare_url:
        compare_product_url.append(compare_urls.strip())
    return compare_product_url





def ReadFromListUrl():

    # url_lists = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/kennametal.csv")["URL"]

    url_list = [

        'https://www.lalizas.com/category/117-liferafts',
        'https://www.lalizas.com/category/138-throw-overboard',
        'https://www.lalizas.com/category/139-throw-overboard-self-righting',
        'https://www.lalizas.com/category/140-davit-launched',
        'https://www.lalizas.com/category/141-davit-launched-self-righting',
        'https://www.lalizas.com/category/142-open-reversible',
        'https://www.lalizas.com/category/143-yachting',
        'https://www.lalizas.com/category/174-liferaft-equipment',
        'https://www.lalizas.com/category/118-inflatable-lifejackets',
        'https://www.lalizas.com/category/144-iso-inflatable-lifejackets',
        'https://www.lalizas.com/category/145-solas-inflatable-lifejackets',
        'https://www.lalizas.com/category/146-inflatable-lifejackets-accessories',
        'https://www.lalizas.com/category/119-foam-lifejackets',
        'https://www.lalizas.com/category/147-iso-foam-lifejacket-lifebelt',
        'https://www.lalizas.com/category/148-solas-foam-lifejackets',
        'https://www.lalizas.com/category/149-iso-watersports-buoyancy-aids',
        'https://www.lalizas.com/category/150-pets-buoyancy-aids',
        'https://www.lalizas.com/category/120-life-saving-lights',
        'https://www.lalizas.com/category/151-lifejackets-lights',
        'https://www.lalizas.com/category/152-lifebuoy-lights',
        'https://www.lalizas.com/category/121-mob-systems',
        'https://www.lalizas.com/category/153-lifebuoy-rings',
        'https://www.lalizas.com/category/154-horseshoes-lifebuoy',
        'https://www.lalizas.com/category/155-life-saving-apparatus',
        'https://www.lalizas.com/category/156-rescue-systems',
        'https://www.lalizas.com/category/157-safety-harness-jacklines',
        'https://www.lalizas.com/category/158-safety-ladders',
        'https://www.lalizas.com/category/159-sea-anchors-drogues',
        'https://www.lalizas.com/category/160-retroreflective-tapes',
        'https://www.lalizas.com/category/122-breathing-apparatus',
        'https://www.lalizas.com/category/161-solas-breathing-apparatus',
        'https://www.lalizas.com/category/123-fire-fighting-equipment',
        'https://www.lalizas.com/category/162-fireman-suits',
        'https://www.lalizas.com/category/163-firefighter-accessories',
        'https://www.lalizas.com/category/164-fire-extinguishers',
        'https://www.lalizas.com/category/165-fire-hoses-nozzles',
        'https://www.lalizas.com/category/166-fire-blanket',
        'https://www.lalizas.com/category/223-imo-signs',
        'https://www.lalizas.com/category/224-imo-symbols-on-self-adhesive-photoluminescent-vinyl',
        'https://www.lalizas.com/category/225-safety-signs-on-self-adhesive-photoluminescent-vinyl',
        'https://www.lalizas.com/category/226-photoluminiscent-direction-signs',
        'https://www.lalizas.com/category/227-fire-signs',
        'https://www.lalizas.com/category/228-fire-control-symbols-to-resolution-a654',
        'https://www.lalizas.com/category/229-fire-control-symbols-to-iso-17631',
        'https://www.lalizas.com/category/230-low-location-lighting',
        'https://www.lalizas.com/category/231-prohibition-signs',
        'https://www.lalizas.com/category/232-mandatory-signs',
        'https://www.lalizas.com/category/233-hazard-signs-diamonds',
        'https://www.lalizas.com/category/234-isps-code-signs-security-signs',
        'https://www.lalizas.com/category/235-deck-and-engine-room-signs',
        'https://www.lalizas.com/category/236-galley-signs',
        'https://www.lalizas.com/category/237-accommodation-signs',
        'https://www.lalizas.com/category/238-combination-signs',
        'https://www.lalizas.com/category/239-training-safety-and-environmental-posters-lalizas-posters',
        'https://www.lalizas.com/category/240-passenger-vessel-and-terminal-building-signs',
        'https://www.lalizas.com/category/241-temporary-tie-tags',
        'https://www.lalizas.com/category/242-pipe-identification',
        'https://www.lalizas.com/category/243-special-projects',
        'https://www.lalizas.com/category/125-navigation-lights',
        'https://www.lalizas.com/category/167-led-navigation-lights',
        'https://www.lalizas.com/category/168-standard-navigation-light',
        'https://www.lalizas.com/category/169-bulbs',
        'https://www.lalizas.com/category/132-marine-distress-signals-pyrotechnics',
        'https://www.lalizas.com/category/170-day-signals-reflectors',
        'https://www.lalizas.com/category/175-sound-signals',
        'https://www.lalizas.com/category/256-pyrotechnics',
        'https://www.lalizas.com/category/177-service',
        'https://www.lalizas.com/category/178-ffe-service',
        'https://www.lalizas.com/category/179-lifeboat-service',
        'https://www.lalizas.com/category/180-liferaft-service',
        'https://www.lalizas.com/category/181-breathing-apparatus-service',
        'https://www.lalizas.com/category/182-refurbishing',
        'https://www.lalizas.com/category/183-lifesaving-appliances-service',
        'https://www.lalizas.com/category/192-imo-signs',
        'https://www.lalizas.com/category/134-personal-protection',
        'https://www.lalizas.com/category/171-workwear',
        'https://www.lalizas.com/category/285-flashlights',
        'https://www.lalizas.com/category/135-survival-craft',
        'https://www.lalizas.com/category/176-lifeboat-equipment',
        'https://www.lalizas.com/category/116-buoys',
        'https://www.lalizas.com/category/137-round-buoys',
        'https://www.lalizas.com/category/115-mega-yacht-inflatable-fenders',
        'https://www.lalizas.com/category/124-immersion-suits',
        'https://www.lalizas.com/category/126-chemical-gas-protection-equipment',
        'https://www.lalizas.com/category/127-medical-equipment',
        'https://www.lalizas.com/category/128-embarkation-poilot-ladders',
        'https://www.lalizas.com/category/130-navigation-instruments',
        'https://www.lalizas.com/category/131-polar-survival-equipment',
        'https://www.lalizas.com/category/133-emergency-communication-devices',

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
        except Exception as e:
            print(f"Error processing {product_url}: {e}")
        finally:
            try:
                driver.quit()
            except:
                pass

        # save running url
        last_product_url = product_url
        file_path = 'already-scrape-url.csv'
        header = 'URL'
        file_exists = os.path.exists(file_path)
        with open(file_path, 'a', newline='', encoding='utf-8') as save:
            if not file_exists:
                save.write(f"{header}\n")
            save.write(f"{last_product_url}\n")

        driver.quit()
    print('Saved Url')


def main():
    ReadFromListUrl()


if __name__ == "__main__":
    main()
