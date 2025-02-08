import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# url = "https://drum-handlers.liftomatic.com/"
#
# driver.get(url)
# time.sleep(5)
# for u in driver.find_elements(By.XPATH,
#                               "//ul[contains(@class,'ui-widget-content ui-corner-all plp-list-margin')]//div//ul//li//a"):
#     url_link = u.get_attribute('href')
#     if "#" not in url_link:
#         print(url_link)


mylist = [

    'https://drum-handlers.liftomatic.com/viewitems/forklift-mounted-drum-handlers/standard-duty-forklift-mounted-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/forklift-mounted-drum-handlers/heavy-duty-forklift-mounted-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/forklift-mounted-drum-handlers/high-volume-forklift-mounted-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/forklift-mounted-drum-handlers/light-duty-forklift-mounted-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/portable-drum-handling-equipment/es',
    'https://drum-handlers.liftomatic.com/viewitems/portable-drum-handling-equipment/ergomatic-counter-balanced',
    'https://drum-handlers.liftomatic.com/viewitems/portable-drum-handling-equipment/epd',
    'https://drum-handlers.liftomatic.com/viewitems/portable-drum-handling-equipment/ht',
    'https://drum-handlers.liftomatic.com/viewitems/below-hook-hoist-mounted-drum-handlers-2/um-handlers-heavy-duty-hoist-mounted-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/below-hook-hoist-mounted-drum-handlers-2/e-drum-and-double-drum-hoist-mounted-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/below-hook-hoist-mounted-drum-handlers-2/economical-hoist-mounted-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/below-hook-hoist-mounted-drum-handlers-2/ultiple-drum-hoist-and-crane-mounted-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/below-hook-hoist-mounted-drum-handlers-2/-application-crane-and-hoist-mounted-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/below-hook-hoist-mounted-drum-handlers-2/ies-drum-dumping-equipment-below-hook-drum-dumpers',
    'https://drum-handlers.liftomatic.com/viewitems/dde/forklift-mounted-drum-dumpers',
    'https://drum-handlers.liftomatic.com/viewitems/dde/ies-drum-dumping-equipment-below-hook-drum-dumpers',
    'https://drum-handlers.liftomatic.com/viewitems/dde/portable-drum-dumpers',
    'https://drum-handlers.liftomatic.com/viewitems/l-categories-customized-fork-mounted-drum-handle-2/ed-drum-handlers-customized-below-hook-attachments',
    'https://drum-handlers.liftomatic.com/viewitems/l-categories-customized-fork-mounted-drum-handle-2/nted-drum-handlers-customized-forklift-attachments',
    'https://drum-handlers.liftomatic.com/viewitems/l-categories-customized-fork-mounted-drum-handle-2/ed-drum-handlers-customized-portable-drum-handlers',
    'https://drum-handlers.liftomatic.com/viewitems/all-categories-other-material-handling-products/ther-material-handling-products-fork-mounted-hooks',
    'https://drum-handlers.liftomatic.com/viewitems/all-categories-replacement-parts-and-components/replacement-parts-for-dcm-units',
    'https://drum-handlers.liftomatic.com/viewitems/all-categories-replacement-parts-and-components/all-categories-replacement-parts-for-dcmj',
    'https://drum-handlers.liftomatic.com/viewitems/all-categories-replacement-parts-and-components/s-and-components-replacement-parts-for-l4f-and-s4f',
    'https://drum-handlers.liftomatic.com/viewitems/all-categories-replacement-parts-and-components/ent-parts-and-components-replacement-parts-for-fta',
    'https://drum-handlers.liftomatic.com/viewitems/all-categories-replacement-parts-and-components/t-parts-and-components-preventive-maintenance-kits',

]

for url in mylist:
    driver.get(url)
    time.sleep(2)

    for u in driver.find_elements(By.XPATH, "//div[@class='plp-2-column-center']//div//div//a"):
        url_link = u.get_attribute('href')
        if 'addtocart' not in url_link:
            print(url_link)
            save = open('liftomatic-urls.txt', 'a+', encoding="utf-8")
            save.write('\n' + url_link)
        print("save url in txt files")
