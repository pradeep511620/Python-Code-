# import time
# import pyautogui as gui
# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
# mylist = [
#
#     # 'https://handle-it.com/collections/cages-and-stillages/products/platform-truck-with-4-mesh-sides',
#


#
#
# def save_pdf(url):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(url)
#     time.sleep(2)
#     title = driver.find_element(By.XPATH, "//h1[@class='product-single__title header-flavour']").text.replace('|', "_").replace('/', '')
#     titles = title + "-"
#     print("Title...", titles)
#     time.sleep(2)
#     s = driver.find_element(By.XPATH, "//*[@id='specification']/div[2]")
#     driver.execute_script("arguments[0].scrollIntoView();", s)
#
#     gui.hotkey('tab')
#     gui.hotkey('up')
#     gui.hotkey('enter')
#     time.sleep(2)
#     gui.hotkey('tab')
#     for i in range(0, 4):
#         gui.hotkey('tab')
#     gui.press('down')
#     gui.press("enter")
#     time.sleep(2)
#     for i in range(0, 5):
#         gui.hotkey('tab')
#     gui.press("enter")
#     time.sleep(2)
#     gui.press('backspace')
#     time.sleep(2)
#     gui.typewrite(titles)
#     time.sleep(3)
#     gui.press("enter")
#     time.sleep(1)
#     print('Download Successfully')
#     driver.quit()
#
#
# def main():
#     i = 0
#     for url in mylist:
#         i += 1
#         save_pdf(url)
#         print('Product-url...', i, url)
#
#
# main()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()

mylist = [
    # "https://www.grainger.com/product/DDS-Rotary-Shaft-Seal-2-Lip-w-52WD96"
    "https://www.grainger.com/product/52WE02"
    # 'https://www.grainger.com/product/457W93'
]

for url in mylist:
    driver.get(url)
    time.sleep(4)
    print(url)

    # click to box
    options = driver.find_element(By.CLASS_NAME, "YkO8lF")
    options.click()
    time.sleep(3)
    # find value of box
    li_options = options.find_element(By.XPATH, "//ul[@class='PkAjij']").find_elements(By.TAG_NAME, 'li')
    id_lst = []
    for li in li_options:
        option = li.get_attribute('data-testid')    # get value to unique id
        id_lst.append(option)
        print(option)

    q = 0
    for d in id_lst:
        q += 1
        if q != 1:
            options1 = driver.find_element(By.CLASS_NAME, "YkO8lF")
            options1.click()
        else:
            pass
        time.sleep(2)
        val_id = driver.find_element(By.XPATH,"//*[@data-testid='"+str(d)+"']")
        val_id.click()
        time.sleep(2)
