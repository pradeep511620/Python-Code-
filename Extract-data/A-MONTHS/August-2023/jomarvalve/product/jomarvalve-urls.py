import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# Step One
"""
url = 'https://www.jomarvalve.com/featured-product-lines/'

driver.get(url)
time.sleep(1)
for u in driver.find_elements(By.XPATH, "//*[@class='fusion-image-wrapper']//a"):
    print(u.get_attribute('href'))

"""
# step Two


mylist = [
    'https://www.jomarvalve.com/product/ball-valves/',
    'https://www.jomarvalve.com/product/balancing-valves/',
    'https://www.jomarvalve.com/product/butterfly-valves/',
    'https://www.jomarvalve.com/product/tankless-water-heater-valves/',
    'https://www.jomarvalve.com/product/gates-checks-strainers/',
    'https://www.jomarvalve.com/product/cast-iron/',
    'https://www.jomarvalve.com/product/actuation/',
    'https://www.jomarvalve.com/product/cpvcpvc/',
    'https://www.jomarvalve.com/product/lockwings/',
    'https://www.jomarvalve.com/product/dielectric-unions/',
    'https://www.jomarvalve.com/product/low-pressure/',
    'https://www.jomarvalve.com/product/add-a-valve/',
    'https://www.jomarvalve.com/product/basket-strainers/',
    'https://www.jomarvalve.com/product/thread-sealant/',
    'https://www.jomarvalve.com/product/accessories/',

]

for url in mylist:
    driver.get(url)
    time.sleep(1)
    print('product-url', url)
    length = driver.find_elements(By.XPATH,
                                  "(//ul[@class='fusion-grid fusion-grid-4 fusion-flex-align-items-flex-start fusion-grid-posts-cards'])//a")
    print(len(length))
    for u in driver.find_elements(By.XPATH,
                                  "(//ul[@class='fusion-grid fusion-grid-4 fusion-flex-align-items-flex-start fusion-grid-posts-cards'])//a"):
        url_link = (u.get_attribute('href'))
        print(url_link)
        save = open('jomarvalve-urls-step2.txt', 'a+', encoding='utf-8')
        save.write('\n' + "'" + url_link + "',")

# step Three


mylist = [
    # 'https://www.bodine-electric.com/products/dc-motors/24a-series-permanent-magnet-dc-motor/',

]
for url in mylist:
    driver.get(url)
    time.sleep(1)
    print('product-url', url)
    driver.find_element(By.XPATH, "//div[@class='accordion']").click()
    time.sleep(1)
    # length = driver.find_elements(By.XPATH, "//div[@class='col-xs-12 product-models no-spacing hidden-xs']//ul[@class='dLocator']//li//a")
    length = driver.find_elements(By.XPATH, "//div[@class='accordion__content']//div//a")
    print(len(length))

    # for url_links in driver.find_elements(By.XPATH, "//div[@class='col-xs-12 product-models no-spacing hidden-xs']//ul[@class='dLocator']//li//a"):
    for url_links in driver.find_elements(By.XPATH, "//div[@class='accordion__content']//div//a"):
        url_link = url_links.get_attribute('href')
        print(url_link)

        save = open('bodine-urls-step3.txt', 'a+', encoding='utf-8')
        save.write('\n' + "'" + url_link + "',")
