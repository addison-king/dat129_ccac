"""
Brandyn Gilbert
    Wed Apr  1 11:16:29 2020
    Python 2 - DAT-129 - Spring 2020
    Homework #####
    TITLE OF HOMEWORK
"""
#PLAN
import urllib
from bs4 import BeautifulSoup
import re

def _get_Search_URL(term, page_number):
    url = 'https://www.goodreads.com/search?page=%d&qid=MpPJ3DuY5H&query=%s&tab=books' % (page_number, str(term))

    return url

def _get_Page_Text(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)

    return response.read()

def main():
    page_number = 1
    average = 0
    votes = 0
    counter = 0

    while page_number < 6:
        author = 'Stephen-King'
        url = _get_Search_URL(author, page_number)

        pageText = _get_Page_Text(url)
        soup = BeautifulSoup(pageText, 'html.parser')

        parent_tag = soup.find_all('tr', {'itemtype':'http://schema.org/Book'})
        for tag in parent_tag:
            author = tag.find('a', 'authorName').text
            if author.lower() == 'stephen king':
                counter += 1

                rating = tag.find('span', {'class' : 'minirating'}).text
                avg_rating = rating.split(' avg rating — ')

                for i in avg_rating:
                    i = i.replace(',', '')
                    i = i.split()

                    for j in i:
                        try:
                            floaters = float(j)
                            if len(str(floaters)) < 5:
                                average = average + floaters
                            else:
                                votes = votes + floaters

                        except ValueError:
                            pass


        page_number -=- 1

    votes = int(votes)
    print('In total, across', counter, 'books Stephen King has: ')
    print('\tTotal votes:    ', f'{votes:,}')

    # print('Total average:  ', average)
    real_avg = str(round(average / counter, 2))
    print('\tAverage rating: ', real_avg)


if __name__ == "__main__":
    main()
