import csv
import numpy as np
import ga_list
import ga_sol

# given cities
cities = []
# sol1ution
sol1 = [0 for _ in range(1000)]
sol2 = [0 for _ in range(1000)]

with open('./../example_solution.csv', mode='r', newline='') as solution:

    order = 0
    # read sol1ution sequence
    reader = csv.reader(solution)
    for row in reader:
        sol1[int(row[0])] = order
        order += 1

# need to change this file into new csv sol2
with open('./../greedy_solution.csv', mode='r', newline='') as solution:

    order = 0
    # read sol1ution sequence
    reader = csv.reader(solution)
    for row in reader:
        sol2[int(row[0])] = order
        order += 1

# get TSP city map
with open('./../2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
    # read TSP city map
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)

# Euclidean distance measuring function


def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist


def make_csv(path, sol):
    f = open(path, 'w')
    # write each element of sol to the csv file
    for i in sol:
        f.write(str(i) + '\n')


def cal_total_cost(sol):
    # evaluate solution cost
    total_cost = 0
    for idx in range(len(sol)-1):
        # get city positions
        pos_city_1 = [float(cities[sol[idx]][0]), float(cities[sol[idx]][1])]
        pos_city_2 = [float(cities[sol[idx+1]][0]),
                      float(cities[sol[idx+1]][1])]

    # distance calculation
        dist = distance(pos_city_1, pos_city_2)

    # accumulation
        total_cost += dist
    return total_cost
    # print('final cost: '+str(total_cost))


# main function
if __name__ == '__main__':
    min_td = float("inf")
    # ga_sol 여러번 돌리기
    for i in range(500):
        sol1 = ga_sol.ga_sol(ga_list.make_adj_list(sol1, sol2))
        tmp = cal_total_cost(sol1)
        if min_td >= tmp:
            min_td = tmp
        sol2 = ga_sol.ga_sol(ga_list.make_adj_list(sol1, sol2))
        tmp = cal_total_cost(sol2)
        if min_td >= tmp:
            min_td = tmp

    make_csv("ga_solution.csv", sol2)
    print(tmp)
