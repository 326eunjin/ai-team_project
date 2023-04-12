import random as rd
import csv
import numpy as np
import ga_sol as gl

# given cities
cities = []
# sol1ution
sol1 = [0 for _ in range(1001)]
sol2 = [0 for _ in range(1001)]

# need to change this file into new csv sol1
with open('./../example_solution.csv', mode='r', newline='') as solution:

    order = 0
    # read sol1ution sequence
    reader = csv.reader(solution)
    for row in reader:
        sol1[order] = int(row[0])
        order += 1

# need to change this file into new csv sol2
with open('./../random/random_solution.csv', mode='r', newline='') as solution:

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
    sol = sol[:1000]
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


class Ga_sol:
    def __init__(self, sol1, sol2, cities):
        self.sol1 = sol1
        self.sol2 = sol2
        self.cities = cities
        self.visited_cities = set()
        self.centroid = [0, 0]
        for city in self.cities:
            self.centroid[0] += float(city[0])
            self.centroid[1] += float(city[1])
        self.centroid[0] /= 1000
        self.centroid[1] /= 1000

    def generation_change(self, super_child1, super_child2):   # 세대 교체 메소드
        self.sol1 = super_child1
        self.sol2 = super_child2

    def make_adj_list(self):
        adjacency_list = [0 for _ in range(1000)]
        for i in range(1000):
            tmp_set = set()
            tmp_set.add(self.sol1[(self.sol1.index(i)+999) % 1000])
            tmp_set.add(self.sol2[(self.sol2.index(i)+999) % 1000])
            tmp_set.add(self.sol1[(self.sol1.index(i)+1) % 1000])
            tmp_set.add(self.sol2[(self.sol2.index(i)+1) % 1000])
            adjacency_list[i] = list(tmp_set)
        return adjacency_list

    # GA Algorithm Solution
    def ga_sol(self):
        if len(self.visited_cities) < 999:
            adj = self.make_adj_list()
        else:
            adj = list(self.visited_cities - set([i for i in range(1000)]))
        # visited_cities = set()      # the set of visited cities
        visit = 0                   # current city (start at 0)
        order = 0

        self.visited_cities.add(visit)
        self.centroid = self.update_centroid(visit)

        sol = [0 for _ in range(1001)]
        # visit all cities
        while len(self.visited_cities) < 1000:
            # rd.shuffle(adj[visit])
            adj[visit] = self.heuristic(adj, visit)
            for i in range(len(adj[visit])):
                if adj[visit][i] not in self.visited_cities:
                    visit = adj[visit][i]               # visit next city
                    order += 1
                    # record the order of city
                    sol[order] = visit
                    self.visited_cities.add(visit)
                    self.centroid = self.update_centroid(visit)
                    break
                elif i == len(adj[visit]) - 1:
                    visit = adj[visit][rd.choice(range(len(adj[visit])))]
            # if len(self.visited_cities) == 1000:
        print(sol)
        return sol

    def update_centroid(self, visit):
        if len(self.visited_cities) == 999:
            return [0, 0]
        return [((float(self.centroid[0]) * (1000 - len(self.visited_cities))) - float(cities[visit][0]))/(999 - len(self.visited_cities)),
                ((float(self.centroid[1]) * (1000 - len(self.visited_cities))) - float(cities[visit][1]))/(999 - len(self.visited_cities))]

    def heuristic(self, adj, visit):
        centroid = self.update_centroid(visit)
        return sorted(adj[visit], key=lambda x:
                      distance([float(cities[x][0]), float(cities[x][1])],
                               [float(centroid[0]), float(centroid[0])])
                      / distance([float(cities[0][0]), float(cities[0][1])],
                                 [float(centroid[0]), float(centroid[1])]))


# main function
if __name__ == '__main__':
    print(cal_total_cost(sol1))
    print(cal_total_cost(sol2))
    sol = []
    ga = Ga_sol(sol1, sol2, cities)
    super_child1 = sol1
    super_child2 = sol2
    for _ in range(10):        # GA algorithm
        # 세대교체
        child1_tc = cal_total_cost(sol1)
        child2_tc = cal_total_cost(sol2)
        # ga_sol 여러번 돌리기
        for _ in range(10):     # 자식 pool 만들기 (range >= 2)
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
    sol = (super_child1 if child1_tc < child2_tc else super_child2)
    make_csv("ga_solution.csv", sol)
    print(cal_total_cost(sol))
