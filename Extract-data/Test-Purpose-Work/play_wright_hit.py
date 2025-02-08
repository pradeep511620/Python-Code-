import time
from playwright.sync_api import sync_playwright

url = 'https://blinkit.com/cn/hair-care/cid/13/77'
# url = 'https://blinkit.com/prn/godrej-expert-creme-hair-colour-for-women-men-natural-black/prid/22415'

with sync_playwright() as play:
    browser = play.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # start_time = time.time()
    page.goto(url)
    end_time = time.time()
    # time_taken = end_time - start_time
    time.sleep(2)
    print(f'URL: {url}')
    # print(f'Time taken to load the page: {time_taken:.2f} seconds')
    # title_name_list = [title.inner_html() for title in page.query_selector_all('div[class="tw-mb-1.5"] div')]
    # print(title_name_list)
    title = [title.inner_text().split('\n')[0] for title in page.query_selector_all('.Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10')]
    print(title)
    browser.close()

