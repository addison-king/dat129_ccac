"""
Brandyn Gilbert
    Wed Apr  1 07:06:33 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 8
    HTML Scraping
"""
#PLAN
## https://www.goodreads.com/shelf/show/mystery


import urllib
from bs4 import BeautifulSoup

def getSearchURL(term, number):
    url = 'https://www.goodreads.com/shelf/show/%s?page=%d' % (str(term), number)
    return url

def getPageText(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    req = urllib.request.Request(url, headers = headers)

    with urllib.request.urlopen(req) as response:
        return response.read()

def main():
    genres = [
'Art', 'Biography', 'Business', 'Chick-Lit', 'Children-s', 'Christian',
'Classics', 'Comics', 'Contemporary', 'Cookbooks', 'Crime', 'Ebooks',
'Fantasy', 'Fiction', 'lgbt', 'Graphic-Novels',
'Historical-Fiction', 'History', 'Horror', 'Humor', 'Manga',
'Memoir', 'Music', 'Mystery', 'Nonfiction', 'Paranormal', 'Philosophy',
'Poetry', 'Psychology', 'Religion', 'Romance', 'Science', 'Science-Fiction',
'Self-Help', 'Suspense', 'Spirituality', 'Sports', 'Thriller', 'Travel',
'Young-Adult']

    counter = 0

    while counter < len(genres):
        author_counter = {}
        term = genres[counter]
        i = 1

        while i < 3:
            print(genres[counter], 'Page:', i, '...', end='')

            url = getSearchURL(term, i)
            pageText = getPageText(url)
            soup = BeautifulSoup(pageText, 'html.parser')

            bookatags = soup.find_all('a', 'authorName')

            for book in bookatags:
                author = book.find('span').string
                # print('\t', author)
                if author not in author_counter.keys():
                    author_counter[author] = 1
                else:
                    author_counter[author] += 1
            # input()
            print(' Done')
            i += 1
        print(author_counter)
        print()
        # input()
        # for i in author_counter:
        #     print(author_counter[i])
        counter += 1

if __name__ == "__main__":
    main()
