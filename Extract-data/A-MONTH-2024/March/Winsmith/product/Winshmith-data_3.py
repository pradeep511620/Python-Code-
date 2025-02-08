import time

import pandas as pd
import requests
from bs4 import BeautifulSoup
import concurrent.futures

urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Winsmith/data/Winsmith11.csv", "a+", encoding="utf-8")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


def GetSoupUrl(urls):
    ress = requests.get(urls)
    soup = BeautifulSoup(ress.content, "lxml")
    return soup


def Product_Details(urls, soup):
    print("Product-url---: ", urls)
    time.sleep(4)
    catlvl1 = ''
    catlvl2 = ''
    catlvl3 = ''

    try:
        l3_name_l3 = []
        for l3 in soup.find_all(itemprop="item"):
            l3_name_l3.append(l3.text.strip())
        l3_name = "## ".join(l3_name_l3)
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = 'N/A'
        print('l3_name.....', l3_name)
    #
    if l3_name_l3:
        try:
            catlvl1 = l3_name_l3[1]
            print('catlvl1.....', catlvl1)
        except IndexError:
            catlvl1 = ''
            print("Index 1 is out of range")

        try:
            catlvl2 = l3_name_l3[2]
            print('catlvl2.....', catlvl2)
        except IndexError:
            catlvl2 = ''
            print("Index 2 is out of range")

        try:
            catlvl3 = l3_name_l3[3]
            print('catlvl3.....', catlvl3)
        except IndexError:
            catlvl3 = ''
            print("Index 3 is out of range")

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find("h1", {"class": "product-card__title"}).text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = ''
        try:
            product_title = soup.find("div", {"class": "productDetail--info"}).find('h2').text.strip()
            print('product_title.....', product_title)
        except AttributeError:
            print("No product title found.")

    # --------------------------------------------------- MPN ----------------------------------------------------------
    try:
        part_number = soup.find('p', {"class": "modelNo"}).text.strip()
        mpn = part_number
        print('mpn.....', mpn)
    except AttributeError:
        mpn = 'N/A'
        print('mpn.....', mpn)


    # -------------------------------------------------- Price-- -------------------------------------------------------
    price_details = soup.find("p", {"class": "price"}).text.strip()
    price = {"List_price": price_details}
    print('price.....', price)
    # try:
    #     price_details = soup.find("p", {"class": "price"}).text.strip()
    #     price = {"List_price": price_details}
    #     print('price.....', price)
    #     price_found = True
    # except AttributeError:
    #     price = {'List_price': '$-.--'}
    #     print('price.....', price)

    # -------------------------------------------------- Shipping - Weight ---------------------------------------------

    # ---------------------------------------------- Description_1 -----------------------------------------------------
    try:
        des = soup.find_all(class_="rich-description")[0].text.strip()
        description_1 = {"desc": [des]}
        print('description_1.....', description_1)
    except IndexError:
        description_1 = {"desc": []}
        print('description_1.....', description_1)

    # ---------------------------------------------- Description_2 -----------------------------------------------------
    try:
        description_2 = []
        for des_1 in soup.find(id="tab-description").find('ol').find_all('li'):
            text_1 = des_1.text.strip()
            if text_1:
                description_2.append(text_1)
        print('description_2.....', description_2)
    except (AttributeError, TypeError):
        description_2 = []
        print('description_2.....', description_2)

    # -------------------------------------------------- Images --------------------------------------------------------
    try:
        images = []
        for images_html in soup.find('div', {"class": "productDetail--image"}).find_all('img'):
            if images_html:
                image_src = images_html['src']
                alt_tag = images_html.get('alt')
                image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                images.append(image_tag_and_alt_tag)
        print('images.....', images)
    except AttributeError:
        images = ''
        print('images.....', images)

    # --------------------------------------------------- Video --------------------------------------------------------
    try:
        video = []
        for video_details in soup.find(class_="embed-responsive embed-responsive-16by9").find_all('iframe'):
            video.append(video_details.get('src'))
        print('video.....', video)
    except (AttributeError, TypeError):
        video = []
        print('video.....', video)
    # ------------------------------------------------ Datasheet -------------------------------------------------------
    try:
        datasheet = []
        for pdf in soup.find(id="tab-description").find_all('iframe'):
            datasheet.append(pdf.get('data-src'))
        print('datasheet.....', datasheet)
    except (AttributeError, TypeError):
        datasheet = []
        print('datasheet.....', datasheet)

    # ------------------------------------------------- Realated -------------------------------------------------------
    try:
        realate_url = []
        for realated_href_tag in soup.find(class_="related products").find(class_="products columns-3").find_all('a'):
            realate_url.append(realated_href_tag.get('href'))
        realated_url = [{'accessories': realate_url}]
        print("realated.....", realated_url)
    except AttributeError:
        realated_url = [{'accessories': []}]
        print("realated.....", realated_url)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        attr_name_1 = []
        attr_value_1 = []
        specifications_1_1 = []
        table = soup.find(class_="o-grid-table")
        for key in table.find_all(class_="key"):
            attr_name_1.append(key.text.strip())
        for value in table.find_all(class_="value"):
            attr_value_1.append(value.text.strip())
        for name_1, value_1 in zip(attr_name_1, attr_value_1):
            specifications_1_1.append({name_1: value_1})
        # print('specifications_1_1.....', specifications_1_1)
    except AttributeError:
        specifications_1_1 = []
        print('specifications_1_1.....', specifications_1_1)

    try:
        attr_name = []
        attr_value = []
        for th in soup.find_all('div', {"class": "flex-table--head"}):
            tab_1 = th.text.strip()
            attr_name.append(tab_1)

        for td in soup.find_all('div', {"class": "flex-table--body"}):
            tab_2 = td.text.strip()
            attr_value.append(tab_2)
        specifications_1 = []
        for name, value in zip(attr_name, attr_value):
            specifications_1.append({name: value})
        # print('specifications_1.....', specifications_1)
    except AttributeError:
        specifications_1 = []
        print('specifications_1.....', specifications_1)

    specs = str(specifications_1_1) + ", " + str(specifications_1)
    print(specs)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        attr_name_3 = []
        attr_value_3 = []
        specifications_2 = []
        table_3 = soup.find(class_="description-table")
        for th_3 in table_3.find_all('th'):
            attr_name_3.append(th_3.text.strip())

        for td_3 in table_3.find_all('td'):
            attr_value_3.append(td_3.text.strip())
        for name_3, value_3 in zip(attr_name_3, attr_value_3):
            specifications_2.append(f"{name_3}:, {value_3}")
        print('specifications_2.....', specifications_2)
    except (AttributeError, TypeError):
        specifications_2 = []
        print('specifications_2.....', specifications_2)

    # ----------------------------------------------- Miscellaneous ----------------------------------------------------
    try:
        ship_in_details = soup.find("p", class_="muted reset").text.strip().split(": ")
        measurement = {ship_in_details[0]: ship_in_details[1]}
    except AttributeError:
        measurement = ''
        pass
    try:
        refund_details = soup.find_all("p", class_="u-margin-bottom")[1].text.strip().split(':')
        order = {refund_details[0]: refund_details[1]}
    except IndexError:
        order = ''
        pass

    miscellaneous = str(measurement) + " , " + str(order)
    print('miscellaneous.....', miscellaneous)

    # ------------------------------------------------------------------------------------------------------------------

    list_column = [
        "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
        "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
        "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
        "scraped_by"
    ]
    raw_data = [{
        "brand": "Winsmith", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": urls,
        "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": 'N/A',
        "breadscrumbs": l3_name, "image_urls": images, "mpn": mpn,
        "specification_1": specs, "specification_2": specifications_2, "datasheets": datasheet,
        "product_description_1": description_1, "product_description_2": description_2,
        "accessories": [{'accessories': []}], "video_links": [], "miscellaneous": miscellaneous,
        "scraped_by": "Pradeep Kumar",
    }]
    print('Complete all Your Program')
    print()
    Data_Save(raw_data, list_column)

# except Exception as e:
#     print(f"Error....{e}")
#     print("Breaking the process due to error encountered.")
#     return
# ------------------------------------------------------------------------------------------------------------------


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def ReadUrlFromList():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Winsmith/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 15000
    for url_count, url in enumerate(url_links[i:15200], start=i):
        urls.append(url)
        # print('product_url.....', url_count, url)

        # soup = GetSoupUrl(url)
        # Product_Details(url, soup)
    return urls


def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(lambda url: Product_Details(url, GetSoupUrl(url)), url_1)
        print('*******************************************************************************************************')


if __name__ == "__main__":
    main()
