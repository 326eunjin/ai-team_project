import csv
import numpy as np
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
            tmp_set.add(self.sol1[(self.sol1.index(i)+999) % 1000])
            tmp_set.add(self.sol2[(self.sol2.index(i)+999) % 1000])
            tmp_set.add(self.sol1[(self.sol1.index(i)+1) % 1000])
            tmp_set.add(self.sol2[(self.sol2.index(i)+1) % 1000])
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
        while len(visited_cities) < 1000:
            rd.shuffle(adj[visit])
            for i in range(len(adj[visit])):
                if adj[visit][i] not in visited_cities:
                    visit = adj[visit][i]               # visit next city
                    order += 1
                    # record the order of city
                    sol[order] = visit
                    visited_cities.add(visit)
                    break
                elif i == len(adj[visit]) - 1:
                    visit = adj[visit][i]
        return sol


class Main:
    def __init__(self):
        # given cities
        self.cities = []
        # sol1ution
        self.sol1 = [0 for _ in range(1001)]
        self.sol2 = [0 for _ in range(1001)]
        self.optimization = []

        # need to change this file into new csv sol1
        with open('./../greedy_solution.csv', mode='r', newline='') as solution:

            order = 0
            # read sol1ution sequence
            reader = csv.reader(solution)
            for row in reader:
                self.sol1[order] = int(row[0])
                order += 1

        # need to change this file into new csv sol2
        with open('./../random/random_solution.csv', mode='r', newline='') as solution:

            order = 0
            # read sol1ution sequence
            reader = csv.reader(solution)
            for row in reader:
                self.sol2[order] = int(row[0])
                order += 1

        # get TSP city map
        with open('./../2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
            # read TSP city map
            reader = csv.reader(tsp)
            for row in reader:
                self.cities.append(row)

        # Euclidean distance measuring function

    def distance(self, x, y):
        dist = np.linalg.norm(np.array(x) - np.array(y))
        return dist

    def make_csv(self, path, sol):
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
            dist = self.distance(pos_city_1, pos_city_2)

        # accumulation
            total_cost += dist
        return total_cost

    def cal_four_points(self, x, y):

        q_1 = []
        q_2 = []
        q_3 = []
        q_4 = []
        tmp = 0
        ret = []
        # ret은 2차원리스트인데 가장 작은 점을 포함
        # # 여기서부터 이제 사분면을 기준으로 가장 먼점을 계산하는 함수
        for i, j in self.cities:
            if (float(i) > x and float(j) > y):
                q_1.append([float(i), float(j)])
            elif (float(i) < x and float(j) > y):
                q_2.append([float(i), float(j)])
            elif (float(i) < x and float(j) < y):
                q_3.append([float(i), float(j)])
            elif (float(i) > x and float(j) < y):
                q_4.append([float(i), float(j)])

        max_1 = 0
        for i in q_1:
            dist = self.distance(i, [x, y])
            if (dist >= max_1):
                max_1 = dist
                tmp = i
        ret.append(tmp)
        tmp = 0
        max_2 = 0
        for i in q_2:
            dist = self.distance(i, [x, y])
            if (dist >= max_2):
                max_2 = dist
                tmp = i
        ret.append(tmp)
        tmp = 0
        max_3 = 0
        for i in q_3:
            dist = self.distance(i, [x, y])
            if (dist >= max_3):
                max_3 = dist
                tmp = i
        ret.append(tmp)
        tmp = 0
        max_4 = 0
        for i in q_4:
            dist = self.distance(i, [x, y])
            if (dist >= max_4):
                max_4 = dist
                tmp = i
        ret.append(tmp)
        return (ret)

    def cal_heuristic(self, index):
        x = float(self.cities[index][0])
        y = float(self.cities[index][1])
        ret = 0
        point_list = self.cal_four_points(x, y)
        length = len([point_list for z in point_list if z])
        # 1개일때
        if (length == 1):
            ret = self.distance(point_list[0], [x, y])
        # 2개일때
        elif (length == 2):
            tmp = [z for z in point_list if z]
            tmp.append([x, y])
            tmp.sort()
            ret = self.distance(tmp[0], tmp[1]) \
                + self.distance(tmp[1], tmp[2]) + self.distance(tmp[0], tmp[2])
        # 3개일때
        elif (len == 3):
            # if (point_list[0]==0):
            #     ret = self.distance(point_list[1],[x,y])+self.distance(point_list[1],point_list[2])+self.distance(point_list[2],point_list[3])+self.distance([x,y],point_list[3])
            # elif (point_list[1]==0):
            #     ret = self.distance(point_list[0],[x,y])+self.distance([x,y],point_list[2])+self.distance(point_list[2],point_list[3])+self.distance(point_list[3],point_list[0])
            # elif (point_list[2]==0):
            #     ret = self.distance(point_list[0],point_list[1])+self.distance([x,y],point_list[1])+self.distance(point_list[3],[x,y])+self.distance(point_list[3],point_list[0])
            # elif (point_list[3]=='[]'):
            #     ret = self.distance(point_list[0],[x,y])+self.distance(point_list[1],point_list[0])+self.distance(point_list[2],point_list[1])+self.distance(point_list[2],[x,y])
            if 0 in point_list:
                idx = point_list.index(0)
                indices = [idx-1, idx+1, idx-2, idx+2]
                ret = sum(self.distance(point_list[i], point_list[j]) for i, j in zip(
                    indices, indices[1:]+indices[:1]))

        # 4개일때
        else:
            dist = []
            tmp = []
            for i in range(4):
                dist.append([self.distance([x, y], point_list[i]), i])
                # dist에는 [거리,i]이렇게 들어감 i는 분면 근데 i=0인게 1사분면
                # dist.sort()[0][0]#가장 짧은 거리
            sorted_dist = sorted(dist, key=lambda x: x[0], reverse=False)
            if (sorted_dist[1][1] % 2 == sorted_dist[0][1] % 2):  # 대각선인경우
                tmp.append(sorted_dist[2])
            else:
                tmp.append(sorted_dist[1])
            tmp.append(sorted_dist[0])
            ret = self.distance(point_list[0], point_list[1])+self.distance(point_list[1], point_list[2])+self.distance(point_list[2], point_list[3])+self.distance(point_list[3], point_list[0])\
                - self.distance(point_list[tmp[0][1]],
                                point_list[tmp[1][1]])+tmp[0][0]+tmp[1][0]
        return ret

    def make_tree(self):
        # 최적화 경로를 트리를 이용해서 구하는 함수
        ga = Ga_sol(self.sol1, self.sol2)
        adjacency_list = ga.make_adj_list()
        for i in range(1000):
            opt_len = float("inf")
            j = 0
            city = adjacency_list[i]  # 인접도시 리스트
            next_city = 0
            for j in range(len(city)):
                if (city[j] not in set(self.optimization)):
                    # 인접 도시의 인접 도시 문제를 어떻게 해결할 것인가
                    # sprint(self.cal_total_cost(self.optimization))
                    tmp = self.cal_heuristic(
                        city[j])+self.cal_total_cost(self.optimization)
                if (tmp <= opt_len):
                    opt_len = tmp
                    next_city = city[j]  # 그 다음로 갈 도시
            self.optimization.append(next_city)
        self.optimization.append(0)  # 원점으로 돌아가야하니깐
        return self.optimization


# # main function
if __name__ == '__main__':
    opt = []
    main = Main()
    ga = Ga_sol(main.sol1, main.sol2)
    opt = main.make_tree()
    main.make_csv("tree_solution.csv", opt)
    print(main.cal_total_cost(opt))
