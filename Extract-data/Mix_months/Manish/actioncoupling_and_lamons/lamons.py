import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd


base_url = "https://www.lamons.com/products/"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36"
}

"""create a session Object as sess"""
sess = requests.Session()

"""product data variable"""
product_data = open("lamons_product_data.csv", 'a', encoding='utf-8')
product_link = ['https://www.lamons.com/products/fasteners/specialty',
                'https://www.lamons.com/services/engineered-solutions/custom-gasket-engineering/',
                'https://www.lamons.com/products/fasteners/all-thread-rod',
                'https://www.lamons.com/products/fasteners/standard/',
                'https://www.lamons.com/services/engineered-solutions/special-machined-parts/',
                'https://www.lamons.com/products/hoses-and-expansion-joints/hoses/industrial-utility-hoses/',
                'https://www.lamons.com/products/gaskets/non-metallic/elastomeric-fiber-sheet/',
                'https://www.lamons.com/products/hoses-and-expansion-joints/hoses/chemical-petroleum-hoses/',
                'https://www.lamons.com/services/engineered-solutions/prototyping/',
                'https://www.lamons.com/products/gaskets/metallic/',
                'https://www.lamons.com/products/gaskets/semi-metallic/kammprofile-gaskets/',
                'https://www.lamons.com/products/fasteners/standard/stud-bolts',
                'https://www.lamons.com/products/gaskets/semi-metallic/spiral-wound/',
                'https://www.lamons.com/products/hoses-and-expansion-joints/expansion-joints/',
                'https://www.lamons.com/engineered-solutions/reverse-engineering/',
                'https://www.lamons.com/products/fasteners/',
                'https://www.lamons.com/products/fasteners/specialty/washers',
                'https://www.lamons.com/products/hoses-and-expansion-joints/',
                'https://www.lamons.com/products/gaskets/',
                'https://www.lamons.com/products/gaskets/non-metallic/compressed-non-asbestos-sheet/',
                'https://www.lamons.com/products/fasteners/specialty/headed-fasteners',
                'https://www.lamons.com/products/hoses-and-expansion-joints/expansion-joints/rubber',
                'https://www.lamons.com/products/hoses-and-expansion-joints/expansion-joints/ptfe-lined-rubber',
                'https://www.lamons.com/products/hoses-and-expansion-joints/hoses/flexible-metal-hoses/',
                'https://www.lamons.com/products/fasteners/standard/nuts',
                'https://www.lamons.com/products/gaskets/non-metallic/',
                'https://www.lamons.com/products/hoses-and-expansion-joints/hoses/',
                'https://www.lamons.com/products/gaskets/metallic/kammprofile-ring-type-joint',
                'https://www.lamons.com/products/gaskets/semi-metallic/',
                'https://www.lamons.com/products/gaskets/metallic/ring-joint/']


def extract_urls_recursive(url, visited=None):
    """
    Extracts all URLs from a webpage and any pages it links to, recursively.
    :param url: the URL of the starting page
    :param visited: a set of URLs that have already been visited
    :return: a set of all unique URLs found on the pages
    """
    if visited is None:
        visited = set()
    urls = set()
    try:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            product_links = soup.findAll(class_="is-layout-flow wp-block-column")
            for link in product_links:
                next_url = urljoin(base_url, link.find('a')['href'])
                if next_url not in visited:
                    visited.add(next_url)
                    urls.add(next_url)
                    urls = urls.union(extract_urls_recursive(next_url, visited))
    except Exception as e:
        print(e)
    return urls


