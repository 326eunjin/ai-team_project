import random as rd
import csv
import numpy as np


# Euclidean distance measuring function
def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist


# 도시 및 solution에 대한 주요 정보 기록
class Main:
    # given cities
    def __init__(self):
        self.cities = []

        # get TSP city map
        with open('../2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
            # read TSP city map
            reader = csv.reader(tsp)
            for row in reader:
                self.cities.append(row)

    # sol 리스트를 받아 csv파일 생성
    def make_csv(self, path, sol):
        sol = sol[:1000]
        f = open(path, 'w')
        # write each element of sol to the csv file
        for i in sol:
            f.write(str(i) + '\n')

    # sol 리스트를 받아 총 거리 반환
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


# random 알고리즘
class Random_sol:
    def random_sol(self):
        # random solution from 0 -> 999 , first citi is 0
        sol = [0] + rd.sample((range(1, 1000)), 999)
        sol.append(int(0))
        return sol


# main function
if __name__ == '__main__':
    sol = []
    main = Main()
    rand = Random_sol()
    total_cost = float("inf")
    # 가장 우수한 해 선정
    for idx in range(500):
        tmp_sol = rand.random_sol()
        tmp_tc = main.cal_total_cost(tmp_sol)
        if total_cost > tmp_tc:
            sol = tmp_sol
            total_cost = tmp_tc
    main.make_csv("solution_03.csv", sol)
    print(main.cal_total_cost(sol))
