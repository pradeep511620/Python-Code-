import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

mylst = [
    # 'https://www.pureairemonitoring.com/universal-gas-detector',
    # 'https://www.pureairemonitoring.com/universal-gas-detector-with-remote-sensor',
    # 'https://www.pureairemonitoring.com/all-categories-gas-monitorsair-check-o2-oxygen-deficiency-monitor-for-co2-n2-storage-areas/',
    # 'https://www.pureairemonitoring.com/product/air-check-o2-digital-remote-sensor-0-25/',
    # 'https://www.pureairemonitoring.com/air-check-o2-sample-draw-monitor-2/',
    # 'https://www.pureairemonitoring.com/combo-o2co2-monitor/',
    # 'https://www.pureairemonitoring.com/oxygen-analyzer-0-1000ppm',
    # 'https://www.pureairemonitoring.com/product/pureaire-co2-safety-monitor/',
    # 'https://www.pureairemonitoring.com/air-check-o2-sample-draw-monitor-water-resistant',
    # 'https://www.pureairemonitoring.com/oxygen_monitor_chambers',
        # 'https://www.pureairemonitoring.com/air-check-o2-ex-oxygen-deficiency-monitor-html/',
    # 'https://www.pureairemonitoring.com/multi-channel-controller/',
        # 'https://www.pureairemonitoring.com/air-check-o2-oxygen-deficiency-monitor-for-glove-box-and-chambers/',
    # 'https://www.pureairemonitoring.com/water-resistant-sample-draw-dual-oxygen-0-25/carbon-dioxide-0-50000-ppm-monitor',
    # 'https://www.pureairemonitoring.com/st-48-combustible-toxic-gas-monitor',
        # 'https://www.pureairemonitoring.com/product/air-check-ex-h2-gas-monitoring-system-3/',
    # 'https://www.pureairemonitoring.com/product/oxygen-deficiency-monitor-0-30/',
        # 'https://www.pureairemonitoring.com/combo-o2co2-monitor-50000ppm/',
        # 'https://www.pureairemonitoring.com/trace-oxygen-analyzer-kf25-0-100-ppm',
        # 'https://www.pureairemonitoring.com/air-check-ex-toxic-gas-monitor-3/',
        # 'https://www.pureairemonitoring.com/ppb-oxygen-analyzer-kf25-0-10-ppm',
    # 'https://www.pureairemonitoring.com/product/st-48-hydrogen-sulfide-combustible-gas-monitor',
    # 'https://www.pureairemonitoring.com/product/8-channel-programmable-controller-for-o2-or-gas-monitors/99196',
    'https://www.pureairemonitoring.com/channel-modbus-master-display-alarm-monitorcontroller-2/',
    # 'https://www.pureairemonitoring.com/dual-o2/-co2-ip67-water-proof-monitor',
        # 'https://www.pureairemonitoring.com/product/air-check-carbonyl-sulfide-monitor/',
    # 'https://www.pureairemonitoring.com/air-check-advantage-methyl-bromide-gas-monitor/',

]


def get_url(url):

    print("product - urls", url)


def table_specs(url):
    driver.get(url)
    time.sleep(6)
    # driver.maximize_window()

    # bread = driver.find_element(By.XPATH, "//nav[@class='woocommerce-breadcrumb']").text.strip().replace('\n', '<<<')
    # print('BreadCrumb...', bread)
    #
    # title = driver.find_element(By.XPATH, "//h1[@class='product_title entry-title']").text.strip()
    # print(title)
    #
    # item = driver.find_element(By.XPATH, "//div[@class='gases_detect']").text.strip()
    # print("Item...", item)
    #
    # price = driver.find_element(By.XPATH, "//p[@class='price']").text.strip()
    # print("Price...", item)
    #
    # product = driver.find_element(By.XPATH, "//div[@class='woocommerce-product-details__short-description']/p[1]").text.strip().replace('\n', '')
    # print("Product...", product)
    #
    # feature1 = driver.find_element(By.XPATH, "//div[@id='tab-description']//ul").text.replace('\n', " >> ")
    # # print("Description...", feature1)
    #
    # feature2 = driver.find_element(By.XPATH, "//div[@class='woocommerce-tabs wc-tabs-wrapper']//p[1]").text.strip().replace('\n', '')
    # # print("Description...1", feature2)
    #
    # feature3 = driver.find_element(By.XPATH, "//div[@class='woocommerce-tabs wc-tabs-wrapper']//p[2]").text.strip().replace('\n', '')
    # # print("Description...2", feature3)
    # features = feature1, feature2, feature3
    # print("features......", features)

    # time.sleep(1)
    # driver.execute_script("window.scrollBy(0, 800)", "")
    # time.sleep(1)
    # driver.find_element(By.CLASS_NAME, "icon-close").click()
    # time.sleep(3)

    try:
        driver.find_element(By.XPATH, "//li[@id='tab-title-3']//a").click()
        time.sleep(4)
    except:
        pass

    i = 0
    name = []
    value = []
    # table = driver.find_elements(By.XPATH, "//div[@id='tab-3']//table//tr//td")
    # table = driver.find_elements(By.XPATH, "//body/div[@id='primary']/main[@id='main']/div[@id='container']/div[@id='content']/div[@id='product-15482']/div[@class='woocommerce-tabs wc-tabs-wrapper']/div[@id='tab-2']/table//tr//td")
    table = driver.find_elements(By.XPATH, "//div[@id='tab-1']//table//tr//td")
    for td in table:
        i += 1
        tdd = td.text.strip()
        if i % 2 != 0:
            name.append(tdd.replace('\n', ""))
        else:
            value.append(tdd.replace('\n', ''))

    for a, b in zip(name, value):
        print(a, "..........", b)
        saved = open('pureaire-table.txt', 'a+', encoding='utf-8')
        saved.write('\n' + url + "\t" + a + "\t" + b)
    print("save table into text files")


def main():
    # get_url()
    i = 0
    for item_url in mylst[i:]:
        table_specs(item_url)
        print(i, "....................", item_url)
        i += 1


main()
