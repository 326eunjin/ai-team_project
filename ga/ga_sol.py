from ga_list import make_adj_list
import random as rd
# GA Algorithm Solution
sol = []


def ga_sol(adj):
    visit = 0                   # current city (start at 0)
    visited_cities = set()      # the set of visited cities

    visited_cities.add(visit)
    # visit all citeis
    while len(visited_cities) < 1000:
        rd.shuffle(adj[visit])
        for i in range(len(adj[visit])):
            if adj[visit][i] not in visited_cities:
                visit = adj[visit][i]               # visit next city
                sol.append(visit)                  # record the order of city
                visited_cities.add(visit)
                break
        if i == len(adj[visit]) - 1:
            visit = adj[visit][i]
    return sol
