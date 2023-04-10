import random as rd

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
            tmp_set.add(self.sol1[i-1])
            tmp_set.add(self.sol1[i+1])
            tmp_set.add(self.sol2[i-1])
            tmp_set.add(self.sol2[i+1])
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
        sol[0] = 0
        while len(visited_cities) < 1000:
            rd.shuffle(adj[visit])
            for i in range(len(adj[visit])):
                if adj[visit][i] not in visited_cities:
                    visit = adj[visit][i]               # visit next city
                    order += 1
                    sol[order] = visit                  # record the order of city
                    visited_cities.add(visit)
                    break
            if i == len(adj[visit]) - 1:
                visit = adj[visit][i]
        return sol
