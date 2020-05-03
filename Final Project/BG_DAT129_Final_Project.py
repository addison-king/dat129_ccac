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
    _create_db_table()
    _scrape_series(auth_headers)

def _create_db_table():
    sql_table = '''CREATE table IF NOT EXISTS TV_Series (
                        id integer,
                        seriesId text,
                        seriesName text,
                        aliases text,
                        season integer,
                        poster text,
                        banner text,
                        fanart text,
                        status text,
                        firstAired text,
                        network text,
                        networkId text,
                        runtime text,
                        language text,
                        genre text,
                        overview text,
                        lastUpdated text,
                        airsDayOfWeek text,
                        airsTime text,
                        rating text,
                        imdbId text,
                        zap2itId text,
                        added text,
                        addedBy text,
                        siteRating text,
                        siteRatingCount text,
                        slug text
                        )'''
    connection = _db_connection()
    c = connection.cursor()
    c.execute(sql_table)
    connection.commit()
    connection.close()

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

def _get_api_json(start_num, headers):
    url = 'https://api.thetvdb.com/series/'+ str(start_num)
    r = requests.get(url, headers=headers)
    text = r.json()
    return text

def _db_error_id(start_num):
    print('\nError ID -', start_num)
    n_lis = [start_num, None, None, None, None, None, None, None, None, 
           None, None, None, None, None, None, None, None, None, None, 
           None, None, None, None, None, None, None, None]
    n_tup = tuple(n_lis)
    
    connection = _db_connection()
    c = connection.cursor()
    c.execute('''INSERT INTO TV_Series VALUES
              (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
              n_tup)
    connection.commit()
    connection.close()

def _db_max_value():
    connection = _db_connection()
    c = connection.cursor()
    c.execute('''SELECT MAX(id)
                 FROM TV_Series''')
    rows = c.fetchall()

    for i in rows:
        for j in i:
            if j == None:
                j = 1
            else:
                j += 1
    connection.close()

    return j

def _scrape_series(headers):

    # first_series_id = 70326,
    # start_num = first_series_id
    start_num = _db_max_value()
    scraping_length = 54432
    end_num = start_num + scraping_length
      
    while start_num < end_num:
        
        text = _get_api_json(start_num, headers)

        if 'Error' in text.keys():
            _db_error_id(start_num) 
            
            start_num += 1
            
                    
        else:
            print('\nGood ID -', start_num)
            start_num += 1
        
            text2 = text['data']
            
          # convert the list of genres to a string  
            genres = text2['genre']
            genre_str = ', '.join(genres)
            text2['genre'] = genre_str
          # convert the list of aliases to a string
            aliases = text2['aliases']
            alias_str = ', '.join(aliases)
            text2['aliases'] = alias_str
    
            columns = ', '.join(str(x).replace('/', '_') for x in text2.keys())
            values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in text2.values())
        
            res = tuple(list(text2.values()))
            
                        
            columns = ', '.join("'" + str(x).replace('/', '_') + "'" for x in text2.keys())
            sql_insert = ''''INSERT INTO %s (%s) VALUES %s''' % ('TV_Series', columns, res)
            
            connection = _db_connection()
            c = connection.cursor()
            
            c.execute('''INSERT INTO TV_Series VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', res)
            print('\tData inserted')
            connection.commit()
            connection.close()





if __name__ == "__main__":
    main()
