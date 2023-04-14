import random as rd
import csv
import numpy as np


def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist

class Main:
    def __init__(self):
        self.cities = []

        # get TSP city map
        with open('../2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
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
    
class Random_sol:
    def random_sol(self):
        # random solution from 0 -> 999 , first citi is 0
        sol = [0] + rd.sample((range(1, 1000)), 999)
        sol.append(int(0))
        return sol

if __name__ == '__main__':
    sol = []
    main = Main()
    rand = Random_sol()
    total_cost = float("inf")
    for idx in range(500):
        tmp_sol = rand.random_sol()
        tmp_tc = main.cal_total_cost(tmp_sol)
        if total_cost > tmp_tc:
            sol = tmp_sol
            total_cost = tmp_tc
    main.make_csv("random_solution.csv", sol)
    print(main.cal_total_cost(sol))
