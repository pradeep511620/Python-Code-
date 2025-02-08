import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# Step One

# url = 'https://www.gesafety.com/products/freeze_resistant/freeze_resistant.shtml'
#
# driver.get(url)
# time.sleep(1)
# for u in driver.find_elements(By.XPATH, "(//div[@class='intro'])//a"):
#     print(u.get_attribute('href'))

# step Two
#
mylist = [
    #     # 'http://www.gesafety.com/products/showers/showers.shtml',
    #     'http://www.gesafety.com/products/eye_face_wash/eye_facewashes.shtml',#
    #     # 'http://www.gesafety.com/products/eyewash/eyewashes.shtml',
    #     # 'http://www.gesafety.com/products/stations/safety_stations.shtml',
    #     # 'http://www.gesafety.com/products/drench_hose/drench_hose_units.shtml',
    #     # 'http://www.gesafety.com/products/recessed/reccessed_units.shtml',
    #     'http://www.gesafety.com/products/barrier_free/barrier_free.shtml',#
    #     'http://www.gesafety.com/products/corrosion.shtml',#
    #     # 'http://www.gesafety.com/products/safety-centers/safety-centers.shtml',
    #     'http://www.gesafety.com/products/freeze_resistant/freeze_resistant.shtml',#
    #     # 'http://www.gesafety.com/products/portable/portable_units.shtml',
    #     # 'http://www.gesafety.com/products/faucet_mounted/faucet_mounted.shtml',
    #     # 'http://www.gesafety.com/products/alarms/alarms.shtml',
    #     # 'http://www.gesafety.com/products/accessories/accessories.shtml',
    # 'https://www.gesafety.com/products/freeze_resistant/gfr_3100_series.shtml',
    # 'https://www.gesafety.com/products/freeze_resistant/gfr_3500_series.shtml',
    # 'https://www.gesafety.com/products/freeze_resistant/gfr_3200_series.shtml',
    # 'https://www.gesafety.com/products/freeze_resistant/freeze-standard.shtml',
    # 'https://www.gesafety.com/products/freeze_resistant/freeze-portable.shtml',
    'https://www.gesafety.com/products/corrosion.shtml',
    # 'https://www.gesafety.com/products/recessed/reccessed_units.shtml',
    # 'https://www.gesafety.com/products/barrier_free/bf_stations.shtml',
    # 'https://www.gesafety.com/products/barrier_free/bf_showers.shtml',
    # 'https://www.gesafety.com/products/barrier_free/bf_eyeface.shtml',

]

for url in mylist:
    driver.get(url)
    time.sleep(1)
    print('product-url', url)
    length = driver.find_elements(By.XPATH, "//*[@id='panel']//a")
    print(len(length))
    for u in driver.find_elements(By.XPATH, "//div[@id='inner_panel']//a"):
        url_link = (u.get_attribute('href'))
        print(url_link)
        save = open('gesafety.txt', 'a+', encoding='utf-8')
        save.write('\n' + "'" + url_link + "',")

# step Three

"""
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
"""
