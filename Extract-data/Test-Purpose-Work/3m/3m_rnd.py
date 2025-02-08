import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import ElementNotInteractableException, NoSuchElementException, TimeoutException, \
    UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options





chrome_options = Options()
# chrome_options.add_argument('--headless=New')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()





headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

# my_url_list = [
#     # 'https://www.3m.com/3M/en_US/p/d/b49000219/',
#     # 'https://www.3m.com/3M/en_US/p/d/b5005321087/',
#     'https://www.3m.com/3M/en_US/p/d/b40065653/',
#     # 'https://www.3m.com/3M/en_US/p/d/b40065643/',
#     # 'https://www.3m.com/3M/en_US/p/d/b5005321042/',
#     # 'https://www.3m.com/3M/en_US/p/d/v100809912/',
# ]




file_path = r"P:\Web-scrapings\Test-Purpose-Work\3m\Book1.csv"
my_url_lists = pd.read_csv(file_path)['URL']


final_data = []

def Product_details():
    start_url = 1277
    for url_count, url in enumerate(my_url_lists[start_url:2000], start=start_url):
        driver.get(url)
        print(url_count, url)
        time.sleep(2)

        try:
            click_to_check_box = driver.find_element(By.CSS_SELECTOR, "[aria-label='dismiss cookie message']")
            click_to_check_box.click()
            time.sleep(3)
        except (ElementNotInteractableException, NoSuchElementException, TimeoutException, UnexpectedAlertPresentException):
            print('No cookie message to dismiss')

        try:
            driver.execute_script("window.scrollBy(0, 450);")
            time.sleep(3)
        except (ElementNotInteractableException, NoSuchElementException):
            print('Error scrolling')

        try:
            wait = WebDriverWait(driver, 3)
            click_product_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.sps2-pdp_pSelector--selectors_btn")))
            driver.execute_script("arguments[0].click();", click_product_button)
            time.sleep(2)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            print(f" Error -- {e} -- ")

        l3_name = ''
        try:
            bread = [l3.text.strip() for l3 in driver.find_elements(By.CSS_SELECTOR, "ol.MMM--breadcrumbs-list li [itemprop='name']")]
            l3_name = '## '.join(bread)
            print('l3_name-----:', l3_name)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {l3_name}")


        part_number = ''
        id_3m = ''
        upc_id = ''
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, "ul.sps2-pdp_header--details_container_ids li")

            if not elements:
                print('No elements found with the given CSS selector')

            for element in elements:
                data_div = element.text.strip()
                if "Number" in data_div:
                    part_number = 'rp_' + data_div.replace('Part Number ', '')
                    print(part_number)
                elif "ID" in data_div:
                    id_3m = 'rp_' + data_div.replace('3M ID ', '')
                    print(id_3m)
                elif "UPC" in data_div:
                    upc_id = 'rp_' + data_div.replace('UPC ', '')
                    print(upc_id)
                else:
                    print('No matching data found')

        except NoSuchElementException as e:
            print(f'Exception occurred: {e}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')


        product_title = []
        try:
            product_title = driver.find_element(By.CSS_SELECTOR, "h1.sps2-pdp_header--name").text.strip()
            print('product_title-----: ', product_title)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {product_title}")

        images = []
        try:
            images = [{'src': img.get_attribute('src'), 'alt': img.get_attribute('alt')} for img in driver.find_elements(By.CSS_SELECTOR, "div.sps2-pdp_gallery--box img")]
            print('images-----: ', images)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {images}")

        Highlights = []
        try:
            Highlights = [high.text.strip() for high in driver.find_elements(By.CSS_SELECTOR, "ul.sps2-pdp_details--highlights_list li")]
            print('Highlights -----: ', Highlights)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {Highlights}")

        feature = []
        try:
            feature = [fea.text.strip() for fea in driver.find_elements(By.CSS_SELECTOR, "div.sps2-pdp_details--upper_details")]
            print('feature-----:', feature)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {feature}")

        table_dict = []
        try:
            rows = driver.find_elements(By.CSS_SELECTOR, "table.mds-dataTable tbody tr")
            table_dict = []
            for row in rows:
                tab = [cell.text.strip() for cell in row.find_elements(By.CSS_SELECTOR, "td")]
                if len(tab) == 2:
                    key, value = tab
                    table_dict.append({key: value})
            print('table_dict-----:', table_dict)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {table_dict}")

        datasheet = []
        try:
            datasheet = [pdf.get_attribute('href') for pdf in driver.find_elements(By.CSS_SELECTOR, "a.sps2-pdp_pSelector--dataSheets-mb-16")]
            if not datasheet:
                datasheet = [pdf.get_attribute('href') for pdf in driver.find_elements(By.CSS_SELECTOR, "div.mds-prodBar_item--link")]
            print('datasheet', datasheet)
        except (NoSuchElementException, AttributeError, TypeError, ValueError, IndexError, Exception) as e:
            print(f"Error{e} {datasheet}")

        data = [url, l3_name, product_title, images, Highlights, feature, table_dict, datasheet, part_number, id_3m, upc_id]
        final_data.append(data)
        df = pd.DataFrame(final_data)
        df.to_csv('3m_data_pk.csv', mode='a', header=not pd.io.common.file_exists('3m_data_pk.csv'), index=False)
        try:
            scrollable_container = driver.find_element(By.CSS_SELECTOR, ".mds-dataTable_container")
            buttons = scrollable_container.find_elements(By.CSS_SELECTOR, "button.sps2-pdp_no-style-btn")
            for button in buttons:
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                driver.execute_script("arguments[0].click();", button)
                time.sleep(1)
        except:
            pass

        hrefs_list = []
        imgs_list = []
        id_3m = []
        upc = []
        number = []
        tr_values = []

        rows = driver.find_elements(By.CSS_SELECTOR, "tbody.mds-dataTable_body.body tr")
        for row in rows:
            row_text = row.text.strip().replace("\n", ">>").replace("3M ID>>", "3M ID ").replace("UPC>>", "UPC ").replace(
                "3M Product Number>>", "3M Product Number ").replace("Part Number", "").split(">>")

            columns = row.find_elements(By.TAG_NAME, 'td')
            column_texts = [col.text.strip() for col in columns]
            tr_value = '>>'.join(column_texts).split('>>')[1:]
            # tr_value_row = '>>>>'.join(tr_value)
            # row_list = tr_value_row.split('>>>>')

            temp_id_3m = None
            temp_upc = None
            temp_number = None
            temp_hrefs = []
            temp_img = []
            hrefs = [link.get_attribute("href") for link in row.find_elements(By.CSS_SELECTOR, "div.sps2-pdp_product-options--name_ids a.mds-link.mds-link_primary")]
            temp_hrefs.extend(hrefs)
            image_tag = [img.get_attribute('src') for img in row.find_elements(By.CSS_SELECTOR, "div.sps2-pdp_product-options--name_ids_first-row-img-container img")]
            temp_img.extend(image_tag)

            for text in row_text:
                if "3M ID" in text:
                    temp_id_3m = text.strip()
                elif "UPC" in text:
                    temp_upc = 'rp_' + text.strip()
                elif "Number" in text:
                    temp_number = 'rp_' + text.strip()

            id_3m.append(temp_id_3m)
            upc.append(temp_upc)
            number.append(temp_number)
            hrefs_list.append(temp_hrefs)
            imgs_list.append(temp_img)
            tr_values.append(tr_value)

        data_save = {
            'URL': [url] * len(id_3m),
            'l3_name': [l3_name] * len(id_3m),
            'product_title': [product_title] * len(id_3m),
            'images': [str(images)] * len(id_3m),
            'Highlights': [str(Highlights)] * len(id_3m),
            'feature': [str(feature)] * len(id_3m),
            'table_dict': [str(table_dict)] * len(id_3m),
            'Image_2': [', '.join(imgs) if imgs else 'None' for imgs in imgs_list],
            'hrefs': [', '.join(hrefs) if hrefs else 'None' for hrefs in hrefs_list],
            '3M ID': id_3m,
            'UPC': upc,
            'Product Number': number,
            'tr_value_row': [" ' , '".join(row) for row in tr_values]
        }
        print(data_save)
        df = pd.DataFrame(data_save)
        # Append DataFrame to CSV
        # df.to_csv('3m_data_d.csv', mode='a', header=not pd.io.common.file_exists('3m_data_d.csv'), index=False)
        # print('Data saved into CSV')


    driver.quit()


Product_details()
