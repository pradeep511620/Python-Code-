import time

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as gui

sess = requests.Session()


base_url = 'https://www.alcofilters.com/en-gb/home/'

product_urls = []
# product_url = open("alcoFilter_product_urls.csv", 'a', encoding='utf-8')
product_data = open("alcoFilter_product_data.csv", 'a', encoding='utf-8')


def pdf_print_using_selenium(url, title):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="TypeTabs"]/img')
    gui.hotkey('ctrl', 'p')
    time.sleep(2)
    for i in range(0, 5):
        gui.hotkey('tab')
    gui.press('down')
    gui.press("enter")
    for i in range(0, 5):
        gui.hotkey('tab')
    gui.press("enter")
    gui.press('backspace')
    time.sleep(5)
    gui.typewrite(title)
    time.sleep(5)
    gui.press("enter")
    time.sleep(5)


def request_func(url):
    """Send Requests and Get Response from webpage and return Soup"""
    res = sess.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    return soup


def urljoin_func(url):
    """function takes a relative url and convert it into absolute url and returns"""
    return urljoin(base_url, url)


def product_link(url):
    """find all the product links and save as csv file"""
    soup = request_func(url)
    product_links = soup.findAll(class_="fl-post-image")
    for link in product_links:
        product_urls.append(urljoin_func(link.find('a')['href']))
    # df = pd.DataFrame(product_urls)
    # df.to_csv(product_url, lineterminator='\n')


def product_details(url):
    """Get product details(Respective Product url, title, breadcrumb, item no, image url
    video url, pdf url, product details, product specifications) and call data save function(file as txt or csv)"""

    cols = ["url", "title", "bread_crumb", "images", "attr_name", "attr_value"]

    row = []

    soup = request_func(url)
    title = soup.h1.text.strip()
    bread_crumb = soup.find(id="ctl00_plcMain_TitleBreadCrumbs").text.replace('\n', '')
    # print("title >>> ", title)
    try:
        images = soup.find(class_="col-xs-12 col-md-4 col-lg-4").findAll('img')
        image_list = []
        for image in images:
            image_list.append(urljoin_func(image['src']))
        # print(image_list)

        pdf_list = []
        try:
            pdfs = soup.find(id="downloads-section").findAll('a')
            for pdf in pdfs:
                # print(pdf['href'])
                pdf_list.append(urljoin_func(pdf['href']))
            # print("pdf >>> ", pdf_list)
        except AttributeError:
            pass

        try:
            row.append({
                "url": url,
                "title": title,
                "bread_crumb": bread_crumb,
                "images": image_list,
            })
            """table_content = soup.find(class_='col-xs-12 col-md-8 col-lg-8')
            for item in table_content:
                for td in item.findAll('tr'):
                    td = td.text.split(":")
                    attr_name.append(td[0].replace('\xa0', ''))
                    try:
                        attr_value.append(td[1].strip().replace('\n', '').replace('\r', '').replace('*', ''))
                    except IndexError:
                        attr_value.append(" ")
            table_content = soup.find(class_='col-xs-12 col-md-12 col-lg-12')
            for item in table_content:
                for td in item.findAll('tr'):
                    td = td.text.split(":")
                    attr_name.append(td[0].replace('\xa0', ''))
                    try:
                        attr_value.append(td[1].strip().replace('\n', '').replace('\r', '').replace('*', '').replace('\xa0', ''))
                    except IndexError:
                        attr_value.append("")"""
            df = pd.read_html(url)
            title_df = pd.DataFrame(row)
            df1 = pd.concat([df[1], df[2]], axis=0, join='inner').reset_index()
            if len(df) > 3:
                try:
                    df[4][2] = df[4][2].apply(lambda x: f"rp_{x}")
                    df_merge = pd.concat(
                        [title_df, df1.drop('index', axis=1), df[3].drop([0], axis=1), df[4].drop([0], axis=1)], axis=1)
                    df_merge = df_merge.ffill(axis=0)
                    # print(df_merge)
                    df_merge.to_csv(product_data, header=False, index=False, lineterminator='\n')
                    pdf_print_using_selenium(url, title)
                except IndexError:
                    df[3][2] = df[3][2].apply(lambda x: f"rp_{x}")
                    df2 = pd.DataFrame(columns=["Manufacturer", "Model", "Motor", "From - To Date"])
                    df_merge = pd.concat([title_df, df1.drop('index', axis=1), df2, df[3].drop([0], axis=1)], axis=1)
                    df_merge = df_merge.ffill(axis=0)
                    # print(df_merge)
                    df_merge.to_csv(product_data, header=False, index=False, lineterminator='\n')
                    pdf_print_using_selenium(url, title)
            else:
                df_merge = pd.concat([title_df, df1.drop('index', axis=1)], axis=1)
                df_merge = df_merge.ffill(axis=0)
                df_merge.to_csv(product_data, header=False, index=False, lineterminator='\n')
                pdf_print_using_selenium(url, title)

        except AttributeError:
            pass
    except AttributeError:
        pass


def main():
    i = 2192
    product_url = "https://www.alcofilters.com/en-gb/catalogue/filter/?filterId="
    """using i indexing product url default i value is 0"""
    for link in range(i, 4460):
        url = f'{product_url}{link}'
        print(i, ">>>>>>>>>>>>>", url)
        product_details(url)
        i += 1


main()

"""Testing Calls"""
# product_details('https://www.alcofilters.com/en-gb/catalogue/filter/?filterId=2')
# print(len(product_urls))

