# """
import time
import pyautogui

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.minimize_window()
action_chains = ActionChains(driver)
options = webdriver.ChromeOptions()
mylst = [
    'https://www.raptorsupplies.com/pd/approved-vendor/5jck8',
    # 'https://www.grainger.com/product/U-S-MOTORS-Motor-Open-Dripproof-56JA19',


]
for url in mylst:
    driver.get(url)
    time.sleep(6)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    driver.close()
# """

"""
import requests
from bs4 import BeautifulSoup

# url = 'https://www.burrellsci.com/2305295/Product/Reagents-ZC51011082'
url = 'https://www.burrellsci.com/2295203/Product/Burrell_Scientific_Digital_Hotplate_Magnetic_Stirrer_077_870_00_00'
re = requests.get(url)
soup = BeautifulSoup(re.content, "html.parser")
des = soup.find("div", {"id":"specificationSection"})
dess = des.find_all('td')
for j in dess:
    print(j.text.strip().replace('\n', ''))

"""


























