# function to check if a vertex exists in the list while calculating the number of cycles
def explore(graph, current_node, visited):
    if current_node in visited:
        return False
    visited.append(current_node)
    print(visited)

    for neighbor_node in graph.routes_dictionary[current_node]:
        explore(graph, neighbor_node, visited)
    return True
