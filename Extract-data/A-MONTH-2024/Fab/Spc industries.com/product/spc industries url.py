import requests
from bs4 import BeautifulSoup
import csv


def scrape_urls_recursive(url, csv_writer):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        urls = []

        # Find URLs with class 'route categories__link'
        for url_href in soup.find_all('a', class_='route categories__link'):
            product_url = url_href['href']
            urls.append(product_url)
            csv_writer.writerow([product_url])
            print(product_url)

        # Find URLs with class 'BQOwdV'
        for url_href in soup.find_all('a', class_='BQOwdV'):
            product_url = url_href['href']
            urls.append(product_url)
            csv_writer.writerow([product_url])
            print(product_url)

        # Find URLs with class '_1XWWU1'
        for url_href in soup.find_all('a', class_='_1XWWU1'):
            product_url = url_href['href']
            urls.append(product_url)
            csv_writer.writerow([product_url])
            print(product_url)

        # Recursively visit links found on the current page
        for next_url in urls:
            scrape_urls_recursive(next_url, csv_writer)
    else:
        print(f"Failed to fetch URL: {url}")


# Starting URL
start_url = 'https://www.grainger.com/category/brand/Ge'

# Open CSV file for writing
with open('product_urls.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product URL'])  # Write header

    # Call the recursive function
    scrape_urls_recursive(start_url, writer)
