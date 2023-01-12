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


if __name__ == '__main__':
    routes = [
        (1, 2), (2, 1), (2, 3), (3, 4), (4, 3), (4, 5), (5, 27), (6, 3),
        (6, 7), (7, 6), (7, 8), (8, 7), (8, 15), (9, 8), (10, 9), (10, 14), (11, 10), (12, 11),
        (12, 24), (13, 14), (14, 13), (14, 15), (15, 14), (15, 16), (16, 17), (17, 18), (18, 20), (18, 21), (18, 17),
        (19, 20), (19, 18), (20, 18), (21, 20), (21, 18), (21, 22), (22, 23), (23, 24), (29, 30), (29, 28),
        (24, 25), (25, 26), (26, 23), (27, 11), (28, 21), (28, 29), (30, 29), (31, 32),
        (31, 30), (32, 26), (9, 5)
    ]

    my_routes = Graph1(routes)
    print(has_path(my_routes, 5, 32))
    print(count_cycles(my_routes))
