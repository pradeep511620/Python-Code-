import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = 'https://www.applied.com/c-brands/c-regal-rexnord/c-stearns-division/105604100bqf/Series-56-000-Disc-Brake/p/101572175'

firefox_options = Options()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--headless')
driver = webdriver.Firefox(options=firefox_options)
driver.get(url)
time.sleep(2)

driver.quit()