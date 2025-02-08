import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, MoveTargetOutOfBoundsException, TimeoutException, \
    ElementClickInterceptedException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# /var/www/html/webscr/destination_dir
save_files = open(
    "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/COLUMBUS MCKINNON.com/data/COLUMBUS MCKINNON-all-data.csv",
    'a', encoding='utf-8')


def Get_Soup_Url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def Get_Driver_Urls(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument(
        "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    driver.get(url)
    time.sleep(4)
    return driver


def send_email(msg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = ["nkmishra@nextgenesolutions.com", "raptorsupplyuk@gmail.com", ]
    # sender_email = ["nkmishra@nextgenesolutions.com", "nirbhay@raptorsupplies.com", "tajender@raptorsupplies.com"]
    smtp_username = "raptorsupplyuk@gmail.com"
    smtp_password = "unwkbryielvgwiuk"
    # "unwk bryi elvg wiuk"
    message = MIMEMultipart()
    message["From"] = smtp_username
    message["To"] = ','.join(sender_email)
    message["Subject"] = "Script Execution Status"

    body = msg
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, sender_email, message.as_string())
    print("Email sent successfully")


# mgs = "Your web scraping script has been started"
# send_email(mgs)
# print(mgs)


def product_detail(url, driver):
    try:
        driver.find_element(By.XPATH, "(//div[@id='onetrust-button-group']//button)[3]").click()
        print('click pop up...................................1')
    except:
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
        price = driver.find_element(By.XPATH,"(//*[@data-cy='product-detail-main']//app-product-price)[1]").text.strip().replace("\n", ">>").split(">>")[:2]
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
        description = driver.find_element(By.XPATH, "(//*[@data-testid='manufacturer-description']//div)[2]").text.strip()
        description = {'description': description}
        print('description.....', description)
    except (NoSuchElementException, IndexError):
        description = "N/A"
        print('description.....', description)

    # ------------------------------------------------------------------------------------------------------------------
    max_attempts = 5
    attempt = 1
    while attempt <= max_attempts:
        try:
            clk1 = driver.find_element(By.XPATH, "(//button[@class='btn btn-link expand-btn p-off-start mt-6p d-print-none ng-star-inserted'][normalize-space()='Show More'])[1]")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", clk1)
            wait = WebDriverWait(driver, 3)
            wait.until_not(EC.visibility_of_element_located((By.ID, "onetrust-button-group-parent")))
            clk1 = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "(//button[@class='btn btn-link expand-btn p-off-start mt-6p d-print-none ng-star-inserted'][normalize-space()='Show More'])[1]")))
            actions = ActionChains(driver)
            actions.move_to_element(clk1).click().perform()
            print("description_details..........................................................................click")
            break
        except MoveTargetOutOfBoundsException:
            print("Move target out of bounds, retrying...")
            time.sleep(1)
        except TimeoutException:
            print(f"Attempt {attempt}: Timeout waiting for element to be clickable")
        except ElementClickInterceptedException:
            print(f"Attempt {attempt}: Element click intercepted, retrying...")
            time.sleep(1)
        attempt += 1
    if attempt > max_attempts:
        print(f"Maximum attempts ({max_attempts}) reached. Could not click the element.")


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

    max_attempts = 5
    attempt = 1
    while attempt <= max_attempts:
        try:
            clk1 = driver.find_element(By.XPATH, "(//*[@appscrollspytarget='product-specifications']//button)[2]")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", clk1)
            wait = WebDriverWait(driver, 3)
            wait.until_not(EC.visibility_of_element_located((By.ID, "onetrust-button-group-parent")))
            clk1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@appscrollspytarget='product-specifications']//button)[2]")))
            actions = ActionChains(driver)
            actions.move_to_element(clk1).click().perform()
            print("specification.................................................................................click")
            break
        except MoveTargetOutOfBoundsException:
            print("Move target out of bounds, retrying...")
            time.sleep(1)
        except TimeoutException:
            print(f"Attempt {attempt}: Timeout waiting for element to be clickable")
        except ElementClickInterceptedException:
            print(f"Attempt {attempt}: Element click intercepted, retrying...")
            time.sleep(1)
        attempt += 1
    if attempt > max_attempts:
        print(f"Maximum attempts ({max_attempts}) reached. Could not click the element.")

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
        "url": url,
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

    # except Exception as e:
    #     print('Error...', e)
    # send_email(f'Error... {e}')


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# ----------------------------------------------------------------------------------------------------------------------
def ReadUrlFromFile():
    compare_product_url = []
    compare_url = pd.read_csv('Already-Scrape-Url.csv')['URL']
    for compare_urls in compare_url:
        compare_product_url.append(compare_urls.strip())
    return compare_product_url


# ----------------------------------------------------------------------------------------------------------------------
def ReadFromListUrl():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/COLUMBUS MCKINNON.com/url/Product-url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))

    try:
        compare_product_url = ReadUrlFromFile()
    except FileNotFoundError:
        compare_product_url = ''
        print('file not found')

    # Read url one by one using list
    i = 0
    for N0, product_url in enumerate(url_link[i:], start=i):
        print("Product --", N0, product_url)

        # compare url in already exist file
        if product_url in compare_product_url:
            print(f"Skipped this {product_url} Url Because It Is Already Done")
            continue

        # colling function
        # product_detail()
        driver = Get_Driver_Urls(product_url)
        product_detail(product_url, driver)

        # save running url
        last_product_url = product_url
        file_path = 'Already-Scrape-Url.csv'
        header = 'URL'
        file_exists = os.path.exists(file_path)
        with open(file_path, 'a', newline='', encoding='utf-8') as save:
            if not file_exists:
                save.write(f"{header}\n")
            save.write(f"{last_product_url}\n")
    print('Saved Url')


def main():
    ReadFromListUrl()

    # msg = "Your web scraping script has completed "
    # send_email(msg)
    # print(msg)


if __name__ == "__main__":
    main()
