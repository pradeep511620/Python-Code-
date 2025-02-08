import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
# driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver = uc.Chrome()

driver.maximize_window()

L = 0
Result = [

    # 'https://cad.timken.com/category/standard-jaw-couplings-l-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/aluminum-jaw-couplings-al-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/stainless-steel-jaw-couplings-ss-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/w-couplings-w-radially-removable-elastomer-sw-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/w-couplings-w-radially-removable-elastomer-lc-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/ially-removable-spacer-jaw-couplings-rrs-rrsc-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/radially-removable-spacer-jaw-couplings-rrc-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/higher-torque-jaw-couplings-c-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/highest-torque-jaw-couplings-h-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/internal-shaft-locking-device-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/external-shaft-locking-device-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/s-flex-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/torsional-couplings-lf-series?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/jaw-in-shear-type-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/tyle-motion-control-couplings-es-ec-asb-adb-series?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/ows-style-motion-control-couplings-bwc-bwlc-series?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/urved-jaw-style-motion-control-couplings-gs-series?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/style-motion-control-couplings-md-mds-mdsd-series?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/iature-jaw-style-motion-control-couplings-l-series?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/ini-soft-style-motion-control-couplings-msf-series?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/oldham-style-motion-control-couplings-mol-series?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/deltaflex-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/uniflex-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/saga-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/rigid-sleeve-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/shaft-collars?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/econoline-series-variable-speed-drives?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/aluminoline-series-variable-speed-drives?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/wb-series-variable-speed-drives?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/hi-ratio-series-variable-speed-drives?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/adjusta-sheave-series-variable-speed-drives?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/adjustable-motor-bases?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/companion-sheaves?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/hexadrive-variable-speed-drives?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/s-flex-couplings?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/torsional-couplings-lf-series?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/tyle-motion-control-couplings-es-ec-asb-adb-series?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/ows-style-motion-control-couplings-bwc-bwlc-series?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/urved-jaw-style-motion-control-couplings-gs-series?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/ini-soft-style-motion-control-couplings-msf-series?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/oldham-style-motion-control-couplings-mol-series?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/deltaflex-couplings?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/uniflex-couplings?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/saga-couplings?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/econoline-series-variable-speed-drives?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/aluminoline-series-variable-speed-drives?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/wb-series-variable-speed-drives?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/hi-ratio-series-variable-speed-drives?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/adjustable-motor-bases?plpver=1013&pcat=lovejoy#',
    # 'https://cad.timken.com/category/companion-sheaves?plpver=1013&pcat=lovejoy#',

    #

    # 'https://cad.timken.com/category/horizontal-split-cover-grid-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/vertical-split-cover-grid-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/spacer-style-grid-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/runright-tensioner-devices?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/runright-motorbases?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/runright-oscillating-mountings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/runright-rubber-suspension-units?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/runright-anti-vibration-mountings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/industrial-disc-couplings-su-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/industrial-disc-couplings-sx-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/close-coupled-industrial-disc-couplings-sxc-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/drop-in-spacer-disc-couplings-di-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/mini-disc-style-couplings-md-mds-mdsd-series?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/sxcs-type-close-coupled-spilt-spacer?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/d-type-universal-joints?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/hd-type-universal-joints?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/d303-stainless-steel-universal-joints?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/needle-bearing-type-universal-joints?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/loj-jr-4-types-universal-joints?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/dd-ddx-types-universal-joints?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/universal-joint-boots?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/1-side-movable-flange-variable-speed-pulleys?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/2-side-movable-flange-variable-speed-pulleys?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/hexact-electric-control-method?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/hexact-linear-actuation-method?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/manuel-adjustable-driver-pulley?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/hydraulic-pump-motor-mounts-bellhousings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/bnz-series-water-oil-coolers?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/reservoirs-accessories?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/standard-curved-jaw-couplings-cj-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/standard-curved-jaw-couplings-gs-type?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/hercuflex-flanged-style-gear-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/hercuflex-continuous-style-gear-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/flanged-sleeve-gear-type-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/continuous-sleeve-gear-type-couplings?plpver=1013&pcat=lovejoy',
    # 'https://cad.timken.com/category/nylon-sleeve-gear-type-couplings?plpver=1013&pcat=lovejoy',

    # 'https://cad.timken.com/viewitems/hydraulic-components/lh-type-hydraulic-couplings?plpver=1013&pcat=lovejoy',





]
for url in Result:
    L = L + 1
    r = requests.get(url, headers=headers)
    # print(soup.prettify())?page=
    driver.get(url)
    time.sleep(5)
    print("Products Urls", L, url)

    # links = driver.find_element(By.XPATH, "//div[@class='ui-corner-all ui-widget-content plp-table-wrapper']").find_elements(By.TAG_NAME, 'a')
    # print("Lenght", len(links))
    # for x in links:
    #     url_links = (x.get_attribute('href'))
    #     data_urls = ("'" + url_links + "',")
    #     print(data_urls)

    links = driver.find_element(By.XPATH, "//ul[@id='plp-list-description']").find_elements(By.TAG_NAME, 'a')
    print("Lenght", len(links))
    for x in links:
        url_links = (x.get_attribute('href'))
        data_urls = url_links
        print(data_urls)
        save_details: url_links = open("lovejoy.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + "'"+data_urls+"',")
        save_details.close()
    print("\n ***** Record stored into urls  files. *****")

    # clk = driver.find_element(By.CLASS_NAME, "plp-pageRange").find_elements(By.TAG_NAME, "option")
    # for x in clk:
    #     if '200' in x.text:
    #         x.click()
    #         time.sleep(5)
    #     else:
    #         pass
    # l = driver.find_element(By.ID, "pageInfo")
    # cnt = l.text.split()[-1]
    # print("count..", cnt)
    # length = round(int(cnt) / 200+1)
    # print("Loop..", length)
    # for i in range(1, length+1):
    #     driver.find_element(By.XPATH, "//div[@id='plp-page-pagination-table']//div[1]//div[1]//div[2]//a[1]").click()
    #     time.sleep(3)
    #     links = driver.find_element(By.XPATH, "//div[@class='ui-corner-all ui-widget-content plp-table-wrapper']").find_elements(By.TAG_NAME, 'a')
    #     print("links", len(links))
    #     for x in links:
    #         url_links = (x.get_attribute('href'))
    #         print(url_links)
    # #         data_urls = ("'" + url_links + "',")
    # #         print(data_urls)
    #     print(i)

