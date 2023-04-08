import random as rd

sol = [0 for i in range(1000)]

# GA Algorithm Solution
def ga_sol(adj):
    visited_cities = set()      # the set of visited cities
    order = 0                   # the order of each city
    visit = 0                   # current city (start at 0)

    visited_cities.add(visit)
    # visit all citeis
    while len(visited_cities) < 1000:
        rd.shuffle(adj[visit])
        for i in range(len(adj[visit])):
            if adj[visit][i] not in visited_cities:
                visit = adj[visit][i]               # visit next city
                order += 1
                sol[visit] = order                  # record the order of city
                visited_cities.add(visit)
                break
        if i == len(adj[visit]) - 1:                # if there is no new city to go,
            visit = adj[visit][i]                   #  go old city and find new city
    return sol
