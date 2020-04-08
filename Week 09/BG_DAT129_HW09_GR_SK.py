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
import sqlite3
from sqlite3 import Error

def _get_search_url(term, page_number):
    url = 'https://www.goodreads.com/search?'
    url = url + 'page=%d' % (page_number)
    url = url + '&q=%s' % (str(term))
    url = url + '&search_type=books&tab=books'
    return url

def _get_book_page_url(tag):
    link = tag.find('a', {'class', 'bookTitle'}, href=True)
    href_link = 'https://www.goodreads.com' + link['href']
    return href_link

def _get_page_text(url):
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
    print('Number of votes:', reviews[0])
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
    print('\'', title, '\'', sep='')
    return title

def _print_author_list(author):
    for i in author:
        print('\t', i, '. ', author[i], sep='')
    print()

def _get_author():
    author = {1:'Stephen King', 2:'William Shakespeare', 3:'Jane Austen',
              4:'Dean Koontz', 5:'Isaac Asimov', 6:'Agatha Christie',
              7:'Dr. Seuss', 8:'Danielle Steel', 9:'Nora Roberts',
              10:'Robert Ludlum'}

    print('Hello, please select an author to search for by entering the'
          +' corresponding number.')
    _print_author_list(author)

    while True:
        try:
            choice = int(input('Enter a number now: '))
            if choice >= 1 and choice <= 10:
                break
            else:
                print('Not a valid number!')
        except ValueError:
            print('\tThat is not a number!')

    selection = author[choice]
    selection = selection.replace(' ', '+')
    return selection

def _sql_creation():
    try:
        connection = sqlite3.connect('BG_DAT129_HW09_GR_SK.db')
    except Error:
        print(Error)

    cursor_object = connection.cursor()

    cursor_object.execute('DROP TABLE IF EXISTS Author_Data')

    cursor_object.execute('CREATE table IF NOT EXISTS Author_Data(\
                          id integer PRIMARY KEY, \
                          Author text, \
                          Title text, \
                          Page_Count integer, \
                          Average_Rating real, \
                          Number_of_Ratings integer,\
                          Number_of_Reviews integer, \
                          URL_Link text)')
    connection.close()

def _sql_fill(data):
    try:
        connection = sqlite3.connect('BG_DAT129_HW09_GR_SK.db')
    except Error:
        print(Error)

    cursor_object = connection.cursor()
    cursor_object.executemany('INSERT INTO Author_Data VALUES(?, ?, ?, ?, ?, ?, ?, ?)', data)
    connection.commit()
    connection.close()


def main():
    """
     Call many other smaller functions.

        1.  Get the search url (you can choose the author name)
        2.  Grab the page text from the website
        3.  Convert the HTML using beautifulsoup
        4.  Find the author name, make sure it matches our author
        5.  Get the url of the first resulting book from the search
        6.  Grab the page text of the specific book
        7.  Extract the title from the page, print it
        8.  Extract the number of pages the book has, print it
        9.  Extract the average rating of the book, print it
        10. Extract the number of ratings the book has, print it
        11. Extract the number of reviews the book has, print it
        12. Send all the data to a database
        13. Advance the search result page by one
        14. Return to step 1, repeat until top WHILE loop is satisfied

    Returns
    -------
    None.

    """
    counter_id = 0
    page_number = 1
    author_search = _get_author()
    author_name = author_search.replace('+', ' ')
    author_name = author_name.lower()
    author_sql = author_name.title()

    _sql_creation()

    while page_number < 2:

        url = _get_search_url(author_search, page_number)

        page_text = _get_page_text(url)
        soup = BeautifulSoup(page_text, 'html.parser')

        parent_tag = soup.find_all('tr', {'itemtype':'http://schema.org/Book'})
        for tag in parent_tag:
            author = tag.find('a', 'authorName').text
            if author.lower() == author_name:
                counter_id += 1
                href_link = _get_book_page_url(tag)
                print('\n', href_link, sep='')

                page_text_2 = _get_page_text(href_link)
                title = _extract_title(page_text_2)
                page_count = _extract_page_count(page_text_2)
                print('Number of pages:', page_count)
                avg_rating = _extract_avg_rating(page_text_2)
                rating_count = _extract_rating_count(page_text_2)
                review_count = _extract_review_count(page_text_2)

                data = [(counter_id, author_sql, title, page_count, avg_rating,
                        rating_count, review_count, href_link)]
                _sql_fill(data)
        page_number += 1

if __name__ == "__main__":
    main()
