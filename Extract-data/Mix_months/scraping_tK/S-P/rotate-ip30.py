import requests
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime,timedelta




proxies = [
   "http://115.96.208.124:8080",
   'http://20.69.79.158:8443',
    'http://146.70.76.146:3128',
   'http://104.223.135.178:10000',
   'http://157.245.27.9:3128',
   'http://20.69.79.158:8443',

]

urls = [
    'https://www.grainger.com/product/INSIZE-Digital-Microscope-Digital-55VP03',
    'https://www.grainger.com/product/INSIZE-Digital-Auto-Focus-Microscope-55VP01',
   
]

def fetch_url(proxy,driver):
    
    # try:
    #     response = requests.get(url, proxies={'http': proxy, 'https': proxy})
    #     # do something with the response
    #     print(f'Response from {url}: {response.status_code}')
    # except requests.exceptions.RequestException as e:
    #     # handle the error
    #     print(f'Request error: {e}')

        # ssl._create_default_https_context = ssl._create_unverified_context
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")


        dt = datetime.strptime(current_time, '%H:%M:%S')
        u=dt + timedelta(minutes=29)
        c=str(u).split(' ')[1]
        d=c.split
        print("Current Time =", current_time)
        for url in reversed(urls):
            print(url)
            driver.get(url)
            now2 = datetime.now()
            urls.pop()

            print(driver.find_element(By.CLASS_NAME,'lypQpT').text)







def main():
    index = 0
    for i in range(0,len(proxies)):
        
        prox = proxies[index % len(proxies)]
        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy =prox
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server=%s' % proxy.http_proxy)
        print(prox)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        c=0
        fetch_url(proxy,driver)


if __name__ == '__main__':
    main()