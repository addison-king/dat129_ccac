"""
Brandyn Gilbert
    Wed Mar 25 19:23:07 2020
    Python 2 - DAT-129 - Spring 2020
    Lecture Notes
"""
#PLAN

import urllib
from bs4 import BeautifulSoup

def _get_search_url():
    url = 'https://boardgamegeek.com/browse/boardgame'
    return url

def _get_page_text(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read()

def _beautifulsoup(pageText):
    soup = BeautifulSoup(pageText, 'html.parser')
    return soup

def _get_urls_from_soup(soup):
    raw_page = soup.find_all('td', 'collection_thumbnail')
    url_list = []
    for page in raw_page:
        href = page.find('a', href = True)
        url = 'https://boardgamegeek.com' + href['href']
        url_list.append(url)
    return url_list



def main():

    url = _get_search_url()
    pageText = _get_page_text(url)
    soup = _beautifulsoup(pageText)
    url_list = _get_urls_from_soup(soup)

    for i in url_list:
        secondary_page_text = _get_page_text(i)
        secondary_soup = _beautifulsoup(secondary_page_text)
        f= open("soup2.txt","w+")
        soup22 = str(secondary_soup)
        f.write(soup22)
        f.close()
        input()




if __name__ == "__main__":
    main()
