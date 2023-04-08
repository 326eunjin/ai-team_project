import numpy as np
import csv
import ga_list
import ga_sol

# given cities
cities = []
adj = ga_list.make_adj_list()

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
    # 3. evaluate solution cost
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


# 2. get TSP city map
with open('./../2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
    # read TSP city map
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)

if __name__ == '__main__':
    # main function
    # ga_sol 여러번 돌리기
    min_td = float("inf")
    for i in range(1):
        print("*")
        tmp_sol = ga_sol.ga_sol(adj)
        print("**")
        tmp = cal_total_cost(tmp_sol)
        print("3")
        if min_td >= tmp:
            min_td = tmp
    make_csv("ga_sol_ret", tmp_sol)
    print(tmp)
