import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import concurrent.futures
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

urls = []
MAX_WORKERS = 5

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Regalrexnord.com/data/Regalrexnord-all-data11test.csv", 'a', encoding='utf-8')


def Get_Driver_Urls(urls):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    driver.get(urls)
    time.sleep(2)
    return driver


def send_email(msg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = ["nkmishra@nextgenesolutions.com", "raptorsupplyuk@gmail.com", ]
    # sender_email = ["nkmishra@nextgenesolutions.com", "nirbhay@raptorsupplies.com", "tajender@raptorsupplies.com"]
    smtp_username = "raptorsupplyuk@gmail.com"
    smtp_password = "unwkbryielvgwiuk"
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


def product_detail(urls, driver):
    try:
        try:
            driver.find_element(By.XPATH, "(//button[normalize-space()='Accept All'])[1]").click()
            time.sleep(1)
        except:
            driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
            time.sleep(1)

        # ------------------------------------------------------------------------------------------------------------------
        try:
            l3_name = []
            for l3 in driver.find_elements(By.XPATH, "//ol[@class='breadcrumb']//li"):
                bread = l3.text.strip()
                l3_name.append(bread)
            l3_name = "## ".join(l3_name)
            print('l3_name.....', l3_name)
        except (NoSuchElementException, TypeError):
            l3_name = "N/A"
            print('l3_name.....', l3_name)

        # ------------------------------------------------------------------------------------------------------------------
        try:
            product_title = driver.find_element(By.XPATH, "//div[@class='page-title']").text.strip()
            product_title = {'product_title': product_title}
            print('product_title.....', product_title)
        except (NoSuchElementException, TypeError):
            product_title = "N/A"
            print('product_title.....', product_title)

        # ------------------------------------------------------------------------------------------------------------------
        price = ''
        try:
            for price_de in driver.find_elements(By.XPATH, "//div[@class='param-row']"):
                if "List Price:" in price_de.text.strip():
                    price = driver.find_element(By.XPATH,"(//div[@class='product-cart__price']//span)[2]").text.strip().replace('\n', "")
                    price = {"List Price": price}
                    print('price.....', price)
        except (NoSuchElementException, TypeError):
            price = "N/A"
            print('price.....', price)

        # ------------------------------------------------------------------------------------------------------------------
        try:
            mpn = driver.find_element(By.XPATH, "(//div[@class='param-row-list']//span)[2]").text.strip()
            mpn = {'mpn': mpn}
            print("mpn.....", mpn)
        except NoSuchElementException:
            mpn = "N/A"
            print("mpn.....", mpn)

        # ------------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------------------------------------------------------------------------
        try:
            catalog = driver.find_element(By.XPATH, "(//div[@class='param-row-list']//span)[last()]").text.strip()
            catalog = {'catalog': catalog}
        except NoSuchElementException:
            catalog = 'N/A'
            print('catalog.....', catalog)

        # ------------------------------------------------------------------------------------------------------------------
        try:
            weight = driver.find_element(By.XPATH, "(//div[@class='product-cart']//span)[2]").text.strip()
            weight = {'weight': weight}
            print('weight.....', weight)
        except NoSuchElementException:
            weight = 'N/A'
            print('weight.....', weight)

        # ------------------------------------------------------------------------------------------------------------------
        try:
            description = []
            for des_1 in driver.find_elements(By.XPATH, "//div[@class='product-info']//li"):
                des_2 = des_1.text.strip()
                description.append(des_2)
            description = {'description': description}
            print('description.....', description)
        except (NoSuchElementException, IndexError):
            description = "N/A"
            print('description.....', description)

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
            images_a = []
            for img in driver.find_elements(By.XPATH, "//div[@id='gallery-main']//img"):
                img_tag = img.get_attribute('src')
                images_a.append({'image': img_tag})

            image_list = []
            for index, img in enumerate(driver.find_elements(By.XPATH, "//*[@class='mcs-item']//img")):
                img_tag = img.get_attribute('src')
                key = f'image_{index + 1}'
                image_dict = {key: img_tag}
                image_list.append(image_dict)
            image_urls = image_list + images_a
            print('image.....', image_urls)
        except NoSuchElementException:
            image_urls = "N/A"
            print('image.....', image_urls)

        # ------------------------------------------------------------------------------------------------------------------
        datasheet = []
        for pdf_1 in driver.find_elements(By.XPATH, "//div[@class='resource-center']//a"):
            pdf_link = pdf_1.get_attribute('href')
            if ".pdf" in pdf_link:
                datasheet.append(pdf_link)
        print('datasheet.....', datasheet)

        miscellaneous = catalog
        print('miscellaneous.....', miscellaneous)

        # ------------------------------------------------------------------------------------------------------------------
        try:
            for clicks in driver.find_elements(By.XPATH, "//ul[@role='tablist']//li"):
                text_data = clicks.text.strip()
                # print(text_data)
                if "General Specifications" in text_data:
                    try:
                        driver.find_element(By.XPATH, "//a[@id='tab-link-2']")
                        time.sleep(2)
                        print('click General Specifications1')
                    except:
                        driver.find_element(By.XPATH, "(//ul[@role='tablist']//li)[2]")
                        time.sleep(2)
                        print('click General Specifications2')

                elif "Technical Specifications" in text_data:
                    driver.find_element(By.XPATH, "//a[@id='tab-link-1']").click()
                    time.sleep(2)
                    print('click Technical Specifications')
        except NoSuchElementException:
            pass

        row_count = 0
        attr_name = []
        attr_value = []
        for th in driver.find_elements(By.XPATH, "//div[@id='productSpecifications']//td"):
            row_count += 1
            tab = th.text.strip().replace(":", "")
            if (row_count % 2) != 0:
                attr_name.append(tab)
            else:
                attr_value.append(tab)

        dict_list = []

        for i in range(min(len(attr_name), len(attr_value))):
            single_dict = {attr_name[i]: attr_value[i]}
            dict_list.append(single_dict)
        print("specification.....", dict_list)

        # ------------------------------------------------------------------------------------------------------------------
        mylist = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
        ]
        # save data here

        row_data = [{
            "brand": "N/A",
            "catlvl1": "N/A",
            "catlvl2": "N/A",
            "catlvl3": "N/A",
            "url": urls,
            "title": product_title,
            "price_value": price,
            "unit": 'N/A',
            "shipping_weight": weight,
            "breadscrumbs": l3_name,
            "image_urls": image_urls,
            "mpn": mpn,
            "specification_1": dict_list,
            "datasheets": datasheet,
            "product_description_1": description,
            "accessories": "N/A",
            "video_links": "N/A",
            "miscellaneous": miscellaneous,
        }]

        # save data here
        Data_Save(row_data, mylist)

    except Exception as e:
        print('Error...', e)
        # send_email(f'Error... {e}')
    finally:
        driver.quit()


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


# ----------------------------------------------------------------------------------------------------------------------
def ReadUrlFromFileToCompare():
    compare_product_url = []
    try:
        compare_url = pd.read_csv('Already-Scrape-Url.csv')['URL']
        for compare_urls in compare_url:
            compare_product_url.append(compare_urls.strip())
    except FileNotFoundError:
        print('File not found for comparison')
    return compare_product_url


def ReadFromListUrl():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Regalrexnord.com/url/Product-url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))
    # Read url from file to compare url
    compare_product_url = ReadUrlFromFileToCompare()

    i = 9417
    for N0, product_url in enumerate(url_link[i:], start=i):
        urls.append(product_url)
        # compare url in already exist file
        if product_url in compare_product_url:
            # print(f"Skipped this {product_url} Url Because It Is Already Done")
            continue

        # driver = Get_Driver_Urls(product_url)
        # product_detail(product_url, driver)

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
    print(urls)
    return urls


def main():
    urls = ReadFromListUrl()
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(lambda url: product_detail(url, Get_Driver_Urls(url)), urls)
        print('*******************************************************************************************************')

    # msg = "Your web scraping script has completed"
    # send_email(msg)
    # print(msg)


if __name__ == "__main__":
    main()
