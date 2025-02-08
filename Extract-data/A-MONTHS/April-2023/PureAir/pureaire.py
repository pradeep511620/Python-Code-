import time

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

mylst = [
    'https://www.pureairemonitoring.com/universal-gas-detector',
    'https://www.pureairemonitoring.com/universal-gas-detector-with-remote-sensor',
    'https://www.pureairemonitoring.com/all-categories-gas-monitorsair-check-o2-oxygen-deficiency-monitor-for-co2-n2-storage-areas/',
    'https://www.pureairemonitoring.com/product/air-check-o2-digital-remote-sensor-0-25/',
    'https://www.pureairemonitoring.com/air-check-o2-sample-draw-monitor-2/',
    'https://www.pureairemonitoring.com/combo-o2co2-monitor/',
    'https://www.pureairemonitoring.com/oxygen-analyzer-0-1000ppm',
    'https://www.pureairemonitoring.com/product/pureaire-co2-safety-monitor/',
    'https://www.pureairemonitoring.com/air-check-o2-sample-draw-monitor-water-resistant',
    'https://www.pureairemonitoring.com/oxygen_monitor_chambers',
    'https://www.pureairemonitoring.com/air-check-o2-ex-oxygen-deficiency-monitor-html/',
    'https://www.pureairemonitoring.com/multi-channel-controller/',
    'https://www.pureairemonitoring.com/air-check-o2-oxygen-deficiency-monitor-for-glove-box-and-chambers/',
    'https://www.pureairemonitoring.com/water-resistant-sample-draw-dual-oxygen-0-25/carbon-dioxide-0-50000-ppm-monitor',
    'https://www.pureairemonitoring.com/st-48-combustible-toxic-gas-monitor',
    'https://www.pureairemonitoring.com/product/air-check-ex-h2-gas-monitoring-system-3/',
    'https://www.pureairemonitoring.com/product/oxygen-deficiency-monitor-0-30/',
    'https://www.pureairemonitoring.com/combo-o2co2-monitor-50000ppm/',
    'https://www.pureairemonitoring.com/trace-oxygen-analyzer-kf25-0-100-ppm',
    'https://www.pureairemonitoring.com/air-check-ex-toxic-gas-monitor-3/',
    'https://www.pureairemonitoring.com/ppb-oxygen-analyzer-kf25-0-10-ppm',
    'https://www.pureairemonitoring.com/product/st-48-hydrogen-sulfide-combustible-gas-monitor',
    'https://www.pureairemonitoring.com/product/8-channel-programmable-controller-for-o2-or-gas-monitors/99196',
    'https://www.pureairemonitoring.com/channel-modbus-master-display-alarm-monitorcontroller-2/',
    'https://www.pureairemonitoring.com/dual-o2/-co2-ip67-water-proof-monitor',
    'https://www.pureairemonitoring.com/product/air-check-carbonyl-sulfide-monitor/',
    'https://www.pureairemonitoring.com/air-check-advantage-methyl-bromide-gas-monitor/',

]


# for url in mylst:

file = open("test1.csv", 'a', encoding='utf-8')


def get_url(url):
    # r = requests.get(url)
    # time.sleep(6)
    # soup = BeautifulSoup(r.content, "html.parser")
    print("product - urls", url)
    # return soup


def extract_data(url):
    cols = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]
    row = []
    driver.get(url)
    time.sleep(5)
    driver.maximize_window()

    bread = driver.find_element(By.XPATH, "//nav[@class='woocommerce-breadcrumb']").text.strip().replace('\n', '<<<')
    print('BreadCrumb...', bread)

    title = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text.strip()
    print(title)

    try:
        item = driver.find_element(By.XPATH, "//div[@class='gases_detect']").text.strip()
        print("Item...", item)
    except NoSuchElementException:
        item = ''
        print('Unable to locate element')

    images = []
    for img in driver.find_elements(By.XPATH, "//div[@class='images']//div//img"):
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
    print('lol')

    price = driver.find_element(By.XPATH, "//p[@class='price']").text.strip()
    print("Price...", price)

    product = driver.find_element(By.XPATH, "//div[@class='woocommerce-product-details__short-description']/p[1]").text.strip().replace('\n', '')
    print("Product...", product)

    feature1 = driver.find_element(By.XPATH, "//div[@id='tab-description']//ul").text.replace('\n', " >> ")
    print("Description...", feature1)

    feature2 = driver.find_element(By.XPATH, "//div[@class='woocommerce-tabs wc-tabs-wrapper']//p[1]").text.strip().replace('\n', '')
    print("Description...1", feature2)

    feature3 = driver.find_element(By.XPATH, "//div[@class='woocommerce-tabs wc-tabs-wrapper']//p[2]").text.strip().replace('\n', '')
    # print("Description...2", feature3)
    features = feature1, feature2, feature3
    print("features......", features)

    # save data from here to csv
    row.append({
        "Product_title": title,
        "Product_Detail": product,
        "Image_URL_1": imgs1,
        "Image_URL_2": imgs2,
        "Image_URL_3": imgs3,
        "Image_URL_4": imgs4,
        "Image_URL_5": imgs5,
        "Features": features,
        "item_ID": item,
        "Price(usd)": price,
        "Url": url,

    })

    data_save(row, cols)


def data_save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(file, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def main():
    # get_url()
    i = 7
    for item_url in mylst[i:]:
        extract_data(item_url)
        print(i, "....................", item_url)
        i += 1


main()
