import concurrent.futures
import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = []
save_files = open("C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Mwcomponents.com/data/mauldin.csv", "a+", encoding="utf-8")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}


def GetSoupUrl(urls):
    ress = requests.get(urls)
    soup = BeautifulSoup(ress.content, "lxml")
    return soup


def Product_Details(urls, soup):
    print("Product-url---: ", urls)
    try:
        catlvl1 = ''
        catlvl2 = ''
        catlvl3 = ''
        l3_name_l3 = ''
        try:
            l3_name_l3 = []
            for l3 in soup.find_all(class_="breadcrumbs")[1].find_all('li'):
                l3_name_l3.append(l3.text.strip())
            l3_name = "## ".join(l3_name_l3)
            print('l3_name.....', l3_name)
        except AttributeError:
            l3_name = 'N/A'
            print('l3_name.....', l3_name)

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

        # --------------------------------------------------------------------------------------------------------------
        try:
            product_title = soup.find("h1", {"class": "hd-md mb-24"}).text.strip()
            print('product_title.....', product_title)
        except AttributeError:
            product_title = ''
            print('product_title.....', product_title)
        # --------------------------------------------------- MPN ------------------------------------------------------
        try:
            part_number = soup.find('div', {"class": "py-12 whitespace-nowrap"}).text.strip()
            mpn = part_number
            print('mpn.....', mpn)
        except AttributeError:
            mpn = 'N/A'
            print('mpn.....', mpn)


        # -------------------------------------------------- Price-- ---------------------------------------------------
        try:
            price_details = soup.find("div", {"data-controller": "input-float-label"}).find('input')['value']
            price = {"Price": price_details}
            print('price.....', price)
        except (AttributeError, TypeError):
            price = {'Price': '$-.--'}
            print('price.....', price)

        # -------------------------------------------------- Shipping - Weight -----------------------------------------

        # ---------------------------------------------- Description_1 -------------------------------------------------
        try:
            des = soup.find('section', {"id": "overview"}).find_next('p').text.strip()
            description_1 = {"desc": [des]}
            print('description_1.....', description_1)
        except IndexError:
            description_1 = {"desc": []}
            print('description_1.....', description_1)

        # ---------------------------------------------- Description_2 -------------------------------------------------
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

        # -------------------------------------------------- Images ----------------------------------------------------
        try:
            images = []
            for images_html in soup.find('div', {"data-controller": "product-specs"}).find_all('img'):
                if images_html:
                    image_src = images_html['src']
                    alt_tag = images_html.get('alt')
                    image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                    images.append(image_tag_and_alt_tag)
            print('images.....', images)
        except AttributeError:
            images = ''
            print('images.....', images)

        # --------------------------------------------------- Video ----------------------------------------------------
        try:
            video = []
            for video_details in soup.find(class_="embed-responsive embed-responsive-16by9").find_all('iframe'):
                video.append(video_details.get('src'))
            print('video.....', video)
        except (AttributeError, TypeError):
            video = []
            print('video.....', video)
        # ------------------------------------------------ Datasheet ---------------------------------------------------
        try:
            datasheet = []
            for pdf in soup.find(id="tab-description").find_all('iframe'):
                datasheet.append(pdf.get('data-src'))
            print('datasheet.....', datasheet)
        except (AttributeError, TypeError):
            datasheet = []
            print('datasheet.....', datasheet)

        # ------------------------------------------------- Realated ---------------------------------------------------
        try:
            related_url = []
            for href in soup.find_all(class_="space-y-24")[1].find_all('a'):
                resources = href.get('href')
                if "resources" in resources:
                    related_url.append(resources)
            realated = [{'accessories': related_url}]
            print("realated.....", realated)
        except AttributeError:
            realated = [{'accessories': []}]
            print("realated.....", realated)

        # --------------------------------------------------------------------------------------------------------------
        try:
            attr_name = []
            attr_value = []
            for th in soup.find_all('th', {"class": "font-normal"}):
                tab_1 = th.text.strip()
                attr_name.append(tab_1)

            for td in soup.find_all('td', {"class": "font-semibold"}):
                tab_2 = td.text.strip()
                attr_value.append(tab_2)
            specifications_1 = []
            for name, value in zip(attr_name, attr_value):
                specifications_1.append({name: value})
            print('specifications_1.....', specifications_1)
        except AttributeError:
            specifications_1 = []
            print('specifications_1.....', specifications_1)

        # ----------------------------------------------- Miscellaneous ------------------------------------------------
        try:
            cad_details = soup.find_all("div", {"data-controller": "modal-trigger"})[0].find_next('a')['href']
            download_cad = {"Download CAD": cad_details}
            # print('download_cad.....', download_cad)
        except (TypeError, IndexError, AttributeError):
            download_cad = ''
            print('cad_details.....', download_cad)

        miscellaneous = str(download_cad)
        print('miscellaneous.....', miscellaneous)

        # --------------------------------------------------------------------------------------------------------------

        list_column = [
            "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
            "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
            "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
            "scraped_by"
        ]
        raw_data = [{
            "brand": "MAUDLIN", "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": urls,
            "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": 'N/A',
            "breadscrumbs": l3_name, "image_urls": images, "mpn": mpn,
            "specification_1": specifications_1, "specification_2": [], "datasheets": datasheet,
            "product_description_1": description_1, "product_description_2": description_2,
            "accessories": realated, "video_links": [], "miscellaneous": miscellaneous,
            "scraped_by": "Pradeep Kumar",
        }]
        print('Complete all Your Program')
        print()
        Data_Save(raw_data, list_column)

    except Exception as e:
        print(f"Error....{e}")
        with open('remaining_url.txt', 'a+', encoding='utf-8') as remain:
            remain.write(f"{urls}\n")
        print('save remaining url')

# ----------------------------------------------------------------------------------------------------------------------


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


def ReadUrlFromList():
    file_path = "C:/Users/PK/Desktop/web-scrapping/A-MONTH-2024/March/Mwcomponents.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    # print(url_links)
    i = 0
    for url_count, url in enumerate(url_links[i:], start=i):
        urls.append(url)
        # print('product_url.....', url_count, url)

        # soup = GetSoupUrl(url)
        # Product_Details(url, soup)
    return urls


def main():
    url_1 = ReadUrlFromList()

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        try:
            executor.map(lambda url: Product_Details(url, GetSoupUrl(url)), url_1)
            print('---------------------------------------------------------------------------------------------------')
        except Exception as e:
            print(f"Error: {e}")
            print("Breaking the process due to error encountered.")
            raise RuntimeError("Error encountered. Program terminated.")


if __name__ == "__main__":
    main()
