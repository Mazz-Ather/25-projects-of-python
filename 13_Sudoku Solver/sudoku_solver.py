def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None # if no spaces in the puzzle are empty (-1)


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    #step 1: check the row
    row_vals = puzzle[row] 
    if guess in row_vals:
        return False

    #step 2: check the column
    # cols_vals = []
    # for i in range(9):
    #     cols_vals.append(puzzle[i][col])
    cols_vals = [puzzle[i][col] for i in range(9)]
    if guess in cols_vals:
        return False 

    # and then the square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3  # Added missing col_start definition

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):  # Fixed function name spelling
    row, col = find_next_empty(puzzle)

    if row is None:
        return True  # Fixed lowercase true to True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):  # Fixed function name
                return True
        
        puzzle[row][col] = -1

    return False

if __name__ == '__main__':
    # Example puzzle
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    
    print("Original Sudoku:")
    for row in example_board:
        print(row)
    print("\nSolving...\n")
    
    if solve_sudoku(example_board):
        print("Solved Sudoku:")
        for row in example_board:
            print(row)
    else:
        print("No solution exists")