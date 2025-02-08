import pandas as pd
import requests
from bs4 import BeautifulSoup
# from tabulate import tabulate

from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/bakergauges.com/data/bakergauges-all-data.csv", 'a',
                  encoding='utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def Get_Soup_Url(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def Get_Driver_Urls(url):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(options=opts)
    # driver = webdriver.Firefox(options=opts)
    driver.maximize_window()
    driver.get(url)
    # time.sleep(3)
    return driver


def product_detail(url, soup):
    print('soup')

    try:
        l3_name = []
        bread = soup.find('div', {"class": "breadcrumb"}).find_all('li')
        for l3 in bread:
            cleaned_text = ' '.join(l3.text.strip().split())
            cleaned_text = cleaned_text.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
            l3_name.append(cleaned_text)
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_name = []
        breadcrumb_section = soup.find('section', {"class": "breadcrumb"})
        if breadcrumb_section:
            bread = breadcrumb_section.find_all('li')
            for l3 in bread:
                cleaned_text = ' '.join(l3.text.strip().split())
                cleaned_text = cleaned_text.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
                l3_name.append(cleaned_text)
            print('l3_name.....', l3_name)
        else:
            print("Breadcrumb section not found.")


    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find('section', class_="heading").h1.text.strip()
        product_title = product_title.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
        print('product_title.....', product_title)
    except AttributeError:
        product_title = 'Not Found'
        print('object has no attribute ... product_title')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        mpn = soup.find('span', {"class": "product_code"}).text.strip()
        print('mpn.....', mpn)
    except AttributeError:
        mpn = 'Not Found'
        print('Not Found')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        price = soup.find('span', {"itemprop": "price"}).text.strip()
        print('price.....', price)
    except AttributeError:
        price = 'Not Found'
        print('Not Found')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        features_1 = []
        for features in soup.find('div', {"class": "panes"}):
            features_1.append(features.text.replace('\n', '').replace('\t', '').replace('\r', ''))
        print('features_1.....', features_1)
    except AttributeError:
        features_1 = 'Not Found'
        print('object has no attribute ... features_1')
    except TypeError:
        features_1 = 'Not Found'
        print('object has no attribute ... features_1')

    # ------------------------------------------------------------------------------------------------------------------
    description = []
    try:
        for desc in soup.find('div', {"class": "panes"}).find_all('li'):
            description.append(desc.text.strip().replace("\n", ""))
        print('description.....', description)
    except TypeError:
        description = ''
        print('object is not iterable')
    except AttributeError:
        description = ''
        print('object is not iterable')


    # ------------------------------------------------------------------------------------------------------------------
    try:
        datasheet = []
        for pdf in soup.find('div', {"class": "doc_icons"}).find_all('a'):
            href_tag = pdf.get('href')
            datasheet.append(href_tag)
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = ''
        print('object has no attribute ... datasheet')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        part_accessories = []
        part_ass = soup.find('div', {"id": "tab-parts_tab"}).find_all('a')
        for accessories in part_ass:
            part_accessories.append(accessories.get("href"))
        print('part_accessories.....', part_accessories)
    except AttributeError:
        part_accessories = 'Not Found part_accessories'
        print('object has no attribute.......part_accessories')

    # ------------------------------------------------------------------------------------------------------------------
    try:
        zip_card = []
        card = soup.find('div', {"class": "cad-tab-links"}).find_all('a')
        for card_links in card:
            zip_card.append(card_links.get("href"))
        print('zip_card.....', zip_card)
    except AttributeError:
        zip_card = 'Not Found Zip Card'
        print('object has no attribute ... zip_card')

    # --------------------------------------  Images  ------------------------------------------------------------------
    try:
        image = []
        for img_1 in soup.find_all('section', {"class": "product_images"}):
            img_2 = img_1.find_all('img')
            for img2 in img_2:
                src = img2.get('src')
                image.append(src)

        while len(image) < 5:
            image.append('')

        print("Images....", image)
    except AttributeError:
        image = ['Images Not Found'] * 5
        print('object has no attribute ... image')

    # ----------------------------------------------- Video ------------------------------------------------------------
    try:
        video = []
        video_link = soup.find("div", {"class": "video_container"}).find_all('iframe')
        for video_href in video_link:
            video.append(video_href.get("src"))
        print('video.....', video)
    except AttributeError:
        video = ''
        print('object has no attribute ... video')

    # ------------------------------------------------------------------------------------------------------------------
    mylist = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]  # save data here

    row = [{
        "Mpn": mpn,
        # "Grainger_Sku": sku,
        "L3_Name": l3_name,
        "Product_title": product_title,
        "Image_URL_1": image[0],
        "Image_URL_2": image[1],
        "Image_URL_3": image[2],
        "Image_URL_4": image[3],
        "Image_URL_5": image[4],
        # "Image_Name": image_type,
        "Product_Detail": description,
        "Features": features_1,
        # "Accessories": href_type_exe,
        "Datasheet": datasheet,
        # "item_ID": item,
        # "Uses": uses_d,
        "Video_Url": video,
        # "Quantity": stock,
        "Price(usd)": price,
        "Kits/Components": part_accessories,
        "Cross_Reference": zip_card,
        "Url": url,

    }]  # save data here

    Data_Save(row, mylist)
    return product_title, mpn


