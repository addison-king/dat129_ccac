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
    print("_________________________________________________________________")

def get_on():
    '''
    Ask the user for what character to interpret as "on"

    Returns:
        on_char (str): on character.

    '''
    on_char = input("What is your \"on\" character? ")
    print("_________________________________________________________________")
    return on_char

def get_off():
    '''
    Ask the user for what character to interpret as "off"

    Returns:
        off_char (str): off character.

    '''
    off_char = input("What is your \"off\" character? ")
    print("_________________________________________________________________")
    return off_char

def get_on_pixels():
    '''
    Asks the user what they want the filled pixel to be

    Returns:
        on_pixels (str): character + ' '.

    '''
    on_pixels = input("Please enter ONE character to be used"\
                      " as an \"on\" pixel (recommended: \'@\'):  ")
    on_pixels = on_pixels + " "
    print("_________________________________________________________________")
    return on_pixels

def get_off_pixels():
    '''
    Asks the user what they want the empty pixel to be

    Returns:
        off_pixels (str): character + ' '.

    '''
    off_pixels = input("Please enter ONE character to be used"\
                       " as an \"off\" pixel (recommended: \' \'):  ")
    off_pixels = off_pixels + " "
    print("_________________________________________________________________")
    return off_pixels

def get_left_cut():
    '''
    Asks the user how many pixels to chop off the left side of the icon

    Returns:
        left_cut (int): number of pixels per line to omit from the left.

    '''
    left_cut = int(input("How many left columns to cut? (less than 10):  "))
    left_cut = left_cut * 2
    print("_________________________________________________________________")
    return left_cut

def get_right_cut():
    '''
    Asks the user how many pixels to chop off the right side of the icon

    Returns:
       right_cut (int): number of pixels per line to omit from the right.

    '''
    right_cut = int(input("How many right columns to cut? (less than 10):  "))
    right_cut = right_cut * 2
    print("_________________________________________________________________")
    return right_cut

def get_icon(on_char, off_char):
    '''
        Asks the user for input. Stores to a list.

    Returns
    -------
    user_list : LIST
        A string converted to a list of the users input.

    '''
    print("_________________________________________________________________")
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
    print("_________________________________________________________________")
    print("_________________________________________________________________")
    print('\n')
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
            user_choice = int(input("How large would you like to scale \
your icon (any whole number greater than 0): "))
        except ValueError:
            print("That is not a valid choice.\nPlease try again.")
            continue
        if user_choice == 0:
            print("That is not a valid choice.\nPlease try again.")
            continue
        break
    print("_________________________________________________________________")
    return user_choice

def get_invert():
    '''
    Asks for input. The return value is interpreted later for a yes/no

    Returns:
        invert (int): returns either 1 or 0 which is interpreted later.

    '''
    while True:
        try:
            user_choice = input("Would you like to invert the pixels? (Y/N): ")
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
    print("_________________________________________________________________")
    return invert

def get_rotation():
    '''
    Asks the user if they would like to rotate their icon. Options are listed
        in clockwise degrees: 0, 90, 180, 270.

    Returns:
        rotate (int): Returns an int of how much the user would like to rotate.

    '''
    print("\nWould you like to rotate your icon?", end="")
    user_choice = str(input("Rotation choice? (0°, 90°, 180°, 270°): "))
    if user_choice == "90":
        rotate = 90
    elif user_choice == "180":
        rotate = 180
    elif user_choice == "270":
        rotate = 270
    else:
        rotate = 0
    print("_________________________________________________________________")

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
    i = 0
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
            k += 1

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
    k += 1
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

def icon_initial_dict(icon_list):
    '''
    Takes the users input (which is a list at this moment) and converts it into
        a dict for use later on.

    Args:
        icon_list (list): The users input where each char is a item in the lsit

    Returns:
        icon_dict (TYPE): The users input is now a dict. Each original entry
                          by the user is the value and the key is simply an
                          int from 0 to the length of the list.

    '''
    icon_dict = {}
    i = 0
    list_length = len(icon_list)
    while i < list_length:
        icon_dict.update({i:icon_list[i]})

        i += 1
    return icon_dict

