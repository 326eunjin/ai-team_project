import csv

# sol1ution
sol1 = [0 for _ in range(1000)]
sol2 = [0 for _ in range(1000)]
adjacency_list = []

with open('../example_solution.csv', mode='r', newline='') as solution:

    order = 0
    # read sol1ution sequence
    reader = csv.reader(solution)
    for row in reader:
        sol1[int(row[0])] = order
        order += 1

# need to change this file into new csv sol2
with open('../example_solution.csv', mode='r', newline='') as solution:

    order = 0
    # read sol1ution sequence
    reader = csv.reader(solution)
    for row in reader:
        sol2[int(row[0])] = order
        order += 1

def make_adj_list():
    adjacency_list = [0 for _ in range(len(sol1))]
    
    for i in range(1000):
        tmp_set = set()
        tmp_set.add(sol1[i-1])
        tmp_set.add(sol1[(i+1) % len(sol1)])
        tmp_set.add(sol2[i-1])
        tmp_set.add(sol2[(i+1) % len(sol1)])
        adjacency_list[i] = list(tmp_set)

    print(adjacency_list)   ## list test
    return adjacency_list

make_adj_list()
