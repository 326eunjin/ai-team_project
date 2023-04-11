import csv
import numpy as np
import ga_list
import ga_sol

# given cities
cities = []
# sol1ution
sol1 = [0 for _ in range(1000)]
sol2 = [0 for _ in range(1000)]
optimzation = []


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


def make_csv(path, sol):
    f = open(path, 'w')
    # write each element of sol to the csv file
    for i in sol:
        f.write(str(i) + '\n')

# Euclidean distance measuring function


def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist


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


# # main function
# if __name__ == '__main__':
#     min_td = float("inf")
#     # ga_sol 여러번 돌리기
#     for i in range(500):
#         sol1 = ga_sol.ga_sol(ga_list.make_adj_list(sol1, sol2))
#         tmp = cal_total_cost(sol1)
#         if min_td >= tmp:
#             min_td = tmp
#         sol2 = ga_sol.ga_sol(ga_list.make_adj_list(sol1, sol2))
#         tmp = cal_total_cost(sol2)
#         if min_td >= tmp:
#             min_td = tmp

#     make_csv("ga_solution.csv", sol2)
#     print(tmp)

def cal_heuristic(index, opt):
    x = cities[index][0]
    y = cities[index][1]
    # 여기서부터 이제 heuristic을 계산하는 함수


def make_tree(sol1, sol2):
    adjacency_list = ga_sol.make_adj_list()
    for i in range(1000):
        opt_len = float("inf")
        j = 0
        for j in len(adjacency_list[i]):
            # 왠지 여기 다녀온 도시인지도 확인해봐야할거같음 set 추가
            # 인접 도시의 인접 도시 문제를 어떻게 해결할 것인가
            tmp = cal_heuristic(j, optimzation)+cal_total_cost(optimzation)
            if (tmp <= opt_len):
                opt_len = tmp
                next_city = j  # 그 다음로 갈 도시
    optimzation.append(j)
    optimzation.append(0)  # 원점으로 돌아가야하니깐
