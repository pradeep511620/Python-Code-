import concurrent.futures
import time
from urllib.parse import urljoin

import pandas as pd
import playwright.sync_api as pw

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
save_files = open(r"data.csv", "a+", encoding="utf-8")
base_url = 'https://www.onlinecomponents.com/'


class ScrapeDataFromTheWebsite:
    def __init__(self, URL):
        self.url = URL

    def product_details(self):
        with pw.sync_playwright() as play:
            browser = play.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(self.url)
            time.sleep(15)
            print('Product-url:-----', self.url)

            l3_Name = ''
            catlvl1 = ''
            catlvl2 = ''
            catlvl3 = ''
            try:
                Brand = page.query_selector("#divSupplier").inner_text().strip()
            except (AttributeError, TypeError, IndexError, Exception) as e:
                Brand = ''
                print(f"An error occurred: {e} Brand -----: {Brand}")

            try:
                names = [l3.text_content().strip() for l3 in page.query_selector_all("#BreadcrumbScrollToView ul li [itemprop='item']")]
                l3_Name = "## ".join(names)
                print('l3_Name.....', l3_Name)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                print(f"An error occurred: {e} l3_Name -----: {l3_Name}")

            if l3_Name:
                categories = l3_Name.split("## ")
                catlvl1, catlvl2, catlvl3 = [categories[i] if i < len(categories) else None for i in range(2, 5)]
                print('catlvl1.....', catlvl1)
                print('catlvl2.....', catlvl2)
                print('catlvl3.....', catlvl3)
            try:
                product_title = page.query_selector("div.Box-sc-1z9git-0.cOgTzu h1").text_content().strip()
                print('product_title.....', product_title)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                product_title = ''
                print(f"An error occurred: {e} product_title -----: {product_title}")

            try:
                price = ''
                price_details_info = page.query_selector_all(".prod-specs .prod-info-body")
                for price_details in price_details_info:
                    text_content = price_details.text_content().replace("\n", ">>")
                    if "List Price" in text_content:
                        prices = text_content.replace("List Price: ", "")
                price = {'list_price': prices, 'qty': '1', 'moq': '1'}
                print('price.....', price)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                price = {'list_price': price, 'qty': '1', 'moq': '1'}
                print(f"An error occurred: {e} price -----: {price}")

            try:
                mpn = page.query_selector('div:has-text("Part No:") + div').inner_text()
                print('mpn.....', mpn)
            except (AttributeError, TypeError, IndexError) as e:
                mpn = ''
                print(f"An error occurred: {e} mpn -----: {mpn}")

            try:
                short_desc = page.query_selector("#divDescription p").text_content().strip().replace('\n', '')
            except (AttributeError, TypeError, IndexError, Exception) as e:
                short_desc = ''
                print(f"An error occurred: {e} short_desc -----: {short_desc}")

            try:
                desc = page.query_selector('#divFullDescription').text_content()
                description_1 = {"desc": [desc], "instructions": [], "short_desc": short_desc}
                print('description_1.....', description_1)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                description_1 = {"desc": []}
                print(f"An error occurred: {e} description_1 -----: {description_1}")

            try:
                desc_2 = [feature.text_content() for feature in page.query_selector_all('.info-construct.prod-details-div.details-left ul li')]
                description_2 = desc_2
                print('description_2.....', description_2)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                description_2 = []
                print(f"An error occurred: {e} description_2 -----: {description_2}")

            try:
                attr_name = []
                attr_value = []
                for table in page.query_selector_all(".mx-0.priceLine"):
                    tab = table.inner_text().strip().replace('\n', '>>').split('>>')
                    attr_name.append(tab[0])
                    attr_value.append(tab[1])
                specs = [{name: value} for name, value in zip(attr_name, attr_value)]
            except (AttributeError, TypeError, IndexError, Exception) as e:
                specs = []
                print(f"An error occurred: {e} specs -----: {specs}")

            try:
                attr_name2 = [th.text_content().strip() for th in page.query_selector_all(".lstSpecs li .col-5.col-md-4")]
                attr_value2 = [td.text_content().strip() for td in page.query_selector_all(".lstSpecs li .col-7.col-md-8")]
                specs_1 = [{name2: value2} for name2, value2 in zip(attr_name2, attr_value2)]
            except (AttributeError, TypeError, IndexError, Exception) as e:
                specs_1 = []
                print(f"An error occurred: {e} specifications_1 -----: {specs_1}")

            specifications_1 = str(specs_1) + ", " + str(specs)
            print('specification_1......', specifications_1)

            try:
                images = [{'src': urljoin(base_url, img.get_attribute('src')), 'alt': img.get_attribute('alt')} for img
                          in page.query_selector_all(".row.product-wrap .row a img")]
                print('image.....', images)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                images = []
                print(f"An error occurred: {e} image -----: {images}")

            try:
                video = [vdo.get_attribute('src') for vdo in page.query_selector_all(".section-gray-light iframe")]
                print('Video.....', video)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                video = []
                print(f"An error occurred: {e} video -----: {video}")

            try:
                datasheet = [urljoin(base_url, pdf.get_attribute('href')) for pdf in
                             page.query_selector_all("#ResourceTable ul li a") if
                             'datasheet' in pdf.get_attribute('href')]
                print('datasheet.....', datasheet)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                datasheet = []
                print(f"An error occurred: {e} datasheet -----: {datasheet}")

            try:
                realated = [urljoin(base_url, relate_href.get_attribute('href')) for relate_href in
                            page.query_selector_all(".related-products li h3 a")]
                print('realated.....', realated)
            except (AttributeError, TypeError, IndexError, Exception) as e:
                realated = [{'accessories': []}]
                print(f"An error occurred: {e} realated -----: {realated}")

            try:
                Stock = page.query_selector("#trInstock .text-uppercase").text_content().strip().replace('In Stock:\n', '')
            except (AttributeError, TypeError, IndexError, Exception) as e:
                Stock = ''
                print(f"An error occurred: {e} Stock -----: {Stock}")

            try:
                Factory_Lead_Time = page.query_selector_all(".col-7.text-slate-grey.font-weight-400")[-1].text_content().strip().replace(' ', '')
            except (AttributeError, TypeError, IndexError, Exception) as e:
                Factory_Lead_Time = ''
                print(f"An error occurred: {e} Factory_Lead_Time -----: {Factory_Lead_Time}")

            try:
                logo = urljoin(base_url,page.query_selector("#imgMunfImage").get_attribute('src'))
            except (AttributeError, TypeError, IndexError, Exception) as e:
                logo = ''
                print(f"An error occurred: {e} logo -----: {logo}")

            miscellaneous = {"Stock": Stock, "Factory Lead-Time": Factory_Lead_Time, "Logo": logo}
            print('miscellaneous.....', miscellaneous)

            # --------------------------------------------------------------------------------------------------------------
            list_column = [
                "brand", "catlvl1", "catlvl2", "catlvl3", "url", "title", "price_value", "unit", "shipping_weight",
                "breadscrumbs", "image_urls", "mpn", "specification_1", "specification_2", "datasheets",
                "product_description_1", "product_description_2", "accessories", "video_links", "miscellaneous",
                "scraped_by"
            ]
            raw_data = [{
                "brand": Brand, "catlvl1": catlvl1, "catlvl2": catlvl2, "catlvl3": catlvl3, "url": self.url,
                "title": product_title, "price_value": price, "unit": "USD", "shipping_weight": '',
                "breadscrumbs": l3_Name, "image_urls": images, "mpn": mpn,
                "specification_1": specifications_1, "specification_2": [], "datasheets": datasheet,
                "product_description_1": description_1, "product_description_2": description_2,
                "accessories": realated, "video_links": video, "miscellaneous": miscellaneous,
                "scraped_by": "Pradeep_RaptorTech",
            }]

            # Data_Save(raw_data, list_column)
            print('Complete all Your Program')
            print()
            browser.close()


def Data_Save(row, cols):  # using save data into dataframe
    df = pd.DataFrame(row, columns=cols)
    print(df)
    df.to_csv(save_files, header=False, index=False, lineterminator='\n')
    print('save data into csv files')


url = 'https://www.webstaurantstore.com/ts-b-0665-bstrm-mop-sink-faucet/510B665.html'
scrape_data = ScrapeDataFromTheWebsite(url)
scrape_data.product_details()


def main():
    file_path = "P:/Web-scrapings/A-MONTH-2024/July/Onlinecomponents-Brand-Telemechanique.com/url/Product-url.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    Product_url = []
    start_url = 300
    for url_count, url in enumerate(url_links[start_url:], start=start_url):
        Product_url.append(url)

    def ReadUrlFromLists():
        return Product_url

    url_1 = ReadUrlFromLists()
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        try:
            executor.map(lambda url_link: ScrapeDataFromTheWebsite(url_link).product_details(), url_1)
            print(f"{'--' * 30} Thread Running {'--' * 30}")
        except Exception as e:
            print(f"Error: {e}")
            raise RuntimeError("Error encountered. Program terminated.")


# if __name__ == "__main__":
#     main()
