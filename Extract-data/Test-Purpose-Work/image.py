import pandas as pd

def Read_csv_file():
    file_path = r"P:\Web-scrapings\Test-Purpose-Work\hayward.csv"
    url_links = pd.read_csv(file_path)['URL']
    print(len(url_links))
    for u in url_links:
        url_u = u.split(', ')
        for url_f in url_u:
            with open('hayward_url.csv', 'a+', encoding='utf-8') as file_save:
                file_save.write(f"\n{url_f}\n")


Read_csv_file()
