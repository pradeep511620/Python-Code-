import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# opts = Options()
# opts.headless = False

mylist = [

    # # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-xl',    # 2780
    # "https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-xl&view=table",
    #
    # # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-l', # 2202
    # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-l&view=table',
    #
    # # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-htd-3mm',   # 1192
    # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-htd-3mm&view=table',
    #
    # # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-htd-5mm',#  2292
    # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-htd-5mm&view=table',
    #
    # # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-htd-8mm',     # 792
    # 'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-htd-8mm&view=table',

    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-vps',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-vpsr',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=pulleys-companion',   # 38

    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-bearings-carbon-steel-english',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-bearings-stainless-steel-english',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-bearings-carbon-steel-metric',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-bearings-stainless-steel-metric',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-retainer-inch-carbon-steel',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-washer-inch-carbon-steel',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-retainer-inch-stainless-steel',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-washer-inch-stainless-steel',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-retainer-metric-carbon-steel',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-washer-metric-carbon-steel',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-retainer-metric-stainless-steel',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=thrust-washer-metric-stainless-steel',

    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=gear-boxes-sw1',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=gear-boxes-sw5',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=gear-boxes-rab',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=gear-boxes-ra300',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=gear-boxes-ra400',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=gear-boxes-sw3',
    'https://catalog.torquetrans.com/catalog3/d/torquetransmission/?c=fsearch&cid=gear-boxes-sw4',
]

for url in mylist:
    driver.get(url)
    # time.sleep(3)
    u = []

    # Get length of urls
    le = driver.find_element(By.ID, "cds-product-controls-count")
    c = le.text.split(' ')[-2]
    print("count....", c)
    length = round(int(c) / 15 + 1)
    print('click...', length)

    for i in range(1, length + 1):
        try:
            driver.find_element(By.ID, "cds-show-more-products").click()
        except NoSuchElementException:
            print('unable to locate')
        time.sleep(2)
        print("click2", i)
        # Get urls here
    url_links = driver.find_element(By.ID, "cds-product-container").find_elements(By.TAG_NAME, "a")
    # url_links = driver.find_elements(By.XPATH, "//table[@class='cds-product-list-table']//tr//td//a")
    le = len(url_links)
    print("Product-length", le)
    for ur in url_links:
        urls_link = ur.get_attribute('href')
        print(urls_link)

        #   Save urls here
        save = open("urlsss681.txt", "a+", encoding="utf-8")
        save.write("\n" + "'"+urls_link+"',")
    print('save data')
