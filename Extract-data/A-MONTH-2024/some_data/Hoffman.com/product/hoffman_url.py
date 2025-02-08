import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import ChromeOptions


def ReadChromeDriver(product_url):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(product_url)
    time.sleep(3)

    return driver


def ReadSoupUrl(product_url):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    ress = requests.get(product_url, headers=header)
    soup = BeautifulSoup(ress.content, "html.parser")

    return soup


def FetchProductUrl(driver):
    for product in driver.find_elements(By.XPATH, "//*[@class='card-accordion']//a"):
        product_url_main = product.get_attribute('href')
        print(product_url_main)
        with open("prod12244.txt", 'a+', encoding="utf-8") as file_save:
            file_save.write(f"{product_url_main}\n")


    url_length = driver.find_element(By.XPATH, "//div[@class='product-listing__main-results']//header").text.strip().split(" ")[2]
    length = round(int(url_length) / 10 + 1)
    print(length)
    for i in range(2, length):
        driver.find_element(By.XPATH, f"//a[@title='Go to page {i}']").click()
        print('click')
        time.sleep(3)

    for product in driver.find_elements(By.XPATH, "//*[@class='card-accordion']//a"):
        product_url_main = product.get_attribute('href')
        if "products" in product_url_main:
            print("'" + product_url_main + "',")
            with open("prod12244.txt", 'a+', encoding="utf-8") as file_save:
                file_save.write(f"{product_url_main}\n")

    # for i in range(1, 11):
    #     link = driver.find_element(By.XPATH, f"(//button[@class='card-accordion__trigger'])[{i}]").click()
    #     print("..................", link)
    #


