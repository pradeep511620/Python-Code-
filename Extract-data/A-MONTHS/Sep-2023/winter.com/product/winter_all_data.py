# import mysql.connector
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate
from selenium import webdriver
from selenium.common import NoSuchElementException, MoveTargetOutOfBoundsException
from selenium.webdriver import ActionChains
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
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
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(options=opts)
    # driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    return driver


def product_detail(url, driver):
    # print(driver)

    driver.execute_script(
        'return document.querySelector("body > app-root > app-cookies-banner > div > div.dir-row.sub-content > div.dir-row.btn-space > button.red-btn")').click()
    time.sleep(1)

    l3_name = []
    bread = driver.find_elements(By.XPATH, "//ul[@class='breadcrumb']//li")
    for l3 in bread:
        cleaned_text = ' '.join(l3.text.strip().split('/'))
        l3_name.append(cleaned_text)
    print('l3_name.....', l3_name)

    try:
        product_title = driver.find_element(By.XPATH, "//div[@class='container']//h1").text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        print('object has no attribute ... product_title')
    except NoSuchElementException:
        product_title = ''
        print('')

    try:
        feature = driver.find_element(By.XPATH, "//div[@class='check-list'][2]").text.strip()
        print("feature.....", feature)
    except AttributeError:
        feature = ''
        print('object has no attribute ... product_title')
    except NoSuchElementException:
        feature = ''
        print('')

    try:
        description = []
        for desc in driver.find_elements(By.XPATH, "//div[@class='check-list']//ul//li"):
            description.append(desc.text.strip().replace("\n", ""))
        print('description.....', description)
    except AttributeError:
        description = ''
        print('object has no attribute ... product_title')
    except NoSuchElementException:
        description = ''
        print('')


    # -------------------------------------------------------------------------------------------------------------
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
    except NoSuchElementException:
        print('click not found')

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
        save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/winter.com/data/winter_specs1.txt", 'a+', encoding='utf-8')
        save.write('\n' + url + " \t" + product_title + "\t" + a + "\t" + b)
    print('save data into table files ................1')

    # --------------------------------------------------------------------------------------------------------------
    try:
        clk1 = driver.find_element(By.XPATH, "//div[contains(text(),'DRAWINGS')]")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", clk1)
        wait = WebDriverWait(driver, 10)
        clk1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'DRAWINGS')]")))
        actions = ActionChains(driver)
        driver.execute_script("arguments[0].click();", clk1)
        actions.move_to_element(clk1).click().perform()
        driver.execute_script("arguments[0].click();", clk1)
    except MoveTargetOutOfBoundsException:
        time.sleep(1)
        print("An error occurred:")

    datasheet = []
    for pdf in driver.find_elements(By.XPATH, "//div[@class='row drawings-space']//a"):
        pdf_details = pdf.get_attribute('href')
        datasheet.append(pdf_details)
    print('datasheet.....', datasheet)


    # --------------------------------------- Images------------------------------------------------
    # try:
    #     image = []
    #     for img_2 in soup.find('div', class_="product-media").find_all('a'):
    #         image.append(img_2.get("href"))
    #     # print("Images....", image)
    # except AttributeError:
    #     image = ''
    #     print('object has no attribute ... image')
    # #
    # try:
    #     imgs = image[0]
    #     print('imgs...', imgs)
    # except IndexError:
    #     imgs = ''
    #     print('List out of index')
    # try:
    #     imgs1 = image[1]
    #     print('imgs1...', imgs1)
    # except IndexError:
    #     imgs1 = ''
    #     print('List out of index')
    # try:
    #     imgs2 = image[2]
    #     print('imgs2...', imgs2)
    # except IndexError:
    #     imgs2 = ''
    #     print('List out of index')
    # try:
    #     imgs3 = image[3]
    #     print('imgs3...', imgs3)
    # except IndexError:
    #     imgs3 = ''
    #     print('List out of index')
    # try:
    #     imgs4 = image[4]
    #     print('imgs4...', imgs4)
    # except IndexError:
    #     imgs4 = ''
    #     print('List out of index')

    # ------------------------------------------------------------------------------------------------------------------

    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]  # save data here

    row = [{
        # "Mpn": model,
        # "Grainger_Sku": stock,
        "L3_Name": l3_name,
        "Product_title": product_title,
        # "Image_URL_1": imgs,
        # "Image_URL_2": imgs1,
        # "Image_URL_3": imgs2,
        # "Image_URL_4": imgs3,
        # "Image_URL_5": imgs4,
        # "Image_Name": img_1,
        "Product_Detail": description,
        "Features": feature,
        # "Accessories": href_type_exe,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        # "Video_Url": video_d,
        # "Quantity": stock,
        # "Price(usd)": price,
        # "Cross_Reference": category,
        "Url": url,

    }]  # save data here

    data_save(row, mylist)
    # return product_title


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def get_specs(url, driver):
    print('table.......')
    """    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test",
        port=3306
    )
    print('local database connected')
    cursor = conn.cursor()
            # cursor.execute("INSERT INTO scrape_files (url, name, value) VALUES (%s, %s, %s)", (url, a, b))
    conn.commit()
    conn.close()
    """  # save data into database using python
    # driver.execute_script(f"window.scrollBy(0, {700});")

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
    except NoSuchElementException:
        print('click not found')

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

    #     save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/wpg.com/data/wpg_specs1.txt", 'a+', encoding='utf-8')
    #     save.write('\n' + url + " \t" + product_title + "\t" + a + "\t" + b)
    # print('save data into table files ................1')


def main():
    url_link_count = 151
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Sep-2023/winter.com/url/winter_product_url.csv")[
        'url']
    for url in url_link[151:]:
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
