import random as rd
import csv
import numpy as np
import sys

# given cities
cities = []


def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist


# get TSP city map
with open('../2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
    # read TSP city map
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)


def random_sol():
    # random solution from 0 -> 999 , first citi is 0
    sol = [0] + rd.sample((range(1, 1000)), 999)
    return sol


# evaluate solution cost
def cost_calc(sol):
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


# find the final cost in 500 times random solution
def find_final_cost():
    final_cost = sys.maxsize
    for idx in range(500):
        sol = random_sol()
        sol.append(int(0))
        cost = cost_calc(sol)

        if (final_cost > cost):
            final_cost = cost
            f = open('random_solution.csv', 'w')
            # write each element of sol to the csv file
            for i in range(len(sol) - 1):
                f.write(str(sol[i]) + '\n')

    return final_cost


print("FINAL COST : ", find_final_cost())
