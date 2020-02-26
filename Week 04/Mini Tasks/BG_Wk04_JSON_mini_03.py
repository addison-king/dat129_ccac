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
# #     'project area.' If you are feeling ambitious, do the same for 'status'
# #     and 'asset type' since this will come in handy during the search
# #     specification.
# =============================================================================

import csv

def _open_csv_title():
    '''
    Opens the .csv file, and stores the first line of it as a variable.

    Returns
    -------
    title : LIST
        The first line of the .csv.

    '''
    with open('PGH_Capital_Projects.csv', newline='') as csvfile:
    # with open('PGH_Short_mini2.csv', newline='') as csvfile:
        PGH_reader = csv.reader(csvfile)
        title = PGH_reader.__next__()
    return title

def _open_csv_contents():
    '''
    Opens the .csv file, and stores each line into a list. So each item in
        the list is 1 line from the .csv.

    Returns
    -------
    contents : LIST
        Each item is a line from the .csv.

    '''
    with open('PGH_Capital_Projects.csv', newline='') as csvfile:
    # with open('PGH_Short_mini2.csv', newline='') as csvfile:
        PGH_reader = csv.reader(csvfile)
        contents = []
        PGH_reader.__next__()
        for row in PGH_reader:
            contents.append(row)

    return contents

def _combine_title_contents(title, contents):
    '''
    Combines the .csv column titles with the contents, 1 csv-row at a time.
        (So each line in the .csv has titles connected with it.)

    Parameters
    ----------
    title : LIST
        Each list-item is a column header from the csv.
    contents : LIST
        Each list-item is a full line from the csv.

    Returns
    -------
    rows_list : LIST
        Each item is a dictionary. Each dictionary contains 1 line from the
            .csv file as the VALUE. The KEY is the column header.

    '''
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
    '''
    Pretty prints each line from the .csv file with the header column.
        (Probably was a more efficient way of setting the info up before
         printing, but cie la vie).

    Parameters
    ----------
    PGH_list : LIST
        Full list of dictionaries ready to be parsed & printed.
    printing_keys : LIST
        The only column headers that we want to be outputted.
    errors : int
        Number of empty 'area' cells found earlier.

    Returns
    -------
    None.

    '''
    for item in PGH_list:
        print("\n***PROJECT PROFILE***")
        for i in printing_keys:
            print(i, ":", item[i])
        print("\n\n")
    print("________________________________________________________________")
    print("________________________________________________________________")
    print("\nIn total, there were \"", errors, "\" errors.", sep='')
    print("\tSee the .log file in your working directory.")
    print("________________________________________________________________")

def _logMalformedProject(entry_row):
    '''
    Writes errors to a .log file

    Parameters
    ----------
    entry_row : dict
        Contains a line of csv data where the 'area' value is empty.

    Returns
    -------
    None.

    '''
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
    '''
    Checks the whole created dictionary/list item for empty values associated
        with the 'area' header.

    Parameters
    ----------
    full_dictlist : LIST
        Completed list of dictionaries of the whole .csv file.

    Returns
    -------
    i : int
        Number of erros.

    '''
    print(full_dictlist)
    print(type('full_dictlist'))
    input()
    i = 0
    for row in full_dictlist:
        if row['area'] == '':
            _logMalformedProject(row)
            i += 1
    return i

def _unique_values(full_dictlist):
    '''
    Looks for unique values for the columns: area, asset_type, status
        Counts the number of each value for each column
    Prints it all

    Parameters
    ----------
    full_dictlist : LIST
        Completed list of dictionaries of the whole .csv file.

    Returns
    -------
    None.

    '''
    lookup = ['area', 'asset_type', 'status']
    unique_dict = {}

    for i_lookup in lookup:
        for row in full_dictlist:
            if row[i_lookup] != '':
                if row[i_lookup] in unique_dict:
                    unique_dict[row[i_lookup]] += 1
                else:
                    unique_dict.update({row[i_lookup]:1})

        i_lookup_up = i_lookup.upper()
        print("________________________________________________________________")
        print("\n\nHere is a list of unique \"", i_lookup_up, \
              "\" values:", sep='')

        for row in unique_dict:
            print("\t", row, ":", unique_dict[row])

        unique_dict = {}

def main():
    '''
    The main function where everythin else is called/ran out of.

    Returns
    -------
    None.

    '''

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
    _printing(dict_list_complete, keys_to_print, errors)
    _unique_values(dict_list_complete)

    # _print_unique_values(unique_dict)

if __name__ == "__main__":
    main()
