import time
from playwright.sync_api import sync_playwright

def product_data(url):
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        time.sleep(4)
        print('product--url:', page)

        page.query_selector("button#onetrust-reject-all-handler").click()
        time.sleep(3)

        # --------------------------------------------------------------------------------------------------------------
        l3_Name = ''
        try:
            l3_name_div = [bread.inner_text().strip() for bread in page.query_selector_all("ol.breadcrumbs__list li")]
            l3_Name = "## ".join(l3_name_div)
            print("l3_Name -----:", l3_Name)
        except Exception as e:
            print(f"Error{e} ------ {l3_Name}")

        # --------------------------------------------------------------------------------------------------------------
        product_title = ''
        try:
            product_title = page.query_selector("div.product-section__content h1").inner_text()
            print('product_title -----:', product_title)
        except Exception as e:
            print(f"Error{e} ------ {product_title}")

        # --------------------------------------------------------------------------------------------------------------
        feature_div = [fea.inner_text().strip() for fea in page.query_selector_all("div.features-grid__row.row p.paragraph")]
        print('feature-----', feature_div)
        browser.close()



product_data('https://www.nortonabrasives.com/en-us/product/merit-shurstik-ao-medium-grit-cloth-psa-disc#products')
