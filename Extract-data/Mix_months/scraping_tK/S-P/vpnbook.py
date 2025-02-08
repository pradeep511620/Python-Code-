from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = "http://64.225.4.29:9994"
# l=['http://64.225.4.29:9994',"http://212.98.132.243:80"]
options = webdriver.ChromeOptions()
# options.add_argument('--proxy-server=%s' % proxy.http_proxy)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://usproxy.vpnbook.com/browse.php?u=qYMOJ%2F2T%2FQxvAhYUMDrMg3zlewwHgKk8U1mOcx330FJMBtJn48eLUP63VvNo0r%2BNrxboDoEoDcPvul2LAqjTYW7U0pf6&b=0&f=norefer')
time.sleep(5)
i=['https://www.grainger.com/product/INSIZE-Digital-Microscope-Digital-55VP03','https://www.grainger.com/product/INSIZE-Digital-Auto-Focus-Microscope-55VP01']
for j in i:
    try:
        driver.find_element(By.XPATH,'//*[@id="input"]').send_keys(j)
        driver.find_element(By.XPATH,'//*[@id="webproxylocation"]/option[2]').click()
        driver.find_element(By.XPATH,'//*[@id="webproxyform"]/div/input[2]').click()
       
    except:
        driver.find_element(By.XPATH,'//*[@id="vpnbookform"]/form/input[1]').clear()
        driver.find_element(By.XPATH,'//*[@id="vpnbookform"]/form/input[1]').send_keys(j)
        driver.find_element(By.XPATH,'//*[@id="vpnbookform"]/form/input[2]').click()
    print(driver.find_element(By.CLASS_NAME,'lypQpT').text)