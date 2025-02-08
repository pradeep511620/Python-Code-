import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# /var/www/html/webscr/destination_dir

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/some_data/tricocorp.com/data/tricocorp-all-data.csv",
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
        model = []
        for skus in soup.find("div", {"id": "spec-chart"}).find_all('tr'):
            tab = skus.text.strip()
            clean_data = [td.strip() for td in tab.replace("\n", ">>").split(">>") if td.strip()]
            model.append(clean_data[0])
        print(model)
    except AttributeError:
        model = "N/A"
        print('mpn.....1', model)


    # ------------------------------------------------------------------------------------------------------------------
    all_p_tags = []

    try:
        p_tag_1 = soup.find('div', {"class": "product-hero__col-1__inner__bottom"}).text.strip().replace("\n", ">>")
        all_p_tags.append(('description.....1', p_tag_1))
    except AttributeError:
        p_tag_1 = "N/A"
        all_p_tags.append(('description.....1', p_tag_1))

    try:
        p_tag_2 = []
        for feature in soup.find("dl", class_="additional-features__list").find_all('p'):
            features = feature.text.strip().replace("\n", ">>>>")
            p_tag_2.append(features)
        all_p_tags.append(('description.....2', p_tag_2))
    except AttributeError:
        p_tag_2 = "N/A"
        all_p_tags.append(('description.....3', p_tag_2))

    try:
        p_tag_3 = []
        for feature1 in soup.find("div", {"id": "features"}).find_all('p'):
            features1 = feature1.text.strip().replace("\n", ">>>>")
            p_tag_3.append(features1)
        all_p_tags.append(('description.....3', p_tag_3))
    except AttributeError:
        p_tag_3 = "N/A"
        all_p_tags.append(('description.....3', p_tag_3))

    save_files.write(f"{url}\t{model}\t{p_tag_1}\n")
    print(all_p_tags)
    with open('output.txt', 'a+', encoding="utf-8") as file:
        file.write("%s\t%s\t%s\n" % (url, model, all_p_tags))


        #



    # ------------------------------------------------------------------------------------------------------------------
    # all_P_TAG = []
    # for main_content in soup.find("main", {"id": "content"}).find_all('p'):
    #     ptag = main_content.text.strip().replace("\n", ">>>>>")
    #     all_P_TAG.append(ptag)
    # print(all_P_TAG)

    # ------------------------------------------------------------------------------------------------------------------
    # try:
    #     feature = []
    #     for feature_details in driver.find_elements(By.XPATH, "//div[@id='tab-description']//p"):
    #         p_tag = feature_details.text.strip().replace("\n", "")
    #         feature.append(p_tag)
    #     print('feature.....', feature)
    # except NoSuchElementException:
    #     feature = ["N/A"]
    #     print('feature.....', "N/A")



    # --------------------------------------------- Datasheet ----------------------------------------------------------
    # try:
    #     datasheet = []
    #     for pdf_link in driver.find_elements(By.XPATH, "//div[@id='tab-description']//a"):
    #         pdf_links = pdf_link.get_attribute('href')
    #         if ".pdf" in pdf_links:
    #             datasheet.append(pdf_links)
    #     print('datasheet.....', datasheet)
    # except AttributeError:
    #     datasheet = "N/A"
    #     print('datasheet.....', datasheet)

    # ----------------------------------------------- Video ------------------------------------------------------------


    # ------------------------------------------------ Url -------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------



def main():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/some_data/tricocorp.com/url/product_url.csv"
    url_link = pd.read_csv(file_path)['URL']
    print("total url :-----", len(url_link))
    i = 115
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
