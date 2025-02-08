import csv
import time

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# opts = Options()
# opts.headless = False
# reading the CSV file
with open('handle_it_product_urls.csv', 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

# displaying the contents of the CSV file
for url_Links in range(1721, csv_length):
    urls = csv_list[url_Links]
    # print(urls)
    url = urls[0]
    driver.get(url)
    time.sleep(2)
    # r = requests.get(url)
    # soup = BeautifulSoup(r.content, "html.parser")
    print("Product-Length...", url_Links)
    print("Product-Urls......", url)

    files = open("Handle-It-data.csv", 'a', encoding='utf-8')

    title = driver.find_element(By.XPATH, "//h1[@class='product-single__title header-flavour']").text
    print("Title...", title)

    #

    images = []
    for img in driver.find_elements(By.XPATH, "//div[@class='photos__item photos__item--main']//div//img"):
        images.append(img.get_attribute('src'))

    try:
        imgs1 = images[0]
    except IndexError:
        imgs1 = ''
        print('list index out of range')
    try:
        imgs2 = images[1]
    except IndexError:
        imgs2 = ''
        print('list index out of range')
    try:
        imgs3 = images[2]
    except IndexError:
        imgs3 = ''
        print('list index out of range')
    try:
        imgs4 = images[3]
    except IndexError:
        imgs4 = ''
        print('list index out of range')
    try:
        imgs5 = images[4]
    except IndexError:
        imgs5 = ''
        print('list index out of range')
    print('images..', images)

    des = [driver.find_element(By.XPATH, "//div[@id='description']//div[@class='rte product-single__description scroll_container']").text.replace('\n', ">>>>>")]
    print("Descriptions...", des)

    try:
        href = []
        for pdf in driver.find_elements(By.XPATH, "//div[@class='rte product-single__description scroll_container']//div[@class='handleit-description']//p//a"):
            href.append(pdf.get_attribute("href"))
        print("pdf...", href)
    except NoSuchElementException:
        print("Not Found Pdf")

    cols = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]

    row = []

    row.append({
        # "Mpn": mpn,
        # "L3_Name": l3_name,
        "Product_title": title,
        "Product_Detail": des,
        "Image_URL_1": imgs1,
        "Image_URL_2": imgs2,
        "Image_URL_3": imgs3,
        "Image_URL_4": imgs4,
        "Image_URL_5": imgs5,
        "Datasheet": href,
        # "Features": features,
        # "item_ID": item,
        # "Price(usd)": price,
        "Url": url,
    })

    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')
