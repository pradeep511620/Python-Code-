from bs4 import BeautifulSoup
# import json
import concurrent.futures
import pandas as pd
import requests



file_path = r"P:\Web-scrapings\A-MONTH-2024\Aug\Grainger\url\Product-url.csv"
urls = pd.read_csv(file_path)['URL']


headers = {
    'authority': 'www.grainger.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.8',
    'referer': 'https://www.grainger.com/product/102EW3',
    'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}


final_df = []
def get_results(url):
    try:
        print("Product-url -----:", url)
        response = requests.get(url, headers=headers)
        print("Status Code:", response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser')

        # --------------------------------------------------------------------------------------------------------------
        try:
          bread = [l3.text.strip() for l3 in soup.select('ul[data-testid="breadcrumbs"] li a')]
          l3_name = '## '.join(bread)
          print('l3_name ----- :', l3_name)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          l3_name = None
          print('l3_name ----- :', l3_name)

        # --------------------------------------------------------------------------------------------------------------
        try:
          title = soup.h1.text
          print('title ----- :', title)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          title = None
          print('title ----- :', title)

        # --------------------------------------------------------------------------------------------------------------
        try:
          item_id = soup.find(class_="iYMkrn").find("dd").text
          print('item_id ----- :', item_id)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          item_id = None
          print('item_id ----- :', item_id)
        

        # --------------------------------------------------------------------------------------------------------------
        try:
          manufacture_id = soup.select("dd.rOM8HV.hRRBwT")[1].text.strip()
          print('manufacture_id ----- :', manufacture_id)
        except:
          manufacture_id = None
          print('manufacture_id ----- :', manufacture_id)

        # --------------------------------------------------------------------------------------------------------------
        try:
          qty = soup.select_one("div.XCqnjh span.G32gdF.KjtQT.N5ad3.dS3bX").text.strip()
          # print('qty ----- :', qty)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          qty = None
          print('qty ----- :', qty)

        try:
          price = soup.select_one("div.XCqnjh .HANkB").text.strip() + '' + qty
          print('price ----- :', price)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          price = None
          print('price ----- :', price)


        # --------------------------------------------------------------------------------------------------------------
        try:
          weight = soup.select_one('div[data-testid="shipping-weight"] strong').text.strip()
          print('weight ----- :', weight)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          weight = None
          print('weight ----- :', weight)

        # --------------------------------------------------------------------------------------------------------------
        try:
          description = [des.text.strip() for des in soup.select('div[data-testid="product-description"] p')]
          print('description ----- :', description)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          description = []
          print('description ----- :', description)
        

        # --------------------------------------------------------------------------------------------------------------
        try: 
          Images = [{'src': src.get('src'), 'alt': src.get('alt')} for src in soup.select('div[data-testid="product-gallery"] img')]
          print('Images ----- :', Images)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          Images = None
          print('Images ----- :', Images)

        # --------------------------------------------------------------------------------------------------------------
        try:
          attr_name = [th.text.strip() for th in soup.select("dl[data-testid='product-techs'] dt")]
          attr_value = [td.text.strip() for td in soup.select("dl[data-testid='product-techs'] dd")]
          specs = [{name: value} for name, value in zip(attr_name, attr_value)]
          print('specification ----- :', specs)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          specs = []
          print('specification ----- :', specs)

        # --------------------------------------------------------------------------------------------------------------
        try:
          datasheet = [pdf.get('href') for pdf in soup.select("div[data-testid='product-documents-list'] a")]
          print('datasheet ----- :', datasheet)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          datasheet = []
          print('datasheet ----- :', datasheet)

        # --------------------------------------------------------------------------------------------------------------
        try:
          alternate = [realated.get('href') for realated in soup.select('ul[data-testid="alternate-products-accordion-items"] li a')]
          print('alternate ----- :', alternate)
        except (AttributeError, IndexError, TypeError,ValueError) as e:
          print(f"An error occurred: {e}")
          alternate = []
          print('alternate ----- :', alternate)

        # --------------------------------------------------------------------------------------------------------------
        data = [url, l3_name, title, item_id, manufacture_id, price, weight, description, Images, specs, datasheet, alternate]
        final_df.append(data)

       
    except Exception as e:
        print(f"An error occurred: {e}")



# get_results("https://www.grainger.com/product/TOUCHNTUFF-Disposable-Gloves-ISO-5-46C632")



with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    start_url = 80000
    futures = [executor.submit(get_results, url) for index, url in enumerate(urls[start_url:90000], start=start_url)]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

    column_names = ['URL', 'Breadcrumbs', 'Title', 'Item ID', 'Manufacture ID', 'Price', 'Weight', 'Description', 'Images', 'Specifications', 'Datasheet', 'Alternate Products']
    df = pd.DataFrame(final_df, columns=column_names)
    df.to_csv('Grainger_116k_products.csv', mode='a', header=not pd.io.common.file_exists('Grainger_116k_products.csv'), index=False)
    print('save data into csv files')





"""
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Submit each download task to the thread pool
    start_url = 0
    futures = [executor.submit(get_results, url) for index, url in enumerate(urls[start_url:50], start=start_url)]
    # Wait for all tasks to complete and retrieve the results
    results = [future.result() for future in concurrent.futures.as_completed(futures)]
    # Print the contents of each file
    for result in results:
        print(final_df)

    df = pd.DataFrame.from_records(final_df)
    # print(df)
    df.to_csv("Grainger_116k_products.csv")
"""