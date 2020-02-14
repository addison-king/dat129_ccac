"""
Brandyn Gilbert
    Fri Feb 14 07:57:58 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 3
    "Warm-up 1: Looping to a file"
"""
#PLAN
#   Write a program that prints 0123456789, then 12345678 ... finally 0
#
#   Start with a 0123456789 string
#   String slice it based on how many times the loop has run
#   Print-baby-print


def _main():
    '''
    Creates the starting string to loop over "looping_str"
    Sets the iterating variable to length of "looping_str"
    Slices "looping_str", starting with the largest, then decreasing by 1
        after every "print"

    Returns:
        None.

    '''
    looping_str = "0123456789"
    i = len(looping_str)
    while i > 0:
        print(looping_str[0:i])
        i = i - 1

if __name__ == "__main__":
    _main()
