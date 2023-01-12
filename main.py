# function to check if a vertex exists in the list while calculating the number of cycles
def explore(graph, current_node, visited):
    if current_node in visited:
        return False
    visited.append(current_node)
    print(visited)

    for neighbor_node in graph.routes_dictionary[current_node]:
        explore(graph, neighbor_node, visited)
    return True


def count_cycles(graph):  # creating a function to calculate the total number of cycles in the graph
    visited = []
    count = 0
    for node in graph.routes_dictionary:
        if explore(graph, node, visited):
            count += 1
    return count
