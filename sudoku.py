import random
import os

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
    """
    Performs new_game functions and then begins the game.
    """
    difficulty = get_difficulty()
    board = generate_board()
    remove_cells(board,difficulty)
    #play_game

def get_difficulty():
    """
    Displays the difficulty options and then prompts the user for a number correlating
    to the difficulty of their choice. Will loop until a valid option is selected.

    ASCII text art generated by: https://fsymbols.com/generators/carty/
    """
    difficulty = ''

    valid = False
    while not valid: 
        display_difficulties()
        difficulty = input('Please enter the difficulty number: ')
        if difficulty in [1,2,3,4,5]:
            valid = True
        else:
            print(f'\n"{difficulty}" is not a valid option.')
    
    return difficulty

def display_difficulties():
    """
    Displays the difficulty options.

    ASCII text art generated by: https://fsymbols.com/generators/carty/
    """
    print('\n█▀▄ █ █▀▀ █▀▀ █ █▀▀ █░█ █░░ ▀█▀ █ █▀▀ █▀')
    print('█▄▀ █ █▀░ █▀░ █ █▄▄ █▄█ █▄▄ ░█░ █ ██▄ ▄█')
    print('▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄ ▄▄')
    print('░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░\n')
    print('(1) Beginner')
    print('(2) Easy')
    print('(3) Medium')
    print('(4) Hard')
    print('(5) Extreme\n')

def load_game():

    if not check_saved_dir():
        main_menu()
    else:
        #display_saved
        #get_file
        #load_board
        pass

def check_saved_dir():

    cwd = os.path.abspath(os.getcwd())
    if not os.path.isdir('saved_games'):
        path = os.path.join(cwd,'saved_games')
        os.mkdir(path)
        print('It looks like there wasn\'t a folder for the saved games.\n\nA new folder was created to hold them named "saved_games".\n\nEnter option 1 in the main menu to start a new game.\n')
        return False
    elif len(os.listdir(os.path.join(cwd,'saved_games'))) == 0:
        print('It looks like there weren\'t any saved games in your saved_games folder.\n\nEnter option 1 in the main menu prompt to start a new game.\n')
        return False
    elif not check_json(os.listdir(os.path.join(cwd,'saved_games'))):
        print('It looks like there are not any json files in the saved_games folder.\n\nEnter option 1 in the main menu prompt to start a new game.\n')
        return False
    else:
        return True
    
def check_json(directory):

    for file in directory:
        if len(file) >= 5:
            if file[-5:] == '.json':
                return True
    return False

def display_saved():


    pass

def how_to_play():

    pass

def generate_board():
    # Initialize board
    board = [[0 for i in range(9)] for j in range(9)]
    
    # Place numbers in diagonal boxes
    for i in range(0,9,3):
        square = [1,2,3,4,5,6,7,8,9]
        random.shuffle(square)
        for j in range(3):
            for k in range(3):
                board[i+j][i+k] = square.pop()
                
    # Solve board
    solve_board(board)
    
    # Return solved board
    return board

def solve_board(board):
    """
    Solve the Sudoku board using a backtracking algorithm.
    """
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve_board(board):
                return True
            board[row][col] = 0
    return False

def find_empty(board):
    # Find the next empty cell in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    
    # If there are no empty cells, return None
    return None


def valid(board, num, pos):
    """
    Check if the board is valid.
    """
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # Check square
    square_x = pos[1] // 3
    square_y = pos[0] // 3
    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x * 3, square_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def remove_cells(board, difficulty):
    # Determine number of cells to remove based on difficulty
    if difficulty == 1:
        num_cells = 34
    elif difficulty == 2:
        num_cells = 45
    elif difficulty == 3:
        num_cells = 49
    elif difficulty == 4:
        num_cells = 53
    elif difficulty == 5:
        num_cells = 64
    else:
        raise ValueError("Invalid difficulty level")
    
    # Create a list of all cell coordinates
    cell_coords = [(i, j) for i in range(9) for j in range(9)]
    
    # Shuffle the list of cell coordinates
    random.shuffle(cell_coords)
    
    # Create a copy of the board
    board_copy = [row[:] for row in board]
    
    # Remove cells until desired number is reached
    for coord in cell_coords:
        i, j = coord
        
        # Remove cell value
        board_copy[i][j] = 0
        
        # Check if board has multiple solutions
        if not has_unique_solution(board_copy):
            # If there are multiple solutions, restore cell value
            board_copy[i][j] = board[i][j]
        
        # Stop when desired number of cells have been removed
        num_cells -= 1
        if num_cells == 0:
            break
    
    # Modify input board with removed cells
    for i in range(9):
        for j in range(9):
            board[i][j] = board_copy[i][j]

def has_unique_solution(board):
    # Create a copy of the board
    board_copy = [row[:] for row in board]
    
    # Solve board
    solve_board(board_copy)
    
    # Check if board has a unique solution
    for i in range(9):
        for j in range(9):
            if board_copy[i][j] == 0:
                # If there is a blank cell, the board has multiple solutions
                return False
    
    # If there are no blank cells, the board has a unique solution unless the difficulty was hard or extreme.
    return True

def print_board(board):
    print("  A B C   D E F   G H I ")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("  ------+-------+------")
        print(f"{i+1} ", end="")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if board[i][j] == 0:
                print("  ", end="")
            else:
                print(f"{board[i][j]} ", end="")
        print() 

"""if __name__ == '__main__':
    main()"""