import numpy as np
import random as rd
import csv

cities = []
sol = []


def distance(x, y):
    dist = np.linalg.norm(np.array(x)-np.array(y))
    return dist


with open('2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
    # read TSP city map
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)


def greedy_sol():
    pos_city_1 = [float(cities[sol[idx]][0]), float(cities[sol[idx]][1])]
    pos_city_2 = [float(cities[sol[idx+1]][0]), float(cities[sol[idx+1]][1])]

    # distance calculation
    dist = distance(pos_city_1, pos_city_2)
