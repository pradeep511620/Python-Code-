from playwright.sync_api import sync_playwright
from urllib.parse import urljoin
import pandas as pd


base_url = 'https://www.applied.com'

def get_url(URL):
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False)
        context = browser.new_context(viewport=None)
        page = context.new_page()
        page.goto(URL)
        page.wait_for_timeout(2000)
        product_urls = set()
        for category_url in page.query_selector_all("div.dc-product-list a[itemprop='url']"):
            product_url = urljoin(base_url, category_url.get_attribute('href'))
            product_urls.add(product_url)
        else:
            print()
        df = pd.DataFrame(list(product_urls), columns=['URL'])
        df.to_csv('product_urls.csv',mode='a+', index=False)

        print(f"Saved {len(df)} unique product URLs to 'product_urls.csv'.")

    print('with end')

for i in range(600, 847 + 1):
    url = f'https://www.applied.com/brands/regal-rexnord/stearns-division/c/Brand-1640?q=:&override=true&isLevelUp=false&usePlp=&page={i}'
    get_url(url)

