import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

mylist = [

    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/General-Purpose-/c/US_MT_NEMA_GENERAL/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Severe-Duty/c/US_MT_NEMA_SEVEREDUTY/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Explosion-Proof-DIP/c/US_MT_NEMA_HAZARDOUS/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Air-Handling/c/US_MT_NEMA_AIRHANDLING/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Brake-Motor/c/US_MT_NEMA_BRAKE/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Washdown/c/US_MT_NEMA_WASHDOWN/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Variable-Speed/c/US_MT_NEMA_VFD/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Farm-Duty/c/US_MT_NEMA_FARMDUTY/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Definite-Purpose/c/US_MT_NEMA_DEFINITE/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/General-Purpose-/ODP-Rolled-Steel/c/US_MT_NEMA_ODP_ROLLEDSTEEL/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/General-Purpose-/ODP-Cast-Iron/c/US_MT_NEMA_ODP_CASTIRON/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/General-Purpose-/TEAO-TEFC-Rolled-Steel/c/US_MT_NEMA_TEFC_ROLLEDSTEEL/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/General-Purpose-/TEFC-Cast-Iron/c/US_MT_NEMA_TEFC_CASTIRON/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Severe-Duty/Cooling-Tower/c/US_MT_NEMA_COOLINGTOWER/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Explosion-Proof-DIP/Class-I-%26-Class-II/c/US_MT_NEMA_CLASS_I_II/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Pump/Close-Coupled-JM-JP/c/US_MT_NEMA_CLOSECOUPLED/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Pump/Close-Coupled-JM-JP-AEGIS%C2%AE/c/US_MT_NEMA_AEGIS_CLOSECOUPLED/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Pump/Fire-Pump/c/US_MT_NEMA_FIREPUMP/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Pump/Jet-Pump/c/US_MT_NEMA_JETPUMP/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Pump/P-Base/c/US_MT_NEMA_PBASE/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Pump/AEGIS%C2%AE-Inside/c/US_MT_NEMA_AEGIS_PUMP/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Pump/Oil-Well-Pump/c/US_MT_NEMA_OILWELL/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Air-Handling/Resilient-Mount/c/US_MT_NEMA_RESILIENTMOUNT/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Air-Handling/Pad-Mount/c/US_MT_NEMA_PADMOUNT/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Variable-Speed/AEGIS%C2%AE-Inside/c/US_MT_NEMA_AEGIS_VFD/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Farm-Duty/Grain-Dryer/c/US_MT_NEMA_FARMDUTY_GRAINDRYER/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Farm-Duty/Poultry-Fan/c/US_MT_NEMA_FARMDUTY_POULTRYFAN/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---NEMA/Definite-Purpose/Compressor-Duty/c/MT_NEMA_LV_ODP_COMPRESSORDUTY/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---IEC/General-Purpose/Cast-Iron-Frame/c/US_MT_IEC_GENERAL_CASTIRON/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---IEC/Hazardous-Area-IEC---Ex-ATEX/Ex-db/c/US_MT_IEC_HAZARDOUS_EXD/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/Large-Induction-Motors/TEFC-Motors/c/US_MT_LARGE_TEFC/list',
    # 'https://www.weg.net/catalog/weg/US/en/Coatings-and-Varnishes/Liquid-Coatings/Marine/c/TV_TL_Maritima/list',
    # 'https://www.weg.net/catalog/weg/US/en/Spare-Parts/Motors/c/GLOBAL_SP_MOTORS/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---IEC/General-Purpose/c/US_MT_IEC_GENERAL/list',
    # 'https://www.weg.net/catalog/weg/US/en/Electric-Motors/AC-Motors---IEC/Hazardous-Area-IEC---Ex-ATEX/c/US_MT_IEC_HAZARDOUS/list',
    'https://www.weg.net/catalog/weg/US/en/Drives/Accessories-for-Drives/Line-and-Load-Reactors/c/GLOBAL_WDC_DRV_LINE_REACTORS_UL/list',

]

for url in mylist:
    driver.get(url)
    time.sleep(5)
    print('product-urls...', url)

    driver.execute_script('return document.querySelector("#btnCloseCookieDisclaimer")').click()

    link = driver.find_elements(By.XPATH, "//ul[contains(@class,'list-unstyled xtt-listing-grid')]//li//a")
    print("length.....", len(link))
    for urs in driver.find_elements(By.XPATH, "//ul[contains(@class,'list-unstyled xtt-listing-grid')]//li//a"):
        url_links = urs.get_attribute('href')
        if '#' not in url_links and "classifications" not in url_links:
            print(url_links)
            save = open('Product_url_weg2.txt', 'a+', encoding='utf-8')
            save.write('\n' + url_links)
    print('save url into files1')

    le = driver.find_element(By.XPATH, "//div[@class='xtt-pagination-showing']")
    c = le.text.replace(',', '').split()[-2]
    print("count....", c)
    length = round(int(c) / 20 + 1)
    print("loop.... ", length)
    for i in range(1, length + 1):
        try:
            driver.find_element(By.XPATH, "//li[@class='next']").click()
        except NoSuchElementException:
            print('Unable to locate element:')
        time.sleep(4)
        print(i)

        urls = set()
        link = driver.find_elements(By.XPATH, "//ul[contains(@class,'list-unstyled xtt-listing-grid')]//li//a")
        print("length.....", len(link))
        for urs in driver.find_elements(By.XPATH, "//ul[contains(@class,'list-unstyled xtt-listing-grid')]//li//a"):
            url_links = urs.get_attribute('href')
            if '#' not in url_links and "classifications" not in url_links:
                urls.add(url_links)

            for ur in urls:
                url_link = ur
                save = open('Product_url_weg2.txt', 'a+', encoding='utf-8')
                save.write('\n' + url_link)
        print('save url into files')
