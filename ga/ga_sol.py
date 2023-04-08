import random as rd

# GA Algorithm Solution
sol = [0 for i in range(1000)]
adj = adj_cities()              # get adjacency list of cities  @@은진님 파트@@

def ga_sol():
    order = 0                   # the order of each city
    visit = 0                   # current city (start at 0)
    visited_cities = set()      # the set of visited cities

    visited_cities.add(visit)
    # visit all citeis
    while len(visited_cities) < 1000:
        order += 1
        rd.shuffle(adj[visit])
        for i in len(adj[visit]):
            if adj[visit][i] not in visited_cities:
                visit = adj[visit][i]               # visit next city
                sol[visit] = order                  # record the order of city
                visited_cities.add(visit)
                break
    
    # make solution as csv file
    f = open('ga_solution.csv', 'w')
    for i in sol:
        f.write(str(i) + '\n')

    return sol
