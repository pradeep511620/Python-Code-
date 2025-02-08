import requests
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures

urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Promaxtool.com/data/Promaxtool.csv", "a+",
                  encoding="utf-8")


def GetSoupUrl(urls):
    ress = requests.get(urls)
    soup = BeautifulSoup(ress.content, "html.parser")
    return soup


def Product_Details(urls, soup):
    print("Product-url---: ", urls)
    # try:
    try:
        l3_name = []
        for bread in soup.find("div", {"class": "breadcrumbs noprint"}).find_all('a'):
            l3_name.append(bread.text.strip())
        l3_names = "## ".join(l3_name)
        print('l3_name.....', l3_names)
    except AttributeError:
        l3_names = 'N/A'
        print('l3_name.....', l3_names)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find("span", {"itemprop": "name"}).text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = 'N/A'
        print('product_title.....', product_title)

    try:
        mpn = soup.find("span", {"itemprop": "model"}).text.strip()
        print('mpn.....', mpn)
    except AttributeError:
        mpn = 'N/A'
        print('mpn.....', mpn)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find("div", {"id": "productsPrice_each"}).text.strip().split(":  ")[1]
        price = {"Price Each": price}
        print('price.....', price)
    except AttributeError:
        price = 'N/A'
        print('price.....', price)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    try:
        images = []
        for images_html in soup.find(id="rightImages").find_all('img'):
            if images_html:
                image_src = images_html['src']
                alt_tag = images_html.get('alt')
                image_tag_and_alt_tag = {"src": "https://www.promaxtools.com/" + image_src, "alt": alt_tag}
                images.append(image_tag_and_alt_tag)
        print('images.....', images)
    except AttributeError:
        images = ''
        print('images.....', images)

    # ------------------------------------------------------------------------------------------------------------------

    attr_name = []
    attr_value = []
    for table in soup.find('ul', {'class': 'product_info_filters'}).find_all('li'):
        tab = table.text.strip().split(': ')
        attr_name.append(tab[0])
        attr_value.append(tab[1])
    specifications_1 = []
    for name, value in zip(attr_name, attr_value):
        specifications_1.append({name: value})
    print("specifications_1.....", specifications_1)

    # ------------------------------------------------------------------------------------------------------------------
    list_column = [
        "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
        "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
        "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
        "scraped_by"
    ]
    raw_data = [{
        "brand": "ProMax", "catlvl1": "N/A", "catlvl2": "N/A", "catlvl3": "N/A", "url": urls,
        "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": "N/A", "breadscrumbs": l3_names,
        "image_urls": images, "mpn": mpn,
        "specification_1": specifications_1, "specification_2": [], "datasheets": [],
        "product_description_1": "N/A", "product_description_2": [],
        "accessories": [{'accessories': []}], "video_links": [], "miscellaneous": "N/A",
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
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Promaxtool.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path, encoding='latin1')['URL']
    i = 0
    for url_count, url in enumerate(url_links[i:], start=i):
        urls.append(url)
        # print(url)

        # soup = GetSoupUrl(url)
        # Product_Details(url, soup)
    return urls


def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(lambda url: Product_Details(url, GetSoupUrl(url)), url_1)
        print('*******************************************************************************************************')


if __name__ == "__main__":
    main()