def Data_Save(row, cols):
    # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def Get_Specs_Table(url, soup, product_title):
    print('Tables')

    try:
        table = soup.find('table', {"class": "tablepress"}).find('tbody').find_all('tr')
        for ttd in table:
            t = ttd.find_all('td')
            ss = []
            for dd in t:
                row = dd.text.strip().replace('\n', " ")
                ss.append(row)
            if ss:
                data_table = '\t'.join(ss)
                data_table = data_table.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
                print(data_table)
                save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/bakergauges.com/data/baker-specs.txt", 'a+', encoding='utf-8')
                # # save.write(f"{url}\t{product_title}\t{mpn}\t{data_table}\n")
                save.write(f"{url}\t{data_table}\n")
    except AttributeError:
        print('ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt')

    # try:
    #     count_i = 0
    #     attr_name = []
    #     attr_value = []
    #     table_details = soup.find_all('div', {"x-show": "tab === 'specs'"})
    #     for td in table_details:
    #         text = td.text.strip()
    #         lines = text.split('\n')
    #         table = [line.strip() for line in lines if line.strip()]
    #         for th in table:
    #             count_i += 1
    #             tab_table = th
    #             tab_table = tab_table.encode('latin-1', errors='ignore').decode('utf-8', errors='ignore')
    #             if count_i % 2 != 0:
    #                 attr_name.append(tab_table)
    #             else:
    #                 attr_value.append(f"{'rp_'}" + tab_table)
    #     for a, b in zip_longest(attr_name, attr_value):
    #         print(a, "..........", b)
    #         # save = open("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/airvice.com/data/airvice-specs.txt", 'a+', encoding='utf-8')
    #         # save.write(f"{url}\t{product_title}\t{mpn}\t{a}\t{b}\n")
    # except AttributeError:
    #     print('do not catch the data')





def main():
    url_link = pd.read_csv("C:/Users/PK/Desktop/web-scrapping/A-MONTHS/Oct-2023/bakergauges.com/url/bakergauges_product_url.csv")['URL']
    i = 111
    for url_count, url in enumerate(url_link[i:], start=i):
        print("Product-Length...", url_count)
        print("Product-Urls......", url)
        soup = Get_Soup_Url(url)
        product_title, mpn = product_detail(url, soup)
        # Get_Specs_Table(url, soup, product_title)

        # selenium calling here
        # driver = getDriveUrls(url)
        # product_title = product_detail(url, driver)
        # get_specs(url, driver, product_title)
    print('loop End')


if __name__ == "__main__":
    main()
