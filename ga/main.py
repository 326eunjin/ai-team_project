import csv
import numpy as np
import ga_sol as gl

# given cities
cities = []
# sol1ution
sol1 = [0 for _ in range(1001)]
sol2 = [0 for _ in range(1001)]

# with open('./../example_solution.csv', mode='r', newline='') as solution:
with open('./../example_solution.csv', mode='r', newline='') as solution:

    order = 0
    # read sol1ution sequence
    reader = csv.reader(solution)
    for row in reader:
        sol1[order] = int(row[0])
        order += 1

# need to change this file into new csv sol2
with open('./../greedy_solution.csv', mode='r', newline='') as solution:

    order = 0
    # read sol1ution sequence
    reader = csv.reader(solution)
    for row in reader:
        sol2[order] = int(row[0])
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
        pos_city_2 = [float(cities[sol[idx+1]][0]), float(cities[sol[idx+1]][1])]

    # distance calculation
        dist = distance(pos_city_1, pos_city_2)

    # accumulation
        total_cost += dist
    return total_cost
    # print('final cost: '+str(total_cost))


# main function
if __name__ == '__main__':
    sol = []
    ga = gl.Ga_sol(sol1, sol2)
    for _ in range(100):     # GA algorithm
        super_child1 = ga.ga_sol()
        super_child2 = ga.ga_sol()
        child1_tc = cal_total_cost(super_child1)
        child2_tc = cal_total_cost(super_child2)
        # ga_sol 여러번 돌리기
        for _ in range(10):    # 자식 pool 만들기
            tmp_sol = ga.ga_sol()
            tmp_tc = cal_total_cost(tmp_sol)
            if (child1_tc > tmp_tc) | (child2_tc > tmp_tc):          # 가장 우수한 자식쌍 유지
                if child1_tc > child2_tc:
                    super_child1 = tmp_sol
                    child1_tc = tmp_tc
                else:
                    super_child2 = tmp_sol
                    child2_tc = tmp_tc
        ga.generation_change(super_child1, super_child2)
    sol = (super_child1 if child1_tc > child2_tc else super_child2)
    make_csv("ga_solution.csv", sol)
    print(cal_total_cost(sol))
