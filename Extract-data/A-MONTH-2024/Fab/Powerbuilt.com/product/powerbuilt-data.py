import requests
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures

urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Powerbuilt.com/data/Powerbuilt.csv", "a+",
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
        for bread in soup.find("ol", {"class": "breadcrumb__list"}).find_all('li'):
            l3 = bread.text.strip()
            l3_name.append(l3)
        l3_names = "## ".join(l3_name)
        print('l3_name.....', l3_names)
    except AttributeError as e:
        l3_names = 'N/A'
        print('Error in l3_name:', e)
        print('l3_name.....', l3_names)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find("h1", {"class": "product-meta__title heading h3"}).text.strip()
        print('product_title.....', product_title)
    except AttributeError as e:
        product_title = 'N/A'
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        mpn = soup.find("span", {"class": "product-meta__sku-number"}).text.strip()
        print('mpn.....', mpn)
    except AttributeError:
        mpn = 'N/A'
        print('mpn.....', mpn)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find("span", {"class": "price price--large"}).text.strip().replace("Sale price", "")
        price = {"list_price": price}
        print('price.....', price)
    except AttributeError:
        price = 'N/A'
        print('price.....', price)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description_1 = []
        for des_2 in soup.find_all("div", {"class": "product-tabs__content"}):
            if "Description" in des_2.text.strip():
                des_3 = des_2.find_next(class_="product-tabs__tab-item-content rte")
                for dd in des_3:
                    description_1.append(dd.text.strip())
                description_1 = {"desc": description_1}
        print('description_1.....', description_1)
    except AttributeError:
        description_1 = 'N/A'
        print('description_1.....', description_1)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description_2 = []
        for des_2_des in soup.find(class_="product-form__text").find('ul').find_all('li'):
            description = des_2_des.text.strip()
            description_2.append(description)
        print('description_2.....', description_2)
    except AttributeError:
        description_2 = 'N/A'
        print('description_2.....', description_2)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        images = []
        for img_1 in soup.find_all("div", {"class": "product__media-image-wrapper aspect-ratio aspect-ratio--natural"}):
            for img_2 in img_1.find_all('img'):
                if img_2:
                    img_tag = img_2.get('src')
                    alt_tag = img_2.get('alt')
                    images_tag_alt_tag = {'src': img_tag.replace("//", ""), 'alt': alt_tag}
                    images.append(images_tag_alt_tag)
                else:
                    print('Not found images')
        print('images.....', images)
    except AttributeError:
        images = 'N/A'
        print('images.....', images)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        for pdf_1 in soup.find("div", {"class": "gc_productLiterature"}).find_all("a"):
            pdf_links = pdf_1.get('href')
            if ".pdf" in pdf_links:
                datasheet.append("https://www.janesvilletool.com" + pdf_links)
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = []
        print('datasheet.....', datasheet)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        video = soup.find('external-video', class_="video-wrapper").find('iframe').get('src')
        video_links = [video]
        print('video_link.....', video_links)
    except AttributeError:
        video_links = []
        print('video_link.....', video_links)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        relateds = []
        related_scroller = soup.find("div", class_="product-list__inner product-list__inner--scroller hide-scrollbar")
        if related_scroller:
            for related_url in related_scroller.find_all_next('a'):
                related_href = related_url.get('href')
                print(related_href)
                if related_href and "/P" in related_href:
                    relateds.append("https://www.janesvilletool.com" + related_href)
        print("relateds.....", relateds)
    except AttributeError as e:
        print("Error:", e)
        relateds = "N/A"
        print("relateds:", relateds)

    try:
        soldout = soup.find("product-payment-container", id="MainPaymentContainer").text.strip()
        soldout = {"Availability": soldout}
        print('soldout.....', soldout)
    except AttributeError:
        soldout = 'N/A'
        print('soldout.....', soldout)

    # ------------------------------------------------------------------------------------------------------------------

    # try:
    #     attr_name = []
    #     attr_value = []
    #     for th in soup.find('div', {"id": "Specs"}).find('tbody').find_all('th'):
    #         attr_name.append(th.text.strip())
    #     for td in soup.find('div', {"id": "Specs"}).find('tbody').find_all('td'):
    #         attr_value.append(td.text.strip())
    #
    #     specifications_1 = []
    #     for name, value in zip(attr_name, attr_value):
    #         specifications_1.append({name: value})
    #     print("specifications_1.....", specifications_1)
    # except AttributeError:
    #     specifications_1 = 'N/A'
    #     print('NNNNN')

    # ------------------------------------------------------------------------------------------------------------------
    list_column = [
        "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
        "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
        "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
        "scraped_by"
    ]
    raw_data = [{
        "brand": "POWERBUILT", "catlvl1": "N/A", "catlvl2": "N/A", "catlvl3": "N/A", "url": urls,
        "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": "N/A", "breadscrumbs": l3_names,
        "image_urls": images, "mpn": mpn,
        "specification_1": [], "specification_2": [], "datasheets": datasheet,
        "product_description_1": description_1, "product_description_2": description_2,
        "accessories": relateds, "video_links": video_links, "miscellaneous": soldout,
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
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/Fab/Powerbuilt.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    i = 0
    for url_count, url in enumerate(url_links[i:], start=i):
        urls.append(url)
        # print(url)

        # soup = GetSoupUrl(url)
        # Product_Details(url, soup)
    return urls


def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(lambda url: Product_Details(url, GetSoupUrl(url)), url_1)
        print('*******************************************************************************************************')


if __name__ == "__main__":
    main()
