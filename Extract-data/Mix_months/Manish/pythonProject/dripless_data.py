import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from urllib.parse import urljoin

# base_url = 'https://dripless.com/en/driplessecwidcom/#!/5-Gallon-Follow-Plate/p/192566188/category=0'

urls_list = [
'https://dripless.com/en/driplessecwidcom/#!/Big-Dawg/p/190212282/category=0',
 'https://dripless.com/en/driplessecwidcom/#!/15-oz-Bulk-Loader/p/190128568/category=0',
 'https://dripless.com/en/driplessecwidcom/#!/30-oz-Bulk-Loader/p/193785272/category=0',
 'https://dripless.com/en/driplessecwidcom/#!/5-Gallon-Follow-Plate/p/192566188/category=0',
 'https://dripless.com/en/driplessecwidcom/#!/ETS2000P/p/382626765/category=0',
 'https://dripless.com/en/driplessecwidcom/#!/ETS1100/p/173714951/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS1200/p/173714952/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS1300/p/173714953/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS1400/p/173714954/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS2000/p/173714955/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS3000/p/190619444/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS3000-385ml-version/p/192861728/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS5000-Quart/p/190622104/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS6000-Composite-Sausage-Gun/p/190630171/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS9000-High-Ratio/p/192546171/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS4000-400ml-Sausage-Gun/p/347932764/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/ETS2000P/p/382626765/category=44608161',
 'https://dripless.com/en/driplessecwidcom/#!/C150-DIY-Caulker/p/192582608/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/Chrome-Caulker/p/192861678/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/CH200/p/192578833/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/CR175-DIY-Ratchet-Caulker/p/192577841/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/CR200/p/192582626/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/Classic-Ratchet-Caulker/p/192863503/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/CR400-Quart/p/192578813/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/HR300-High-Ratio/p/192546580/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/High-Ratio-Quart/p/192547753/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/The-Brute/p/192578891/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/SH200/p/192577912/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/Mid-Range-Metal-10-oz/p/192577998/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/Mid-Range-Metal-Quart/p/192582785/category=49489621',
 'https://dripless.com/en/driplessecwidcom/#!/ETS4000-400ml-Sausage-Gun/p/347932764/category=48753066',
 'https://dripless.com/en/driplessecwidcom/#!/ETS6000-Composite-Sausage-Gun/p/190630171/category=48753066',
 'https://dripless.com/en/driplessecwidcom/#!/Economy-Metal-Sausage-Gun/p/192583258/category=48753066',
 'https://dripless.com/en/driplessecwidcom/#!/N03LW-Long-Wide-Nozzle-10-pack/p/129184576/category=48753066',
 'https://dripless.com/en/driplessecwidcom/#!/N03L-Long-Nozzle-10-pack/p/129184557/category=48753066',
 'https://dripless.com/en/driplessecwidcom/#!/N03-Thin-Nozzle-10-pack/p/127802998/category=48753066',
 'https://dripless.com/en/driplessecwidcom/#!/EZS-Easy-Switch-Push-Plate/p/191797695/category=48753066',
 'https://dripless.com/en/driplessecwidcom/#!/Dual-cartridge-measurements/p/192607526/category=48763063',
 'https://dripless.com/en/driplessecwidcom/#!/DC200L/p/191525420/category=48763063',
 'https://dripless.com/en/driplessecwidcom/#!/DC600/p/190197893/category=48763063',
 'https://dripless.com/en/driplessecwidcom/#!/DC900/p/191531121/category=48763063',
 'https://dripless.com/en/driplessecwidcom/#!/FG450/p/192565126/category=49357227',
 'https://dripless.com/en/driplessecwidcom/#!/Brass-tip/p/192868802/category=49357227',
 'https://dripless.com/en/driplessecwidcom/#!/15-oz-Bulk-Loader/p/190128568/category=48767035',
 'https://dripless.com/en/driplessecwidcom/#!/30-oz-Bulk-Loader/p/193785272/category=48767035',
 'https://dripless.com/en/driplessecwidcom/#!/N03-Thin-Nozzle-10-pack/p/127802998/category=48767035',
 'https://dripless.com/en/driplessecwidcom/#!/N03L-Long-Nozzle-10-pack/p/129184557/category=48767035',
 'https://dripless.com/en/driplessecwidcom/#!/N03LW-Long-Wide-Nozzle-10-pack/p/129184576/category=48767035',
 'https://dripless.com/en/driplessecwidcom/#!/5-Gallon-Follow-Plate/p/192566188/category=48767035',
 'https://dripless.com/en/driplessecwidcom/#!/One-Gallon-Follow-Plate/p/192616389/category=48767035',
 'https://dripless.com/en/driplessecwidcom/#!/Giant-Paint-Spatula/p/190630111/category=47597403',
 'https://dripless.com/en/driplessecwidcom/#!/Paint-Dawg/p/190216155/category=47597403',
 'https://dripless.com/en/driplessecwidcom/#!/Big-Dawg/p/190212282/category=47597403',
 'https://dripless.com/en/driplessecwidcom/#!/Paint-Grid/p/193608393/category=47597403',
 'https://dripless.com/en/driplessecwidcom/#!/Bulk-Loader-seal-and-seal-washer-assembly/p/190197366/category=47983658',
 'https://dripless.com/en/driplessecwidcom/#!/ETS4000-ETS6000-Nozzle-End-Cap/p/129184636/category=47983658',
 'https://dripless.com/en/driplessecwidcom/#!/Brass-tip/p/192868802/category=47983658',
 'https://dripless.com/en/driplessecwidcom/#!/Front-Cap-Ring-for-Bulk-Loaders/p/200109864/category=47983658',
 'https://dripless.com/en/driplessecwidcom/#!/ETS4000-ETS6000-Rear-Cap-Ring/p/200124918/category=47983658']

