from selenium import webdriver
import time

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://web.whatsapp.com/')
print("Scan the QR code and then press enter")
# input()

# Replace 'Name' with the name of your contact or group
target = 'Shallu'

# Replace with the message you want to send
message = 'Your message here'
time.sleep(70)
# Locate the search bar and search for the target
print('search box')
search_box = driver.find_element(By.XPATH, "//div[@class='g0rxnol2 ln8gz9je lexical-rich-text-input']")
search_box.click()
search_box.send_keys(target)
time.sleep(2)
print('search box end')


# Select the target
selected_contact = driver.find_element(By. XPATH, f'//span[@title="{target}"]')
selected_contact.click()
time.sleep(2)

# Locate the message box and send the message
message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
message_box.send_keys(message)
message_box.send_keys(webdriver.common.keys.Keys.ENTER)

# Close the webdriver
driver.quit()
