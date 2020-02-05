"""
Brandyn Gilbert
    Thu Jan 30 13:52:28 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 1
    Icon Processing
"""
#PLAN
"""
    Print an icon using a static input
        loop through list, print @ if 1, " " if 0
        At (position +1 % 10), print new line
        Keep looping until done
    Modify the code to allow scaling by an integer
        create a string to add the printable chars to
        set on=@, off=" " ;; use scale*on for length scaling ;; add to string
        Once the end of icon line reached, add "\n" to end
        print(str*scale) ;; this accounts for height scaling
    Modify the code further to allow inverting the icon
        if YES, then set on=" ", off=@
        if NO,  then set on=@  , off=" "
    FLesh out user inputs for scaling & inverting
        get the inputs, check for exclusions
        return the choice to main
    Modify the code for rotating the icon
    Allow user input for custom icons
"""

def greeting():
    print("Hello, welcome to icon processing.\n")
    print("Please have your icon ready as a single line of 1s & 0s.")
    print("\t\"1s\" will be interpreted as a filled pixel.")
    print("\t\"0s\" will be interpreted as a blank pixel.")
    input("Press ENTER to when you are ready to continue.")
    return

def get_Icon():
    '''
        Asks the user for input. Must be 100 numbers. Stores to a list.

    Returns
    -------
    user_list : LIST
        A string converted to a list of the users input.

    '''
    print("\n")
    print("Remember: This program requires you enter 100 numbers (1s & 0s)")
    print("\t (No tabs, no spaces, no commas)")
    while True:
        try:
            user_input = int(input("Please enter your 100 numbers now: "))
        except ValueError:
            print("That is not a valid choice.\nPlease try again.")
            continue
        if len(str(user_input)) != 100:
            print("That is not a valid choice.\nPlease try again.")
            continue
        break
    user_list = list(str(user_input))
    return user_list

def get_Scale():
    '''
        Asks for input. Uses that integer to scale the icon.


    Returns
    -------
    user_choice : INT
        Integer the user wants to scale the icon by.

    '''
    while True:
        try:
            user_choice = int(input("Scale? " +
                                    "(any whole number greater than 0): "))
        except ValueError:
            print("That is not a valid choice.\nPlease try again.")
            continue
        if user_choice == 0:
            print("That is not a valid choice.\nPlease try again.")
            continue
        break
    return user_choice


def get_Invert():
    '''
        Asks for input. The return value is interpreted later for a yes/no

    Returns
    -------
    int
        1: is a yes, invert
        2: is a no, do not invert

    '''
    while True:
        try:
            user_choice = input("Invert? (Y/N): ")
            user_choice = user_choice.upper()
        except ValueError:
            print("That is not a valid choice.\nPlease try again.")
            continue
        if user_choice != "Y" and user_choice != "N":
            print("That is not a valid choice.\nPlease try again.")
            continue
        break
    if user_choice == "Y":
        return 1
    else:
        return 0
    
def get_Rotation():
    '''
        Currently not used.
    '''
    user_choice = str(input("Rotate? (0, 90, 180, 270): "))
    if user_choice == "90":
        return 90
    elif user_choice == "180":
        return 180
    elif user_choice == "270":
        return 270
    else:
        return 0

def alpha_Icon(icon_list, scale, on, off):
    '''
    This function takes the raw icon list, the scale integer, the 'on' string, 
        and the 'off' string, creates 1 line of the icon, sends that line to 
        the next function for final processing
    Initialize: an empty string, variable = 0
    Use the for loop to go through the list 1 char at a time
    Once the end of the line is reached, send to beta_Icon, then continue
        the for loop until end    

    Parameters
    ----------
    icon_list : LIST
        List of numbers the user inputed to be turned into an icon.
    scale : INT
        The scale by which the icon should be amplified.
    on : STR
        The chars for every "on" pixel in the icon.
    off : STR
        The chars for every "off" pixel in the icon.

    Returns
    -------
    None.

    '''
    
    building_str = ""
    j = 0
    for i in icon_list:
        j -=- 1
        if i == "1":
            building_str = building_str + scale * on
        else:
            building_str = building_str + scale * off
        if j != 0 and j % 10 == 0:
            building_str = beta_Icon(building_str, scale)
    return

def beta_Icon(print_str, scale):
    '''
        Takes the first full line of the icon. 
        Prints the line multiplied by the scale (vertical scaling)

    Parameters
    ----------
    print_str : STRING
        Ready to print line of the icon.
    scale : INT
        Integer to scale the line by.

    Returns
    -------
    none

    '''
    
    print_str = print_str + "\n"
    print_str = scale * print_str
    print(print_str, end='')
    print_str = ''
    return 

def main():
    '''
    MAIN function. 
    Calls all of the other functions in the program.
    With an if/else to decide what the print icon pixels should be.

    Returns
    -------
    None.

    '''
    greeting()
    icon_list = get_Icon()
    scale = get_Scale()
    invert = get_Invert()
    if invert == 1:
        on = "  "
        off = "||"
    else:
        on = "||"
        off = "  "
    # rotate = get_Rotation()
    alpha_Icon(icon_list, scale, on, off)
    
    

if __name__ == "__main__":
    main()
