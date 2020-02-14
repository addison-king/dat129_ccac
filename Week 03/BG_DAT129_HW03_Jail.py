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
    # csv_raw = open('jail_short.csv', 'r')
    csv_raw = open('jail.csv', 'r')
    csv_str = csv_raw.read()
    csv_raw.close()
    return csv_str

def _key_making(jail_string):
    jail_list = jail_string.split("\n")
    # print(jail_list)
    key_first_str = jail_list[0]
    key_list = key_first_str.split(",")
    # print(key_list)
    # jail_dict_keys = dict.fromkeys(key_list)
    # print(jail_dict_keys)
    # print("\n", key_list[0], key_list[1])

    jail_list_info = jail_list[1:]
    # print(jail_list_info)
    new_dict_list = []
    new_dict = {}
    for i in jail_list_info:
        j = i.split(",")
        # print(jail_list_info)
        # print(i)
        # print(j)
        new_dict = {}
        k = 0
        while k < 5:
            new_dict.update({key_list[k]:j[k]})
            k -=- 1
        new_dict_list.append(new_dict)
        # print(new_dict_list)
        # input()
        # j -=- 1
    # print(new_dict_list)
    return new_dict_list

def _in_class(jail_dict, focus_date):

    # races = {'B': 0, 'W': 0}
    races = {}
# =============================================================================
#     races = {}
#     for row in input_file:
#         # print(row)
#         # input()
#         if len(row['Race']) > 0:
#             if row['Race'] not in races:
#                 races[row['Race']] = 0
# 
#     f.seek(0)
#     for row in input_file:
#         if row['Date'] == focus_date:
#             if row['Race'] in races:
#                 races[row['Race']] -=- 1
# =============================================================================
    for entry in jail_dict:
        if len(entry['Race']) > 0:
            if entry['Race'] not in races:
                races[entry['Race']] = 0

    for entry in jail_dict:
        for key in entry:
            if entry[key] == focus_date:
                if entry['Race'] in races:
                    races[entry['Race']] -=- 1


    return races
    # print(races)

def _print_totals(totals, focus_date):
    print("On the chosen day, ", focus_date, ", here is a census from",
      " that day.", sep='')
    for key in totals:
        print('\t', key, ": ", totals[key], sep='')


def _main():
    focus_date = '2019-06-01'
    jail_string = _read_csv()
    # print(jail_string)
    jail_dict = _key_making(jail_string)
    totals = _in_class(jail_dict, focus_date)
    _print_totals(totals, focus_date)
if __name__ == "__main__":
    _main()
