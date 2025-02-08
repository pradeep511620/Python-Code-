import csv
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import pandas as pd

opts = Options()
# Set headless mode
# opts.headless = True
# browser = webdriver.Firefox()

save_files = open('file.csv', 'a', encoding='utf-8')


url = 'https://advancetabco.com/'


def getDriveUrls(url):
    # driver = webdriver.Chrome()
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(url)
    print("Product_urls", url)
    time.sleep(3)
    return browser


def product_detail(url):
    browser = getDriveUrls(url)
    browser.find_element(By.XPATH, "//input[@class='searchbox_inside form-control']").send_keys(url)
    time.sleep(1)

    browser.find_element(By.XPATH, "//input[@value='Product Search']").click()
    time.sleep(1)

    get_url = browser.current_url
    print('Current_urls...', get_url)

    try:
        model = browser.find_element(By.XPATH, "//div[@class='col-md-9']//h4[1]").text.strip()
        print("model..", model)
    except NoSuchElementException:
        model = ''
        print("Not Found")

    try:
        price = browser.find_element(By.XPATH, "//div[@class='col-md-9']//h4[2]").text.strip()
        print("price..", price)
        save = open('watts_all_data.txt', 'a+', encoding='utf-8')
        save.write('\n' + get_url + "\t" + model + "\t" + price)
    except NoSuchElementException:
        price = ''
        print('Not Found')

    try:
        images = browser.find_element(By.XPATH, "//span[@data-toggle='modal']").find_element(By.TAG_NAME, 'img')
        image = images.get_attribute('src')
        print('Images...', image)
    except AttributeError:
        image = ''

    all_data1 = browser.find_elements(By.XPATH, "//div[@class='col-md-9']//p[1]")
    length = len(browser.find_elements(By.XPATH, "//div[@class='col-md-9']//p"))
    for l1 in range(0, length + 1):
        if l1 == 1:
            for all_data in all_data1:
                data = all_data.text.split('\n')
                #
                try:
                    description = data[1]
                    print('descriptions...', description)
                    save = open('watts_all_data.txt', 'a+', encoding='utf-8')
                    save.write('\n' + get_url + "\t" + model + "\t" + price + "\t" + description)
                except AttributeError:
                    print('Not Found')
                try:
                    attr_name = []
                    attr_value = []
                    w1 = data[0].strip()
                    table1 = w1.split('  ')
                    # print('unchanged', table1)
                    for tab1 in table1:
                        tabs1 = tab1.split(': ')
                        attr_name.append(tabs1[0])
                        attr_value.append(tabs1[1])
                    for a1, b1 in zip(attr_name, attr_value):
                        print(a1, '....', b1)
                        save = open('data.txt', 'a+', encoding='utf-8')
                        save.write('\n' + get_url + "\t" + model + "\t" + a1 + "\t" + b1)
                except IndexError:
                    print('Index out of range')

                #
                try:
                    td = []
                    td1 = []
                    w = data[2].strip()
                    table = w.split('  ')
                    for tab in table:
                        tabs = tab.split(': ')
                        td.append(tabs[0])
                        td1.append(tabs[1])
                    for a, b in zip(td, td1):
                        print(a, '....', b)
                        save = open('data.txt', 'a+', encoding='utf-8')
                        save.write('\n' + get_url + "\t" + model + "\t" + a + "\t" + b)
                except IndexError:
                    print('Index out of range')

                break
                # ------------------------------------------------------------------------------------------------------------------
                mylist = [
                    "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name",
                    "item_ID",
                    "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
                    "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals",
                    "Installation",
                    "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4",
                    "Image_URL_5",
                    "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)",
                    "weight(kg)",
                    "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
                ]

                row = [{
                    # "Mpn": part_n,
                    # "Grainger_Sku": sku,
                    # "L3_Name": l3_Name,
                    # "Product_title": product_title,
                    # "Image_URL_1": imgs,
                    # "Image_URL_2": imgs1,
                    # "Image_URL_3": imgs2,
                    # "Image_URL_4": imgs3,
                    # "Image_URL_5": imgs4,
                    # "Product_Detail": des,
                    # "Features": features,
                    # "Accessories": related_url,
                    # "Datasheet": datasheet,
                    # "item_ID": item,
                    # "Uses": uses_d,
                    # "Video_Url": video,
                    # "Quantity": stock,
                    "Price(usd)": price,
                    # "Cross_Reference": Cross_Reference,
                    "Url": url,

                }]

                print(row)

                data_save(row, mylist)



def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


with open("C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/Advancetabco.com/urls/watts_mpn.csv", 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

for csv_link in range(67, 100):
    url = csv_list[csv_link][0].replace('ï»¿', '').replace('rp_', '')
    print("Product-Length...", csv_link)
    print("Urls......", url)
    product_detail(url)