def product_page(url):
    """Get parent product details(Url, Features, Product_Detail, Image_URL_1,
    Standards_and_Approvals, Uses) and call data save function for data save(save as txt or csv)"""
    res1 = sess.get(url, headers=header)
    soup = BeautifulSoup(res1.content, 'lxml')
    content = soup.find(class_="max-width-block__interior").findAll('a')
    try:
        application = soup.findAll(class_="wp-block-ub-tabbed-content-tab-content-wrap")[0].text
    except IndexError:
        application = ''
    try:
        benefit = soup.findAll(class_="wp-block-ub-tabbed-content-tab-content-wrap")[1].text
    except IndexError:
        benefit = ''
    try:
        certificates = soup.findAll(class_="wp-block-ub-tabbed-content-tab-content-wrap")[2].text
    except IndexError:
        certificates = ''

    for data in content:
        try:
            image = data.find('img')['src']
            link = data['href']
            # print(image)
            # print(link)
            product_details(urljoin(base_url, link), image, application, benefit, certificates)
        except TypeError:
            pass


def product_details(url, image, application, benefit, certificate):
    """Get product details(   "Url": url,
        "Item_Name, L3_Name, Parent_name, Features, Product_Detail, Image_URL_1, Standards_and_Approvals, Uses")
        and call data save function for data save(save as txt or csv)"""

    cols = [
        "S.No", "Mpn", "Label", "Upc", "Grainger_Sku", "Entity_Id", "L3_Name", "L3_Entity_ID", "Item_Name", "item_ID",
        "Parent_name", "Parent_Name_Id", "Product_title", "Accessories", "Kits/Components", "Spare_Parts",
        "Product_Detail", "Uses", "Features", "Working_Mechanism", "Standards_and_Approvals", "Installation",
        "Accessories", "Image_Name", "Image_URL_1", "Image_URL_2", "Image_URL_3", "Image_URL_4", "Image_URL_5",
        "Video_Url", "Datasheet", "Shipping_length(mm)", "Shipping_height(mm)", "Shipping_width(mm)", "weight(kg)",
        "Quantity", "Price(usd)", "Discount(%)", "Country_of_Origin", "Cross_Reference", "Url", "Remarks"
    ]

    row = []

    res = sess.get(url, headers=header)
    soup = BeautifulSoup(res.content, 'lxml')
    parent = soup.find(id="child-header-title").text
    try:
        headers = soup.find(class_="product-list").findAll('h3')
    except AttributeError:
        headers = []
    try:
        desc = soup.find(class_="product-list").findAll(class_='wp-block-ub-tabbed-content-tabs-content')
    except AttributeError:
        desc = soup.findAll(class_='wp-block-ub-tabbed-content-tabs-content')

    title = []
    description = []
    for h3, details in zip(headers, desc):
        title.append(h3.text)
        description.append(details.text)

    bread_crumb = soup.find(id='breadcrumbs').text.strip()

    """
    print("child >>>>>>>>>>>>>", parent)
    print(h3.text, ">>>>>>>>>>>", details.text)
    print("bread crumb >>>>>>>>>>>>>>>>", bread_crumb)
    print("image >>>>>>>>>>>>>", image)
    print("application >>>>>>>>>>>>>", application)
    print("benefit >>>>>>>>>>>>>>>>>>", benefit)
    print("certificate >>>>>>>>>>>>", certificate)
    """

    """Converting Data into Dict form"""
    row.append({
        "Url": url,
        "Item_Name": title,
        "L3_Name": bread_crumb,
        "Parent_name": parent,
        "Features": description,
        "Product_Detail": application.strip(),
        "Image_URL_1": image,
        "Standards_and_Approvals": certificate,
        "Uses": benefit,
    })

    data_save(row, cols)


def data_save(row, cols):
    """function takes row and columns convert into dataframe and filter out and save data into the file"""
    df = pd.DataFrame(row, columns=cols)
    print("item name df >>>>>>>>>>>>>>>>>>>>>>", df['Item_Name'])
    df = df.apply(pd.Series.explode).reset_index()
    print(df)
    df.to_csv(product_data, index=False, lineterminator='\n', header=False)
    # df.to_csv("test.csv")


def main():
    i = 0
    """using i for indexing product url default i value is 0"""
    for url in product_link[i:]:
        print(i, ">>>>>>>>>>>>>>>>>>>", url)
        product_page(url)
        i += 1


main()
