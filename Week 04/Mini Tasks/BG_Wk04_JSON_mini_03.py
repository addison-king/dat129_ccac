"""
Brandyn Gilbert
    Tue Feb 25 14:17:21 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 4
    Week 04 - JSON - Mini task 3
"""
#PLAN
# =============================================================================
# # Mini task 3: 
# #     Create a method that assembles a list of unique values for the 
# #     project area. If you are feeling ambitious, do the same for 'status' 
# #     and 'asset type' since this will come in handy during the search 
# #     specification.
# =============================================================================

import csv
import os.path
from os import path

def _open_csv_title():
    # with open('PGH_Capital_Projects.csv', newline='') as csvfile:
    with open('PGH_Short_mini2.csv', newline='') as csvfile:
        PGH_reader = csv.reader(csvfile)
        title = PGH_reader.__next__()
    return title

def _open_csv_contents():
    # with open('PGH_Capital_Projects.csv', newline='') as csvfile:
    with open('PGH_Short_mini2.csv', newline='') as csvfile:
        PGH_reader = csv.reader(csvfile)
        contents = []
        PGH_reader.__next__()
        for row in PGH_reader:
            contents.append(row)

    return contents
    
def _combine_title_contents(title, contents):
    row_dict = {}
    rows_list = []
    for row in contents:

        i = 0
        for item in row:
            row_dict.update({title[i]:item})
            
            i += 1
        rows_list.append(row_dict)
        row_dict = {}

    return rows_list      

def _printing(PGH_list, printing_keys, errors):
    for item in PGH_list:
        print("\n***PROJECT PROFILE***")
        for i in printing_keys:
            print(i, ":", item[i])
        print("\n\n")  
    print("\nIn total, there were \"", errors,"\" errors.", sep='')
    print("\tSee the .log file in your working directory.")

def _logMalformedProject(entry_row): 
    if entry_row['name'] == '':
        file_out = open("area_empty.log", "a")
        file_out.write("id \t:" + entry_row['id'] + "\n")
        file_out.write("name \t: (name is blank)\n")
        file_out.write("_________________________________________________\n\n")
        file_out.close()
        
    else:
        file_out = open("area_empty.log", "a")
        file_out.write("id \t:" + entry_row['id'] + "\n")
        file_out.write("name \t:" + entry_row['name'] + "\n")
        file_out.write("_________________________________________________\n\n")
        file_out.close()
        
    
def _verify_dictionary(full_dictlist):
    i = 0
    for row in full_dictlist:
        if row['area'] == '':
            _logMalformedProject(row)
            i += 1
    return i

def _unique_values(full_dictlist):
    
    print()
    
def main():

    file_out = open("area_empty.log", "w")
    file_out.write('')
    file_out.close()

    keys_to_print = ["name", "inactive", "fiscal_year", "budgeted_amount", \
                     "task_description", "start_date", "area", "asset_id", \
                     "asset_type", "status", "id"]

    title = _open_csv_title()       # list with strings
    contents = _open_csv_contents() # list of lists
    dict_list_complete = _combine_title_contents(title, contents)
    errors = _verify_dictionary(dict_list_complete)
    _unique_values(dict_list_complete)
    _printing(dict_list_complete, keys_to_print, errors)

if __name__ == "__main__":
    main()