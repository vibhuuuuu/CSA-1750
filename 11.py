def map_coloring(graph, colors, assignment={}):
    if len(assignment) == len(graph):
        return assignment

    for node in graph:
        if node not in assignment:
            for color in colors:
                if is_valid(graph, assignment, node, color):
                    assignment[node] = color
                    result = map_coloring(graph, colors, assignment)
                    if result:
                        return result
                    del assignment[node]
            return None

def is_valid(graph, assignment, node, color):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Example usage:
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW']
}

colors = ['R', 'G', 'B']

assignment = map_coloring(graph, colors)
print("Map Coloring:", assignment)
