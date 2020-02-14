"""
Brandyn Gilbert
    Thu Feb 12 17:46:01 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 2
    Icon Processing
        Adjustment A & B
        Output to file and terminal
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
    print("Please have your icon ready as a single line of characters"\
          " in a binary arrangement.")
    print("\tOne character will be interpreted as a filled pixel.")
    print("\tThe other character will be interpreted as a blank pixel.")
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

def get_on_pixels():
    '''
    Asks the user what they want the filled pixel to be

    Returns:
        on_pixels (str): character + ' '.

    '''
    on_pixels = input("Please enter 1 character to be used"\
                      " as an \"on\" pixel (recommended: \'@\'):  ")
    on_pixels = on_pixels + " "
    return on_pixels

def get_off_pixels():
    '''
    Asks the user what they want the empty pixel to be

    Returns:
        off_pixels (str): character + ' '.

    '''
    off_pixels = input("Please enter 1 character to be used"\
                       " as an \"off\" pixel (recommended: \' \'):  ")
    off_pixels = off_pixels + " "
    return off_pixels

def get_left_cut():
    '''
    Asks the user how many pixels to chop off the left side of the icon

    Returns:
        left_cut (int): number of pixels per line to omit from the left.

    '''
    left_cut = int(input("How many left columns to cut? (less than 10):  "))
    left_cut = left_cut * 2
    return left_cut

def get_right_cut():
    '''
    Asks the user how many pixels to chop off the right side of the icon

    Returns:
       right_cut (int): number of pixels per line to omit from the right.

    '''
    right_cut = int(input("How many right columns to cut? (less than 10):  "))
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

    Returns:
        invert (int): returns either 1 or 0 which is interpreted later.

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

def alpha_icon(icon_list, scale, on_print, off_print, on_char,
               left_cut, right_cut):
    '''
    This function takes the raw icon list, the scale integer, the 'on' string,
        and the 'off' string, creates 1 line of the icon, sends that line to
        the next function for final processing
    Initialize: an empty string, variable = 0
    Use the for loop to go through the list 1 char at a time
    Once the end of the line is reached, send to beta_icon, then continue
        the for loop until end

    Args:
        icon_list (list): list of the users icon to be printed.
        scale (int): an integer by which the users icon will be amplified.
        on_print (str): the charecters to be printed as "on".
        off_print (str): the charecters to be printed as "off".
        on_char (str): the character the user wants to be interpreted as "on".
        left_cut (int): how many pixels of the icon to cut from the left.
        right_cut (int): how many pixels of the icon to cut from the right.

    Returns:
        None.

    '''
    building_str = ""
    j = 0
    k = 0
    temp_left = left_cut * scale
    temp_right = -1 * right_cut * scale
    for i in icon_list:
        j -= -1
        if i == on_char:
            building_str = building_str + scale * on_print
        else:
            building_str = building_str + scale * off_print
        if len(building_str) == 10 * scale * 2:
            if left_cut > 0 or right_cut > 0:
                building_str = building_str[temp_left:temp_right]
            building_str = beta_icon(building_str, scale, k)
            k -=- 1

def beta_icon(print_str, scale, k):
    '''
        Takes the first full line of the icon.
        Creates a file to save the icon to.
        First time through, the file is written to.
        Second time ++ through, the file is appended to.
        Prints the line multiplied by the scale (vertical scaling) ((console))

    Parameters
    ----------
    print_str : STRING
        Ready to print line of the icon.
    scale : INT
        Integer to scale the line by.
    k : INT
        Integer tracking for how many lines have passed so far

    Returns:
        print_str (str): a blank string to reset 'building_str' in the previous
                            function, alpha_icon.

    '''
    if k == 0:
        file_out = open("icon.txt", "w")
    k -=- 1
    print_str = print_str + "\n"
    print_str = scale * print_str
    saving_str = print_str
    if k == 1:
        #write
        file_out = open("icon.txt", "w")
        file_out.write(saving_str)
        file_out.close()
    elif k > 1:
        #append
        file_out = open("icon.txt", "a")
        file_out.write(saving_str)
        file_out.close()

    print(print_str, end='')
    print_str = ''
    return print_str

def main():
    '''
    MAIN function.
        Calls all of the other functions in the program.
        With an if/else to decide what the print icon pixels should be.

    Returns:
        None.

    '''
    greeting()
    on_char = get_on()
    off_char = get_off()
    on_pixels = get_on_pixels()
    off_pixels = get_off_pixels()
    left_cut = get_left_cut()
    right_cut = get_right_cut()
    icon_list = get_icon(on_char, off_char)
    scale = get_scale()
    invert = get_invert()
    if invert == 1:
        on_print = off_pixels
        off_print = on_pixels
    else:
        on_print = on_pixels
        off_print = off_pixels
    # rotate = get_rotation()
    alpha_icon(icon_list, scale, on_print, off_print, on_char,
               left_cut, right_cut)

if __name__ == "__main__":
    main()
