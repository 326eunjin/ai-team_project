import random as rd

# GA Algorithm Solution
sol = [0 for i in range(1000)]
visited_cities = set()

def ga_sol():
    adj = adj_cities()          # get adjacency list of cities  @@은진님 파트@@
    order = 0                   # the order of each city
    visit = 0                   # current city (start at 0)
    visited_cities.add(visit)   # the set of visited cities

    # until visiting all citeis
    while len(visited_cities) < 1000:
        order += 1
        rd.shuffle(adj[visit])
        for i in len(adj[visit]):
            if adj[visit][i] not in visited_cities:
                visit = adj[visit][i]               # visit next city
                sol[visit] = order                  # record the order of city
                visited_cities.add(visit)
                break
    
    f = open('ga_solution.csv', 'w')
    for i in sol:
        f.write(str(i) + '\n')

    return sol
