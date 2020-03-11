"""
Brandyn Gilbert
    Wed Mar  4 08:52:09 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 5
    Week 05 - APIs
"""
#PLAN
# Buffy : 70327

import requests
import json
from os import path
from json.decoder import JSONDecodeError
import pandas as pd

def main():
    user_choice = _user_greeting_choice()
    if user_choice == 1:
        auth_headers = _get_token()
        _scrape_series(auth_headers)
    elif user_choice == 2:
        _analyze_data()
    elif user_choice == 3:
        _json_manipulation()

def _user_greeting_choice():
    print("Would you like to do webscraping or calculations?")
    print("1: Webscraping\n2: Calculations\n3: Conversion (json to csv)")
    user_choice = int(input("Choice: "))
    print('\n\n')
    return user_choice

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
    ended = 0
    running = 0
    errors = 0
    jstorage = []

    if not path.exists('Series_list.json'):
        with open('Series_list.json', 'w'):
            print("Created file...")
            series_count = 0
    else:
        series_count = _get_json_length()

    first_series_id = 70327
    start_num = series_count + first_series_id
    scraping_length = _get_scraping_length()
    end_num = start_num + scraping_length

    while start_num < end_num:
        max_count += 1
        print(start_num)

        url = 'https://api.thetvdb.com/series/'+ str(start_num)

        r = requests.get(url, headers=headers)
        start_num += 1
        text = r.text
        j_text = json.loads(text)
        jstorage.append(j_text)

        if 'Error' not in j_text:
            for i in j_text:
                if j_text[i]['status'] == 'Ended':
                    ended += 1
                else:
                    running += 1
        else:
            errors += 1

    print(ended, "of", max_count, "shows are no longer airing.")
    print(running, 'of', max_count, 'shows are still airing.')
    print(errors, 'of', max_count, 'are non-valid tv series numbers.')

    with open('Series_list.json', 'r') as file_object:
        try:
            data = json.load(file_object)
            data_dump = data + jstorage
        except JSONDecodeError:
            data_dump = jstorage
# =============================================================================
# Got the above code idea at:
#     https://stackoverflow.com/questions/57191718/how-to-json-loadfilename-on-an-empty-file
# =============================================================================

    with open('Series_list.json', 'w') as out_file:
    # out_file = open('Series_list.json', 'w')
        json.dump(data_dump, out_file, indent=3)
    # out_file.close()

def _get_json_length():
    with open('Series_list.json') as file_obj:
        data = json.load(file_obj)
    length = len(data)
    # print(length)
    # input()
    return length

def _analyze_data():
    print()
    data_file = open("Series_list.json", "r")
    json_data = json.load(data_file)
    count = 0
    overall_length = _get_json_length()
    for main_dict in json_data:
        for key1 in main_dict:
            if not key1 == 'Error':
                if main_dict[key1]['status'] == 'Continuing':
                    count += 1
                    print('______________________________________')
                    print('Series Name: ',  main_dict[key1]['seriesName'])
                    print('id: ', main_dict[key1]['id'])
                    print('Status: ', main_dict[key1]['status'])


    data_file.close()
    print('======================================')
    print('======================================\n')
    print("Of the", overall_length, "series already scrapped,")
    print("there are", count, "found shows still airing.")

def _user_analyze_choice():
    print("Would you like to do webscraping or calculations?")
    print("1: Webscraping\n2: Calculations")
    user_choice = int(input("Choice: "))
    print('\n\n')
    return user_choice

def _get_scraping_length():
    print("How many series would you like to scrape?")
    print("CAUTION :: 1,000 queries takes over 3 mins.")
    user_choice = int(input("Number of series to scrape: "))
    if user_choice > 1000:
        password = input("Enter bypass password: ")
        if password != "1024":
            user_choice = 1000
            print("That is too many. I've trimmed it down to 1,000 queries.")
            input("Press ENTER to continue.")
    return user_choice

def _json_to_csv():
    df = pd.read_json(r'C:\Users\BKG\OneDrive\Desktop\GitHub\dat129_ccac\Week 05\TEMP_data.json')
    df.to_csv(r'C:\Users\BKG\OneDrive\Desktop\GitHub\dat129_ccac\Week 05\Series_list.csv', index = None)

def _json_manipulation():
    building = []
    with open('Series_list.json', 'r') as file_object:
        data = json.load(file_object)

    for row in data:
        for key in row:
            if key == 'data':
                building.append(row['data'])

    with open('TEMP_data.json', 'w') as out_file:
        json.dump(building, out_file, indent=3)
        input('built')

    _json_to_csv()

if __name__ == "__main__":
    main()
