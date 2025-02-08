from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.headless = True
opts.add_argument(
    "--user-agent=" + "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")

driver = webdriver.Chrome()
driver.maximize_window()

mylist = pd.read_csv("C:/Users/PK/Documents/Ge.csv")['URL']
i = 14
for index, url in enumerate(mylist[i:15], start=i):

    driver.get(url)
    time.sleep(5)
    print('Product-url', index, url)

    total_height = driver.execute_script(
        "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    scroll_position = driver.execute_script(
        "return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")
    for i in range(int(scroll_position), int(total_height) - 800, 800):
        driver.execute_script("window.scrollBy(0, 900)", "")
        time.sleep(3)
        for product in driver.find_elements(By.XPATH, "//*[@class='IRCkOB I-gesu']//a"):
            url_link = product.get_attribute('href')
            print(url_link)
            with open("GE2.txt", 'a+', encoding="utf-8") as save_file:
                save_file.write('\n' + "'" + url_link + "',")

    while True:
        try:
            # Click the button to load more content
            button = driver.find_element(By.XPATH, "//div[@class='q2HlH8']//button")
            button.click()
            print("Button clicked.")
            time.sleep(4)  # Wait for the content to load

            # Scroll down the page to collect URLs
            total_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
            scroll_position = driver.execute_script("return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")
            for i in range(int(scroll_position), int(total_height) - 800, 800):
                driver.execute_script("window.scrollBy(0, 900)", "")
                time.sleep(3)
                for product in driver.find_elements(By.XPATH, "//*[@class='IRCkOB I-gesu']//a"):
                    url_link = product.get_attribute('href')
                    print(url_link)
                    with open("GE2.txt", 'a+', encoding="utf-8") as save_file:
                        save_file.write('\n' + "'" + url_link + "',")
        except Exception as e:
            print("Exception occurred:", e)
            print("No more content to load.")
            break

# Close the WebDriver
driver.quit()