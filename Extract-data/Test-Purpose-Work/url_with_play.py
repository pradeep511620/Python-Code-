import time
import playwright.sync_api as pw
from urllib.parse import urljoin

base_url = 'https://www.dillonsupply.com'

def get_url(url):
    with pw.sync_playwright() as play:
        browser = play.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # Navigate to the URL
        page.goto(url)
        time.sleep(14)
        current_url = page.url
        print('current_url.....', current_url)
        for product_cate in page.query_selector_all(".item-details .item-name a"):
            product_url = urljoin(base_url, product_cate.get_attribute('href'))
            print(product_url)
            with open('Dillonsupply-anvil.txt', 'a+', encoding='utf-8') as file_save:
                file_save.write(f"{product_url}\n")



def main():
    for i in range(1, 36):
        print(i)
        url = 'https://www.dillonsupply.com/Brands/anvil/Catalog/All'
        # url = f'https://www.dillonsupply.com/Brands/anvil/Catalog/All?page={i}&pageSize=40&sort=1'
        get_url(url)




if __name__ == "__main__":
    main()
