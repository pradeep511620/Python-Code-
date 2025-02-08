import time

import requests
import pandas as pd
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter, Retry


base_url = 'https://www.mrosupply.com/'

sess = requests.Session()
header = {
    "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

# product_data = open("/var/www/html/web_scr/scrapped_data/stearn_brakes_mroSupplies_product_data.csv", 'a', encoding='utf-8')
product_data = open("stearn_brakes_mroSupplies_product_data.csv", 'a', encoding='utf-8')
# product_specs = open("/var/www/html/web_scr/scrapped_data/stearn_brakes_mroSupplies__specs.csv", 'a', encoding='utf-8')
product_specs = open("stearn_brakes_mroSupplies__specs.csv", 'a', encoding='utf-8')


def request_func(url):
    """Send Requests and Get Response from webpage and return Soup"""
    n_retries = 4
    backoff_factor = 0.4        # 0.9 at the end point
    status_codes = [504, 503, 502, 500, 429]
    sess = requests.Session()
    retries = Retry(connect=n_retries, backoff_factor=backoff_factor, status_forcelist=status_codes)
    sess.mount("https://", HTTPAdapter(max_retries=retries))
    sess.mount("http://", HTTPAdapter(max_retries=retries))
    res = sess.get(url, headers=header)
    time.sleep(2)
    soup = BeautifulSoup(res.content, 'lxml')
    return soup


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
        breadcrumb = soup.find(class_='m-breadcrumbs').text.strip().replace('\n', '>')
        print("Breadcrumb >>>>>>>>>>> ", breadcrumb)

        try:
            grainer_sku = soup.find(class_='productDetail--card').find(class_="modelNo").text
            grainer_sku = f'rp_ {grainer_sku}'
            print("grainer_sku >>>>>>>>>>> ", grainer_sku)
        except AttributeError:
            grainer_sku = ''

        try:
            description = ''
            descriptions = soup.find(id='additionalDescription').findAll(class_='m-accordion--item--body')
            for desc in descriptions:
                description = f'{description} {desc.h5.text}'
                for li in desc.findAll('li'):
                    description = f'{description} {li.text}'
            print("description >>>>>>> ", description)
        except AttributeError:
            description = ''

        try:
            features = soup.find(class_='product attribute overview').find(class_='value').text.strip().replace('\n', ' ')
            print("features >>> ", features)
        except AttributeError:
            features = ''

        try:
            shipping_info = soup.find(class_='free-ship').text.strip()
            print("shipping_info >>>>>>>>>> ", shipping_info)
        except Exception as e:
            shipping_info = ''

        try:
            price = soup.find(class_='price').text.strip()
            print("price >>> ", price)
        except AttributeError:
            price = ''

        try:
            remark = soup.find(class_='u-margin-bottom muted').text.strip()
            print("remark >>> ", remark)
        except AttributeError:
            remark = ''

        image_list = [None] * 5
        try:
            images = soup.find(class_="productDetail--image").findAll('img')
            # print(">>>>>>>>>>>", images)
            for i, image in enumerate(images[:5], start=0):
                image_list[i] = image['src']
            print("image >>>>>>>>>>>>", image_list)
        except AttributeError as e:
            print(e)

        pdf_list = []
        try:
            pdfs = soup.find(class_="documents").findAll(class_='documents--item')
            for pdf in pdfs:
                pdf_list.append(pdf.find('a')['href'])
            print("pdf >>> ", pdf_list)
        except Exception as e:
            print(e)

        attr_name = []
        attr_value = []
        specs = soup.find(class_="flex-table").findAll(class_="flex-table--item")
        for data in specs:
            for dt, dd in zip(data.findAll(class_='flex-table--head'), data.findAll(class_='flex-table--body')):
                attr_name.append(dt.text.strip())
                attr_value.append("rp_"+str(dd.text.strip()))
        print("attr_name >>>>>>>>>>>>> ", attr_name)
        print("attr_value >>>>>>>>>>>>> ", attr_value)

        """Convert data into dictionary form for pandas"""
        row.append({
            "Url": url,
            "Product_title": title,
            "L3_Name": breadcrumb,
            "Grainger_Sku": grainer_sku,
            "Product_Detail": description.strip(),
            "Features": features.strip(),
            "Image_URL_1": image_list[0],
            "Image_URL_2": image_list[1],
            "Image_URL_3": image_list[2],
            "Image_URL_4": image_list[3],
            "Image_URL_5": image_list[4],
            "Datasheet": pdf_list,
            "Price(usd)": price,
            "Shipping_info": shipping_info,
            "Remarks": remark,
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


def main():
    """Read urls from Stearn_brakes.csv and calling product_urls one by one"""
    i = 10000
    # product_urls = pd.read_csv('/var/www/html/web_scr/url_source/Stearn_brakes.csv')['Product_url']
    product_urls = pd.read_csv('Stearn_brakes.csv')['Product_url']
    """using i indexing product url default i value is 0"""
    for url in product_urls[i:10000]:   # start point 0 to 10000
        print(i, ">>>>>>>>>>>>>", url)
        try:
            row, cols = product_details(url)
            data_save(row, cols)
        except TypeError:
            pass
        i += 1
        # time.sleep(1)


main()

# product_details('https://www.mrosupply.com/clutches-and-brakes/2129040_1082011m2cqf_stearns/')
