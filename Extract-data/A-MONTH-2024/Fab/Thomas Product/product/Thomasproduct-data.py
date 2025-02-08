import time
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures
from urllib.parse import urljoin
from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidArgumentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Thomas Product/data/Thomas Product.csv", "a+", encoding="utf-8")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


def GetSoupUrl(urls):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get(urls)
    time.sleep(3)



    return driver


def Product_Details(urls, driver):
    print("Product-url---: ", urls)
# try:
    try:
        driver.find_element(By.XPATH, "//*[@aria-label='Close']").click()
        print('click pop up...................................1')
        time.sleep(2)
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//*[@aria-label='Close']").click()
        print('click pop up...................................1')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title_element = driver.find_element(By.CSS_SELECTOR, ".product_title")
        product_title = product_title_element.text.strip()
        print('product_title.....', product_title)
    except NoSuchElementException:
        product_title = 'N/A'
        print('product_title.....', product_title)

    # --------------------------------------------------- MPN ----------------------------------------------------------
    try:
        part_number = driver.find_element(By.XPATH, "//span[@class='sku_wrapper']//span").text.strip()
        mpn = part_number
        print('mpn.....', mpn)
    except NoSuchElementException:
        mpn = 'N/A'
        print('mpn.....', mpn)

    # -------------------------------------------------- Price-- -------------------------------------------------------

    price1 = driver.find_element(By.XPATH, "//p[@class='price']").text.strip()

    try:
        price_details = driver.find_element(By.XPATH, "(//span[@class='price'])[1]").text.strip()
        price = {"List_price": price_details, 'List_prices': price1}
        print('price.....', price)
    except NoSuchElementException:
        price = {'List_price': '$-.--'}
        print('price.....', price)
    # -------------------------------------------------- Shipping - Weight ---------------------------------------------

    # ---------------------------------------------- Description_1 -----------------------------------------------------
    try:
        short_des = driver.find_element(By.XPATH, "//div[@class='woocommerce-variation-description']").text.strip()
    except NoSuchElementException:
        short_des = ''

    try:
        description_1 = []
        for des in driver.find_elements(By.XPATH, "//div[@id='tab-description']//p"):
            texts = des.text.strip()
            if texts:
                description_1.append(texts)
        description_1 = {"desc": description_1, 'short-desc': short_des}
        print('description_1.....', description_1)
    except NoSuchElementException:
        description_1 = []
        print('description_1.....', description_1)

    # ---------------------------------------------- Description_2 -----------------------------------------------------
    try:
        description_2 = []
        for des_1 in driver.find_elements(By.XPATH, "//div[@id='tab-description']//ol//li"):
            text_1 = des_1.text.strip()
            if text_1:
                description_2.append(text_1)
        print('description_2.....', description_2)
    except NoSuchElementException:
        description_2 = []
        print('description_2.....', description_2)

    # -------------------------------------------------- Images --------------------------------------------------------
    try:
        images = []
        for images_html in driver.find_elements(By.XPATH, "//div[@class='woocommerce-product-gallery woocommerce-product-gallery--with-images woocommerce-product-gallery--columns-4 images']//img"):
            if images_html:
                image_src = images_html.get_attribute('src')
                alt_tag = images_html.get_attribute('title')
                image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                images.append(image_tag_and_alt_tag)
        print('images.....', images)
    except NoSuchElementException:
        images = ''
        print('images.....', images)

    # ------------------------------------------------ Datasheet -------------------------------------------------------
    try:
        datasheet = []
        for pdf in driver.find_elements(By.XPATH, "//div[@id='tab-description']//iframe"):
            datasheet.append(pdf.get_attribute('data-src'))
        print('datasheet.....', datasheet)
    except NoSuchElementException:
        datasheet = []
        print('datasheet.....', datasheet)

    # ------------------------------------------------- Realated -------------------------------------------------------
    try:
        realate_url = []
        for realated_href_tag in driver.find_elements('section', {"class": "d45Cza"}):
            if "Alternate Products" in realated_href_tag.text.strip():
                for alternet_url in realated_href_tag.find_all_next('a'):
                    alt_name = alternet_url.get('href')

        realated_url = [{'accessories': realate_url}]
        print("realated.....", realated_url)
    except (NoSuchElementException, InvalidArgumentException):
        realated_url = [{'accessories': []}]
        print("realated.....", realated_url)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        driver.find_element(By.XPATH, "(//ul[@role='tablist']//li)[2]").click()
        time.sleep(1)

        attr_name = []
        attr_value = []
        labels = driver.find_elements(By.CSS_SELECTOR, ".woocommerce-product-attributes-item__label")
        for label in labels:
            attr_name.append(label.text.strip())
        values = driver.find_elements(By.CSS_SELECTOR, ".woocommerce-product-attributes-item__value")
        for value in values:
            attr_value.append(value.text.strip())
        specifications_1 = []
        for name, value in zip(attr_name, attr_value):
            specifications_1.append({name: value})
        print("specifications_1.....", specifications_1)
    except NoSuchElementException:
        specifications_1 = []
        print("specifications_1.....", specifications_1)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        specifications_2 = []
        for specs_2 in driver.find_elements(By.XPATH, "//table[@id='tablepress-1']//tbody//td"):
            specifications_2.append(specs_2.text.strip())
        print('specifications_2.....', specifications_2)
    except NoSuchElementException:
        specifications_2 = []
        print('specifications_2.....', specifications_2)

    # ----------------------------------------------- Miscellaneous ----------------------------------------------------
    # try:
    #     cate_details = soup.find(class_="rOM8HV hRRBwT").text.strip()
    #     category = {"Item": cate_details}
    #     print('Item.....', category)
    # except AttributeError:
    #     category = []
    #     print('Item.....', category)

    # ------------------------------------------------------------------------------------------------------------------
    list_column = [
        "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
        "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
        "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
        "scraped_by"
    ]
    raw_data = [{
        "brand": "Thomas Products Ltd.", "catlvl1": 'N/A', "catlvl2": 'N/A', "catlvl3": 'N/A', "url": urls,
        "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": 'N/A',
        "breadscrumbs": 'N/A', "image_urls": images, "mpn": mpn,
        "specification_1": specifications_1, "specification_2": specifications_2, "datasheets": datasheet,
        "product_description_1": description_1, "product_description_2": description_2,
        "accessories": [{'accessories': []}], "video_links": [], "miscellaneous": 'N/A',
        "scraped_by": "Pradeep Kumar",
    }]
    print('Complete all Your Program')
    print()

    Data_Save(raw_data, list_column)
# except Exception as e:
#     print(f"Error....{e}")
#     print("Breaking the process due to error encountered.")
#     return
# ------------------------------------------------------------------------------------------------------------------


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def ReadUrlFromList():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Thomas Product/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:], start=i):
        urls.append(url)
        # print(url)

        # soup = GetSoupUrl(url)
        # Product_Details(url, soup)
    return urls


def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(lambda url: Product_Details(url, GetSoupUrl(url)), url_1)
        print('*******************************************************************************************************')


if __name__ == "__main__":
    main()
