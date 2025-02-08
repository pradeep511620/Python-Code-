import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#
driver = webdriver.Chrome()
driver.maximize_window()

mylist = [

    'https://www.hilti.com/c/CLS_FASTENER_7135/CLS_ANCHOR_RODS_ELEMENTS_7135/r8704625'
]
i = 1
for url in mylist:
    driver.get(url)
    time.sleep(3)

    driver.execute_script('return document.querySelector("#marketing-L2NvbnRlbnQvaGlsdGkvVzEvVVMvZW4vbWFya2V0aW5nLWJhbm5lcnMvY3VzdG9taXplZC1hbmNob3Itcm9kcw > div > button")').click()
    driver.find_element(By.ID, "didomi-notice-agree-button").click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 900)", "")
    driver.find_element(By.XPATH, "//button[@class='a-button-link a-link a-link--medium a-link--arrow-after hidden-xs hidden-sm pull-right a-spacing-mt--xs js-variant-list a-variant-list ng-isolate-scope']").click()
    time.sleep(9)

    for u in driver.find_elements(By.XPATH, "//div[contains(@class,'m-showmore-container m-showmore-container--advanced js-showmore-responsivetable-container is-hidden')]//a"):
        print(u.get_attribute('href'))
