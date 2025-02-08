import time

from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()

mylist = [
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-indoor/hid-certavision-for-cdm/LP_CF_DCDMCV_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-horticulture/hid-greenvision-gp-son/LP_CF_DGVGPSON_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-basic-bhl-for-hpl-hpi/LP_CF_DBCHP_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/ignitors/electronic-semi-parallel-ignitor-for-hid-lamp-circuits/LP_CF_IGNSN_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-indoor/primavision-power-for-cdm/LP_CF_DPVPWR_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-indoor/primavision-economy-for-cdm-lamps/LP_CF_DPVCDMEC_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/ignitors/electronic-series-ignitor-for-hid-lamp-circuits/LP_CF_IGNSU_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-basic-semi-parallel-economic-ballasts-for-son-cdm-mh-lamps/LP_CF_DBCSONE_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/hid-pv-dv-economy-for-cpo-cdm/LP_CF_DCVCPOCD_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/primavision-xtreme-for-cpo/LP_CF_DPVCPOXT_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-basic-bhl-mk4-for-hpl-hpi/LP_CF_DBCHP4_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-indoor/primavision-compact-for-cdm/LP_CF_DPVCMPCT_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/ignitors/hid-ignitors-for-mk4-semi-parallel-systems/LP_CF_IGHID4_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-basic-semi-parallel-ballasts-for-son-cdm-mh-lamps/LP_CF_DBCSON_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/dynavision-programmable-xtreme-for-son/LP_CF_DDVPXSON_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/ignitors/electronic-ignitors-for-hid-lamp-circuits-india/LP_CF_IN_IGNIT_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-basic-gearbox-system-for-son-india/LP_CF_IN_GEARB_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/dynavision-programmable-xtreme-for-cdme/LP_CF_DDVPXCDM_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-basic-semi-parallel-ballasts-for-mhn-cdm-lamps/LP_CF_DBCMH_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-constant-wattage-bsx-for-sox/LP_CF_DCWSX_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-heavyduty-bhl-for-hpl-hpi/LP_CF_DHDHP_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/dynavision-programmable-xtreme-for-cdo/LP_CF_DDVPXCDO_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/dynavision-programmable-xtreme-for-cpo/LP_CF_DDVPXCPO_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/primavision-economy-for-cpo/LP_CF_DPVCPOEC_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-indoor/primavision-twin-for-cdm/LP_CF_DPVTWN_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-indoor/primavision-mini-for-cdm/LP_CF_DPCMINI_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-indoor/aspiravision-compact-for-cdm/LP_CF_DAVCMPCT_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-indoor/primavision-for-sdw-tg/LP_CF_DPVSDW-T_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-basic-bsn-bmh-mk4-semi-parallel-for-son-cdo-cdm-mh-hpi/LP_CF_DBCSNSP4_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/controllers/gear-for-sdw-t-lamps/LP_CF_DCSSD_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/primavision-xtreme-for-son/LP_CF_DPVSONXT_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/primavision-baseperform/LP_CF_1245929_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-highpower-for-son-mh-hpl-hpi/LP_CF_DHPSN_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-high-power-ballasts-for-hpl-and-hpi-lamps/LP_CF_DHPHPL_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electronic-outdoor/primavision-for-cdm-elite-mw/LP_CF_DPVCDMXT_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-basic-bhl-for-hpl-hpi-india/LP_CF_IN_BAHPL_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/ignitors/electronic-parallel-ignitor-for-hid-lamp-circuits/LP_CF_IGNSI_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-high-power-ballasts-for-son-mh-lamps/LP_CF_DHPSON_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-high-power-ballasts-for-mh-lamps/LP_CF_DHPMH_EU/family',
    'https://www.lighting.philips.com/prof/lighting-electronics/hid/hid-electromagnetic/hid-basic-bsn-bmh-semi-parallel-for-son-cdo-cdm-mh-hpi/LP_CF_DBCSNSP_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/master-led-hid-hpi/LP_CF_6871562_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/master-led-hid-sox/LP_CF_6486155_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/led-glass-hid-lamps/LP_CF_9033446_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/master-led-hid-hpl/LP_CF_7165331_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/corepro-led-hid-hpl/LP_CF_7903997_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/corepro-led-hid-son-t/LP_CF_8852552_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/master-led-hid-son-t-ultra-efficient/LP_CF_10393397_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/trueforce-core-led-industrial-and-retail-highbay-hpi-son-hpl/LP_CF_7165405_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/trueforce-led-industrial-and-retail-mains-highbay-hpi-son-hpl/LP_CF_7165398_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/led-wallpack-retrofits/LP_CF_7909841_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/led-corn-cobs/LP_CF_7404056_EU/family',
    'https://www.lighting.philips.com/prof/led-lamps-and-tubes/led-hid-replacement/led-highbay/LP_CF_7404055_EU/family',
    'https://www.lighting.philips.com/prof/conventional-lamps-and-tubes/special-lamps/optical---medical-equipment/hid/cpl/LP_CF_XDCPLP_EU/family',
    'https://www.lighting.philips.com/prof/conventional-lamps-and-tubes/high-intensity-discharge-lamps/hid-horticulture/horticulture/LP_CF_D_HORT_EU/family',
    'https://www.lighting.philips.com/prof/conventional-lamps-and-tubes/special-lamps/optical---medical-equipment/hid/cdm/LP_CF_XDCDMSAP_EU/family',
    'https://www.lighting.philips.com/prof/conventional-lamps-and-tubes/high-intensity-discharge-lamps/hid-horticulture/horti/LP_CF_EMHORTI_EU/family',
    'https://www.lighting.philips.com/prof/conventional-lamps-and-tubes/high-intensity-discharge-lamps/hid-horticulture/ceramalux-agro/LP_CF_D_CERAGR_EU/family',
    'https://www.lighting.philips.com/prof/conventional-lamps-and-tubes/halogen-lamps/mv-halogen-without-reflector/halogena-ide/LP_CF_HIDET_EU/family',
]

for url in mylist:
    browser.get(url)
    time.sleep(5)
    print("Product_urls", url)
    for product in browser.find_elements(By.XPATH, "//table[@class='product-table-list__items']//tr//a"):
        product_link = product.get_attribute('href')
        # if "family" in product_link:
        print("'" + product_link + "',")
        save = open('url1.txt', 'a+', encoding='utf-8')
        save.write(f"{product_link}\n")

    # count = browser.find_element(By.XPATH, "//span[@class='pagination__paging-count']").text.strip()
    # lengths = len(count)
    # length = round(int(lengths) / 12 + 1)
    #
    # for i in range(2, length + 1):
    #     browser.find_element(By.XPATH, "//a[normalize-space()='Next']").click()
    #     time.sleep(2)
    #     print(i)
    #     Result = [
    #         f"{url}/{'page'}/{i}"
    #     ]
    #     for pagination_link in Result:
    #         print("'" + pagination_link + "',")

# url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/sourceasi.com/url/bakergauges_product_url - Copy.csv")['URL']
# url_length = 602
# for url_count, url in enumerate(url_link[url_length:], start=url_length):
#     browser.get(url)
#     time.sleep(1)
#     print("Product-Urls......", url)
#