data_file = open('dripless_data.csv', 'a', encoding='utf-8')


def driver_call(base_url):
    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(6)
    # source_code = driver.page_source
    # print(source_code)

    row_data = []
    name = driver.find_element(By.XPATH, '//*[@id="my-store-2442022"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/h1').text
    try:
        upc = driver.find_element(By.XPATH, '//*[@id="my-store-2442022"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/span[2]').text
    except NoSuchElementException:
        upc = 'upc not available'
    try:
        description = driver.find_element(By.ID, 'productDescription').text
    except NoSuchElementException:
        description = 'Description Not available'
    pic = driver.find_element(By.XPATH, '//*[@id="my-store-2442022"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[3]')
    pictures = pic.find_elements(By.TAG_NAME, 'img')
    image_link = []
    for pictures_link in pictures:
        image_link.append(pictures_link.get_attribute('src'))
    # print(image_link)
    # primary_img = driver.find_element(By.XPATH, '//*[@id="my-store-2442022"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div/img')
    # print(primary_img.get_attribute('src'))
    # secondary_img = driver.find_element(By.XPATH, '//*[@id="my-store-2442022"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[3]/div[2]/div[2]/div/img')
    # print(secondary_img.get_attribute('src'))

    quantity = driver.find_element(By.XPATH, '//*[@id="my-store-2442022"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div[2]/div[1]/div').text
    price = driver.find_element(By.XPATH, '//*[@id="my-store-2442022"]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]').text
    try:
        ifram = driver.find_element(By.XPATH, '//*[@id="productDescription"]/div/p[6]/iframe')
        video_link = ifram.get_attribute('src')
    except NoSuchElementException:
        video_link = 'No Video Available'

    driver.close()

    row_data.append({
        "product_url": base_url,
        "product_name": name,
        "product_upc": upc,
        "product_description": description,
        "image_links": image_link,
        "product_quantity": quantity,
        "product_price": price,
        "video_link": video_link
    })

    print(row_data)
    df = pd.DataFrame(row_data)
    df.to_csv(data_file, lineterminator='\n', header=False, index=False)


# driver_call(base_url)


def main():
    x = 31
    for x, base_url in enumerate(urls_list[x:], x):
        driver_call(base_url)
        print("========", x)


main()
