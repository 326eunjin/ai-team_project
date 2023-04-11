import csv

adjacency_list = [0 for _ in range(1000)]


def make_adj_list(sol1, sol2):
    for i in range(1000):
        tmp_set = set()
        tmp_set.add(sol1[i-1])
        tmp_set.add(sol1[(i+1) % len(sol1)])
        tmp_set.add(sol2[i-1])
        tmp_set.add(sol2[(i+1) % len(sol1)])
        adjacency_list[i] = list(tmp_set)

    return adjacency_list
