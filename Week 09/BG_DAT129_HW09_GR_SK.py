"""
Brandyn Gilbert
    Thu Apr  2 09:52:23 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 9
    HTML Scraping - EXPANDED
"""
#PLAN
# Extract link from search page
# Send link to _get_Page_Text
# BeautifulSoup it
# EXTRACT: Rating, Ratings, Reviews, Title, Page Count
# Send all that data to a database
# ????
# Profit


import urllib
from bs4 import BeautifulSoup
import re

def _get_Search_URL(term, page_number):
    url = 'https://www.goodreads.com/search?page='
    url = url + '%d&qid=MpPJ3DuY5H&query=%s&tab=books' % (page_number, str(term))
    return url

def _get_book_page_url(tag):
    link = tag.find('a', {'class', 'bookTitle'}, href=True)
    href_link = 'https://www.goodreads.com' + link['href']
    return href_link

def _get_Page_Text(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return response.read()

def _extract_avg_rating(page_text):
    soup = BeautifulSoup(page_text, 'html.parser')
    rating = soup.find('span', {'itemprop':'ratingValue'}).string
    rating = rating.strip()
    print('Average rating:', rating)
    return rating

def _extract_rating_count(page_text):
    soup = BeautifulSoup(page_text, 'html.parser')
    review_tag = soup.find('div', 'reviewControls--left greyText').text
    review_tag = review_tag.replace(',', '')
    review_tag = review_tag.replace('·', '')
    reviews = review_tag.split()

    print('Number of rating votes:', reviews[0])
    return reviews[0]

def _extract_review_count(page_text):
    soup = BeautifulSoup(page_text, 'html.parser')
    review_tag = soup.find('div', 'reviewControls--left greyText').text
    review_tag = review_tag.replace(',', '')
    review_tag = review_tag.replace('·', '')
    reviews = review_tag.split()

    print('Number of book reviews:', reviews[2])
    return reviews[2]

def _extract_page_count(page_text):
    soup = BeautifulSoup(page_text, 'html.parser')
    page_tag = soup.find('span', {'itemprop':'numberOfPages'}).text
    i = page_tag.split()
    for j in i:
        try:
            floaters = int(j)
        except ValueError:
            pass
    return floaters

def _extract_title(page_text):
    soup = BeautifulSoup(page_text, 'html.parser')
    title = soup.find('h1', 'gr-h1 gr-h1--serif').text
    title = title.strip()
    print('\'',title,'\'', sep='')
    return title



def main():
    page_number = 1
    average = 0
    votes = 0
    counter = 0

    while page_number < 2:
        author = 'Stephen-King'
        url = _get_Search_URL(author, page_number)

        pageText = _get_Page_Text(url)
        soup = BeautifulSoup(pageText, 'html.parser')

        parent_tag = soup.find_all('tr', {'itemtype':'http://schema.org/Book'})
        for tag in parent_tag:
            author = tag.find('a', 'authorName').text
            if author.lower() == 'stephen king':

                href_link = _get_book_page_url(tag)
                print('\n', href_link)

                page_text_2 = _get_Page_Text(href_link)
                # soup2 = BeautifulSoup(page_text_2, 'html.parser')
                # parent_tag2 = soup2.find_all('div', 'uitext stacked')
                #print(parent_tag2)
                _extract_title(page_text_2)
                page_count = _extract_page_count(page_text_2)
                print('Number of pages:', page_count)
                _extract_avg_rating(page_text_2)
                _extract_rating_count(page_text_2)
                _extract_review_count(page_text_2)






        page_number -=- 1



























if __name__ == "__main__":
    main()
