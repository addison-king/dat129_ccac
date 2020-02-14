"""
Brandyn Gilbert
    Fri Feb 14 08:27:43 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 3
    Warm-up 2: String formatting program specification
"""
#PLAN
#   read the file into string
#   break each string using .split()
#   print

# =============================================================================
# Gretchen Nowiki
# Gerald Brown
# Kevin Spacey
# Norine Letarchia
# =============================================================================

def _read_file():
    '''
    Opens the names.txt
    Read the whole document to a string
    Close the names.txt

    Returns:
        name_file_text (str): A string of the names. Each pair per line.

    '''
    name_file_raw = open('names.txt', 'r')
    name_file_text = name_file_raw.read()
    name_file_raw.close()
    return name_file_text

def _print_names(name_str):
    '''
    Takes the string of names and splits it based on whitespace to a list
    i = the length of the list divided by 2 (to account for first/last names)
    j is the counter, starts at 0
    while loop continues until the counter is >= i (list length/2)
    prints the message inside each while loop

    Args:
        name_str (str): A string of the names. Each pair per line.

    Returns:
        None.

    '''
    name_list = name_str.split()

    i = len(name_list)/2
    j = 0

    while j < i:
        last_name = name_list[j*2+1]
        first_name = name_list[j*2]
        print("Good evening Dr. ", last_name, ", Would you mind if I",
              " call you ", first_name, "?", sep="")
        j = j + 1

def _main():
    '''
    main function.
        Calls the other functions

    Returns:
        None.

    '''
    name_file_text = _read_file()
    _print_names(name_file_text)

if __name__ == "__main__":
    _main()
