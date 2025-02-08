import time
from select import select
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

l = 0
mylist = [

    'https://signaling.fedsig.com/product/121aled',
    # 'https://signaling.fedsig.com/product/slm300-slm350-streamline',
    # 'https://signaling.fedsig.com/product/explosion-proof-industrial-telephone',
    # 'https://signaling.fedsig.com/product/break-glass-call-point',
    # 'https://signaling.fedsig.com/product/310-mv-audiomaster-two-way-intercom',
    # 'https://signaling.fedsig.com/product/310-mv-mnc-audiomaster-two-way-intercom',
    # 'https://signaling.fedsig.com/product/fire-alarm-pull-station',
    # 'https://signaling.fedsig.com/product/121aled-n-nsf',


]
for url in mylist:
    l = l + 1
    driver.get(url)
    driver.get(driver.current_url)
    time.sleep(4)
    print("Products Urls", l, url)

    title_d = ''
    sku_d = ''
    Description_d = ''
    feature_d = ''
    price_d = ''
    pdf_d = ''
    option_d = ''
    # =================================================== Find breadcrumb =============================================
    # Breadcrumb_d = []
    # print("*********************************** Breadcrumb : **************************************")
    # Breadcrumb = driver.find_elements(By.ID, 'breadcrumbElement')
    # for x in Breadcrumb:
    #     Breadcrumb_d.append(x.text)
    # print("Breadcrumb = ", Breadcrumb_d)
    # try:
    #     # ================================================ find title =====================================================
    #     print("***********************************  Title : **************************************")
    #     title = driver.find_element(By.CLASS_NAME, 'visible-lg')
    #     title_d = title.text
    #     print("title = ", title_d)
    # except:
    #     print("Not Found")

    try:
        print('*********************** First Options *************************')
        all_options = driver.find_element(By.ID, 'wi700851-fs-product-variants-id').find_elements(By.TAG_NAME, 'option')
        op = []
        for o in all_options:
            print("options=========== ", o.text)
            if "..." not in o.text:
                op.append(o.text)
        dropdown = Select(driver.find_element(By.CLASS_NAME, 'cc-skuDropdown'))
        input1 = len(dropdown.options)
        print("inputs = ", input1)

        # for option, item in zip(op, range(1, input1)):
        #     time.sleep(3)
        #     dropdown = Select(driver.find_element(By.CLASS_NAME, 'cc-skuDropdown'))
        #     print("first loop = ", item)
        #     dropdown.select_by_index(item)
        #     option_d = option
        #     print("options = ", option_d)
        #     time.sleep(3)

            # try:
            #     print("************************************* Price : ****************************************")
            #     price = driver.find_element(By.ID, 'wi700851-fs-product-list-price-id')
            #     price_d = price.text
            #     print("Price = ", price_d)
            # except:
            #     price_d = "Not Found"
            #     print("Not Found Price")
            # try:
            #     print("************************************* sku : ****************************************")
            #     sku = driver.find_element(By.CLASS_NAME, 'cc-sku')
            #     sku_d = sku.text
            #     print("sku = ", sku_d)
            #     save_details: TextIO = open("main_files.xlsx", "a+", encoding="utf-8")
            #     save_details.write("\n" + url + "\t" + "".join(Breadcrumb_d) + "\t" + title_d + "\t" + option_d + "\t" + price_d + "\t" + sku_d)
            #     print("End")
            #     save_details.close()
            # except:
            #     print("Not Found SKU")
        #  =====================================================================================================================
        #     try:
        #         print('*********************** Second Options ************************')
        #         second = Select(driver.find_element(By.XPATH, '//*[@id="CC-prodDetails-sku-VisualSignals_x_lensStyleVariant"]'))
        #         input2 = len(second.options)
        #         time.sleep(3)
        #         for item2 in range(1, input2):
        #             second = Select(driver.find_element(By.XPATH, '//*[@id="CC-prodDetails-sku-VisualSignals_x_lensStyleVariant"]'))
        #             print("second loop = ", item2)
        #             second.select_by_index(item2)        #
        #             time.sleep(3)
        #             driver.get(driver.current_url)
        #             time.sleep(3)
        #
        #             try:
        #                 print("************************************* Price : ****************************************")
        #                 price = driver.find_element(By.ID, 'wi700851-fs-product-list-price-id')
        #                 price_d = price.text
        #                 print("Price = ", price_d)
        #             except:
        #                 price_d = "Not Found"
        #                 print("Not Found Price")
        #             try:
        #                 print("************************************* sku : ****************************************")
        #                 sku = driver.find_element(By.CLASS_NAME, 'cc-sku')
        #                 sku_d = sku.text
        #                 print("sku = ", sku_d)
        #
        #                 # save_details: TextIO = open("main_files.xlsx", "a+", encoding="utf-8")
        #                 # save_details.write("\n" + url + "\t" + "".join(Breadcrumb_d) + "\t" + title_d + "\t" + price_d + "\t" + sku_d)
        #                 # print("End")
        #                 # save_details.close()
        #                 # print("\n ***** Record stored into federal signal  files. *****")
        #             except:
        #                 print("Not Found SKU")
        #     except:
        #             print("Second Options is Not Found")

    except:
        """
        print("Not Found For Loop data")
        # print(e)
    # =================================================================================================================
    try:
        print("************************************* Price : ****************************************")
        price = driver.find_element(By.ID, 'wi700851-fs-product-list-price-id')
        price_d = price.text
        print("Price = ", price_d)
    except:
        price_d = "Not Found"
        print("Not Found Price")

    try:
        print("************************************* sku : ****************************************")
        sku = driver.find_element(By.CLASS_NAME, 'cc-sku')
        sku_d = sku.text
        print("sku = ", sku_d)
    except:
        print("Not Found SKU")

    try:
        print("************************************* Description : ****************************************")
        Description = driver.find_element(By.ID, 'wi700851-fs-product-long-description-id')
        Description_d = Description.text.replace('\n', '')
        print("Description = ", Description_d)
    except:
        print("Not Found")

    try:
        print("************************************* Feature : ****************************************")
        feature = driver.find_element(By.ID, 'Features')
        feature_d = feature.text.replace('\n', '')
        print("feature = ", feature_d)
    except:
        print("Not Found")

    try:
        print("************************************* pdf : ****************************************")
        pdf = driver.find_elements(By.CLASS_NAME, 'link-design ')
        for d in pdf:
            pdf_d = d.get_attribute('href')
            print("Pdf = ", pdf_d)

            save_details: TextIO = open("main_files.xlsx", "a+", encoding="utf-8")
            save_details.write("\n" + url + "\t" + "".join(Breadcrumb_d) + "\t" + title_d + "\t" + option_d + "\t" + price_d + "\t" + sku_d + "\t" + Description_d + "\t" + feature_d + "\t" + pdf_d)
            print("End")
            save_details.close()
            print("\n ***** Record stored into pdf  files. *****")
    except:
        print("Not Found")

    try:
        print("************************************* Images : ****************************************")
        image = driver.find_element(By.ID, 'cc_img__resize_wrapper').find_elements(By.TAG_NAME, 'img')
        for imgs in image:
            image_d = imgs.get_attribute('src')
            print("image_d = ", image_d)

            save_details: TextIO = open("main_files.xlsx", "a+", encoding="utf-8")
            save_details.write("\n" + url + "\t" + "".join(Breadcrumb_d) + "\t" + title_d + "\t" + option_d + "\t" + price_d + "\t" + sku_d + "\t" + Description_d + "\t" + feature_d + "\t" + pdf_d + "\t" + image_d)
            print("End")
            save_details.close()
            print("\n ***** Record stored into Images  files. *****")
    except:
        print("Not Found")
"""