def rotate_90(icon_length):
    '''
    This will take the users input dict and rotate it 90-clockwise.
    Creating is in 3 stages:
        1. Set the top left corner number
        2. Set the first row based on the top left corner number
        3. Set the rest of the icon based on the first row data

    Args:
        icon_length (int): the length of the users icon list.

    Returns:
        r90_dict (dict): the users icon, in raw dict format, is now rotated
                            90-clockwise.

    '''
    r90_dict = {}
    position = 0
    row = 0

  # Setup the first position, top left corner
    r90_dict.update({position:int(icon_length-icon_length**0.5)})
    position += 1

  # Setup the rest of the first full row
    while position < icon_length**0.5:
        r90_dict.update({position:int(r90_dict[position-1]-icon_length**0.5)})
        position += 1

  # The rest of the icon is setup, 1 row at a time, based on the 1st row data
    row += 1
    i = 0
    while row < icon_length**0.5:
        while position < (row + 1) * icon_length**0.5:
            r90_dict.update({position:r90_dict[i]+row})

            i += 1
            position += 1
        row += 1
        i = 0

    return r90_dict

def rotate_180(total_length):
    '''
    This will take the users input dict and rotate it 180-clockwise.
        The key:value relationship is inverse. So just create a dict where
        the 0th key has a value of the max length of the icon list.

    Args:
        total_length (int): the length of the users icon list..

    Returns:
        r180_dict (dict): the users icon, in raw dict format, is now rotated
                            180-clockwise..

    '''
    r180_dict = {}
    position = 0
    i = total_length -1

    while position < total_length:
        r180_dict.update({position : i})
        position += 1
        i -= 1

    return r180_dict

def rotate_270(total_length):
    '''
    This will take the users input dict and rotate it 270-clockwise.
    Creating is in 3 stages:
        1. Set the top left corner number
        2. Set the first row based on the top left corner number
        3. Set the rest of the icon based on the first row data
    **NOTE: this is the same operations as the 90-clockwise function, but
            inverse. So instead of add, say 1, it subtracts.

    Args:
        total_length (int): the length of the users icon list.

    Returns:
        r270_dict (dict): the users icon, in raw dict format, is now rotated
                            270-clockwise.

    '''
    r270_dict = {}
    position = 0
    row = 0
    i = total_length**0.5

    r270_dict.update({position : int(i - 1)})
    position += 1

    while position < i:
        r270_dict.update({position : int(r270_dict[position-1] + i)})
        position += 1

    row += 1
    j = 0

    while row < i:
        while position < (row + 1) * i:
            r270_dict.update({position : r270_dict[j] - row})

            j += 1
            position += 1
        row += 1
        j = 0

    return r270_dict

def dict_to_list(new_icon_dict, icon_dict):
    '''
    This takes the users original icon input as a dict and takes the ROTATED
        icon dict and combines them. The keys will be the same. The value for
        the ROTATED icon dict will be converted to the corresponding value in
        the original icon dict. All of this, turn it into a list.

    Args:
        new_icon_dict (dict): ROTATED users icon dict.
        icon_dict (dict): original users icon dict.

    Returns:
        rotated_list (list): The icon list ready to be sent to print.

    '''
    rotated_dict = {}

    for key in new_icon_dict:
        rotated_dict[key] = icon_dict[new_icon_dict[key]]

    rotated_list = []

    for key in rotated_dict:
        rotated_list.append(rotated_dict[key])

    return rotated_list

def main():
    '''
    MAIN function.
        Calls all of the other functions in the program.
        With an if/else to decide what the print icon pixels should be.
        With an if/elif/elif to decide how to rotate the icon.

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
    # icon_list = get_icon(on_char, off_char)
    scale = get_scale()
    invert = get_invert()
    if invert == 1:
        on_print = off_pixels
        off_print = on_pixels
    else:
        on_print = on_pixels
        off_print = off_pixels
    rotate = get_rotation()
    icon_list = get_icon(on_char, off_char)
    icon_dict = icon_initial_dict(icon_list)

    icon_length = len(icon_list)
    if rotate == 90:
        new_icon_dict = rotate_90(icon_length)
        icon_list = dict_to_list(new_icon_dict, icon_dict)
    elif rotate == 180:
        new_icon_dict = rotate_180(icon_length)
        icon_list = dict_to_list(new_icon_dict, icon_dict)
    elif rotate == 270:
        new_icon_dict = rotate_270(icon_length)
        icon_list = dict_to_list(new_icon_dict, icon_dict)

    alpha_icon(icon_list, scale, on_print, off_print, on_char,
               left_cut, right_cut)

    print("\nP.S. ~ Be sure to look in your working directory for a txt file",
          "with your icon saved in it!")

if __name__ == "__main__":
    main()
