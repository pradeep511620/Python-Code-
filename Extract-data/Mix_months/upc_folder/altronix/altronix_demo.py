import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
opts = Options()
opts.headless = False
driver = webdriver.Chrome()

# driver = webdriver.Chrome()
driver.maximize_window()

l = 0
i = 0
# url = 'https://www.jmac.com/Altronix_EBRIDGE1CR_p/altronix-ebridge1cr.htm'
# url = 'https://www.jmac.com/Altronix_EBRIDGE1CT_p/altronix-ebridge1ct.htm'
url = 'https://www.jmac.com/Altronix_HUBWAYAVPPK_p/altronix-hubwayavppk.htm'

l = l + 1
driver.get(url)
print("Product_urls", l, url)
time.sleep(2)

lst = [
        'EBRIDGE1CR',
        # 'EBRIDGE1CRT',
        # 'EBRIDGE1CT',
]

for i in lst:
    rp = i.replace("rp_", "")
    print("running_mpns....", rp)
    title = ''
    upc_d = ''
    current = ''
    try:
        driver.find_element(By.XPATH, "//div[@id='search']//input[@placeholder='Search JMAC']").send_keys(rp)
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='search']//input[@value='Go']").click()
        time.sleep(2)
    except:
        pass

    # click to product urls
    try:
        for jh in driver.find_elements(By.CLASS_NAME, 'v-product'):
            print(jh.text)
            jd = jh.text.split(' ')
            if i == jd[1].replace('\nOur', ''):
                jh.find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
    except Exception as e:
        print('Error', e)



# upc = driver.find_element(By.XPATH, "(//span[@id='product_description'])[1]").text.split("\n")[19]
# print("upc....", upc)
# upc = driver.find_element(By.ID, "product_description").text.replace('\n', '').split('UPC:')
# print(upc)
# U = upc[1]
# print(U)
# ss = U.split('Average')
# upc_d = ss[0]
# print("upc...", upc_d)
