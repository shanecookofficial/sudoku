def main():

    display_intro()
    main_menu()

def display_intro():
    """
    Prints the introductory message in the terminal.

    ASCII text art generated by: https://fsymbols.com/generators/carty/
    """
    print('░██████╗██╗░░░██╗██████╗░░█████╗░██╗░░██╗██╗░░░██╗')
    print('██╔════╝██║░░░██║██╔══██╗██╔══██╗██║░██╔╝██║░░░██║')
    print('╚█████╗░██║░░░██║██║░░██║██║░░██║█████═╝░██║░░░██║')
    print('░╚═══██╗██║░░░██║██║░░██║██║░░██║██╔═██╗░██║░░░██║')
    print('██████╔╝╚██████╔╝██████╔╝╚█████╔╝██║░╚██╗╚██████╔╝')
    print('╚═════╝░░╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░')
    print('\n')
    print('█▄▄ █▄█ ▀   █▀ █░█ ▄▀█ █▄░█ █▀▀   █▀▀ █▀█ █▀█ █▄▀')
    print('█▄█ ░█░ ▄   ▄█ █▀█ █▀█ █░▀█ ██▄   █▄▄ █▄█ █▄█ █░█')
    print('\n')

def main_menu():
    display_menu()
    menu_selection = get_menu_selection()
    do_menu_selection(menu_selection)

def display_menu():
    """
    Prints the main menu options in the terminal.

    ASCII text art generated by: https://fsymbols.com/generators/carty/
    """  
    print('█▀▄▀█ ▄▀█ █ █▄░█   █▀▄▀█ █▀▀ █▄░█ █░█')
    print('█░▀░█ █▀█ █ █░▀█   █░▀░█ ██▄ █░▀█ █▄█\n')
    print('(1) New Game')
    print('(2) Load Game')
    print('(3) How to Play')
    print('(4) Quit\n')
    
def get_menu_selection():
    """
    Prompts the user to select a menu option.

    Loops until the user selects a valid option.

    Returns the choice stored in the menu_selection variable.
    """
    valid = False
    while not valid:
        menu_selection = input('Enter menu option: ')
        if menu_selection in ['1','2','3','4']:
            valid = True
        else:
            print('That option is not valid. Please enter 1, 2, 3, or 4.\n')
    return menu_selection

def do_menu_selection(menu_selection):
    """
    Performs actions correlated to the menu option selected by the user.
    """
    if menu_selection == '1':
        # UNDER CONSTRUCTION
        pass
    elif menu_selection == '2':
        # UNDER CONSTRUCTION
        pass
    elif menu_selection == '3':
        # UNDER CONSTRUCTION
        pass
    elif menu_selection == '4':
        exit()

def new_game():

    pass

def load_game():

    pass

def how_to_play():

    pass

if __name__ == '__main__':
    main()