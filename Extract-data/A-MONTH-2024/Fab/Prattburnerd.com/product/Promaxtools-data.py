import requests
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures

urls = []
save_files = open("D:/Web-Scrapping/A-MONTH-2024/Fab/Promaxtool.com/data/data.csv", "a+",encoding="utf-8")


def GetSoupUrl(urls):
    ress = requests.get(urls)
    soup = BeautifulSoup(ress.content, "html.parser")
    return soup


def Product_Details(urls, soup):
    print("Product-url---: ", urls)
    # try:
    try:
        l3_name = []
        for bread in soup.find("span", {"typeof": "BreadcrumbList"}).find_all('span'):
            l3 = bread.text.strip()
            if l3 != '$' and l3 != '':
                l3_name.append(l3)
        seen = set()
        unique_list = []
        for item in l3_name:
            if item not in seen:
                unique_list.append(item)
                seen.add(item)
        l3_names = "## ".join(unique_list)
        print('l3_name.....', l3_names)
    except AttributeError as e:
        l3_names = 'N/A'
        print('l3_name.....', l3_names)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.select(".et_pb_text_inner")[1].text.strip()
        print('product_title.....', product_title)
    except IndexError as e:
        product_title = 'N/A'
        print('product_title.....', product_title)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        country = soup.find('h3').text.strip()
        country = {"country": country}
        print('country.....', country)
    except AttributeError:
        country = ''
        print('country.....', country)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    try:
        images = []
        for images_html in soup.find(class_="et_pb_module et_pb_image et_pb_image_0_tb_body").find_all('img'):
            if images_html:
                image_src = images_html['src']
                alt_tag = images_html.get('title')
                image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                images.append(image_tag_and_alt_tag)
        print('images.....', images)
    except AttributeError:
        images = ''
        print('images.....', images)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_size_html = soup.find(class_="product-size").text.strip()
        description_1 = {'short_desc': [product_size_html]}
        print('description_1.....', description_1)
    except AttributeError:
        description_1 = ''
        print('description_1.....', description_1)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        description_2 = []
        for des_html in soup.select("div.et_pb_module.et_pb_post_content.et_pb_post_content_0_tb_body ul li"):
            description_2.append(des_html.text.strip())
        print('description_2.....', description_2)
    except AttributeError:
        description_2 = ''
        print('description_2.....', description_2)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    specifications_1 = []
    for table in soup.find_all(class_="tablepress"):
        try:
            if "Model No.*" in table.text.strip() or "Part No." in table.text.strip() or "Part Number" in table.text.strip():
                first_row_elements = [element.text.strip() for element in
                                      table.find('tbody').find_all('tr')[0].find_all('td')]
                second_row_elements = [element.text.strip() for element in
                                       table.find('tbody').find_all('tr')[1].find_all('td')]
                third_row_elements = [header.text.strip() for header in
                                      soup.find(class_='tablepress').find('thead').find('tr').find_all('th')]
                fourth_row_elements = [element.text.strip() for element in
                                       table.find('tbody').find_all('tr')[0].find_all('td')]

                if "Part No." in first_row_elements:
                    for row in soup.find(class_='tablepress').find("tbody").find_all('tr')[1:-1]:
                        td = [td_row.text.strip() for td_row in row.find_all("td")]
                        for value, key_header in enumerate(first_row_elements):
                            if value < len(td):
                                specifications_1.append({key_header: td[value]})

                elif "Part No." in second_row_elements:
                    for row in soup.find(class_='tablepress').find("tbody").find_all('tr')[2:-1]:
                        td = [td_row.text.strip() for td_row in row.find_all("td")]
                        for value, key_header in enumerate(second_row_elements):
                            if value < len(td):
                                specifications_1.append({key_header: td[value]})

                elif "Model No.*" in third_row_elements:
                    for row in soup.find(class_='tablepress').find("tbody").find_all('tr')[1:-1]:
                        td = [td_row.text.strip() for td_row in row.find_all("td")]
                        for value, key_header in enumerate(third_row_elements):
                            if value < len(td):
                                specifications_1.append({key_header: td[value]})

                elif "Part Number" in fourth_row_elements:
                    for row in soup.find(class_='tablepress').find("tbody").find_all('tr')[2:-1]:
                        td = [td_row.text.strip() for td_row in row.find_all("td")]
                        for value, key_header in enumerate(fourth_row_elements):
                            if value < len(td):
                                specifications_1.append({key_header: td[value]})

        except Exception as e:
            print('An Error....', e)

        print("specifications.....", specifications_1)

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


    # ------------------------------------------------------------------------------------------------------------------
    list_column = [
        "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
        "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
        "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
        "scraped_by"
    ]
    raw_data = [{
        "brand": "Pratt Burnerd America", "catlvl1": "N/A", "catlvl2": "N/A", "catlvl3": "N/A", "url": urls,
        "title": product_title, "price_value": "N/A", "unit": "USD", "shipping_weight": "N/A", "breadscrumbs": l3_names,
        "image_urls": images, "mpn": "N/A",
        "specification_1": specifications_1, "specification_2": [], "datasheets": datasheet,
        "product_description_1": description_1, "product_description_2": description_2,
        "accessories": relateds, "video_links": video_links, "miscellaneous": country,
        "scraped_by": "Pradeep Kumar",
    }]
    print('Complete all Your Program')
    print()

    # Data_Save(raw_data, list_column)


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
    file_path = "D:/Web-Scrapping/A-MONTH-2024/Fab/Promaxtool.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path, encoding='latin1')['URL']
    i = 0
    for url_count, url in enumerate(url_links[i:1], start=i):
        urls.append(url)
        # print(url)

        soup = GetSoupUrl(url)
        Product_Details(url, soup)
    return urls


ReadUrlFromList()


# def main():
#     url_1 = ReadUrlFromList()
#
#     with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#         executor.map(lambda url: Product_Details(url, GetSoupUrl(url)), url_1)
#         print('*******************************************************************************************************')
#
#
# if __name__ == "__main__":
#     main()
