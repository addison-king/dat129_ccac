"""
Brandyn Gilbert
    Fri Feb 14 09:23:20 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 3
    jail.csv WITHOUT csv module
"""
#PLAN
#   Take the csv file, but don't use the csv module
#   Read, split, zip(?)
#   Lots of calculations
#   Print number of inmates by race
#   Print percentage of race inmates



def _read_csv():
    '''
    Opens the .csv file
    Reads the file into a string
    Closes the .csv file

    Returns:
        csv_str (str): A string that contains all the info from the .csv.

    '''
    csv_raw = open('jail.csv', 'r')
    csv_str = csv_raw.read()
    csv_raw.close()
    return csv_str

def _keys_making(jail_string):
    '''
    Takes in a string containing the whole csv file
    Splits it up based on return char
    String split the first line to a str to be used as keys later
    String split based on ',' char to a list. Each item in this list be used
        as a key later on in a dictionary.

    Args:
        jail_string (str): a string containing the whole csv file.

    Returns:
        key_list (list): a list to be used as keys for a later dict:
                         (Date, Gender, Race, Age at Booking, Current Age).

    '''
    jail_list = jail_string.split("\n")
    keys_str = jail_list[0]
    key_list = keys_str.split(",")

    return key_list

def _values_splitting(jail_string):
    '''
    Takes in a string containing the whole csv file
    Splits it up based on return char
    String split the 2nd line to the end, store it to a str:
        to be used as values in a dict later

    Args:
        jail_string (str): a string containing the whole csv file.

    Returns:
        jail_info_list (list): a list containing all info, except for original
                               csv file column headers.

    '''
    jail_list = jail_string.split("\n")
    jail_info_list = jail_list[1:]

    return jail_info_list

def _dict_making(jail_string):
    '''
    Sends the string containing the whole csv file to be stripped and returned
        as a list, soon to be KEYS in a dict
    Sends the string containing the whole csv file to be stripped and returned
        as a list, soon to be VALUES in a dict
    Create an empty list

    `for` loop:
        The first 'row' in the list containing soon-to-be VALUES:
            Create an empty dict
            Split the first 'row' up based on the ',' char
            Set an iterating-tracking variable to 0
            `while` loop:
                Update the empty dict with a KEY:VALUE pair...
                    KEY = positional string split from the key list
                    VALUE = positional string split, of the 'row' variable
                            in the `for` loop (j='row' split) (k=positional)
            When `while` loop is done, append the temp dict, to a list

    Args:
        jail_string (str): a string containing the whole csv file..

    Returns:
        new_dict_list (list): A list of dictionaries.

    '''

    key_list = _keys_making(jail_string)
    jail_info_list = _values_splitting(jail_string)
    new_dict_list = []

    for row in jail_info_list:
        new_dict = {}
        j = row.split(",")
        k = 0

        while k < 5:
            new_dict.update({key_list[k]:j[k]})
            k += 1
        new_dict_list.append(new_dict)

    return new_dict_list

def _census_calc(jail_dict, focus_date):
    '''
    Create an empty dict
    First `for` loop:
        Looking at each dict entry in the list...
            `if` the race is not in our Races dict...
                add that race to our Races dict with a value of 0

    Second `for` loop:
        Looking at each dict entry in the list...
            Looking at each key in the entry...
                `if` the 'entry'['key'] is our date:
                    `if` the 'entry'["Race"] is in our races dict:
                        The corresponding race key in our dict is +1

    Args:
        jail_dict (list): A list of dictionaries.
        focus_date (str): The hard-coded date we want to analize.

    Returns:
        races (dict): A dict containing KEY(races):VALUE(pop. size) pairs.

    '''
    races = {}

    for entry in jail_dict:
        if len(entry['Race']) > 0:
            if entry['Race'] not in races:
                races[entry['Race']] = 0

    for entry in jail_dict:
        for key in entry:
            if entry[key] == focus_date:
                if entry['Race'] in races:
                    races[entry['Race']] += 1
    return races

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

def _main():
  # hardcode the date we want to analyze
    focus_date = '2019-06-01'
  # read the csv to a string
    jail_string = _read_csv()
  # take the csv.string, turn it into a list of dicts, 1 dict per list item
    jail_dict = _dict_making(jail_string)
  # use the dict/list and the date to get the totals as a dict
    totals = _census_calc(jail_dict, focus_date)
  # use the totals.dict and the date.str to print results for the user
    _print_totals(totals, focus_date)

if __name__ == "__main__":
    _main()
