"""
Brandyn Gilbert
    Fri Mar  6 07:20:38 2020
    Python 2 - DAT-129 - Spring 2020
    Homework #####
    TITLE OF HOMEWORK
"""
#PLAN

import pandas as pd
import json

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

def main():

    _json_manipulation()


if __name__ == "__main__":
    main()
