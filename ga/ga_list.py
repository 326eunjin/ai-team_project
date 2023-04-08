import numpy as np
import csv

# given cities
cities = []
# sol1ution
sol1 = []
sol2 = []
adjacency_list = []

with open('1.csv', mode='r', newline='') as sol1ution:

    # read sol1ution sequence
    reader = csv.reader(sol1ution)
    for row in reader:
        sol1.append(int(row[0]))

    # reordering sol1ution sequence
    idx = sol1.index(0)

    front = sol1[idx:]
    back = sol1[0:idx]

    sol1 = front + back

    # expand 0 city (start) for simplicity
    sol1.append(int(0))

# need to change this file into new csv sol2
with open('2.csv', mode='r', newline='') as sol1ution:

    # read sol1ution sequence
    reader = csv.reader(sol1ution)
    for row in reader:
        sol2.append(int(row[0]))

    # reordering sol1ution sequence
    idx = sol2.index(0)

    front = sol2[idx:]
    back = sol2[0:idx]

    sol2 = front + back

    # expand 0 city (start) for simplicity
    sol2.append(int(0))


def make_adj_list():
    adjacency_list = [[] for _ in range(len(sol1))]
    for i in range(len(sol1)):  # 처음부터 돌면서
        # 위치를 일단 찾아
        for j in sol1:
            if sol1[j] == i:
                loc = j
                break
        if loc == 0:
            adjacency_list.append(sol1[loc+1])
        elif loc == 999:
            adjacency_list.append(sol1[loc-1])
        else:
            adjacency_list.append([sol1[loc-1], sol1[loc+1]])

    for i in range(len(sol2)):  # 처음부터 돌면서
        # 위치를 일단 찾아
        for j in sol2:
            if sol2[j] == i:
                loc = j
                break
        if loc == 0:
            adjacency_list[loc].append(sol2[loc+1])
        elif loc == 999:
            adjacency_list[loc].append(sol2[loc-1])
        else:
            adjacency_list[loc].append(sol2[loc-1])
            adjacency_list[loc].append(sol2[loc+1])


make_adj_list()
