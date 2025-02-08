from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import  pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
# Set headless mode
chrome_options.add_argument('--headless')

driver = webdriver.Chrome()
driver.maximize_window()

mylist = pd.read_csv("C:/Users/PK/Documents/Ge.csv")['URL']


c = 0
for url in mylist[c:1]:

    c = c + 1
    driver.get(url)
    time.sleep(5)
    print('Product-url', c, url)

    total_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    # Execute JavaScript to get the current scroll position in the window
    scroll_position = driver.execute_script("return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")
    # Print the total height and current scroll position
    # print("Total height of scrollable area:", total_height)
    for i in range(scroll_position, total_height - 800, 800):
        driver.execute_script("window.scrollBy(0, 900)", "")
        time.sleep(3)
        # print(i)
        # driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        for product in driver.find_elements(By.XPATH, "//*[@class='IRCkOB I-gesu']//a"):
            url_links = product.get_attribute('href')
            print(url_links)
            save = open("GE1.txt", 'a+', encoding="utf-8")
            save.write('\n' + "'" + url_links + "',")
        while True:
            try:
                driver.find_element(By.XPATH, "//div[@class='q2HlH8']//button").click()
                print("Button clicked.")
                time.sleep(4)
                total_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
                scroll_position = driver.execute_script("return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;")
                for i in range(scroll_position, total_height - 800, 800):
                    driver.execute_script("window.scrollBy(0, 900)", "")
                    time.sleep(3)
                    for product in driver.find_elements(By.XPATH, "//*[@class='IRCkOB I-gesu']//a"):
                        url_link = product.get_attribute('href')
                        print(url_link)
                        with open("GE1.txt", 'a+', encoding="utf-8") as save_file:
                            save_file.write('\n' + "'" + url_link + "',")
            except Exception as e:
                print("Exception occurred:", e)
                print("Button not clicked.")
                break


driver.quit()