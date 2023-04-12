import csv
import numpy as np
import random as rd


def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist

class Ga_sol:
    def __init__(self, sol1, sol2):
        self.sol1 = sol1
        self.sol2 = sol2
    
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
        sol = [0 for _ in range(1001)]
        adj = self.make_adj_list()
        visited_cities = set()      # the set of visited cities
        visit = 0                   # current city (start at 0)
        order = 0

        visited_cities.add(visit)
        # visit all cities
        while len(visited_cities) < 1000:
            rd.shuffle(adj[visit])
            for i in range(len(adj[visit])):
                if adj[visit][i] not in visited_cities:
                    visit = adj[visit][i]               # visit next city
                    order += 1
                    sol[order] = visit                  # record the order of city
                    visited_cities.add(visit)
                    break
                elif i == len(adj[visit]) - 1:
                    visit = adj[visit][i]
        return sol

class Main:
# given cities
    def __init__(self, sol1, sol2):
        self.cities = []
# sol1ution
        self.sol1 = [0 for _ in range(1001)]
        self.sol2 = [0 for _ in range(1001)]
# with open('./../example_solution.csv', mode='r', newline='') as solution:
        with open('./../example_solution.csv', mode='r', newline='') as solution:

            order = 0
        # read sol1ution sequence
            reader = csv.reader(solution)
            for row in reader:
                self.sol1[order] = int(row[0])
                order += 1

    # need to change this file into new csv sol2
        with open('./../greedy_solution.csv', mode='r', newline='') as solution:

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

        # Euclidean distance measuring function

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
                pos_city_1 = [float(self.cities[sol[idx]][0]), float(self.cities[sol[idx]][1])]
                pos_city_2 = [float(self.cities[sol[idx+1]][0]), float(self.cities[sol[idx+1]][1])]

            # distance calculation
                dist = distance(pos_city_1, pos_city_2)

            # accumulation
                total_cost += dist
            return total_cost
            # print('final cost: '+str(total_cost))        

# main function
if __name__ == '__main__':
    sol = []
    main = Main()
    ga = Ga_sol(main.sol1, main.sol2)
    for _ in range(100):     # GA algorithm
        super_child1 = ga.ga_sol()
        super_child2 = ga.ga_sol()
        child1_tc = main.cal_total_cost(super_child1)
        child2_tc = main.cal_total_cost(super_child2)
        # ga_sol 여러번 돌리기
        for _ in range(10):    # 자식 pool 만들기
            tmp_sol = ga.ga_sol()
            tmp_tc = main.cal_total_cost(tmp_sol)
            if (child1_tc > tmp_tc) | (child2_tc > tmp_tc):          # 가장 우수한 자식쌍 유지
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