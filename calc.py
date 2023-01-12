import sys
from heapq import heappush, heapify


from numpy import n


def calculate_cost(graph1, start, end):
    infinity = sys.maxsize
    node_data = {
        1: {'cost': infinity, 'size': []},
        2: {'cost': infinity, 'size': []},
        3: {'cost': infinity, 'size': []},
        4: {'cost': infinity, 'size': []},
        5: {'cost': infinity, 'size': []},
        6: {'cost': infinity, 'size': []},
        7: {'cost': infinity, 'size': []},
        8: {'cost': infinity, 'size': []},
        9: {'cost': infinity, 'size': []},
        10: {'cost': infinity, 'size': []},
        11: {'cost': infinity, 'size': []},
        12: {'cost': infinity, 'size': []},
        13: {'cost': infinity, 'size': []},
        14: {'cost': infinity, 'size': []},
        15: {'cost': infinity, 'size': []},
        16: {'cost': infinity, 'size': []},
        17: {'cost': infinity, 'size': []},
        18: {'cost': infinity, 'size': []},
        19: {'cost': infinity, 'size': []},
        20: {'cost': infinity, 'size': []},
        21: {'cost': infinity, 'size': []},
        22: {'cost': infinity, 'size': []},
        23: {'cost': infinity, 'size': []},
        24: {'cost': infinity, 'size': []},
        25: {'cost': infinity, 'size': []},
        26: {'cost': infinity, 'size': []},
        27: {'cost': infinity, 'size': []},
        28: {'cost': infinity, 'size': []},
        29: {'cost': infinity, 'size': []},
        30: {'cost': infinity, 'size': []},
        31: {'cost': infinity, 'size': []},
        32: {'cost': infinity, 'size': []},
    }
    # assigning the starting point a cost of zero
    node_data[start]['cost'] = 0
    visited = []
    temporary_start = start
    # print(len(graph1))
    for i in range(n):
        if temporary_start not in visited:
            # print(temporary_start)
            visited.append(temporary_start)
            min_heap = []
            for neighbors in graph1[temporary_start]:
                # print(neighbors)
                if neighbors not in visited:
                    temporary_start_cost = node_data[temporary_start]['cost'] + graph1[temporary_start][neighbors]
                    # print(temporary_start_cost)
                    if temporary_start_cost < node_data[neighbors]['cost']:
                        # assigning the cost of neighbors
                        node_data[neighbors]['cost'] = temporary_start_cost
                        node_data[neighbors]['size'] = node_data[neighbors]['size'] + list(graph1[temporary_start])
                    heappush(min_heap, (node_data[neighbors]['cost'], neighbors))
                    # print(min_heap)
        heapify(min_heap)
        temporary_start = min_heap[0][1]
    return node_data[end]['cost'], node_data[end]['size']


if __name__ == '__main__':
    graph = {
        1: {2: 8.5},
        2: {1: 8.5, 3: 7.5},
        3: {4: 7.5},
        4: {3: 7.5, 5: 5.5},
        5: {27: 7.5},
        6: {3: 5.5, 7: 6.5},
        7: {6: 5, 8: 5.5},
        8: {7: 6.5, 15: 8.5},
        9: {8: 6, 5: 7},
        10: {9: 5.5, 14: 8.5},
        11: {10: 9},
        12: {11: 8.5, 24: 11},
        13: {14: 6},
        14: {13: 5.5, 15: 8},
        15: {14: 7.5, 16: 4},
        16: {17: 8.5},
        17: {18: 4},
        18: {20: 9, 21: 4, 17: 8.5},
        19: {20: 9.2, 18: 2.5},
        20: {20: 10.5, 18: 3},
        21: {20: 11.5, 18: 4.5, 22: 11},
        22: {23: 5},
        23: {24: 10.5},
        24: {25: 10.5},
        25: {26: 11},
        26: {23: 12},
        27: {11: 7},
        28: {21: 12.5, 29: 3.5},
        29: {30: 15, 28: 4},
        30: {29: 17.5},
        31: {32: 15.5, 30: 4.5},
        32: {26: 13}
    }

    start = 1
    end = 32

    calculate_cost(graph, start, end)
