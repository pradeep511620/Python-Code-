import requests
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures

urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Sunextool.com/data/sunextool.csv", "a+",
                  encoding="utf-8")


def GetSoupUrl(urls):
    ress = requests.get(urls)
    soup = BeautifulSoup(ress.content, "html.parser")
    return soup


def Product_Details(urls, soup):
    print("Product-url---: ", urls)
    # try:
    catlvl1 = ''
    catlvl2 = ''
    try:
        l3_name = []
        for bread in soup.find_all("p", {"id": "breadcrumbs"}):
            l3_name.append(bread.text.strip().replace(" > ", "## "))
        # l3_names = "## ".join(l3_name)
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = 'N/A'
        print('l3_name.....', l3_name)

    if l3_name:
        try:
            catlvl1 = l3_name[0].split("## ")[1]
            print("catlvl1...[1]:", catlvl1)
        except IndexError:
            print("Element [1]: Index out of range")
        try:
            catlvl2 = l3_name[0].split("## ")[2]
            print("catlvl2...[2]:", catlvl2)
        except IndexError:
            print("Element [2]: Index out of range")

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find("h1", {"class": "product_title"}).text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = 'N/A'
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        part_number = []
        for table in soup.find(class_="shop_attributes").find_all(class_="alt"):
            part = table.text.strip()
            if "Part Number" in part:
                part_number.append(part.replace("\n", ">>").split(">>")[1])
        mpn = part_number
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
        price = "{'List_price': '$-.--',}"
        print('price.....', price)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        description_1 = []
        for des in soup.find(itemprop="description").find_all('li'):
            description_1.append(des.text.strip())
        description_1 = {"desc": description_1}
        print('description.....', description_1)
    except AttributeError:
        description_1 = []
        print('description.....', description_1)


    # ------------------------------------------------------------------------------------------------------------------
    try:
        images = []
        for images_html in soup.find(class_="col-lg-5 col-md-5 col-sm-12 col-xs-12").find_all('img'):
            if images_html:
                image_src = images_html['src']
                alt_tag = images_html.get('alt')
                image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                images.append(image_tag_and_alt_tag)
        print('images.....', images)
    except AttributeError:
        images = ''
        print('images.....', images)

    try:
        datasheet = []
        for pdf in soup.find(class_="download-product-files").find_all('a'):
            datasheet.append(pdf.get('href'))
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = []
        print('datasheet.....', datasheet)

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
        attr_name = []
        attr_value = []
        for th in soup.find('table', {'class': 'shop_attributes'}).find_all('th'):
            tab1 = th.text.strip()
            attr_name.append(tab1)
        for td in soup.find('table', {'class': 'shop_attributes'}).find_all('td'):
            tab2 = td.text.strip()
            attr_value.append(tab2)

        specifications_1 = []
        for name, value in zip(attr_name, attr_value):
            specifications_1.append({name: value})
        print("specifications_1.....", specifications_1)
    except AttributeError:
        specifications_1 = []


    # ------------------------------------------------------------------------------------------------------------------
    list_column = [
        "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
        "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
        "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
        "scraped_by"
    ]
    raw_data = [{
        "brand": "Sunex Tools", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": "N/A", "url": urls,
        "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": "N/A",
        "breadscrumbs": l3_name, "image_urls": images, "mpn": mpn,
        "specification_1": specifications_1, "specification_2": [], "datasheets": datasheet,
        "product_description_1": "N/A", "product_description_2": [],
        "accessories": realated_url, "video_links": [], "miscellaneous": "N/A",
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
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Sunextool.com/url/Product-url.csv"
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=9) as executor:
        executor.map(lambda url: Product_Details(url, GetSoupUrl(url)), url_1)
        print('*******************************************************************************************************')


if __name__ == "__main__":
    main()
