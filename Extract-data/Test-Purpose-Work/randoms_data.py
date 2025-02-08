
import pandas as pd
import re
def find_unique_urls1():
    file_path1 = "D:/Web-Scrapping/Test-Purpose-Work/scraped_urls.csv"
    urls1 = pd.read_csv(file_path1)['URL']
    pattern = re.compile(r'\d+\.html$')

    for url in urls1:
        if pattern.search(url):
            with open('text.csv', 'a+', encoding='utf-8') as file:
                file.write(f"{url}\n")


find_unique_urls1()
