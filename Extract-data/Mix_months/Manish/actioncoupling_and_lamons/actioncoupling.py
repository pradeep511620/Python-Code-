import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as gui
import pandas as pd

sess = requests.Session()

base_url = 'http://www.actioncoupling.com/products'


"""files for url and data"""
# product_url = open("actionCoupling_product_urls.csv", 'a', encoding='utf-8')
product_data = open("actionCoupling_product_data.csv", 'a', encoding='utf-8')


def pdf_print_using_selenium(url, title):
    """save pages as pdf using selenium and pyautogui"""
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    """getting print button location"""
    driver.find_element(By.XPATH, '/html/body/div[2]/div/section/div/div/div/div/div/div[2]/div[1]/div[3]/div/a')
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


def extract_urls_recursive(url, visited=None):
    """
    Extracts all URLs from a webpage and any pages it links to, recursively.
    :param url: the URL of the starting page
    :param visited: a set of URLs that have already been visited
    :return: a set of all unique URLs found on the pages
    """
    if visited is None:
        visited = set()
    urls = set()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            product_links = soup.findAll(class_="sqs-block-button-container sqs-block-button-container--center")
            for link in product_links:
                next_url = urljoin_func(link.find('a')['href'])
                if next_url not in visited:
                    visited.add(next_url)
                    urls.add(next_url)
                    urls = urls.union(extract_urls_recursive(next_url, visited))
    except Exception as e:
        print(e)
    return urls


def product_link(url):
    """find all the product links and save as csv file"""
    soup = request_func(url)
    product_links = soup.findAll(class_="sqs-block-button-container sqs-block-button-container--center")
    for link in product_links:
        # print(urljoin_func(link.find('a')['href']))
        product_link(urljoin_func(link.find('a')['href']))
        print(urljoin_func(link.find('a')['href']))
        # product_urls.append(urljoin_func(link.find('a')['href']))


def product_details(url):
    """Get product details(Respective Product url, title, breadcrumb, item no, image url
    video url, pdf url, product details, product specifications) and call data save function(file as txt or csv)"""

    cols = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]

    row = []

    soup = request_func(url)
    content = soup.findAll(class_='col sqs-col-6 span-6')
    title = content[0].h1.text.strip()
    print("title >>> ", title)
    try:
        description = content[1].find(class_='sqs-block html-block sqs-block-html').text.replace('\n', ' ')
        print("description >>> ", description)
    except AttributeError:
        description = ''
    try:
        grainer_sku = soup.find(class_="image-caption").text.strip()
        print(grainer_sku)
    except AttributeError:
        grainer_sku = ''
    try:
        video_link = content[0].find('a')['href']
        print("Video >>>>>>>", video_link)
    except TypeError:
        video_link = ''
    images = soup.findAll(class_="image-block-wrapper")
    image_list = []
    for image in images:
        image_list.append(urljoin_func(image.find("img")['src']))
    print(image_list)

    pdf_list = []
    try:
        pdfs = soup.findAll(class_="sqs-block-button-container sqs-block-button-container--center")
        for pdf in pdfs:
            # print(pdf['href'])
            pdf_list.append(urljoin_func(pdf.find('a')['href']))
        print("pdf >>> ", pdf_list)
    except AttributeError:
        pass

    row.append({
        "Url": url,
        "Item_Name": title,
        "Grainger_Sku": grainer_sku,
        "Features": description.strip(),
        "Video_Url": video_link,
        "images": image_list,
        "Datasheet": pdf_list,
    })

    data_save(row, cols)

    """Download the page as pdf"""
    try:
        pdf_print = soup.find(class_='printfriendly').text
        # print(pdf_print)
        pdf_print_using_selenium(url, title)
    except AttributeError:
        pass


def data_save(row, cols):
    """function takes row and columns convert into dataframe and filter out and save data into the file"""
    df = pd.DataFrame(row, columns=cols)
    # df = df.explode(["images"])
    # df = df.explode(['pdfs'])
    # df = df.drop('index', axis=1)
    print(df)
    # df.to_csv(product_data, index=False, lineterminator='\n', header=False)
    df.to_csv("test.csv")


def main():
    """Main get the all urls and call product details one by one"""
    product_urls = extract_urls_recursive("http://www.actioncoupling.com/products")
    # df = pd.DataFrame(urlss)
    # df.to_csv(product_url, lineterminator='\n')
    i = 0
    """using i for indexing product url default i value is 0"""
    for url in product_urls[i:]:
        print(i, ">>>>>>>>>>>>>", url)
        product_details(url)
        i += 1


# main()

"""For testing only"""
# product_details('http://www.actioncoupling.com/the-green-machine')
# product_details('http://www.actioncoupling.com/ace-a-series-extruded-fire-hose-couplings')

