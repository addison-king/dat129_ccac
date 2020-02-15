"""
Brandyn Gilbert
    Wed Feb 12 20:03:15 2020
    Python 2 - DAT-129 - Spring 2020
    IN CLASS
    Dict's & JSON & Data Sets
"""
# =============================================================================
# PLAN
#   Iterates over Allegheny county jail census data to tabulate inmates by race
#   Using the file 'jail201906.csv'
#   "To what degree does the inmate pop by race reflect the composition
#       of the county?"
# =============================================================================
import csv

##    This commented out block below is an example for reading the .csv file,
##       presented to us in class. Not needed since it was rewrote.
# =============================================================================
# def process_CSV():
#     file = open('test2.csv', newline='')
#     # read_file = file.read()
#     reader = csv.DictReader(file)
#     race_count = {'B': 0, 'W': 0}
#     focus_date = '6/1/2019'
#
#     for row in reader:
#         print('HERE')
#         if row['Date'] == focus_date:
#             # ask dictionary if race key is present
#             if row['Race'] == 'B':
#                 race_count['B'] = race_count['B'] + 1
#             elif row['Race'] == 'W':
#                 race_count['W'] = race_count['W'] + 1
#     file.close()
#     return(race_count)
# =============================================================================

def _new(focus_date):
    '''
    Open the csv file, call csv.DictReader on the now open file
    Create an empty dict to add to.

    1st `for` loop: (creating a dict for us to process/count)
        look at the first line of the OrderedDict
        if the length of the first line, subsection 'Race', is >0, add to dict

    "file.seek(0)" is used to go back to the top of the file/OrderedDict

    2nd `for` loop: (looking at lines that only have our date in it):
        look at the first line of the OrderedDict
        if the line, subsection 'Date', is the date we want:
            if the line, subsection 'Race', is in our dict called 'races':
                add 1 to the value for the corresponding key
                (example: 'B' is the race in the OrderedDict : +1 to our dict)

    Args:
        focus_date (str): Contains the date for printing.

    Returns:
        None.

    '''
    file = open("jail.csv", newline='')
    input_file = csv.DictReader(file)
    races = {}

    for row in input_file:
        if len(row['Race']) > 0:
            if row['Race'] not in races:
                races[row['Race']] = 0
    file.seek(0)
    for row in input_file:
        if row['Date'] == focus_date:
            if row['Race'] in races:
                races[row['Race']] += 1
    return races

##        This commented out block below is from in-class. Not needed since it
##        was originally hardcoded, instead of modular.
# =============================================================================
#     file.seek(0)
#     race_count = {'B':0, 'W':0}
#     for row in input_file:
#         if row['Date'] == focus_date:
#             if row['Race'] == 'B':
#                 race_count['B'] = race_count['B'] + 1
#             if row['Race'] == 'W':
#                 race_count['W'] = race_count['W'] + 1
# =============================================================================

def _print_totals(totals, focus_date):
    '''
    Prints the results in a nice, user-friendly fashion

    Args:
        totals (dict): A dictionary where each KEY is a race, and
                       each VALUE is the population of that race.
        focus_date (str): Contains the date for printing.

    Returns:
        None.

    '''
    print("On the chosen day, ", focus_date, ", here is the census from",
          " that day.", sep='')
    for key in totals:
        print('\t', key, ": ", totals[key], sep='')

def main():
    '''
    Create a str with the date we want to analyze
    Send the date to the function to be processed
    Send the date & the totals to be printed

    Returns:
        None.

    '''
    focus_date = '2019-06-01'
    # process_CSV()
    totals = _new(focus_date)
    _print_totals(totals, focus_date)

if __name__ == "__main__":
    main()
