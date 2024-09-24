import itertools

def tsp_brute_force(cities, distances):
    min_distance = float('inf')
    best_route = None

    for route in itertools.permutations(cities):
        distance = 0
        for i in range(len(route) - 1):
            distance += distances[route[i]][route[i + 1]]
        distance += distances[route[-1]][route[0]]  # add distance from last city back to first city

        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance

# Example usage:
cities = ['A', 'B', 'C', 'D']
distances = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

best_route, min_distance = tsp_brute_force(cities, distances)
print("Best Route:", best_route)
print("Minimum Distance:", min_distance)
