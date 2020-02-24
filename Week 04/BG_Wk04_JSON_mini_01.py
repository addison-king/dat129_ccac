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
# idk..something something json

import csv

def _open_csv():
    # with open('PGH_Capital_Projects.csv', newline='') as csvfile:
    with open('PGH_Short_Testing.csv', newline='') as csvfile:
        PGH_reader = csv.reader(csvfile)
        title = PGH_reader.__next__()
        
        for row in PGH_reader:
            print(row)
            input()


    return title
def main():
    title = _open_csv()
    print("__________________________")
    print(title)
    
    
if __name__ == "__main__":
    main()
