"""
Brandyn Gilbert
    Wed Feb 26 08:44:30 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 4
    Week 04 - PROJECT
"""
#PLAN
# =============================================================================
# # # # Purpose # # #
# # Implement search criteria defined in the JSON format for searching for
# # capital projects in PGH dataset, outputting resulting projects into a
# # file in JSON format
# # Write code that can read in a search criterion JSON file of your
# # specification. You'll need to be prepared to share this specification
# # with others in the class
# =============================================================================
# # Allow the user to specify search criteria for project fiscal year,
# # start date, area, asset_type, and planning status
# =============================================================================

import csv
import json

def main():
    _user_input()

    raw_data = _get_data()

    filter_data = _filter_json()

    filtered_csv = _filter_csv(raw_data, filter_data)

    _write_to_file(filtered_csv)

def _user_input():
    print("Welcome to PGH Capital Projects. Now with search features!")
    print("Which topic would you like to search in?")
    print("\t1. Project fiscal year\
          \n\t2. Start date\
          \n\t3. Area\
          \n\t4. Asset type\
          \n\t5. Planning status")
    user_choice = int(input("Make your selection now: "))
    user_query = input("Great! Now please enter a valid search query: ")
    user_choice_2 = _convert_user_choice(user_choice)

    _write_search_to_json(user_choice_2, user_query)




def _convert_user_choice(user_choice):
    return_value = ""
    if user_choice == 1:
        return_value = 'fiscal_year'
    elif user_choice == 2:
        return_value = 'start_date'
    elif user_choice == 3:
        return_value = 'area'
    elif user_choice == 4:
        return_value = 'asset_type'
    else:
        return_value = 'status'

    return return_value



def _write_search_to_json(user_choice, user_query):
    file_path = 'MAIN.json'
    search_path = 'Capital_Projects.json'

    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)

    search = {user_choice: user_query}
    json_data.update(search)

    with open(search_path, 'w') as json_file:
        json.dump(json_data, json_file)



def _printing(i):
    print(i)
    print("===============================")
    print("The type is:", type(i))
    input("STOP - _printing")
    print()

def _get_data():

    project_data_list = []
    # file_path = 'Testing.csv'
    file_path = 'PGH_Capital_Projects.csv'

    with open(file_path, newline='') as data_file:
        data = csv.DictReader(data_file)
        for i in data:
            project_data_list.append(i)

    # print("Raw Data type:", type(project_data_list))
    return project_data_list

def _filter_json():

    file_path = 'Capital_Projects.json'
    filter_dict = {}

    with open(file_path) as json_file:
        json_data = json.load(json_file)

        for i in json_data:
            if json_data[i] != '':
                filter_dict.update({i : json_data[i]})
    # print("Filter type:", type(filter_dict))
    return filter_dict

def _filter_csv(input_list, filter_data):

    filtered_project = []

    matching_count = len(filter_data)

    for i in input_list:

        for j in filter_data:
            count = 0

            if filter_data[j] == i[j]:
                count += 1

        if count == matching_count:
            filtered_project.append(i)

    return filtered_project

def _write_to_file(data_to_write):

    keys = data_to_write[0].keys()
    length = len(data_to_write)

    with open('PGH_filtered.csv', 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, keys)
        writer.writeheader()
        writer.writerows(data_to_write)

    print()
    print("\t\t\tWe found", length, "results!")
    print("The file \"PGH_filtered.csv\" has been written to your working",
          "directory with the results.")
    print("\t\t  Thank you for using this program.")





















if __name__ == "__main__":
    main()
