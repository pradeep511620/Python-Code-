import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

base_url = 'https://www.fabory.com/en/'
product_urls = []

def soup_get_url(url):
    ress = requests.get(url)
    soup = BeautifulSoup(ress.content, "lxml")
    return soup

def get_url(url):
    soup = soup_get_url(url)
    page_product_urls = []  # Store URLs for this specific page
    for href_tag in soup.select("a.anchor-neutral"):
        product_url = urljoin(base_url, href_tag.get('href'))
        if 'com/group' not in product_url and "tel" not in product_url:
            page_product_urls.append(product_url)
        print(product_url)
    return page_product_urls

def process_urls_concurrently(urls):
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(get_url, url): url for url in urls}
        for future in as_completed(future_to_url):
            try:
                result = future.result()
                product_urls.extend(result)
            except Exception as e:
                print(f"Error processing URL: {future_to_url[future]}, Error: {e}")



file_path = r"P:\Web-scrapings\A-MONTH-2024\Sep\Fabory-products\product\fabory_url4.csv"
read_file = pd.read_csv(file_path)['URL']
start_url = 0
urls_to_process = read_file[start_url:]
print(f'Starting to process {len(urls_to_process)} URLs concurrently.')

# Call the function to process the URLs concurrently
process_urls_concurrently(urls_to_process)

# Save the product URLs to a CSV file
df = pd.DataFrame(product_urls, columns=['URL'])
print(df)
df.to_csv('fabory_url5.csv', mode='w', index=False)
























