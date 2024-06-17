
import random

def generate_sudoku():
    def is_valid(board, row, col, num):
        """
        Method to check for row checker, column checker, and 3x3 subgrid checker
        """
        # check if the number is already used in the row
        if num in board[row]:
            return False

        # check if the number is already used in the column
        if num in [board[i][col] for i in range(9)]:
            return False

        # check if the number is already used in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve(board):
        """
        Use backtracking algo (depth first search - DFS algo) to generate/solve the board efficiently
        - Goes through each hole of 9x9 and plug in random number from 1-9
        - Check if board is valid
        - If not valid, call `solve` function for recursive call until it is resolved
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in random.sample(range(1, 10), 9):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board): #this is a recursive call (if solve(board) returns False then fill the hole as 0 so it will keep running until the correct number is filled on the hole)
                                return True
                            board[row][col] = 0
                    return False
        return True

    # create an empty sudoku board (9 x 9) filled with 0 as placeholder
    board = [[0] * 9 for _ in range(9)]

    # solve the board
    solve(board)

    return board

def print_board(board):
    """
    Method used to print sudoku board
    """
    for row in board:
        print(" ".join(map(str, row)))

def main():
    sudoku_board = generate_sudoku()

    print("Generate Sudoku board....")
    print_board(sudoku_board)

if __name__ == "__main__":
    main()