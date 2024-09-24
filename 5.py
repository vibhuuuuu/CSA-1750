from collections import deque

def is_valid(ML, CL, MR, CR):
    # Check if state is valid: not more cannibals than missionaries on either side
    return (ML == 0 or ML >= CL) and (MR == 0 or MR >= CR)

def missionaries_and_cannibals():
    initial_state = (3, 3, 0, 0, 0)  # (ML, CL, MR, CR, Boat)
    goal_state = (0, 0, 3, 3, 1)

    visited = set()
    queue = deque([((3, 3, 0, 0, 0), [])])

    while queue:
        (ML, CL, MR, CR, B), path = queue.popleft()

        # Add the current state to the path
        current_path = path + [f"(ML: {ML}, CL: {CL}, MR: {MR}, CR: {CR}, Boat: {'Left' if B == 0 else 'Right'})"]

        # Check if we have reached the goal
        if (ML, CL, MR, CR, B) == goal_state:
            return current_path + ["Goal reached!"]

        # Possible actions
        possible_moves = []
        if B == 0:  # Boat is on the left side
            if ML >= 2:
                possible_moves.append((ML - 2, CL, MR + 2, CR, 1))  # 2 missionaries
            if ML >= 1:
                possible_moves.append((ML - 1, CL, MR + 1, CR, 1))  # 1 missionary
            if CL >= 2:
                possible_moves.append((ML, CL - 2, MR, CR + 2, 1))  # 2 cannibals
            if CL >= 1:
                possible_moves.append((ML, CL - 1, MR, CR + 1, 1))  # 1 cannibal
            if ML >= 1 and CL >= 1:
                possible_moves.append((ML - 1, CL - 1, MR + 1, CR + 1, 1))  # 1 missionary and 1 cannibal
        else:  # Boat is on the right side
            if MR >= 2:
                possible_moves.append((ML + 2, CL, MR - 2, CR, 0))  # 2 missionaries
            if MR >= 1:
                possible_moves.append((ML + 1, CL, MR - 1, CR, 0))  # 1 missionary
            if CR >= 2:
                possible_moves.append((ML, CL + 2, MR, CR - 2, 0))  # 2 cannibals
            if CR >= 1:
                possible_moves.append((ML, CL + 1, MR, CR - 1, 0))  # 1 cannibal
            if MR >= 1 and CR >= 1:
                possible_moves.append((ML + 1, CL + 1, MR - 1, CR - 1, 0))  # 1 missionary and 1 cannibal

        for next_state in possible_moves:
            next_ML, next_CL, next_MR, next_CR, next_B = next_state
            if is_valid(next_ML, next_CL, next_MR, next_CR) and next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, current_path))

    return ["No solution"]

# Example usage
steps = missionaries_and_cannibals()
for step in steps:
    print(step)
