import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/some_data/watts.com/data/watts-all-data.csv",
                  'a',
                  encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def Get_Page_Source(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(options=opts)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    page_source = driver.page_source
    soup1 = BeautifulSoup(page_source, "html.parser")
    return soup1


def Get_Soup_Url(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def Get_Driver_Urls(url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    return driver




def product_detail(url, soup):
    try:
        model_text = soup.find('h1', class_="page-title")
        model = model_text.text.strip() if model_text else "N/A"
        mpn = {"mpn": model}
        print('mpn.....', mpn)
    except AttributeError:
        mpn = "N/A"
        print('mpn.....1', mpn)

    # print(soup.prettify())
    # ------------------------------------------------------------------------------------------------------------------
    try:
        p_tags = []
        for des in soup.find("div", {"class": "product__info"}).find_all('p'):
            p_tag = des.text.strip().replace("\n", ">>>>>")
            p_tags.append(p_tag)
        p_tags_details = {"p_tags": p_tags}
        print('p_tags_details.....', p_tags_details)
    except AttributeError:
        p_tags_details = "N/A"
        print('p_tags.....', p_tags_details)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        li_tags = []
        for feature1 in soup.find_all("div", {"class": "product__additional-details"}):
            fea = feature1.text.strip()
            if "Features" in fea:
                li_tag = feature1.find_next('ul').text.strip().replace("\n", " >> ")
                li_tags.append(li_tag)
        li_tags_details = {"li_tags": li_tags}
        print('li_tags_details.....', li_tags_details)
    except AttributeError:
        li_tags_details = "N/A"
        print('li_tags.....', li_tags_details)

    # save_files.write(f"{url}\t{model}\t{p_tag_1}\n")



    # ------------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------




    # --------------------------------------------- Datasheet ----------------------------------------------------------
    try:
        datasheet = []
        for pdf_tag in soup.find('ul', class_="product-downloads").find_all('a'):
            pdf_links = pdf_tag.get('href')
            datasheet.append("https://www.watts.com/products" + pdf_links)
        pdf_details = {"pdf_tag": datasheet}
        print('pdf_details.....', pdf_details)
    except AttributeError:
        pdf_details = "N/A"
        print('pdf_details.....', pdf_details)

    # ----------------------------------------------- Video ------------------------------------------------------------


    # ------------------------------------------------ Url -------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------

    with open('watts.txt', 'a+', encoding="utf-8") as file:
        file.write("%s\t%s\t%s\t%s\t%s\n" % (url, mpn, p_tags_details, li_tags_details, pdf_details))


def main():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/some_data/watts.com/url/product_url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))
    i = 1742
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)
        soup = Get_Soup_Url(url)
        product_detail(url, soup)
        # Get_Specs_Table(url, soup, product_title)
        # Get_Specs_Table(url, soup)

        # selenium calling here
        # driver = Get_Driver_Urls(url)
        # product_detail(url, driver)
        # Get_Specs_Table(url, driver, product_title)



if __name__ == "__main__":
    main()
