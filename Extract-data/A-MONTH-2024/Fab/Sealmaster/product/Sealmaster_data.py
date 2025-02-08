import concurrent.futures
import threading
import time
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Sealmaster/data/Sealmaster-all-data.csv", 'a', encoding='utf-8')
csv_lock = threading.Lock()

urls = []
MAX_WORKERS = 5


def Get_Driver_Urls(urls):
    opts = Options()
    opts.headless = True
    opts.add_argument("--no-sandbox")
    opts.add_argument("--headless")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    driver.get(urls)
    time.sleep(1)
    return driver


def product_detail(urls, driver):
    # try:
    try:
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        print('click pop up...................................1')
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//div[@id='onetrust-close-btn-container']//button").click()
        print('click pop up...................................1')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        l3_name = []
        for l3 in driver.find_elements(By.XPATH, "//*[@class='link-text ng-star-inserted']"):
            bread = l3.text.strip()
            l3_name.append(bread)
        l3_name = "## ".join(l3_name)
        print('l3_name.....', l3_name)
    except (NoSuchElementException, TypeError):
        l3_name = "N/A"
        print('l3_name.....', l3_name)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = driver.find_element(By.XPATH, "(//*[@data-testid='item-description'])[3]").text.strip()
        product_title = {'product_title': product_title}
        print('product_title.....', product_title)
    except (NoSuchElementException, TypeError):
        product_title = "N/A"
        print('product_title.....', product_title)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        Brand = driver.find_element(By.XPATH, "(//*[@data-testid='mfr-name'])[3]").text.strip()
        Brand = {'Brand': Brand}
        print('Brand.....', Brand)
    except (NoSuchElementException, IndexError):
        Brand = "N/A"
        print('Brand.....', Brand)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        price = driver.find_element(By.XPATH, "(//*[@data-cy='product-detail-main']//app-product-price)[1]").text.strip().replace("\n", ">>").split(">>")
        price = {'List Price': price}
        print('price.....', price)
    except (NoSuchElementException, TypeError):
        price = "N/A"
        print('price.....', price)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        mpn = driver.find_element(By.XPATH, "(//*[@data-testid='mfr-part-no-display'])[3]//span[2]").text.strip()
        mpn = {"MFR": mpn}
        print('mpn.....', mpn)
    except IndexError:
        mpn = 'N/A'
        print('mpn.....', mpn)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        item_number = driver.find_element(By.XPATH, "(//*[@data-testid='item-no-display'])[3]//span[2]").text.strip()
        item_number = {'MI ITEM': item_number}
        # print("item_number.....", item_number)
    except IndexError:
        item_number = "N/A"
        print("item_number.....", item_number)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description = driver.find_element(By.XPATH,
                                          "(//*[@data-testid='manufacturer-description']//div)[2]").text.strip()
        description = {'description': description}
        print('description.....', description)
    except (NoSuchElementException, IndexError):
        description = "N/A"
        print('description.....', description)

    # ------------------------------------------------------------------------------------------------------------------
    clickable_1 = driver.find_element(By.XPATH, "//*[@appscrollspytarget='product-overview']").text.strip()
    if "OVERVIEW" in clickable_1:
        try:
            driver.find_element(By.XPATH, "//*[@appscrollspytarget='product-overview']//button").click()
            time.sleep(1)
            print('description_details.....................................................................1')
        except (ElementNotInteractableException, NoSuchElementException):
            print('Not click description')

    try:
        description_tag = []
        for des_2 in driver.find_elements(By.XPATH, "//*[@data-testid='point-wrapper']//li"):
            description_details = des_2.text.strip()
            description_tag.append(description_details)
        description_tag = {'description_tag': description_tag}
        print('description_tag.....', description_tag)
    except (NoSuchElementException, IndexError):
        description_tag = "N/A"
        print('description_tag.....', description_tag)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    try:
        image = []
        img_tag_text = ''
        for img in driver.find_elements(By.XPATH, "(//*[@class='content-container'])[1]//picture//img"):
            img_tag_text = img.get_attribute('alt')
            img_tag_text = {'alt': img_tag_text}

        for img in driver.find_elements(By.XPATH, "//*[@type='image/.jpg']"):
            img_tag = img.get_attribute('srcset')
            image.append("https://www.motion.com" + img_tag)
        image = list(set(image))
        image = {'image': image}
        dect_img = str(image) + ", " + str(img_tag_text)
        print('image.....', dect_img)
    except NoSuchElementException:
        dect_img = "N/A"
        print('image.....', dect_img)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        safety = []
        for safety_tag in driver.find_elements(By.XPATH, "(//div[@class='row'])[1]//a"):
            safety.append(safety_tag.get_attribute('href'))
        # print('safety.....', safety)
    except NoSuchElementException:
        safety = 'N/A'
        print('safety.....', safety)

    miscellaneous = str(safety) + ", " + str(item_number)
    print('miscellaneous.....', miscellaneous)

    # ------------------------------------------------------------------------------------------------------------------
    clickable = driver.find_element(By.XPATH, "//*[@appscrollspytarget='product-specifications']").text.strip()
    if "SPECIFICATIONS" in clickable:
        try:
            driver.find_element(By.XPATH, "(//*[@appscrollspytarget='product-specifications']//button)[2]").click()
            time.sleep(1)
            print(
                'click specification ..............................................................................2')
        except (ElementNotInteractableException, NoSuchElementException):
            print(
                'Not click specs....................................................................................')

    attr_name = []
    attr_value = []
    for th in driver.find_elements(By.XPATH, "//*[@class='col-6 col-md-auto label px-12p px-md-24p']"):
        first_tab = th.text.strip()
        attr_name.append(first_tab)

    for td in driver.find_elements(By.XPATH, "//*[@class='col-6 col-md value pe-12p pe-md-24p']"):
        second_tab = td.text.strip().replace("\n", ">>")
        attr_value.append(second_tab)

    dict_list = []

    for i in range(min(len(attr_name), len(attr_value))):
        single_dict = {attr_name[i]: attr_value[i]}
        dict_list.append(single_dict)
    print("specification.....", dict_list)

    # ------------------------------------------------------------------------------------------------------------------
    mylist = [
        "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "usd", "unit", "shipping_weight",
        "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
        "product_description_1",
        "product_description_2", "accessories", "video_links", "miscellaneous",
    ]
    # save data here

    row_data = [{
        "brand": Brand,
        "catlvl1": "N/A",
        "catlvl2": "N/A",
        "catlvl3": "N/A",
        "url": urls,
        "title": product_title,
        "price_value": price,
        "usd": "usd",
        "unit": "N/A",
        "breadscrumbs": l3_name,
        "image_urls": dect_img,
        "mpn": mpn,
        "specification_1": dict_list,
        "datasheets": "N/A",
        "product_description_1": description,
        "product_description_2": description_tag,
        # "accessories": safety,
        "video_links": "N/A",
        "miscellaneous": miscellaneous,
    }]

    # save data here
    Data_Save(row_data, mylist)

    driver.quit()


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def ReadFromListUrl():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Sealmaster/url/Product-url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))
    i = 0
    for url_count, url in enumerate(url_link[i:], start=i):
        urls.append(url)
        # driver = Get_Driver_Urls(product_url)
        # product_detail(product_url, driver)

    print(urls)
    return urls


def main():
    urls = ReadFromListUrl()
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(lambda url: product_detail(url, Get_Driver_Urls(url)), urls)
        print('*******************************************************************************************************')


if __name__ == "__main__":
    main()
