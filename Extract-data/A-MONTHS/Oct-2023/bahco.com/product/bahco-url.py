import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
# from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--headless")
opts.add_argument("--no-sandbox")

browser = webdriver.Chrome()
# browser = webdriver.Firefox(options=opts)
browser.maximize_window()
"""
mylist = [
    'https://www.bahco.com/int_en/products/multipurpose-kits.html',
    # 'https://www.bahco.com/int_en/products/bandsaws-power-saws.html',
    # 'https://www.bahco.com/int_en/products/files.html',
    # 'https://www.bahco.com/int_en/products/wrenches.html',
    # 'https://www.bahco.com/int_en/products/sockets-ratchets.html',
    # 'https://www.bahco.com/int_en/products/torque-tools.html',
    # 'https://www.bahco.com/int_en/products/power-tool-accessories.html',
    # 'https://www.bahco.com/int_en/products/screwdrivers.html',
    # 'https://www.bahco.com/int_en/products/l-keys.html',
    # 'https://www.bahco.com/int_en/products/pliers.html',
    # 'https://www.bahco.com/int_en/products/pipe-wrenches-tubing-tools.html',
    # 'https://www.bahco.com/int_en/products/air-tools.html',
    # 'https://www.bahco.com/int_en/products/cordless-power-tools.html',
    # 'https://www.bahco.com/int_en/products/automotive-tools.html',
    # 'https://www.bahco.com/int_en/products/lighting-equipment.html',
    # 'https://www.bahco.com/int_en/products/inspection-tools.html',
    # 'https://www.bahco.com/int_en/products/extractors-pullers.html',
    # 'https://www.bahco.com/int_en/products/tool-storage-toolkits.html',
    # 'https://www.bahco.com/int_en/products/tools-at-height.html',
    # 'https://www.bahco.com/int_en/products/insulated-tools.html',
    # 'https://www.bahco.com/int_en/products/non-sparking-tools.html',
    # 'https://www.bahco.com/int_en/products/stainless-steel-tools.html',
    # 'https://www.bahco.com/int_en/products/tweezers-electronics-specialty-tools.html',
    # 'https://www.bahco.com/int_en/products/measuring-layout.html',
    # 'https://www.bahco.com/int_en/products/wall-tools.html',
    # 'https://www.bahco.com/int_en/products/hand-hacksaws.html',
    # 'https://www.bahco.com/int_en/products/handsaws.html',
    # 'https://www.bahco.com/int_en/products/wood-chisels.html',
    # 'https://www.bahco.com/int_en/products/scissors-knives.html',
    # 'https://www.bahco.com/int_en/products/clamps-vices.html',
    # 'https://www.bahco.com/int_en/products/hammers.html',
    # 'https://www.bahco.com/int_en/products/tree-felling-forestry-tools.html',
    # 'https://www.bahco.com/int_en/products/cold-chisels-punches.html',
    # 'https://www.bahco.com/int_en/products/pry-bars.html',
    # 'https://www.bahco.com/int_en/products/planting-cultivating-tools.html',
    # 'https://www.bahco.com/int_en/products/pruning-tools.html',
    # 'https://www.bahco.com/int_en/products/air-tools-outdoor.html',
    # 'https://www.bahco.com/int_en/products/battery-power-tools-outdoor.html',

]

for url in mylist:
    browser.get(url)
    print("Product_urls", url)
    time.sleep(2)
    for product in browser.find_elements(By.XPATH, "//ul[@class='category-list']//li//a"):
        product_link = product.get_attribute('href')
        print("'" + product_link + "',")
        # save = open('url111.txt', 'a+', encoding='utf-8')
        # save.write(f"{product_link}\n")
"""

# def send_email():
#     smtp_server = "smtp.gmail.com"
#     smtp_port = 587
#     sender_email = "pk511620@@gmail.com"
#     smtp_username = "pk.s7723337@gmail.com"
#     smtp_password = "Google@#123"
#
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = smtp_username
#     message["Subject"] = "Script Execution Completed"
#
#     body = "Your web scraping script has completed running."
#     message.attach(MIMEText(body, "plain"))
#
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()
#         server.login(sender_email, smtp_password)
#         text = message.as_string()
#         server.sendmail(sender_email, smtp_username, text)
# send_email()


url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/bahco.com/url/bahco-sub-product_url.csv")['URL']
url_length = 25
for url_count, url in enumerate(url_link[url_length:26], start=url_length):
    browser.get(url)
    time.sleep(1)
    print("Product-Urls......", url)

    # total_height = browser.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    # scroll_position = browser.execute_script("return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")
    # print("Total height of scrollable area:", total_height)
    # for i in range(scroll_position, total_height - 900, 900):
    #     browser.execute_script("window.scrollBy(0, 900)", "")
    #     time.sleep(3)
    #     print(i)

    for product in browser.find_elements(By.XPATH, "//div[@class='products wrapper grid products-grid']//a"):
        product_link = product.get_attribute('href')
        if product_link is not None:
            print(product_link)
        #     save = open('url.txt', 'a+', encoding='utf-8')
        #     save.write(f"{product_link}\n")
