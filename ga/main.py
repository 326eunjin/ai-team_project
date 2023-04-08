import numpy as np
import csv

# given cities
cities = []

# Euclidean distance measuring function


def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist


# 2. get TSP city map
with open('2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
    # read TSP city map
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)