def ReadFromListUrl():
    # file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Jan/Knapeandvogt.com/url/Product-url.csv"
    # url_lists = pd.read_csv(file_path)["URL"]

    url_list = [
        # 'https://hoffman.nvent.com/products/zonex-atex-iecex-type-4x-hinged-316ss-atex-design-0',
        # 'https://hoffman.nvent.com/products/zonex-non-metallic-terminal-enclosure',
        # 'https://hoffman.nvent.com/products/zonex-sa-series-junction-boxes',
        # 'https://hoffman.nvent.com/products/spectracool-narrow-hazardous-location-indooroutdoor',
        # 'https://hoffman.nvent.com/products/hazardous-location-heaters',
        # 'https://hoffman.nvent.com/products/purge-and-pressurization-systems',
        # 'https://hoffman.nvent.com/products/hazardous-location-led-lights-strip',
        # 'https://hoffman.nvent.com/products/hazardous-location-led-light-can',
        # 'https://hoffman.nvent.com/products/hazardous-location-breather-drains',
        # 'https://hoffman.nvent.com/products/hazardous-location-window-kits',
        # 'https://hoffman.nvent.com/products/hazardous-location-hole-seals',
        # 'https://hoffman.nvent.com/products/panels-zonex-non-metallic-terminal-enclosure',
        # 'https://hoffman.nvent.com/products/replacement-hardware-kit-hazardous-location-led-lights',
        # 'https://hoffman.nvent.com/products/hazardous-location-door-switch',
        # 'https://hoffman.nvent.com/products/hyshed-stand-kit-ip69k',
        # 'https://hoffman.nvent.com/products/h2omit-vent-drains-0',
        # 'https://hoffman.nvent.com/products/flange-mount-disconnect-mcf',
        # 'https://hoffman.nvent.com/products/internal-disconnect-shield',
        # 'https://hoffman.nvent.com/products/sequestr-external-disconnect-accessory',
        # 'https://hoffman.nvent.com/products/electrical-interlock-0',
        # 'https://hoffman.nvent.com/products/electrical-interlock-safety-lockout-0',
        # 'https://hoffman.nvent.com/products/electrical-interlock-defeater',
        # 'https://hoffman.nvent.com/products/secondary-door-interlock-kit-fms',
        # 'https://hoffman.nvent.com/products/safety-lockout-0',
        # 'https://hoffman.nvent.com/products/dual-access-safety-lockout-0',
        # 'https://hoffman.nvent.com/products/intersafe-data-interface-port-ethernetprofinet-0',
        # 'https://hoffman.nvent.com/products/intersafe-data-interface-port-ethernet-0',
        # 'https://hoffman.nvent.com/products/intersafe-data-interface-port-controlnet-0',
        # 'https://hoffman.nvent.com/products/intersafe-data-interface-port-dh-modbus-plus-ethernet-0',
        # 'https://hoffman.nvent.com/products/intersafe-data-interface-port-usb-10-ft-cable-0',
        # 'https://hoffman.nvent.com/en-us/products/iec-enclosure-accessories',
        # 'https://hoffman.nvent.com/products/extreme-environments-enclosure-0',
        # 'https://hoffman.nvent.com/products/extreme-environments-air-conditioner-0',
        # 'https://hoffman.nvent.com/en-us/products/extreme-enclosure-gasket-replacement-kit-epdm-0',
        # 'https://hoffman.nvent.com/products/mild-steel-modular-industrial-enclosures',
        # 'https://hoffman.nvent.com/products/stainless-steel-modular-industrial-enclosures',
        # 'https://hoffman.nvent.com/products/mild-steel-freestanding-industrial-enclosures',
        # 'https://hoffman.nvent.com/products/mild-steel-wall-mounted-industrial-enclosures',
        # 'https://hoffman.nvent.com/products/stainless-steel-wall-mounted-industrial-enclosures',
        # 'https://hoffman.nvent.com/products/mild-steel-freestanding-industrial-disconnect-enclosures',
        # 'https://hoffman.nvent.com/products/mild-steel-wall-mounted-industrial-disconnect-enclosures',
        # 'https://hoffman.nvent.com/products/mild-steel-industrial-terminal-and-junction-boxes',
        # 'https://hoffman.nvent.com/products/spectracool-advanced-corrosion-protection-0',
        # 'https://hoffman.nvent.com/products/fans-and-filter-fans',
        # 'https://hoffman.nvent.com/products/thermoelectric-coolers',
        # 'https://hoffman.nvent.com/products/liquid-cooling',
        # 'https://hoffman.nvent.com/products/compact-series-2',
        # 'https://hoffman.nvent.com/products/compact-series-4',
        # 'https://hoffman.nvent.com/products/syspend-180-max',
        # 'https://hoffman.nvent.com/products/syspend-281-max',
        # 'https://hoffman.nvent.com/products/industrial-workstation-0',
        # 'https://hoffman.nvent.com/products/vertical-motion-arms',
        # 'https://hoffman.nvent.com/products/pedestals',
        # 'https://hoffman.nvent.com/products/support-arm-systems',
        # 'https://hoffman.nvent.com/products/hmi-enclosure-systems',
        # 'https://hoffman.nvent.com/products/industrial-wireway',
        # 'https://hoffman.nvent.com/products/cable-entry-systems',
        'https://hoffman.nvent.com/products/industrial-enclosure-accessories',
        'https://hoffman.nvent.com/products/cooling-accessories',
        'https://hoffman.nvent.com/products/iec-enclosure-accessories',
        'https://hoffman.nvent.com/products/led-light-kit',
        'https://hoffman.nvent.com/products/seismic-2-post-open-frame-rack',
        'https://hoffman.nvent.com/products/seismic-4-post-open-frame-rack',
        'https://hoffman.nvent.com/products/seismic-cabinet',
        'https://hoffman.nvent.com/products/seismic-rack-panel-kit',
        'https://hoffman.nvent.com/products/seismic-panel-mounting-kits',
        'https://hoffman.nvent.com/products/syspend-sanitary-hmi-system',
        'https://hoffman.nvent.com/products/vortex-coolers',
        'https://hoffman.nvent.com/products/extreme-environments-air-conditioner',
        'https://hoffman.nvent.com/products/spectracool-advanced-corrosion-protection',
        'https://hoffman.nvent.com/products/spectracool-narrow-advanced-corrosion-protection',
        'https://hoffman.nvent.com/products/spectracool-narrow-advanced-corrosion-protection-compact',
        'https://hoffman.nvent.com/products/proair-harsh-environment',
        'https://hoffman.nvent.com/products/h2omit-thermoelectric-dehumidifier',
        'https://hoffman.nvent.com/products/h2omit-vent-drains',
        'https://hoffman.nvent.com/products/cleantray-90-degree-elbow-outside-cover-sloped-0',
        'https://hoffman.nvent.com/products/replacement-gasket-hyshed-hinge-cover-enclosures',
        'https://hoffman.nvent.com/products/replacement-gasket-hyshed-screw-cover-enclosures',
        'https://hoffman.nvent.com/products/watershed-stainless-steel-padlocking-latch-kit-0',
        'https://hoffman.nvent.com/products/watershed-stainless-steel-handle-kit',
        'https://hoffman.nvent.com/products/watershed-stainless-steel-stand-kits',
        'https://hoffman.nvent.com/products/floor-stand-kit',
        'https://hoffman.nvent.com/products/concept-single-door-enclosures',
        'https://hoffman.nvent.com/products/modular-industrial-enclosures',
        'https://hoffman.nvent.com/products/junction-box-lay-hinged-cover-0',
        'https://hoffman.nvent.com/products/spectracool-narrow-compact-indoor',
        'https://hoffman.nvent.com/products/spectracool-slim-fit-indoor-air-conditioner',
        'https://hoffman.nvent.com/products/spectracool-indooroutdoor',
        'https://hoffman.nvent.com/products/filter-fan-standard',
        'https://hoffman.nvent.com/products/wireway-hanger-feed-through-0',
        'https://hoffman.nvent.com/products/aluminum-wall-mounted-industrial-enclosures',
        'https://hoffman.nvent.com/products/fiberglass-and-thermoplastic-wall-mounted-industrial-enclosures',
        'https://hoffman.nvent.com/products/fiberglass-and-thermoplastic-industrial-terminal-and-junction-boxes',
        'https://hoffman.nvent.com/products/vortex-ac-enclosure-coolers-hazardous-location',
        'https://hoffman.nvent.com/products/corrosion-inhibitor-0',
        'https://hoffman.nvent.com/products/extreme-environments-enclosure',
        'https://hoffman.nvent.com/products/hol-sealers-hole-seal-0',
        'https://hoffman.nvent.com/products/modification-equipment',
        'https://hoffman.nvent.com/products/cable-and-din-rail-cutting',
        'https://hoffman.nvent.com/products/wire-cutting-and-labeling',
        'https://hoffman.nvent.com/products/rack-and-panel-mount-power-distribution-units-pdus',
        'https://hoffman.nvent.com/products/ip-gateway-pdu',
        'https://hoffman.nvent.com/products/cable-pathway',
        'https://hoffman.nvent.com/products/cabletek-horizontal-cable-manager',
        'https://hoffman.nvent.com/products/aisle-containment',
        'https://hoffman.nvent.com/products/rackchiller-cdu800-coolant-distribution-unit-0',
        'https://hoffman.nvent.com/products/protek-single-door-fan-packages',
        'https://hoffman.nvent.com/products/protek-double-hinged-fan-packages',
        'https://hoffman.nvent.com/products/comline-vertical-mount-cabinet',
        'https://hoffman.nvent.com/products/open-frame-rack-2-post',
        'https://hoffman.nvent.com/products/open-frame-rack-4-post',
        'https://hoffman.nvent.com/products/cabletek-vertical-cable-manager',
        'https://hoffman.nvent.com/products/pole-mount-kit',
        'https://hoffman.nvent.com/products/solar-shield-top',
        'https://hoffman.nvent.com/products/straight-section-lay-painted-galvanized-hinged-cover-0',
        'https://hoffman.nvent.com/products/rj-solar-rooftop-junction-box-0',
        'https://hoffman.nvent.com/products/ru-solar-string-transition-box-0',
        'https://hoffman.nvent.com/products/cuf-solar-combiner-box-0',
        'https://hoffman.nvent.com/products/rf-solar-combiner-box-0',
        'https://hoffman.nvent.com/en-us/products/encwfhd3e726830',
        'https://hoffman.nvent.com/products/commercial-wireway-1-3R',
        'https://hoffman.nvent.com/products/pull-and-junction-boxes',
        'https://hoffman.nvent.com/products/modular-single-door-mcss-hp-0',
        'https://hoffman.nvent.com/products/concept-two-door-enclosures-0',
        'https://hoffman.nvent.com/products/concept-single-door-enclosures-0',
        'https://hoffman.nvent.com/products/modular-single-door-mcs-0',
        'https://hoffman.nvent.com/products/proline-s1-cabinet-0',
        'https://hoffman.nvent.com/products/t-series-large-capacity-outdoor-0',
        'https://hoffman.nvent.com/products/spectracool-indooroutdoor-0',
        'https://hoffman.nvent.com/products/hf-side-mount-filter-fans-0',

    ]

    # Read url from file to compare url

    i = 1
    for N0, product_url in enumerate(url_list[i:], start=i):
        print("Product --", N0, product_url)

        # soup = ReadSoupUrl(product_url)
        # FetchProductUrl(soup)

        driver = ReadChromeDriver(product_url)
        try:
            FetchProductUrl(driver)
        except Exception as e:
            print(f"Error processing {product_url}: {e}")
        finally:
            driver.quit()

    print('Saved Url')


def main():
    ReadFromListUrl()


if __name__ == "__main__":
    main()
