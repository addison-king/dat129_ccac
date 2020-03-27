"""
Brandyn Gilbert
    Wed Mar 25 19:23:07 2020
    Python 2 - DAT-129 - Spring 2020
    Homework #####
    TITLE OF HOMEWORK
"""
#PLAN

import urllib
from bs4 import BeautifulSoup

def getSearchURL(term, number):
# assembles a query against goodreads.com give a search term
    #url = 'https://www.goodreads.com/search?query=%s' % (str(term))
    url = 'https://www.goodreads.com/search?page=%d&qid=gI6LAXCK22&query=%s' % (number, str(term))
    return url

def getPageText(url):
# Given a URL, fetches the raw HTML

    # build the request object from the given URL
    req = urllib.request.Request(url)
    # access the network via computer's standard gateway to actually retrieve the HTML from goodreads server
    with urllib.request.urlopen(req) as response:
        return response.read()

def main():

    term = 'pokemon'
    number = 1
    totaltitles = 0
    subtitles = 0
    i = 1
    while i < 6:
        print('Page:', i, '...', end='')
        url = getSearchURL(term, i)
        pageText = getPageText(url)

        soup = BeautifulSoup(pageText, 'html.parser')
        bookatags = soup.find_all('a', 'bookTitle')

        for book in bookatags:
            title = book.find('span').string
            # print('\t', title)
            totaltitles += 1
            if ":" in title:
                subtitles += 1
        print(' Done')
        # print('~~~~~~~~~~~~~~~~~~~~~Page:', i,'~~~~~~~~~~~~~~~~~~~~~')
        i += 1
    print('\nTotal titles: ', totaltitles)
    subts = int(subtitles/totaltitles*100)
    print(subtitles, 'books contain a subtitle')
    print(subts, '% of books have subtitles', sep='')

if __name__ == "__main__":
    main()
