import time

from selenium import webdriver
from selenium.common import NoSuchElementException, JavascriptException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# import undetected_chromedriver as uc

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")
driver = webdriver.Chrome()
# driver = uc.Chrome(options=opts)

driver.maximize_window()


url_list = [

    # 'https://www.regalrexnord.com/products/mechanical-power-transmission-components/tighteners-idlers/sprocket-idlers',
    # 'https://www.regalrexnord.com/products/mechanical-power-transmission-components/tighteners-idlers/tightener-shafts',
    # 'https://www.regalrexnord.com/products/mechanical-power-transmission-components/tighteners-idlers/v-belt-idlers',
    'https://www.tiemannind.com/searchPage.action?pageClick=Y&keyWord=enerpac'




]
for url in url_list:
    # try:
    driver.get(url)
    time.sleep(4)
    print("Product - url : -----", url)
    # res = requests.get(url)
    # soup = BeautifulSoup(res.content, "html.parser")
    save = open('url.txt', "a+", encoding='utf-8')

    total_url_count = driver.find_element(By.XPATH, "//div[@class='searchResults']//p").text.strip().split(" ")[0]
    length = round(int(total_url_count) / 12 + 1)
    print('length.....', length)
    for count in range(1, length):
        multi = count * 12
        adds = '&srchTyp=0&gallery=0&sortBy=score|desc&resultPage=12&pageNo=' + str(multi)
        add_urls = url + adds
        # print(add_urls)
        driver.get(add_urls)
        time.sleep(5)
        print(len(add_urls))

    driver.quit()
