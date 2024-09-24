from collections import deque

# Function to check if the current state is valid
def is_valid(state, max_jug1, max_jug2):
    jug1, jug2 = state
    return 0 <= jug1 <= max_jug1 and 0 <= jug2 <= max_jug2

# Function to solve the water jug problem using BFS
def water_jug_bfs(jug1_max, jug2_max, target):
    queue = deque([(0, 0)])  # Initial state (both jugs empty)
    visited = set([(0, 0)])

    while queue:
        jug1, jug2 = queue.popleft()

        if jug1 == target or jug2 == target:
            return jug1, jug2

        # Possible moves
        moves = [
            (jug1_max, jug2),  # Fill Jug 1
            (jug1, jug2_max),  # Fill Jug 2
            (0, jug2),  # Empty Jug 1
            (jug1, 0),  # Empty Jug 2
            (jug1 - min(jug1, jug2_max - jug2), jug2 + min(jug1, jug2_max - jug2)),  # Pour Jug 1 -> Jug 2
            (jug1 + min(jug2, jug1_max - jug1), jug2 - min(jug2, jug1_max - jug1)),  # Pour Jug 2 -> Jug 1
        ]

        for move in moves:
            if is_valid(move, jug1_max, jug2_max) and move not in visited:
                queue.append(move)
                visited.add(move)

    return None

# Test the function
jug1_max, jug2_max, target = 4, 3, 2
result = water_jug_bfs(jug1_max, jug2_max, target)
if result:
    print("Solution:", result)
else:
    print("No solution found.")
