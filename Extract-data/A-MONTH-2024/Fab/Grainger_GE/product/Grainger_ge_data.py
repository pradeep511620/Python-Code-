import time
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Grainger_GE/data/Grainger_GE_1.csv", "a+", encoding="utf-8")
base_url = 'https://www.grainger.com/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


def GetSoupUrl(urls):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'user-agent={headers["User-Agent"]}')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    try:
        driver.get(urls)
        time.sleep(2)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
    finally:
        driver.quit()

    return soup


def Product_Details(urls, soup):
    print("Product-url---: ", urls)
    try:
        catlvl2 = ''
        catlvl3 = ''
        catlvl1 = ''
        try:
            l3_name_l3 = []
            for l3 in soup.find('ul', {"data-testid": "breadcrumbs"}).find_all('li'):
                l3_name_l3.append(l3.text.strip())
            l3_name = "## ".join(l3_name_l3)
            print('l3_name.....', l3_name)
        except AttributeError:
            l3_name = 'N/A'
            print('l3_name.....', l3_name)


        if l3_name:
            try:
                catlvl1 = l3_name.split("## ")[2]
                print("catlvl1...[1]:", catlvl1)
            except IndexError:
                print("Element [1]: Index out of range")
            try:
                catlvl2 = l3_name.split("## ")[3]
                print("catlvl2...[2]:", catlvl2)
            except IndexError:
                print("Element [2]: Index out of range")
            try:
                catlvl3 = l3_name.split("## ")[4]
                print("catlvl3...[3]:", catlvl3)
            except IndexError:
                print("Element [3]: Index out of range")

        # ------------------------------------------------------------------------------------------------------------------
        try:
            product_title = soup.find("h1", {"class": "lypQpT"}).text.strip()
            print('product_title.....', product_title)
        except AttributeError:
            product_title = 'N/A'
            print('product_title.....', product_title)

        # --------------------------------------------------- MPN ----------------------------------------------------------
        try:
            part_number = soup.find('dd', {"class": "rOM8HV hRRBwT"}).text.strip()
            mpn = part_number
            print('mpn.....', mpn)
        except AttributeError:
            mpn = 'N/A'
            print('mpn.....', mpn)

        # -------------------------------------------------- Price-- -------------------------------------------------------
        try:
            price_details = soup.find("div", {"class": "rZErC5"}).text.strip()
            price = {"Web Price": price_details}
            print('price.....', price)
        except AttributeError:
            price = {'Web Price': '$-.--'}
            print('price.....', price)
        # -------------------------------------------------- Shipping - Weight ---------------------------------------------
        try:
            shipping_weight_details = soup.find('div', {"data-testid": "shipping-weight"}).find('strong').text.strip()
            shipping_weight = shipping_weight_details
            print('shipping_weight.....', shipping_weight)
        except AttributeError:
            shipping_weight = ''
            print('shipping_weight.....', shipping_weight)

        # ---------------------------------------------- Description_1 -----------------------------------------------------
        try:
            description_1 = []
            for des in soup.find('div', {"class": "W7BBCC"}).find_all('p'):
                description_1.append(des.text.strip())
            description_1 = {"desc": description_1}
            print('description_1.....', description_1)
        except AttributeError:
            description_1 = []
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -----------------------------------------------------
        try:
            description_2 = []
            for des in soup.find(itemprop="description").find_all('li'):
                description_2.append(des.text.strip())
            print('description2.....', description_2)
        except AttributeError:
            description_2 = []
            print('description2.....', description_2)

        # -------------------------------------------------- Images --------------------------------------------------------
        try:
            images = []
            for images_html in soup.find('div', {"data-testid": "product-gallery"}).find_all('img'):
                if images_html:
                    image_src = images_html['src']
                    alt_tag = images_html.get('alt')
                    image_tag_and_alt_tag = {"src": urljoin(base_url, image_src), "alt": alt_tag}
                    images.append(image_tag_and_alt_tag)
            print('images.....', images)
        except AttributeError:
            images = ''
            print('images.....', images)

        # ------------------------------------------------ Datasheet -------------------------------------------------------
        try:
            datasheet = []
            for pdf in soup.find_all("a", class_="I6Hnxa"):
                datasheet.append(urljoin(base_url, pdf.get('href')))
            print('datasheet.....', datasheet)
        except AttributeError:
            datasheet = []
            print('datasheet.....', datasheet)

        # ------------------------------------------------- Realated -------------------------------------------------------
        try:
            realate_url = []
            for realated_href_tag in soup.find('section', {"class": "d45Cza"}):
                if "Alternate Products" in realated_href_tag.text.strip():
                    for alternet_url in realated_href_tag.find_all_next('a'):
                        alt_name = alternet_url.get('href')
                        if "altItems" in alt_name:
                            realate_url.append(urljoin(base_url, alt_name))
            realated_url = [{'accessories': realate_url}]
            print("realated.....", realated_url)
        except (AttributeError, TypeError):
            realated_url = [{'accessories': []}]
            print("realated.....", realated_url)

        # ------------------------------------------------------------------------------------------------------------------
        try:
            attr_name = []
            attr_value = []
            table = soup.find('dl', {"data-testid": "product-techs"})
            for th in table.find_all('dt', {'class': 'dQCFHg bWbYay tJ26DT'}):
                tab1 = th.text.strip()
                attr_name.append(tab1)
            for td in table.find_all('dd', {'class': 'rOM8HV'}):
                tab2 = td.text.strip()
                attr_value.append(tab2)
            specifications_1 = []
            for name, value in zip(attr_name, attr_value):
                specifications_1.append({name: value})
            print("specifications_1.....", specifications_1)
        except (AttributeError, TypeError):
            specifications_1 = []

        # ----------------------------------------------- Miscellaneous ----------------------------------------------------
        try:
            cate_details = soup.find(class_="rOM8HV hRRBwT").text.strip()
            category = {"Item": cate_details}
            print('Item.....', category)
        except AttributeError:
            category = []
            print('Item.....', category)

        # ------------------------------------------------------------------------------------------------------------------
        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": "GRIANGER GENERAL ELECTRIC", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": urls,
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": shipping_weight,
            "breadscrumbs": l3_name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": [], "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": description_2,
            "accessories": realated_url, "video_links": [], "miscellaneous": category,
            "scraped_by": "Pradeep Kumar",
        }]
        print('Complete all Your Program')
        print()

        # Data_Save(raw_data, list_column)
    except Exception as e:
        print(f"Error....{e}")
        print("Breaking the process due to error encountered.")
        return
# ------------------------------------------------------------------------------------------------------------------


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def ReadUrlFromList():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Grainger_GE/url/Product-url - Copy.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 1
    for url_count, url in enumerate(url_links[i:1], start=i):
        urls.append(url)
        # print(url)

        # soup = GetSoupUrl(url)
        # Product_Details(url, soup)
    return urls


def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(lambda url: Product_Details(url, GetSoupUrl(url)), url_1)
        print('*******************************************************************************************************')


if __name__ == "__main__":
    main()
