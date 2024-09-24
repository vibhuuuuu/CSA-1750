# Function to print the chessboard
def print_board(board):
    for row in board:
        print(" ".join(str(i) for i in row))
    print()

# Function to check if a queen can be placed at (row, col)
def is_safe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Function to solve the N-Queen problem using backtracking
def solve_n_queen(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queen(board, col + 1, n):
                return True

            board[i][col] = 0  # Backtrack

    return False

# Main function to solve the 8-Queen problem
def solve_8_queen():
    n = 8
    board = [[0] * n for _ in range(n)]

    if not solve_n_queen(board, 0, n):
        print("No solution exists.")
    else:
        print_board(board)

solve_8_queen()
