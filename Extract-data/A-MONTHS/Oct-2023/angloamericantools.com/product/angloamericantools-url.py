import time
from selenium import webdriver
from selenium.common import NoSuchElementException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()

mylist = [
    # 'http://shop.angloamericantools.com/c/chisels-punches_chisels',
    # 'http://shop.angloamericantools.com/c/chisels-punches_punches',
    # 'http://shop.angloamericantools.com/c/chisels-punches_wrecking-bars',
    # 'http://shop.angloamericantools.com/c/clamps_axial-clamps',
    # 'http://shop.angloamericantools.com/c/clamps_c-clamps',
    # 'http://shop.angloamericantools.com/c/clamps_l-clamps',
    # 'http://shop.angloamericantools.com/c/clamps_special-jaw-clamps',
    # 'http://shop.angloamericantools.com/c/clamps_steel-clamps',
    # 'http://shop.angloamericantools.com/c/clamps_u-clamps',
    # 'http://shop.angloamericantools.com/c/files-rasps_axe-files',
    # 'http://shop.angloamericantools.com/c/files-rasps_file-sets',
    # 'http://shop.angloamericantools.com/c/files-rasps_flat-files',
    # 'http://shop.angloamericantools.com/c/files-rasps_half-round',
    # 'http://shop.angloamericantools.com/c/files-rasps_long-angle-lathe',
    # 'http://shop.angloamericantools.com/c/files-rasps_mill-files',
    # 'http://shop.angloamericantools.com/c/files-rasps_rasps',
    # 'http://shop.angloamericantools.com/c/files-rasps_round-files',
    # 'http://shop.angloamericantools.com/c/files-rasps_square-files',
    # 'http://shop.angloamericantools.com/c/files-rasps_taper-files',
    # 'http://shop.angloamericantools.com/c/files-rasps_three-square',
    # 'http://shop.angloamericantools.com/c/files-rasps_warding-files',
    # 'http://shop.angloamericantools.com/c/pliers_hose-clamp-pliers',
    # 'http://shop.angloamericantools.com/c/pliers_locking-pliers',
    # 'http://shop.angloamericantools.com/c/pliers_pliers-sets',
    # 'http://shop.angloamericantools.com/c/pliers_special-jaw-pliers',
    # 'http://shop.angloamericantools.com/c/thread-repair-tools_screw-extractors',
    # 'http://shop.angloamericantools.com/c/thread-repair-tools_tap-wrenches',
    # 'http://shop.angloamericantools.com/c/thread-repair-tools_universal-thread-repair',
    # 'http://shop.angloamericantools.com/c/wrenches_adjustable-wrenches',
    # 'http://shop.angloamericantools.com/c/wrenches_insulated-wrenches',
    # 'http://shop.angloamericantools.com/c/wrenches_open-end-wrenches',
    # 'http://shop.angloamericantools.com/c/wrenches_pipe-wrenches',
    # 'http://shop.angloamericantools.com/c/wrenches_strap-wrenches',
    # 'http://shop.angloamericantools.com/c/wrenches_torque-wrenches',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_berger',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_boa',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_grip-on',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_hazet',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_irega',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_nes-thread-repair',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_osca',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_ox-head',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_ratch-cut',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_rennsteig',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_robert-sorby',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_schroder',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_suprabeam',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_thor',

    # 'http://shop.angloamericantools.com/c/tools-by-factory_tome-feteira',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_turnus',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_virax',
    # 'http://shop.angloamericantools.com/c/tools-by-factory_witte',
    # 'http://shop.angloamericantools.com/c/illumination_led-flashlights',
    # 'http://shop.angloamericantools.com/c/illumination_led-headlamps',
    # 'http://shop.angloamericantools.com/home/index/13516.0.1.1',
    # 'http://shop.angloamericantools.com/c/cutting-tools_chain-pipe-cutters',
    # 'http://shop.angloamericantools.com/c/cutting-tools_tube-cutters',
    # 'http://shop.angloamericantools.com/c/hammers_aluminum-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_ball-pein-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_carpenter-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_club-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_copper-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_dead-blow-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_engineer-machinist-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_mallets',
    # 'http://shop.angloamericantools.com/c/hammers_nylon-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_polyurethane-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_rawhide-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_rubber-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_sledge-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_soft-face-hammers',
    # 'http://shop.angloamericantools.com/c/hammers_split-face-hammers',

    # 'http://shop.angloamericantools.com/c/gardening-tools',
    # 'http://shop.angloamericantools.com/c/screwdrivers',
    # 'http://shop.angloamericantools.com/c/sockets',
    # 'http://shop.angloamericantools.com/c/stamping-tools',
    # 'http://shop.angloamericantools.com/c/tool-storage',
    # 'http://shop.angloamericantools.com/c/woodworking-tools',
    'http://shop.angloamericantools.com/k/partnumlist',
]
for url in mylist:
    browser.get(url)
    print("Product_urls", url)
    time.sleep(1)
    for product in browser.find_elements(By.XPATH, "//table[@id='partNumList']//a"):
        product_url = product.get_attribute('href')
        print(product_url)
        save = open("url1.txt", "a+", encoding="utf-8")
        save.write(f"\n {product_url}")
    print('save url ...........1')

    count = browser.find_element(By.XPATH, "(//td[@align='left'])[4]").text.strip().split(' ')[-2]
    length = round(int(count) / 12 + 1)
    print(count)
    for i in range(1, length):
        try:
            browser.find_element(By.XPATH, "(//a[contains(text(),'Next >>')])[1]").click()
            time.sleep(3)
            print(i)
        except NoSuchElementException:
            print('Unable to locate element')

    #     Result = [
    #         f"{url}/{'page'}/{i}"
    #     ]
    #     for jj in Result:
    #         print("'" + jj + "',")

        for product in browser.find_elements(By.XPATH, "//table[@id='partNumList']//a"):
            product_url = product.get_attribute('href')
            print(product_url)
            save = open("url1.txt", "a+", encoding="utf-8")
            save.write(f"\n {product_url}")
        print('save url ...........2')
