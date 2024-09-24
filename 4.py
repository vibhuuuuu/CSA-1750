from itertools import permutations

# Function to check if a solution is valid for SEND + MORE = MONEY
def is_valid(puzzle, letters, digits):
    equation = ''.join(str(digits[letters.index(char)]) for char in puzzle)
    send = int(equation[:4])
    more = int(equation[4:8])
    money = int(equation[8:])
    return send + more == money

# Cryptarithmetic solver for SEND + MORE = MONEY
def crypt_arithmetic():
    puzzle = "SENDMOREMONEY"
    letters = list(set(puzzle))
    for perm in permutations(range(10), len(letters)):
        if perm[letters.index('S')] == 0 or perm[letters.index('M')] == 0:  # S and M can't be zero
            continue
        if is_valid(puzzle, letters, perm):
            solution = {letters[i]: perm[i] for i in range(len(letters))}
            print("Solution:", solution)
            return solution
    print("No solution found.")
    return None

crypt_arithmetic()
