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
