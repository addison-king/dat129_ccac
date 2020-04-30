"""
Brandyn Gilbert
    Sun Apr 26 08:55:31 2020
    Python 2 - DAT-129 - Spring 2020
    Final Project
    API & Databases
"""
import requests
import json
import os
import sqlite3
from sqlite3 import Error

def main():
    auth_headers = _get_token()
    _scrape_series(auth_headers)


def _db_connection():
    try:
        connection = sqlite3.connect('BG_DAT129_Final_Project.db')
    except Error:
        print(Error)
    return connection

def _get_token():
    header = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    data = '{\n "apikey": "f538d2864846dd50a311ad8542b40f7d",\
          \n  "userkey": "XCXVRW13LTK0XFJY",\
          \n  "username": "falconfoe"\n}'

    response = requests.post('https://api.thetvdb.com/login',
                          headers=header, data=data)

    r_text = response.text
    rj_text = json.loads(r_text)
    token = rj_text['token']
    token_auth = 'Bearer '+ token

    auth_headers = {
    'Accept': 'application/json',
    'Authorization': token_auth,
    }

    return auth_headers

def _scrape_series(headers):
    max_count = 0

    first_series_id = 70327
    start_num = first_series_id
    scraping_length = 1
    end_num = start_num + scraping_length

    while start_num < end_num:
        max_count += 1
        print(start_num)

        url = 'https://api.thetvdb.com/series/'+ str(start_num)

        r = requests.get(url, headers=headers)
        start_num += 1

        text = r.json()
        text2 = text['data']
        print(text2)
        for i in text2:
            print(i)
        connection = _db_connection()
        c = connection.cursor()
        connection.close()
# =============================================================================
#         print(text2['seriesName'])
#         genres = text2['genre']
#         for i in genres:
#             print ('\t', i)
#         print(text2['overview'])
# =============================================================================




if __name__ == "__main__":
    main()
