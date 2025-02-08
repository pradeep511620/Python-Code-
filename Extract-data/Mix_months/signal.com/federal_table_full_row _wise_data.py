import time
from typing import TextIO

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome(r"/home/pradeep/Music/chromedriver_linux64/chromedriver")
driver.maximize_window()

l = 0
mylist = [
    # 'https://signaling.fedsig.com/product/am50-audiomaster',
    # 'https://signaling.fedsig.com/product/121aled',
    # 'https://signaling.fedsig.com/product/slm300-slm350-streamline',
    # 'https://signaling.fedsig.com/product/explosion-proof-industrial-telephone',
    # 'https://signaling.fedsig.com/product/break-glass-call-point',
    # 'https://signaling.fedsig.com/product/310-mv-audiomaster-two-way-intercom',
    # 'https://signaling.fedsig.com/product/310-mv-mnc-audiomaster-two-way-intercom',
    # 'https://signaling.fedsig.com/product/fire-alarm-pull-station',
    # 'https://signaling.fedsig.com/product/121aled-n-nsf',
    # 'https://signaling.fedsig.com/product/telb-telcom-telephone-extension-ringer-device',
    # 'https://signaling.fedsig.com/product/telc-telcom-telephone-extension-ringer-device',
    # 'https://signaling.fedsig.com/product/ps-series-push-button-station',
    # 'https://signaling.fedsig.com/product/121sled-n-nsf-certified-series-sanitation-rotating-led-warning-light',
    # 'https://signaling.fedsig.com/product/310x-mv-audiomaster-hazardous-location-two-way-intercom',
    # 'https://signaling.fedsig.com/product/ad-26-atkinson-dynamics-intercom',
    # 'https://signaling.fedsig.com/product/121sled-vitalite-rotating-led-warning-light',
    # 'https://signaling.fedsig.com/product/push-button-call-point',
    # 'https://signaling.fedsig.com/product/telh-telcom-telephone-extension-ringer-device',
    # 'https://signaling.fedsig.com/product/121x-explosion-proof-rotating-light',
    # 'https://signaling.fedsig.com/product/ad-26p-atkinson-dynamics-panel-mount-intercom',
    # 'https://signaling.fedsig.com/product/K122283A',
    # 'https://signaling.fedsig.com/product/K122341A',
    # 'https://signaling.fedsig.com/product/300fp-field-programmer',
    # 'https://signaling.fedsig.com/product/ad-27-atkinson-dynamics-intercom',
    # 'https://signaling.fedsig.com/product/131st-131dst-starfire-strobe-warning-light',
    # 'https://signaling.fedsig.com/product/K122342A',
    # 'https://signaling.fedsig.com/product/141st-electraflash-strobe-warning-light',
    # 'https://signaling.fedsig.com/product/300gc-selectone',
    # 'https://signaling.fedsig.com/product/ad-27p-atkinson-dynamics-panel-mount-intercom',
    # 'https://signaling.fedsig.com/product/ad-28x-mv-atkinson-dynamics-hazardous-location-intercom',
    # 'https://signaling.fedsig.com/product/151xst-hazardous-location-warning-light',
    # 'https://signaling.fedsig.com/product/300gcx-cn-selectone',
    # 'https://signaling.fedsig.com/product/K122348A',
    # 'https://signaling.fedsig.com/product/K122351A',
    # 'https://signaling.fedsig.com/product/300gcx-selectone',
    # 'https://signaling.fedsig.com/product/ad-56-atkinson-dynamics-intercom',
    # 'https://signaling.fedsig.com/product/154xsthi-and-154xst-cn',
    # 'https://signaling.fedsig.com/product/ad-56p-atkinson-dynamics-panel-mount-intercom',
    # 'https://signaling.fedsig.com/product/154xst-supervised-light',
    # 'https://signaling.fedsig.com/product/K122A299A',
    # 'https://signaling.fedsig.com/product/300mb-commcenter',
    # 'https://signaling.fedsig.com/product/KGL4076215',
    # 'https://signaling.fedsig.com/product/300scw-1-command-unit',
    # 'https://signaling.fedsig.com/product/191xl-cn',
    # 'https://signaling.fedsig.com/product/ad-57-atkinson-dynamics-intercom',
    # 'https://signaling.fedsig.com/product/ad-fp-foot-pedal',
    # 'https://signaling.fedsig.com/product/191xl-led',
    # 'https://signaling.fedsig.com/product/300-selectone-speaker',
    # 'https://signaling.fedsig.com/product/300vsc-1044sb-selectone-rack-mount-command-unit',
    # 'https://signaling.fedsig.com/product/adncm-noise-cancelling-microphone',
    # 'https://signaling.fedsig.com/product/300vsc-1-command-unit',
    # 'https://signaling.fedsig.com/product/K141A129A',
    # 'https://signaling.fedsig.com/product/225XST-n-nsf',
    # 'https://signaling.fedsig.com/product/304x-314x',
    # 'https://signaling.fedsig.com/product/31x-and-41x-horn',
    # 'https://signaling.fedsig.com/product/225xst-strobe',
    # 'https://signaling.fedsig.com/product/K143133A',
    # 'https://signaling.fedsig.com/product/350tr-vibratone-horn',
    # 'https://signaling.fedsig.com/product/K1461138A',
    # 'https://signaling.fedsig.com/product/24xst',
    # 'https://signaling.fedsig.com/product/24xsthi-supervised',
    # 'https://signaling.fedsig.com/product/K1461181A',
    # 'https://signaling.fedsig.com/product/350-vibratone-horn',
    # 'https://signaling.fedsig.com/product/K2001878B',
    # 'https://signaling.fedsig.com/product/27XHSNG',
    # 'https://signaling.fedsig.com/product/350wb-vibratone-horn',
    # 'https://signaling.fedsig.com/product/K2001878B-01',
    # 'https://signaling.fedsig.com/product/350wbx-vibratone-hazardous-location-horn',
    # 'https://signaling.fedsig.com/product/27xl-led-warning-light',
    # 'https://signaling.fedsig.com/product/K2001878B-02',
    # 'https://signaling.fedsig.com/product/27xst-4-supervised',
    # 'https://signaling.fedsig.com/product/3h-6h',
    # 'https://signaling.fedsig.com/product/450e-horn',
    # 'https://signaling.fedsig.com/product/K2001878B-02P',
    # 'https://signaling.fedsig.com/product/27xst-strobe-light',
    # 'https://signaling.fedsig.com/product/K2001878B-05',
    # 'https://signaling.fedsig.com/product/371BRCKT',
    # 'https://signaling.fedsig.com/product/450ewbx',
    # 'https://signaling.fedsig.com/product/K2001878B-07',
    # 'https://signaling.fedsig.com/product/TR',
    # 'https://signaling.fedsig.com/product/371dst-commander',
    # 'https://signaling.fedsig.com/product/504wb-506wb',
    # 'https://signaling.fedsig.com/product/371led-commander',
    # 'https://signaling.fedsig.com/product/K2001878B-08',
    # 'https://signaling.fedsig.com/product/50gcb-selectone',
    # 'https://signaling.fedsig.com/product/K2001878B-18',
    # 'https://signaling.fedsig.com/product/371ledx',
    # 'https://signaling.fedsig.com/product/50gc-selectone',
    # 'https://signaling.fedsig.com/product/av1-led',
    # 'https://signaling.fedsig.com/product/K2001878B-21',
    # 'https://signaling.fedsig.com/product/52-resonating-horn',
    # 'https://signaling.fedsig.com/product/av1st',
    # 'https://signaling.fedsig.com/product/55-and-56-resonating-horns',
    # 'https://signaling.fedsig.com/product/K2001896B',
    # 'https://signaling.fedsig.com/product/bpl26l-battery-powered',
    # 'https://signaling.fedsig.com/product/am15-audiomaster',

    # 'https://signaling.fedsig.com/product/SSM',



    'https://signaling.fedsig.com/product/2000-series-xen1-xen4',



]
for url in mylist:
    try:
        l = l + 1
        driver.get(url)
        time.sleep(30)
        # driver.get(driver.current_url)

        print("Products Urls", l, url)

        print("************************************* Table UPC : ****************************************")
        data = []
        th = []

        table = driver.find_element(by=By.ID, value='sku-specification-table')
        td = table.find_elements(by=By.TAG_NAME, value='tr')
        for dd in td:
            ss = dd.find_elements(By.TAG_NAME, 'th')

            if not ss:
                print('null')
            else:
                save_details: TextIO = open("hh1.xlsx", "a+", encoding="utf-8")
                save_details.write('\n' + url)
                print("\n ***** Record stored into federal signal urls files. *****")

                for f1 in ss:
                    save_details.write('\t' + f1.text)
                    continue

            s = dd.find_elements(By.TAG_NAME, 'td')
            if not s:
                continue

            save_details: TextIO = open("hh1.xlsx", "a+", encoding="utf-8")
            save_details.write('\n' + url)
            for f in s:
                save_details.write('\t' + "rp_"+f.text)
                print("\n ***** Record stored into federal signal tables  files. *****")
    except Exception as e:
        print("Not found")
        save_details: TextIO = open("remaining_urls.xlsx", "a+", encoding="utf-8")
        save_details.write("\n" + url)
        print("End")
        save_details.close()
        print("\n ***** Record stored into Table Specifications 1 . *****")
        print(e)

