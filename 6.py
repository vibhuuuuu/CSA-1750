from collections import deque

def is_valid(state):
    # In the vacuum cleaner problem, any state is considered valid
    return True

def vacuum_cleaner():
    initial_state = ('A', 'dirty', 'dirty')  # (Location, Room A status, Room B status)
    goal_state = ('A', 'clean', 'clean')

    visited = set()
    queue = deque([((initial_state, []))])

    while queue:
        (current_state, path) = queue.popleft()

        # Unpack the state
        location, room_A, room_B = current_state

        # Add the current state to the path
        current_path = path + [f"Location: {location}, Room A: {room_A}, Room B: {room_B}"]

        # Check if we have reached the goal
        if current_state == goal_state:
            return current_path + ["Goal reached!"]

        # Possible actions
        possible_moves = []
        if location == 'A':
            # Move to Room B
            possible_moves.append(('B', room_A, room_B))
            # Clean Room A if it's dirty
            if room_A == 'dirty':
                possible_moves.append(('A', 'clean', room_B))
        else:  # location == 'B'
            # Move to Room A
            possible_moves.append(('A', room_A, room_B))
            # Clean Room B if it's dirty
            if room_B == 'dirty':
                possible_moves.append(('B', room_A, 'clean'))

        for next_state in possible_moves:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, current_path))

    return ["No solution"]

# Example usage
steps = vacuum_cleaner()
for step in steps:
    print(step)
