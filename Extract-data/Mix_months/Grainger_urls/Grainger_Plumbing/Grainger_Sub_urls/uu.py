
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
opts = Options()
opts.headless = True
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")

driver = webdriver.Chrome()
driver.maximize_window()


mylst = [
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/pipe-and-test-plugs?categoryIndex=5',
    # 'https://www.grainger.com/category/plumbing/gaskets/sheet-and-ring-gaskets?categoryIndex=2',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/rotary-swivel-and-expansion-joints/expansion-joints?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/pressure-and-temperature-control-valves/steam-separators?categoryIndex=13',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/valve-actuators-enclosures-and-accessories/valve-and-meter-boxes?categoryIndex=5',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/pipe-saddles?categoryIndex=9',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/flange-covers?categoryIndex=3',
    # 'https://www.grainger.com/category/plumbing/garbage-disposals-and-accessories/garbage-disposal-accessories?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/gaskets/sanitary-gaskets?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/faucets/utility-faucets/laundry-sink-faucets/two-hole-centerset-wall-mount-laundry-sink-faucets/dual-cross-handle-two-hole-centerset-wall-mount-laundry-sink-faucets?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/saddle-clamps?categoryIndex=14',
    # 'https://www.grainger.com/category/plumbing/liquid-level-gauges-and-sight-indicators/gauge-glass-and-rod-kits?categoryIndex=3',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/pipe-supports?categoryIndex=11'
    # 'https://www.grainger.com/category/plumbing/toilets-urinals-repair-parts/toilet-repair-parts-accessories/bedpan-washers-portable-toilet-flushers?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/pressure-and-temperature-control-valves/temperature-and-pressure-relief-valves?categoryIndex=14',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/float-valves-and-accessories/float-rods-adapters-and-nuzzle-assemblies?categoryIndex=2',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/shut-off-valves/truck-valves?categoryIndex=24',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/shut-off-valves/pneumatically-actuated-diaphragm-valves?categoryIndex=19',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/tools?categoryIndex=17',
    # 'https://www.grainger.com/category/plumbing/insulation/removable-blanket-insulation?categoryIndex=14',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/pressure-and-temperature-control-valves/pressure-regulators?categoryIndex=10',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/pipe-hangers-and-clamps?categoryIndex=7',
    # 'https://www.grainger.com/category/plumbing/gas-and-water-line-connectors/gas-connector-fitting?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/fixtures/sink-ac cessories?categoryIndex=1'
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/valve-actuators-enclosures-and-accessories/electric-valve-actuators?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/pipe-hanger-strap?categoryIndex=8',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/rotary-swivel-and-expansion-joints/swivel-joints?categoryIndex=5',
    # 'https://www.grainger.com/category/plumbing/insulation/insulation-boards?categoryIndex=5',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/pipe-straps?categoryIndex=10',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/pipe-tube-valve-and-fitting-protection?categoryIndex=12',
    # 'https://www.grainger.com/category/plumbing/insulation/insulated-pipe-jackets-and-blankets?categoryIndex=3',
    # 'https://www.grainger.com/category/plumbing/insulation/pipe-valve-and-fitting-heated-covers?categoryIndex=13',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/pipe-and-tube-clamps?categoryIndex=6',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/manifolds/pipe-manifolds?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/rotary-swivel-and-expansion-joints/rotary-joint-elbows?categoryIndex=3',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/steel-brackets?categoryIndex=16',
    # 'https://www.grainger.com/category/plumbing/liquid-level-gauges-and-sight-indicators/water-gauges?categoryIndex=4',
    # 'https://www.grainger.com/category/plumbing/toilets-urinals-repair-parts/toilet-repair-parts-accessories/portable-toilet-accessories?categoryIndex=4',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/tube-clamps?categoryIndex=18',
    # 'https://www.grainger.com/category/plumbing/gas-and-water-line-connectors/supply-valve-outlet-boxes?categoryIndex=2',
    # 'https://www.grainger.com/category/plumbing/drains-and-drainage/drains/downspouts-and-extenders?categoryIndex=4',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/float-valves-and-accessories/float-balls?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/gaskets/sheet-and-ring-gaskets?attrs=Product+Type%7CCompression+Packing+Seal&filters=attrs',
    # 'https://www.grainger.com/category/plumbing/gaskets/sheet-and-ring-gaskets?attrs=Product+Type%7CFlange+Gasket&filters=attrs',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/flow-control-valves/saddle-valves?categoryIndex=13',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/pressure-and-temperature-control-valves/relief-valves?categoryIndex=11',
    # 'https://www.grainger.com/category/plumbing/plumbing-replacement-parts/plumbing-parts?categoryIndex=1',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-repair-clamps-and-couplings/pipe-repair-clamps?categoryIndex=2',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/shut-off-valves/stop-and-waste-valves?categoryIndex=23',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/float-valves-and-accessories/float-valves-with-float?categoryIndex=5',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/check-valves-and-backflow-preventers/backwater-valves?categoryIndex=5',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/rotary-swivel-and-expansion-joints/rotary-joints-and-unions?categoryIndex=4',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/shut-off-valves/faucet-and-supply-stop-adapters?categoryIndex=13',
    # 'https://www.grainger.com/category/plumbing/toilets-urinals-repair-parts/toilet-repair-parts-accessories/portable-toilet-accessories?categoryIndex=4',
    # 'https://www.grainger.com/category/plumbing/pipe-accessories/pipe-and-tubing-accessories/tube-clamps?categoryIndex=18',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/shut-off-valves/piston-valves?categoryIndex=18',
    # 'https://www.grainger.com/category/plumbing/gas-and-water-line-connectors/supply-valve-outlet-boxes?categoryIndex=2',
    # 'https://www.grainger.com/category/plumbing/plumbing-valves/shut-off-valves/shut-off-valves?categoryIndex=22',
    # 'https://www.grainger.com/category/plumbing/drains-and-drainage/drains/downspouts-and-extenders?categoryIndex=4',
    'https://www.grainger.com/category/plumbing/plumbing-valves/float-valves-and-accessories/float-balls?categoryIndex=1',
]

c = 0
for url in mylst:
    c = c + 1
    driver.get(url)
    time.sleep(5)
    print('Product-url', c, url)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    a = 0
    b = 5
    while True:
        a += 1
        b += 1
        if driver.execute_script('return document.querySelector("#category-container > section.dNNbs2.category-list-view__wrapper > div > button")'):
            driver.execute_script('return document.querySelector("#category-container > section.dNNbs2.category-list-view__wrapper > div > button")').click()
            time.sleep(b)
            for product in driver.find_elements(By.XPATH, "//section[@aria-label='Category products']//li//a"):
                url_links = (product.get_attribute('href'))
                print(url_links)
                save = open("Motorss.txt", 'a+', encoding="utf-8")
                save.write('\n' + url_links)
            print(a)
            if a > 50:
                break
        else:
            for product in driver.find_elements(By.XPATH, "//section[@aria-label='Category products']//li//a"):
                url_links = (product.get_attribute('href'))
                print(url_links)
                save = open("Motorss.txt", 'a+', encoding="utf-8")
                save.write('\n' + url_links)
            break
