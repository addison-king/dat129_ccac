"""
Brandyn Gilbert
    Mon Feb 24 14:12:38 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 4
    Week 04 - JSON - Mini task 1
"""
#PLAN
#   Mini task 1: Use a for loop to list all project info in a neatly formed 
#       set, like shown in the screen shot below:
# =============================================================================
# #   ***PROJECT PROFILE*** 
# #   name: BRIDGE REPAIRS 
# #   inactive: 0 
# #   fiscal year: 2017 
# #   budgeted amount: 100000.0 
# #   task description: Columbus Avenue Bridge Handicapped Ramp and 
# #       Intersection Improvements 
# #   start date: 2017-02-08 
# #   area: Engineering and Construction 
# #   asset id: Columbus Avenue Bridge asset 
# #   type: Bridge 
# #   status: Planned 
# #   id: 1850147310 
# =============================================================================
# idk..something something csv

import csv

def _greeting():
    print("Hello. This program takes in data from a .csv file, rehsapes it, then \
          prints it out nicely for you.")
    input("1: Cool, thanks!\n2: okay....\n")


def _open_csv_title():
    with open('PGH_Capital_Projects.csv', newline='') as csvfile:
    # with open('PGH_Short_Testing.csv', newline='') as csvfile:
        PGH_reader = csv.reader(csvfile)
        title = PGH_reader.__next__()
    return title

def _open_csv_contents():
    with open('PGH_Capital_Projects.csv', newline='') as csvfile:
    # with open('PGH_Short_Testing.csv', newline='') as csvfile:
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
    return rows_list      

def _printing(PGH_list, printing_keys):

    for item in PGH_list:
        print("\n***PROJECT PROFILE***")
        for i in printing_keys:
            print(i, ":", item[i])
        print("\n\n")  

def main():
    _greeting()
    keys_to_print = ["name", "inactive", "fiscal_year", "budgeted_amount", \
                     "task_description", "start_date", "area", "asset_id", \
                     "asset_type", "status", "id"]

    title = _open_csv_title()       # list with strings
    contents = _open_csv_contents() # list of lists with strings
    dict_list_full = _combine_title_contents(title, contents)
    _printing(dict_list_full, keys_to_print)
    
if __name__ == "__main__":
    main()
