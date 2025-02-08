import time
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--headless')
chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
driver = uc.Chrome(options=chrome_options)
driver.maximize_window()
url = 'https://www.madisonelectric.com/square-d-sqdqo1515'
driver.get(url)
time.sleep(8)
page_sources = driver.page_source
pk = BeautifulSoup(page_sources, 'lxml')

price1 = pk.select_one('span[data-select="priceData"]').text.strip()
print('----------------', price1)