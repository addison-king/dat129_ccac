"""
Brandyn Gilbert
    Wed Mar 25 19:23:07 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 8
    Week 08 - HTML webscraping
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

def _analyze_html(term):
    title_length = 0
    title_count = 0
    i = 1
    while i < 11:
        print('\tPage:', i, '...', end='')
        url = getSearchURL(term, i)
        pageText = getPageText(url)
        soup = BeautifulSoup(pageText, 'html.parser')
        bookatags = soup.find_all('a', 'bookTitle')

        for book in bookatags:
            title = book.find('span').string
            a_len = len(title)
            title_length += a_len
            title_count += 1

        print(' \tDone')
        i += 1
    results = {title_count:title_length}
    return results

def _create_dictionary(terms):
    dictionary = {}
    for i in terms:
        dictionary[i] = 0
    return dictionary

def _analyze_dictionary(dict_terms):
    for j in dict_terms:
        results_dict = _analyze_html(j)
        for i in results_dict:
            title_length = results_dict[i]
            title_count = i

        title_avg = title_length / title_count
        title_avg = int(title_avg)
        dict_terms[j] = title_avg
    return dict_terms

def _print_results(dict_terms2):
    print()
    for i in dict_terms2:
        print(i.title(),'on average, has ', end='')
        print(dict_terms2[i], 'words per book title.\n')

def main():
    terms = ['python', 'java', 'html', 'javascript']
    dict_terms = _create_dictionary(terms)
    dict_terms2 = _analyze_dictionary(dict_terms)
    _print_results(dict_terms2)

if __name__ == "__main__":
    main()
