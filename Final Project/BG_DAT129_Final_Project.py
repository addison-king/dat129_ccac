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
        New TV Series per decade
        Number of shows per season count
        Average runtime
'''

import requests
import json
import sqlite3
from sqlite3 import Error
import pandas as pd


def main():
    auth_headers = _get_token()
    _create_db_table()
    main_user_choice = _main_menu()
    if main_user_choice == 1:
        _scrape_series(auth_headers)
    else:
        _db_analysis()

def _main_menu():
    '''
    Asks the user what they would like to do.

    Returns
    -------
    choice : int
        The users choice to be used in an if statement.

    '''
    print('1. Scrape more from TheTVDB.com')
    print('2. Analyze the database')
    choice = input("Please choose an option: ")
    choice = int(choice)
    return choice

def _create_db_table():
    '''
    Creates a table if it doesn't exist.

    Returns
    -------
    None.

    '''
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
    '''
    Connects to the .db file

    Returns
    -------
    connection : sqlite db connection
        
    '''
    try:
        connection = sqlite3.connect('BG_DAT129_Final_Project.db')
    except Error:
        print(Error)
    return connection

def _get_token():
    '''
    Builds the API token needed for TheTVDB

    Returns
    -------
    auth_headers : str
        Headers used to access the API.

    '''
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
    '''
    Builds the URL for the API, gets the data, then breaks it down into a 
        python/JSON format

    Parameters
    ----------
    start_num : int
        First ID to scrape.
    headers : str
        Headers used to access the API..

    Returns
    -------
    text : dict
        json text of the resulting API request.

    '''
    url = 'https://api.thetvdb.com/series/'+ str(start_num)
    r = requests.get(url, headers=headers)
    text = r.json()
    return text

def _db_error_id(start_num):
    '''
    If the ID doesn't exist/isn't valid, this inserts a row with the ID followed
        by "NULL" for all columns

    Parameters
    ----------
    start_num : int
        The ID currently being scraped.

    Returns
    -------
    None.

    '''
    print('\nError ID -', start_num)
    n_lis = [start_num, None, None, None, None, None, None, None, None, 
           None, None, None, None, None, None, None, None, None, None, 
           None, None, None, None, None, None, None, None]
    n_tup = tuple(n_lis)
    
    connection = _db_connection()
    c = connection.cursor()
    c.execute('''INSERT INTO TV_Series VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
              n_tup)
    connection.commit()
    connection.close()

def _db_max_value():
    '''
    Queries the DB for the max ID that is stored.
    This number is then used to scrape more series without duplicates.

    Returns
    -------
    j : int
        max id value.

    '''
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
    '''
    1. Checks the ID value to see if a series exist or not. 
    2. Good IDs will: 
        a. convert 'genre' and 'aliases' values to str
        b. takes all of the dict values >> list >> tuple
        c. takes said tuple and inserts it into the DB
    

    Parameters
    ----------
    headers : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

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
    
            res = tuple(list(text2.values()))
          
            connection = _db_connection()
            c = connection.cursor()
            
            c.execute('''INSERT INTO TV_Series VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', res)
            print('\tData inserted')
            connection.commit()
            connection.close()

def _db_number_of_seasons():
    '''
    Queries the DB for 'season' which is not empty and under 101
    Each value is added to a list
    List to DataFrame
    Send the DF to be graphed

    Returns
    -------
    None.

    '''
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
    '''
    LOOKING AT TV SHOWS OVER DECADES
    
    Builds strs that will act as lower & upper bounds for dates
    Queries the DB with the built dates
    All values are stored into a list
    List to DataFrame
    DataFrame output graph

    Returns
    -------
    None.

    '''

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
    '''
    LOOKING AT TV SHOWS PER YEAR
    
    Builds strs that will act as lower & upper bounds for dates
    Queries the DB with the built dates
    All values are stored into a list
    List to DataFrame
    DataFrame output graph
    
    Returns
    -------
    None.

    '''
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
    '''
    Queries the DB for runtime values
    Adds all values as int to list
    List to DataFrame
    Output the result to console

    Returns
    -------
    None.

    '''
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
    '''
    Calls other functions to do DB stuff

    Returns
    -------
    None.

    '''
    print('\n\n')
    _db_number_of_seasons()
    _db_decades()
    _db_years()
    _db_runtime()

def _graph_seasons_histogram(df):
    '''
    Graphs the histogram for number of seasons per TV Show

    Parameters
    ----------
    df : pandas dataframe
        Number of seasons for each tv show.

    Returns
    -------
    None.

    '''
    hist_ax = df.plot.hist(logy=True, figsize=(20,10), grid=True, bins=50)
    hist_ax.set_xlabel('Number of Seasons')
    hist_ax.set_ylabel('Frequency')
    hist_ax.set_title('Television Series Divided by Number of Seasons per Show')
    hist_ax.set_xticks([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])

    hist_ax.get_legend().remove()
    print(hist_ax)

if __name__ == "__main__":
    main()
