import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
base_url = 'https://www.grainger.com/'
mylist = [
    'https://www.grainger.com/product/GE-Miniature-Circuit-Breaker-32HY01'
    # 'https://www.grainger.com/product/GE-Miniature-Circuit-Breaker-32HY01',
    # 'https://www.grainger.com/product/GE-Miniature-Circuit-Breaker-32HY03',
    # 'https://www.grainger.com/product/GE-Miniature-Circuit-Breaker-32HY02',
    # 'https://www.grainger.com/product/GE-Miniature-Circuit-Breaker-32HY04'

]

for url in mylist:
    ress = requests.get(url, headers=headers)
    soup = BeautifulSoup(ress.content, "html.parser")
    print(url)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        l3_name_l3 = []
        for l3 in soup.find('ul', {"data-testid": "breadcrumbs"}).find_all('li'):
            l3_name_l3.append(l3.text.strip())
        l3_name = "## ".join(l3_name_l3)
        print('l3_name.....', l3_name)
    except AttributeError:
        l3_names = 'N/A'
        print('l3_name.....', l3_names)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        product_title = soup.find("h1", {"class": "lypQpT"}).text.strip()
        print('product_title.....', product_title)
    except AttributeError:
        product_title = 'N/A'
        print('product_title.....', product_title)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        part_number = soup.find('dd', {"class": "rOM8HV hRRBwT"}).text.strip()
        mpn = part_number
        print('mpn.....', mpn)
    except AttributeError:
        mpn = 'N/A'
        print('mpn.....', mpn)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        cate_details = soup.find(class_="rOM8HV hRRBwT").text.strip()
        category = {"Item": cate_details}
        print('Item.....', category)
    except AttributeError:
        category = []
        print('Item.....', category)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        shipping_weight_details = soup.find('div', {"data-testid": "shipping-weight"}).find('strong').text.strip()
        shipping_weight = shipping_weight_details
        print('shipping_weight.....', shipping_weight)
    except AttributeError:
        shipping_weight = ''
        print('shipping_weight.....', shipping_weight)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        price_details = soup.find("div", {"class": "rZErC5"}).text.strip()
        price = {"Web Price": price_details}
        print('price.....', price)
    except AttributeError:
        price = {'Web Price': '$-.--'}
        print('price.....', price)
    # ------------------------------------------------------------------------------------------------------------------
    try:
        description_1 = []
        for des in soup.find('div', {"class": "W7BBCC"}).find_all('p'):
            description_1.append(des.text.strip())
        description_1 = {"desc": description_1}
        print('description_1.....', description_1)
    except AttributeError:
        description_1 = []
        print('description_1.....', description_1)

    # ------------------------------------------------------------------------------------------------------------------
    try:
        images = []
        for images_html in soup.find('div', {"data-testid": "product-gallery"}).find_all('img'):
            if images_html:
                image_src = images_html['src']
                alt_tag = images_html.get('alt')
                image_tag_and_alt_tag = {"src": image_src, "alt": alt_tag}
                images.append(image_tag_and_alt_tag)
        print('images.....', images)
    except AttributeError:
        images = ''
        print('images.....', images)
    #
    try:
        datasheet = []
        for pdf in soup.find_all("a", class_="plp-download-link"):
            datasheet.append(pdf.get('href'))
        print('datasheet.....', datasheet)
    except AttributeError:
        datasheet = []
        print('datasheet.....', datasheet)
    #
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
    except AttributeError:
        realated_url = [{'accessories': []}]
        print("realated.....", realated_url)

    # # ------------------------------------------------------------------------------------------------------------------
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

    # instruction = []
    # for table2 in soup.find_all('table', class_="plp-item-table"):
    #     for note in table2.find('span', {"data-measure": "general"}).find_all('li'):
    #         instruction.append(note.text.strip())
    # print(instruction)

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
