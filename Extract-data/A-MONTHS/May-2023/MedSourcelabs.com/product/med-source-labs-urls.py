import requests
from bs4 import BeautifulSoup
url = 'https://www.medsourcelabs.com/products/?sf_paged=1'


def get_url(url1):
    r = requests.get(url1)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def pagination(soup):

    for i in range(1, 22):
        url_pagination1 = f'https://www.medsourcelabs.com/products/?sf_paged={i}'
        soup1 = get_url(url_pagination1)
        print(i)
        print(url_pagination1)
        urls = soup1.find('div', class_="elementor-loop-container elementor-grid").find_all('a')
        for url_links in urls:
            url_link = (url_links.get('href'))
            print(url_link)
            save = open('med-source-labs-urls.csv', 'a+', encoding="utf-8")
            save.write("\n" + url_link)
        print('save data into url files')


def main():
    soup = get_url(url)
    pagination(soup)


main()
