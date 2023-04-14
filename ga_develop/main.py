import csv
import numpy as np
import random as rd


# Euclidean distance measuring function
def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist


class Ga_sol:
    def __init__(self, sol1, sol2, cities, dist_bound):
        self.sol1 = sol1
        self.sol2 = sol2
        self.cities = cities
        self.dist_bound = dist_bound
        self.adj = self.make_adj_list()
        self.dist_adj = self.make_dist_adj()
        self.visited_cities = set()

    # 세대 교체 메소드
    def generation_change(self, super_child1, super_child2):
        self.sol1 = super_child1
        self.sol2 = super_child2
        self.adj = self.make_adj_list()

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

    def make_dist_adj(self):
        adj_matrix = [[] for _ in self.cities]
        for _from in range(len(self.cities)):
            for _to in range(len(self.cities)):
                if distance([float(self.cities[_from][0]), float(self.cities[_from][1])],
                            [float(self.cities[_to][0]), float(self.cities[_to][1])]) < self.dist_bound:
                    adj_matrix[_from].append(_to)
        return adj_matrix

    def isin_bound(self, city1, city2):
        return distance([float(city1[0]), float(city1[1])],
                        [float(city2[0]), float(city2[1])]) < self.dist_bound

    def mutation(self, visit):
        while True:
            for i in range(len(self.dist_adj[visit])):
                if self.dist_adj[visit][i] not in self.visited_cities:
                    return self.dist_adj[visit][i]
            visit = rd.choice(self.dist_adj[visit])

    def ga_sol(self, mutation_prob):
        sol = [0 for _ in range(1001)]
        visit = 0
        order = 0

        self.visited_cities = set()
        self.visited_cities.add(visit)
        # visit all cities
        while len(self.visited_cities) < 1000:
            rd.shuffle(self.adj[visit])
            for i in range(len(self.adj[visit])):
                if self.adj[visit][i] not in self.visited_cities:
                    # visit next city (mutation occurs in <mutation_prob>)
                    if rd.random() > mutation_prob or self.isin_bound(self.cities[visit], self.cities[self.adj[visit][i]]):
                        visit = self.adj[visit][i]
                    else:
                        visit = self.mutation(visit)
                    order += 1
                    # record the order of city
                    sol[order] = visit
                    self.visited_cities.add(visit)
                    break
                elif i == len(self.adj[visit]) - 1:
                    visit = self.adj[visit][i]
        return sol


class Main:
    # given cities
    def __init__(self):
        self.cities = []
        # sol1ution
        self.sol1 = [0 for _ in range(1001)]
        self.sol2 = [0 for _ in range(1001)]

        # with open('./../example_solution.csv', mode='r', newline='') as solution:
        with open('./../random/random_solution.csv', mode='r', newline='') as solution:

            order = 0
            # read sol1ution sequence
            reader = csv.reader(solution)
            for row in reader:
                self.sol1[order] = int(row[0])
                order += 1

        # need to change this file into new csv sol2
        with open('./../example_solution.csv', mode='r', newline='') as solution:

            order = 0
            # read sol1ution sequence
            reader = csv.reader(solution)
            for row in reader:
                self.sol2[order] = int(row[0])
                order += 1

        # get TSP city map
        with open('./../2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
            # read TSP city map
            reader = csv.reader(tsp)
            for row in reader:
                self.cities.append(row)

    def make_csv(self, path, sol):
        sol = sol[:1000]
        f = open(path, 'w')
        # write each element of sol to the csv file
        for i in sol:
            f.write(str(i) + '\n')

    def cal_total_cost(self, sol):
        # evaluate solution cost
        total_cost = 0
        for idx in range(len(sol)-1):
            # get city positions
            pos_city_1 = [float(self.cities[sol[idx]][0]),
                          float(self.cities[sol[idx]][1])]
            pos_city_2 = [float(self.cities[sol[idx+1]][0]),
                          float(self.cities[sol[idx+1]][1])]
            # distance calculation
            dist = distance(pos_city_1, pos_city_2)
            # accumulation
            total_cost += dist
        return total_cost


# main function
if __name__ == '__main__':
    sol = []
    dist_bound = 10
    mutation_prob = 1
    main = Main()
    ga = Ga_sol(main.sol1, main.sol2, main.cities, dist_bound)

    # 간선 재조합 알고리즘
    for _ in range(10):
        super_child1 = ga.sol1
        super_child2 = ga.sol2
        child1_tc = main.cal_total_cost(super_child1)
        child2_tc = main.cal_total_cost(super_child2)
        # 자식 pool 만들기
        for _ in range(15):
            tmp_sol = ga.ga_sol(mutation_prob)
            tmp_tc = main.cal_total_cost(tmp_sol)
            # 가장 우수한 자식쌍 유지
            if (child1_tc > tmp_tc) or (child2_tc > tmp_tc):
                if child1_tc > child2_tc:
                    super_child1 = tmp_sol
                    child1_tc = tmp_tc
                else:
                    super_child2 = tmp_sol
                    child2_tc = tmp_tc
        ga.generation_change(super_child1, super_child2)
    sol = (super_child1 if child1_tc > child2_tc else super_child2)
    main.make_csv("ga_solution.csv", sol)
    print(main.cal_total_cost(sol))
