"""
Brandyn Gilbert
    Thu Feb 12 12:27:28 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 2
    Icon Processing
        Adjustment A & B
"""
#PLAN
# =============================================================================
#     Print an icon using a static input
#         loop through list, print @ if 1, " " if 0
#         At (position +1 % 10), print new line
#         Keep looping until done
#     Modify the code to allow scaling by an integer
#         create a string to add the printable chars to
#         set on=@, off=" " ;; use scale*on for length scaling ;; add to string
#         Once the end of icon line reached, add "\n" to end
#         print(str*scale) ;; this accounts for height scaling
#     Modify the code further to allow inverting the icon
#         if YES, then set on=" ", off=@
#         if NO,  then set on=@  , off=" "
#     FLesh out user inputs for scaling & inverting
#         get the inputs, check for exclusions
#         return the choice to main
#     Modify the code for rotating the icon
#     Allow user input for custom icons
# =============================================================================

def greeting():
    '''
    Simple print greeting.

    Returns
    -------
    None.

    '''
    print("Hello, welcome to icon processing.\n")
    print("Please have your icon ready as a single line of 1s & 0s.")
    print("\t\"1s\" will be interpreted as a filled pixel.")
    print("\t\"0s\" will be interpreted as a blank pixel.")
    input("Press ENTER to when you are ready to continue.")

def get_on():
    '''
    Ask the user for what character to interpret as "on"

    Returns:
        on_char (str): on character.

    '''
    on_char = input("What is your \"on\" character? ")
    return on_char

def get_off():
    '''
    Ask the user for what character to interpret as "off"

    Returns:
        off_char (str): off character.

    '''
    off_char = input("What is your \"off\" character? ")
    return off_char

def get_left_cut():
    left_cut = int(input("How many left columns to cut?  "))
    left_cut = left_cut * 2
    return left_cut

def get_right_cut():
    right_cut = int(input("How many right columns to cut?  "))
    right_cut = right_cut * 2
    return right_cut

def get_icon(on_char, off_char):
    '''
        Asks the user for input. Stores to a list.

    Returns
    -------
    user_list : LIST
        A string converted to a list of the users input.

    '''
    print("\n")
    allowed_string = on_char + off_char
    allowed_chars = set(allowed_string)
    while True:
        user_input = input("Enter your icon now: ")
        if not set(user_input).issubset(allowed_chars) or\
            len(user_input) != 100:
            print("Please try again.")
        else:
            break
    user_list = list(str(user_input))
    return user_list

def get_scale():
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

def get_invert():
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
        if user_choice not in ("Y", "N"):
            print("That is not a valid choice.\nPlease try again.")
            continue
        break
    if user_choice == "Y":
        invert = 1
    else:
        invert = 0
    return invert

def get_rotation():
    '''
        Currently not used.
    '''
    user_choice = str(input("Rotate? (0, 90, 180, 270): "))
    if user_choice == "90":
        rotate = 90
    elif user_choice == "180":
        rotate = 180
    elif user_choice == "270":
        rotate = 270
    else:
        rotate = 0
    return rotate

def alpha_icon(icon_list, scale, on_print, off_print, on_char,\
               left_cut, right_cut):
    '''
    This function takes the raw icon list, the scale integer, the 'on' string,
        and the 'off' string, creates 1 line of the icon, sends that line to
        the next function for final processing
    Initialize: an empty string, variable = 0
    Use the for loop to go through the list 1 char at a time
    Once the end of the line is reached, send to beta_icon, then continue
        the for loop until end

    Parameters
    ----------
    icon_list : LIST
        List of numbers the user inputed to be turned into an icon.
    scale : INT
        The scale by which the icon should be amplified.
   on_invert: STR
        The chars for every "on" pixel in the icon.
    off : STR
        The chars for every "off" pixel in the icon.

    Returns
    -------
    None.

    '''

    building_str = ""
    j = 0
    temp_left = left_cut * scale
    temp_right = -1 * right_cut * scale
    print(left_cut, temp_left)
    print(right_cut, temp_right)
    input()
    for i in icon_list:
        j -= -1
        if i == on_char:
            building_str = building_str + scale * on_print
        else:
            building_str = building_str + scale * off_print
        if len(building_str) == 10 * scale * 2:
            if left_cut > 0 or right_cut > 0:
                building_str = building_str[temp_left:temp_right]



# =============================================================================
#             if left_cut > 0:
#                 building_str = building_str[temp_left:]
#             if right_cut > 0:
#                 # print(building_str)
#                 building_str = building_str[:temp_right]
#                 # print(building_str)
#                 # input()
# =============================================================================
            building_str = beta_icon(building_str, scale)

def beta_icon(print_str, scale):
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
    return print_str

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
    on_char = get_on()
    off_char = get_off()
    left_cut = get_left_cut()
    right_cut = get_right_cut()
    icon_list = get_icon(on_char, off_char)
    scale = get_scale()
    invert = get_invert()
    if invert == 1:
        on_print = "  "
        off_print = "@ "
    else:
        on_print = "@ "
        off_print = "  "
    # rotate = get_rotation()
    alpha_icon(icon_list, scale, on_print, off_print, on_char,\
               left_cut, right_cut)

if __name__ == "__main__":
    main()
