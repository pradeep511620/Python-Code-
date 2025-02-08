from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures
import requests


urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Klingspor.com/data/Klingspor.csv", "a+", encoding="utf-8")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


def GetSoupUrl(urls):
    ress = requests.get(urls)
    soup = BeautifulSoup(ress.content, "lxml")
    return soup


def Product_Details(urls, soup):
    print("Product-url---: ", urls)


    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find("span", {"id": "ctl00_CustomerMainContent_lbltitle"}).text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = 'N/A'
        print('product_title.....', product_title)

    # --------------------------------------------------- MPN ----------------------------------------------------------
    try:
        part_number = soup.find('span', {"id": "ctl00_CustomerMainContent_lblProductAliasId"}).text.strip()
        mpn = part_number
        print('mpn.....', mpn)
    except AttributeError:
        mpn = 'N/A'
        print('mpn.....', mpn)

    try:
        cate_details = soup.find(class_="posted_in").text.strip().split(': ')[1]
        category = {"category": cate_details}
        print('category.....', category)
    except AttributeError:
        category = []
        print('category.....', category)

    # -------------------------------------------------- Price-- -------------------------------------------------------
    price_login_details = soup.find('li', {'id': "ctl00_CustomerMainContent_div_lnk_login"}).text.strip()
    try:
        price_details = soup.find("span", {"id": "ctl00_CustomerMainContent_lblBasePrice"}).text.strip()
        price = {"List_price": price_details, 'price_login': [price_login_details]}
        print('price.....', price)
    except AttributeError:
        price = {'List_price': '$-.--'}
        print('price.....', price)
    # -------------------------------------------------- Shipping - Weight ---------------------------------------------

    # ---------------------------------------------- Description_1 -----------------------------------------------------
    short_description = ''
    for short in soup.find(class_="tab-content").find_all('span'):
        if "Short Description" in short.text.strip():
            short_description = short.find_next(class_="tabText").text.strip()

    description_1 = []
    for des in soup.find(class_="tab-content").find_all('span'):
        if "Product Details" in des.text.strip():
            texts = des.find_next(class_="tabText").find('p').text.strip()
            if texts:
                description_1.append(texts)
    description_1 = {"desc": description_1, 'short-desc': short_description}
    print(description_1)

    # ---------------------------------------------- Description_2 -----------------------------------------------------
    try:
        description_2 = []
        for des_1 in soup.find(id="tab-description").find('ol').find_all('li'):
            text_1 = des_1.text.strip()
            if text_1:
                description_2.append(text_1)
        print('description_2.....', description_2)
    except AttributeError:
        description_2 = []
        print('description_2.....', description_2)

    # -------------------------------------------------- Images --------------------------------------------------------
    try:
        images = []
        for images_html in soup.find_all('img', {"id": "ctl00_CustomerMainContent_Image1"}):
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
    except AttributeError:
        video = []
        print('video.....', video)
    # ------------------------------------------------ Datasheet -------------------------------------------------------
    try:
        datasheet = []
        for pdf in soup.find(id="tab-description").find_all('iframe'):
            datasheet.append(pdf.get('data-src'))
        print('datasheet.....', datasheet)
    except AttributeError:
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
        specifications_1 = []
        for specs in soup.find(class_="tab-content").find_all('span'):
            if "Specifications" in specs.text.strip():
                Specifications = specs.find_all_next(class_="tabText")
                for index, spec in enumerate(Specifications):
                    if index != 1:
                        spec_list = spec.get_text(separator='\n').strip().split('\n')
                        spec_dict = {}
                        for item in spec_list:
                            parts = item.split(':')
                            if len(parts) == 2:
                                key = parts[0].strip()
                                value = parts[1].strip()
                            else:
                                key = item.strip()
                                value = ''
                            spec_dict[key] = value
                            specifications_1 = [spec_dict]

        print('specifications_1.....', specifications_1)
    except AttributeError:
        specifications_1 = []
        print('specifications_1.....', specifications_1)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        specifications_2 = []
        for specs_2 in soup.find(class_='tablepress-1'):
            specifications_2.append(specs_2.text.strip())
        print('specifications_2.....', specifications_2)
    except (TypeError, AttributeError):
        specifications_2 = []
        print('specifications_2.....', specifications_2)

    # ----------------------------------------------- Miscellaneous ----------------------------------------------------
    try:
        measurement_details = soup.find_all(class_="tabText")[5].text.strip()
        measurement = {'Unit of Measurement': measurement_details}
    except IndexError:
        measurement = ''
        pass
    try:
        order_details = soup.find_all(class_="tabText")[3].text.strip().split('of ')[-1]
        order = {'Order in Quantities of': order_details}
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
        "brand": "Klingspor", "catlvl1": 'N/A', "catlvl2": 'N/A', "catlvl3": 'N/A', "url": urls,
        "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": 'N/A',
        "breadscrumbs": 'N/A', "image_urls": images, "mpn": mpn,
        "specification_1": specifications_1, "specification_2": specifications_2, "datasheets": datasheet,
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
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Klingspor.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 16712
    for url_count, url in enumerate(url_links[i:], start=i):
        urls.append(url)
        # print(url)

        # soup = GetSoupUrl(url)
        # Product_Details(url, soup)
    return urls


def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(lambda url: Product_Details(url, GetSoupUrl(url)), url_1)
        print('*******************************************************************************************************')


if __name__ == "__main__":
    main()
