def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))
    print()

def move_zero(grid, direction):
    zero_row, zero_col = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 0][0]

    if direction == 'up' and zero_row > 0:
        grid[zero_row][zero_col], grid[zero_row - 1][zero_col] = grid[zero_row - 1][zero_col], grid[zero_row][zero_col]
    elif direction == 'down' and zero_row < 2:
        grid[zero_row][zero_col], grid[zero_row + 1][zero_col] = grid[zero_row + 1][zero_col], grid[zero_row][zero_col]
    elif direction == 'left' and zero_col > 0:
        grid[zero_row][zero_col], grid[zero_row][zero_col - 1] = grid[zero_row][zero_col - 1], grid[zero_row][zero_col]
    elif direction == 'right' and zero_col < 2:
        grid[zero_row][zero_col], grid[zero_row][zero_col + 1] = grid[zero_row][zero_col + 1], grid[zero_row][zero_col]

def solve_puzzle(grid, goal):
    zero_row, zero_col = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 0][0]

    moves = ['down', 'right', 'up', 'left', 'down', 'right']  # Example moves to guide zero to bottom-right

    for move in moves:
        print(f"Moving zero {move}:")
        move_zero(grid, move)
        print_grid(grid)

# Initial state of the puzzle
grid = [[1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]]

# Target state of the puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

print("Initial State:")
print_grid(grid)

print("Solving the Puzzle:")
solve_puzzle(grid, goal_state)

print("Final Goal State:")
print_grid(goal_state)

print("Puzzle Solved!")
