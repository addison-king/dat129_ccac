"""
Brandyn Gilbert
    Sun Apr 26 08:55:31 2020
    Python 2 - DAT-129 - Spring 2020
    Final Project
    API & Databases
"""
'''
Answer the questions:
        New TV Series per year
        Average seasons per show
        Number of shows per season count
        Average runtime
'''

import requests
import json
import os
import sqlite3
from sqlite3 import Error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    auth_headers = _get_token()
    _create_db_table()
    main_user_choice = _main_menu()
    if main_user_choice == 1:
        _scrape_series(auth_headers)
    else:
        _db_analysis()

def _main_menu():
    print('1. Scrape more from TheTVDB.com')
    print('2. Analyze the database')
    choice = input("Please choose an option: ")
    return choice

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
    scraping_length = 1
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

def _db_number_of_seasons():
    connection = _db_connection()
    c = connection.cursor()
    c.execute('''
                SELECT season
                FROM TV_Series
                WHERE seriesName IS NOT NULL and season < 101
                ORDER BY season DESC 
                ''')
    rows = c.fetchall()
    connection.close()
    seasons = []
    for i in rows:
        for j in i:
            seasons.append(j)
        
    df = pd.DataFrame(seasons)
    _graph_seasons_histogram(df)

def _db_decades():

    lower_days = '-01-01'
    upper_days = '-12-31'
    decades = {}
    lower_num = 1951
    while lower_num < 2021:
        upper_num = lower_num + 9
        lower = str(lower_num) + lower_days
        upper = str(upper_num) + upper_days
        lower = '"' + lower + '"'
        upper = '"' + upper + '"'
        decade_label = lower_num - 1
        decade_label = str(decade_label) + '\'s'
        dates = lower + 'AND' + upper
        
        connection = _db_connection()
        c = connection.cursor()
        c.execute('''
                SELECT firstAired
                FROM TV_Series
                WHERE seriesName IS NOT NULL  and 
                      firstAired IS NOT NULL  and
                      firstAired != ""        and
                      firstAired BETWEEN %s 
                ORDER BY firstAired DESC 
                ''' %(dates))
        rows = c.fetchall()
        connection.close()
        years = []
        for i in rows:
            for j in i:
                years.append(j)
        
        decades[decade_label] = len(years)        

        lower_num += 10
    
    df = pd.DataFrame.from_dict(decades, orient='index')

    ax = df.plot.bar(figsize=(20,10), grid=True)
    ax.set_xlabel('Decade')
    ax.set_ylabel('Number of TV Series')
    ax.set_title('Television Series Divided by Decades')
    ax.get_legend().remove()
    print(ax)
    
def _db_years():
    lower_days = '-01-01'
    upper_days = '-12-31'
    years = {}
    lower_num = 2000
    while lower_num < 2021:
        upper_num = lower_num + 1
        lower = str(lower_num) + lower_days
        upper = str(upper_num) + upper_days
        lower = '"' + lower + '"'
        upper = '"' + upper + '"'
        year_label = str(lower_num)

        dates = lower + 'AND' + upper
        
        connection = _db_connection()
        c = connection.cursor()
        c.execute('''
                SELECT firstAired
                FROM TV_Series
                WHERE seriesName IS NOT NULL  and 
                      firstAired IS NOT NULL  and
                      firstAired != ""        and
                      firstAired BETWEEN %s 
                ORDER BY firstAired DESC 
                ''' %(dates))
        rows = c.fetchall()
        connection.close()
        year = []
        for i in rows:
            for j in i:
                year.append(j)
        
        years[year_label] = len(year)        

        lower_num += 1
    
    df = pd.DataFrame.from_dict(years, orient='index')

    ax = df.plot.bar(figsize=(20,10), grid=True)
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of TV Series')
    ax.set_title('New Television Series per Year Beginning in 2000')
    ax.get_legend().remove()
    print(ax)

def _db_runtime():
    connection = _db_connection()
    c = connection.cursor()
    c.execute('''
                SELECT runtime
                FROM TV_Series
                WHERE seriesName IS NOT NULL and 
                runtime IS NOT NULL          and
                runtime != ""
                ORDER BY runtime ASC 
                ''')
    rows = c.fetchall()
    connection.close()
    runtime = []
    for i in rows:
        for j in i:
            runtime.append(int(j))
            
        
    df = pd.DataFrame(runtime)
    df_size = df.size
    df_mean = df.mean()
    for i in df_mean:
        print('Across', df_size, 'shows, the average runtime is:', round(i, 2), 'mins.')
    

def _db_analysis():
    print('\n\n')
    # _db_number_of_seasons()
    # _db_decades()
    # _db_years()
    _db_runtime()

def _graph_seasons_histogram(df):
    hist_ax = df.plot.hist(logy=True, figsize=(20,10), grid=True, bins=50)
    hist_ax.set_xlabel('Number of Seasons')
    hist_ax.set_ylabel('Frequency')
    hist_ax.set_title('Television Series Divided by Number of Seasons per Show')
    hist_ax.set_xticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])

    hist_ax.get_legend().remove()
    print(hist_ax)

if __name__ == "__main__":
    main()
