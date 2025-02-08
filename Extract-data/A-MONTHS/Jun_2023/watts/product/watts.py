# import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = 'https://www.watts.com/'

product_data = open(f'product_data.csv', 'a', encoding='utf-8')
product_specs = open(f'product_specs.csv', 'a', encoding='utf-8')

sess = requests.Session()
header = {
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

product_data = open("/var/www/html/webscr/destination_dir/watts_all_data.csv", 'a', encoding='utf-8')
# product_data = open("C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/watts/data/watts_all_data.csv", 'a', encoding='utf-8')
product_specs = open("/var/www/html/webscr/destination_dir/watts_specs.csv", 'a', encoding='utf-8')
# product_specs = open("C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/watts/data/watts_specs.csv", 'a', encoding='utf-8')


def request_func(url):
    """Send Requests and Get Response from webpage and return Soup"""
    res = sess.get(url, headers=header)
    soup = BeautifulSoup(res.content, 'lxml')
    return soup


def urljoin_func(url, join_url=base_url):
    """function takes a relative url and convert it into absolute url and returns"""
    return urljoin(join_url, url)


def product_details(url):
    """Get product details(Respective Product url, title, breadcrumb, grainer_sku, image url
    features, product details, product specifications) and call data save function(file as txt or csv)"""

    cols = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_info", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)",
        "weight(lb)", "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url",
        "Remarks", "attr_name", "attr_value"
    ]

    row = []

    soup = request_func(url)
    # print(soup)
    try:
        title = soup.h1.text.strip()
        print("title >>> ", title)

        breadcrumb = ''
        breadcrumbs = soup.find(class_="breadcrumbs").findAll('li')
        for crumb in breadcrumbs:
            breadcrumb = f'{breadcrumb} {crumb.text.strip()} >'

        print("breadcrumb >>> ", breadcrumb)

        try:
            grainer_sku = soup.find(class_='ean-ucc-code').text.strip()
            grainer_sku = f'rp_{grainer_sku.split(":")[-1].strip()}'
            print("grainer_sku >>>>>>>>>>> ", grainer_sku)
        except AttributeError:
            grainer_sku = 'Not Found'

        try:
            short_info = soup.find(class_='short-description--series').text.strip()
            print("short_info >>>>>>>>>> ", short_info)
        except Exception as e:
            short_info = 'Not Found'
            print(e)

        try:
            description = soup.find(
                class_="product__additional-details js-jump-links-target js-jump-links-default-label").text.strip()
            print("description >>>>>>>>>>>", description)
        except AttributeError:
            description = 'Not Found'

        try:
            discontinued = soup.find(
                class_="discontinued info").text.strip()
            print("discontinued >>>>>>>>>>>", discontinued)
        except AttributeError:
            discontinued = 'Not Found'

        try:
            features = ''
            feature = soup.findAll(class_='product__additional-details')[1].findAll('li')
            for li in feature:
                features = f'{features}{li.text} '
            print("features >>> ", features)
        except AttributeError:
            features = ''

        try:
            accessories = soup.find(class_='series').text.strip()
            print("accessories >>>>>>>>>> ", accessories)
        except Exception as e:
            accessories = 'Not Found'
            print(e)

        try:
            price = soup.find(id='price').text.strip()
            print("price >>> ", price)
        except AttributeError:
            price = 'Not Found'

        try:
            remark = soup.find(class_='part-number').text.strip()
            print("remark >>> ", remark)
        except AttributeError:
            remark = ''

        image_list = [None] * 5
        try:
            images = soup.find(class_="gallery").findAll(class_='slide-media__container')
            for i, image in enumerate(images[:5], start=0):
                try:
                    image_list[i] = urljoin_func(image.find('img')['src'])
                except TypeError:
                    pass
            print("image >>>>>>>>>>>>", image_list)
        except AttributeError as e:
            print(e)

        pdf_list = []
        try:
            pdfs = soup.find(class_="product-downloads").findAll('a')
            for pdf in pdfs:
                pdf_list.append(urljoin_func(pdf['href']))
            print("pdf >>> ", pdf_list)
        except Exception as e:
            print(e)

        attr_name = []
        attr_value = []

        try:
            table = soup.find(class_="product__specifications").findAll('tr')
            for data in table[1:]:
                attr_name.append(data.findAll('td')[0].text)
                attr_value.append("rp_" + data.findAll('td')[1].text)
                # attr_name.append(data.find('th').text)
                # attr_value.append(data.find('td').text)
        except Exception as e:
            print(e)

        print("attr_name >>>>>>>>>>>>> ", attr_name)
        print("attr_value >>>>>>>>>>>>> ", attr_value)

        """Convert data into dictionary form for pandas"""
        row.append({
            "Url": url,
            "Product_title": title,
            "Grainger_Sku": grainer_sku,
            "Product_Detail": f'{short_info} {description.strip()}',
            "Features": features.strip(),
            "Accessories": accessories.strip(),
            "Image_URL_1": image_list[0],
            "Image_URL_2": image_list[1],
            "Image_URL_3": image_list[2],
            "Image_URL_4": image_list[3],
            "Image_URL_5": image_list[4],
            "Datasheet": pdf_list,
            "Price(usd)": price,
            "Remarks": remark,
            "Cross_Reference": discontinued,
            "attr_name": attr_name,
            "attr_value": attr_value
        })

        return row, cols
    except Exception as e:
        print(e)


def data_save(row, cols):
    """function takes row and columns convert into dataframe and filter out and save data into the file"""

    df = pd.DataFrame(row, columns=cols)

    """Creating subset from Main Dataframe for specifications and drop specs"""
    specs_dataset = df[["Url", "Grainger_Sku", 'attr_name', 'attr_value']]
    specs_dataset = specs_dataset.explode(['attr_name', 'attr_value'])
    df = df.drop(['attr_name', 'attr_value'], axis=1)

    df.to_csv(product_data, lineterminator='\n', header=False, index=False)
    specs_dataset.to_csv(product_specs, lineterminator='\n', header=False, index=False)


# Here is the Read Urls in the csv files
mylst = pd.read_csv("/var/www/html/webscr/source_dir/product.csv")['urls']
# mylst = pd.read_csv("C:/Users/PK/Desktop/Web-Scrapping/Jun_2023/watts/urls/product.csv")['urls']
print('length...', len(mylst))


def main():
    url_length = 0
    for url in mylst[url_length:]:
        print("Product-Urls......", url_length, url)
        try:
            product_details(url)
            row, cols = product_details(url)
            data_save(row, cols)
        except TypeError:
            pass

        url_length += 1


main()

# product_details('https://www.watts.com/products/plumbing-flow-control-solutions/relief-valves/pressure-only-relief-valves/m375/375m1-075')
