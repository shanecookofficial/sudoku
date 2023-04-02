import random

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
    if difficulty == "easy":
        num_cells = 40
    elif difficulty == "medium":
        num_cells = 50
    elif difficulty == "hard":
        num_cells = 60
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
    
    # If there are no blank cells, the board has a unique solution
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


board = generate_board()
remove_cells(board,'easy')
print_board(board)