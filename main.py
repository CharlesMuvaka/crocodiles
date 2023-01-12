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


# create a method to check if there exists a path between nodes
def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = []
    if start == end:
        return True

    if start in visited:
        return False
    else:
        visited = visited + [start]  # appending the source in the list to avoid cycles in the graph
        # print(visited)

    for neighbor in graph.routes_dictionary[start]:
        if has_path(graph, neighbor, end, visited):
            return True
    return False


class Graph1:  # creating a graph
    def __init__(self, edges):
        self.edges = edges
        self.routes_dictionary = {}
        for start, end in self.edges:

            if start in self.routes_dictionary:
                self.routes_dictionary[start].append(end)
            else:
                self.routes_dictionary[start] = [end]

        print(self.routes_dictionary)


