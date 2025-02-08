from itertools import zip_longest

import pandas as pd


def find_unique_urls1():
    file_path1 = r"P:\Web-scrapings\A-MONTH-2024\Sep\Store-hipco-Brand-Flowline.com\url\Product-url.csv"
    file_path2 = r"P:\Web-scrapings\A-MONTH-2024\Sep\Store-hipco-Brand-Flowline.com\url\Product-url - Copy.csv"

    # Read URLs from both CSV files
    urls1 = pd.read_csv(file_path1, encoding='latin1')['URL']
    urls2 = pd.read_csv(file_path2)['URL']

    # Convert to sets
    set_urls1 = set(urls1)
    set_urls2 = set(urls2)

    # Find unique URLs
    unique_to_file1 = set_urls1 - set_urls2
    unique_to_file2 = set_urls2 - set_urls1

    # Combine all unique URLs
    unique_urls = unique_to_file1.union(unique_to_file2)

    if unique_urls:
        print('Unique URLs:')
        for url in unique_urls:
            print(url)
    else:
        print('No unique URLs found.')


# find_unique_urls1()




def find_unique_urls():
    # File paths
    file_path1 = r"P:\Web-scrapings\A-MONTH-2024\Sep\Store-hipco-Brand-Flowline.com\url\Product-url.csv"
    file_path2 = r"P:\Web-scrapings\A-MONTH-2024\Sep\Store-hipco-Brand-Flowline.com\url\Product-url - Copy.csv"

    # Read the URLs from both files
    urls_file1 = pd.read_csv(file_path1)['URL'].dropna().tolist()
    urls_file2 = pd.read_csv(file_path2)['URL'].dropna().tolist()

    # Convert lists to sets for easier comparison
    set_file1 = set(urls_file1)
    set_file2 = set(urls_file2)

    # Find URLs that are unique to each file
    unique_to_file1 = set_file1 - set_file2
    unique_to_file2 = set_file2 - set_file1

    # Print the unique URLs
    if unique_to_file1:
        print("URLs in the first file but not in the second:")
        for url in unique_to_file1:
            print(url)
    else:
        print("No unique URLs in the first file.")

    if unique_to_file2:
        print("\nURLs in the second file but not in the first:")
        for url in unique_to_file2:
            print(url)
    else:
        print("No unique URLs in the second file.")


find_unique_urls()
