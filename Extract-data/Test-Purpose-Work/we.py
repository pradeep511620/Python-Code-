import pandas as pd
import requests
import csv
import time
import threading
import concurrent.futures

MAX_RETRIES = 3


def get_response_code(URL):
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = requests.get(URL, timeout=10)  # Timeout set to 10 seconds
            if response.status_code == 200:
                return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        retries += 1
        print(f"Retry {retries}...")
        time.sleep(1)


# Function to execute the script for a given brand_id
def execute_script_for_brand(row, brand_id):
    # Read the Excel file for the brand_id

    cols = ['Entity ID', 'Landing Page', 'xyz URL', 'pqr URL', 'Brand ID', 'Brand', 'Res 1', 'Res 2']
    flag = 0
    # Iterate over each row and crawl the URLs

    rows = []

    URL1 = row['xyz url']  # Assuming the first URL is in the 'xyz URL' column
    URL2 = row['pqr url']  # Assuming the second URL is in the 'pqr URL' column
    print(URL1)
    flag += 1
    print(flag)
    response_code1 = get_response_code(URL1)
    print(response_code1)
    response_code2 = get_response_code(URL2)
    print(response_code2)
    if response_code1 is not None and response_code1 != 404:
        # if response_code1 is not None:
        rows.append({
            'Entity ID': row['entity_id'],
            'Landing Page': row['Landing Page'],
            'xyz URL': row['xyz url'],
            'pqr URL': row['pqr url'],
            'brand_id': row['brand_id'],
            'brand': row['brand'],
            'Res 1': response_code1,
            'Res 2': response_code2
        })
        d = pd.DataFrame(rows, columns=cols)

        # Save the modified DataFrame to a CSV file named after the brand_id
        d.to_csv(f'pradeep/{brand_id}.csv', mode='a', header=False, index=False, sep=',', quotechar='"',
                 quoting=csv.QUOTE_MINIMAL)

        # Increment the request counter

    # Check if 10 requests have been made, then pause for 500 milliseconds
    if flag % 5 == 0:
        time.sleep(2)  # Pause for 500 milliseconds


brand_ids = [

    # 466000,
    # 466004,
    # 466021,
    # 466027,
    # 466031,
    466044,
    466048,

]

for file in brand_ids:
    df = pd.read_excel(f'pradeep/pradeep/{file}.xls')
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Submit each download task to the thread pool
        futures = [executor.submit(execute_script_for_brand, row, file) for index, row in df.iterrows()]

        # Wait for all tasks to complete and retrieve the results
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
