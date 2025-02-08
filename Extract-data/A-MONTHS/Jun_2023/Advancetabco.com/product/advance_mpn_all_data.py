import csv
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")

# browser = webdriver.Firefox()
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

url = 'https://advancetabco.com/'

browser.get(url)
print("Product_urls", url)
time.sleep(3)
with open("C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/Advancetabco.com/urls/watts_mpn.csv", 'r') as file:
    # with open("/var/www/html/webscr/source_dir/watts_mpn.csv", 'r') as file:
    csv_reader = csv.reader(file)
    csv_list = list(csv_reader)
    csv_length = len(csv_list)

for csv_link in range(0, csv_length):
    url = csv_list[csv_link][0].replace('ï»¿', '').replace('rp_', '')
    print("Product-Length...", csv_link)
    print("Urls......", url)

    browser.find_element(By.XPATH, "//input[@class='searchbox_inside form-control']").send_keys(url)
    time.sleep(1)

    browser.find_element(By.XPATH, "//input[@value='Product Search']").click()
    time.sleep(1)

    get_url = browser.current_url
    print('Current_urls...', get_url)

    try:
        model = browser.find_element(By.XPATH, "//div[@class='col-md-9']//h4[1]").text.strip()
        print("model..", model)
    except NoSuchElementException:
        model = ''
        print("Not Found")

    try:
        images = browser.find_element(By.XPATH, "//span[@data-toggle='modal']").find_element(By.TAG_NAME, 'img')
        image = images.get_attribute('src')
        print('Images...', image)
    except NoSuchElementException:
        image = ''
        print('Not Found')

    try:
        price = browser.find_element(By.XPATH, "//div[@class='col-md-9']//h4[2]").text.strip()
        print("price..", price)
        # save = open('C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/Advancetabco.com/data/watts_all_data.txt', 'a+', encoding='utf-8')
        # save = open('/var/www/html/webscr/destination_dir/watts_all_data.txt', 'a+',encoding='utf-8')
        # save.write('\n' + get_url + "\t" + model + "\t" + price + "\t" + image)
    except NoSuchElementException:
        price = ''
        print('Not Found')

    all_data1 = browser.find_elements(By.XPATH, "//div[@class='col-md-9']//p[1]")
    length = len(browser.find_elements(By.XPATH, "//div[@class='col-md-9']//p"))
    for l1 in range(0, length + 1):
        if l1 == 1:
            for all_data in all_data1:
                data = all_data.text.split('\n')
                try:
                    description = data[1]
                    print('descriptions...', description)
                    # save = open('C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/Advancetabco.com/data/watts_all_data.txt','a+', encoding='utf-8')
                    # save = open('/var/www/html/webscr/destination_dir/watts_all_data.txt', 'a+',encoding='utf-8')
                    # save.write('\n' + get_url + "\t" + model + "\t" + price + "\t" + image + "\t" + description)
                except AttributeError:
                    print('Not Found')
                try:
                    attr_name = []
                    attr_value = []
                    w1 = data[0].strip()
                    table1 = w1.split('  ')
                    for tab1 in table1:
                        tabs1 = tab1.split(': ')
                        attr_name.append(tabs1[0])
                        attr_value.append(tabs1[1])
                    for a1, b1 in zip(attr_name, attr_value):
                        print(a1, '....', b1)
                        # save = open('C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/Advancetabco.com/data/watts_all_data_table.txt', 'a+', encoding='utf-8')
                        # save = open('/var/www/html/webscr/destination_dir/watts_all_data_table.txt', 'a+',encoding='utf-8')
                        # save.write('\n' + get_url + "\t" + model + "\t" + a1 + "\t" + b1)
                except IndexError:
                    print('Index out of range')

                #
                try:
                    td = []
                    td1 = []
                    w = data[2].strip()
                    table = w.split('  ')
                    for tab in table:
                        tabs = tab.split(': ')
                        td.append(tabs[0])
                        td1.append(tabs[1])
                    for a, b in zip(td, td1):
                        print(a, '....', b)
                        # save = open('C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/Advancetabco.com/data/watts_all_data_table.txt', 'a+', encoding='utf-8')
                        # save = open('/var/www/html/webscr/destination_dir/watts_all_data_table.txt', 'a+',encoding='utf-8')
                        # save.write('\n' + get_url + "\t" + model + "\t" + a + "\t" + b)
                except IndexError:
                    print('Index out of range')

                break
