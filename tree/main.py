import csv
import numpy as np
import random as rd


def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist


class Ga_sol:
    def __init__(self, sol1, sol2, cities, dist_bound):
        self.sol1 = sol1
        self.sol2 = sol2
        self.cities = cities
        self.dist_bound = dist_bound
        self.adj = self.make_adj_list()
        self.dist_adj = self.make_dist_adj(dist_bound)
        self.visited_cities = set()
    # 세대 교체 메소드

    def generation_change(self, super_child1, super_child2):
        self.sol1 = super_child1
        self.sol2 = super_child2
        self.adj = self.make_adj_list()

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

    def cal_four_points(self, x, y):
        unvisited_cities = set(list(range(1000))) - self.visited_cities
        q_1 = []
        q_2 = []
        q_3 = []
        q_4 = []
        tmp = 0
        ret = []
        # ret은 가장 작은 점을 포함하는 2차원리스트
        # 사분면을 기준으로 가장 먼점을 계산
        for n in unvisited_cities:
            if n not in self.visited_cities:
                i, j = self.cities[n][0], self.cities[n][1]
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
            dist = distance(i, [x, y])
            if (dist >= max_1):
                max_1 = dist
                tmp = i
        ret.append(tmp)
        tmp = 0
        max_2 = 0
        for i in q_2:
            dist = distance(i, [x, y])
            if (dist >= max_2):
                max_2 = dist
                tmp = i
        ret.append(tmp)
        tmp = 0
        max_3 = 0
        for i in q_3:
            dist = distance(i, [x, y])
            if (dist >= max_3):
                max_3 = dist
                tmp = i
        ret.append(tmp)
        tmp = 0
        max_4 = 0
        for i in q_4:
            dist = distance(i, [x, y])
            if (dist >= max_4):
                max_4 = dist
                tmp = i
        ret.append(tmp)
        return (ret)

    def cal_heuristic(self, city):
        x = float(city[0])
        y = float(city[1])
        ret = 0
        point_list = self.cal_four_points(x, y)
        length = len([point_list for z in point_list if z])
        # 1개일때
        if (length == 1):
            ret = distance(point_list[0], [x, y])
        # 2개일때
        elif (length == 2):
            tmp = [z for z in point_list if z]
            tmp.append([x, y])
            tmp.sort()
            ret = distance(tmp[0], tmp[1]) \
                + distance(tmp[1], tmp[2]) + distance(tmp[0], tmp[2])
        # 3개일때
        elif (length == 3):
            if (point_list[0] == 0):
                ret = distance(point_list[1], [x, y])+distance(point_list[1], point_list[2])+distance(
                    point_list[2], point_list[3])+distance([x, y], point_list[3])
            elif (point_list[1] == 0):
                ret = distance(point_list[0], [x, y])+distance([x, y], point_list[2])+distance(
                    point_list[2], point_list[3])+distance(point_list[3], point_list[0])
            elif (point_list[2] == 0):
                ret = distance(point_list[0], point_list[1])+distance([x, y], point_list[1])+distance(
                    point_list[3], [x, y])+distance(point_list[3], point_list[0])
            elif (point_list[3] == 0):
                ret = distance(point_list[0], [x, y])+distance(point_list[1], point_list[0])+distance(
                    point_list[2], point_list[1])+distance(point_list[2], [x, y])
        # 4개일때
        else:
            dist = []
            tmp = []
            for i in range(4):
                dist.append([distance([x, y], point_list[i]), i])
            # dist에는 [거리,i]이렇게 들어감 i는 분면 근데 i=0인게 1사분면
            # dist.sort()[0][0]#가장 짧은 거리
            sorted_dist = sorted(dist, key=lambda x: x[0], reverse=False)
            if (sorted_dist[1][1] % 2 == sorted_dist[0][1] % 2):  # 대각선인경우
                tmp.append(sorted_dist[2])
            else:
                tmp.append(sorted_dist[1])
            tmp.append(sorted_dist[0])
            ret = distance(point_list[0], point_list[1])+distance(point_list[1], point_list[2])+distance(point_list[2], point_list[3])+distance(point_list[3], point_list[0])\
                - distance(point_list[tmp[0][1]],
                           point_list[tmp[1][1]])+tmp[0][0]+tmp[1][0]
        return ret

    def make_dist_adj(self, dist_bound):
        adj_matrix = [[] for _ in self.cities]
        for _from in range(len(self.cities)):
            for _to in range(len(self.cities)):
                if distance([float(self.cities[_from][0]), float(self.cities[_from][1])],
                            [float(self.cities[_to][0]), float(self.cities[_to][1])]) < dist_bound:
                    adj_matrix[_from].append(_to)
        return adj_matrix

    def isin_bound(self, city1, city2):
        return distance([float(city1[0]), float(city1[1])],
                        [float(city2[0]), float(city2[1])]) < self.dist_bound

    def mutation(self, visit):
        while True:
            for i in range(len(self.dist_adj[visit])):
                if self.dist_adj[visit][i] not in self.visited_cities:
                    return self.dist_adj[visit][i]
            visit = rd.choice(self.dist_adj[visit])

        # GA Algorithm Solution
    def ga_sol(self, mutation_prob):
        sol = [0 for _ in range(1001)]  # 결과값
        visit = 0   # current city (start at 0)
        order = 0
        # flag = True
        self.visited_cities = set()  # 이미 간 도시인지 확인/여기선 초기화
        self.visited_cities.add(visit)  # 현재 도시 집합에 추가

        # visit all cities
        while len(self.visited_cities) < 1000:  # 종료조건 모든 점 순회
            print(len(self.visited_cities), visit)
            # visit 현재 도시
            # x가 갈 수 있는 모든 도시
            self.adj[visit] = sorted(self.adj[visit], key=lambda x:
                                     self.cal_heuristic(self.cities[x]) +
                                     distance([float(self.cities[visit][0]), float(self.cities[visit][1])],
                                              [float(self.cities[x][0]), float(self.cities[x][1])]))
            # g(n)+h(n) 기준 정렬
            for i in range(len(self.adj[visit])):  # 인접도시 돌면서
                if self.adj[visit][i] not in self.visited_cities:  # 인접도시가 방문하지 않은 도시면
                    # 인접 도시와의 거리가 dist_bound보다 작으면 mutation_prob 확률로 이동
                    # if (flag):
                    if rd.random() > mutation_prob or self.isin_bound(self.cities[visit], self.cities[self.adj[visit][i]]):
                        visit = self.adj[visit][i]
                    # 아니면 돌연변이 발생
                    else:
                        visit = self.mutation(visit)
                    # 순서++
                    order += 1
                    sol[order] = visit
                    # 현재 도시 추가
                    self.visited_cities.add(visit)
                    # 갔다온 도시 목록에도 추가
                    break
                # 내가 갈 수 있는 도시가 모두 이미 방문한 도시이면 가까운 도시중 하나로 이동
                elif i == len(self.adj[visit]) - 1:
                    visit = rd.choice(list(self.dist_adj[visit]))
        return sol


class Main:
    # given cities
    def __init__(self):
        self.cities = []
        # sol1ution
        self.sol1 = [0 for _ in range(1001)]
        self.sol2 = [0 for _ in range(1001)]
        # with open('./../example_solution.csv', mode='r', newline='') as solution:
        with open('/Users/jang-eunjin/Desktop/ai-team_project/example_solution.csv', mode='r', newline='') as solution:

            order = 0
            # read sol1ution sequence
            reader = csv.reader(solution)
            for row in reader:
                self.sol1[order] = int(row[0])
                order += 1

        # need to change this file into new csv sol2
        with open('/Users/jang-eunjin/Desktop/ai-team_project/random/random_solution.csv', mode='r', newline='') as solution:

            order = 0
            # read sol1ution sequence
            reader = csv.reader(solution)
            for row in reader:
                self.sol2[order] = int(row[0])
                order += 1

        # get TSP city map
        with open('/Users/jang-eunjin/Desktop/ai-team_project/2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
            # read TSP city map
            reader = csv.reader(tsp)
            for row in reader:
                self.cities.append(row)

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
            dist = distance(pos_city_1, pos_city_2)

            # accumulation
            total_cost += dist
        return total_cost


# main function
if __name__ == '__main__':
    sol = []
    dist_bound = 15
    mutation_prob = 0.5
    main = Main()
    ga = Ga_sol(main.sol1, main.sol2, main.cities, dist_bound)
    # 세대 교체
    for _ in range(50):
        super_child1 = ga.sol1
        super_child2 = ga.sol2
        child1_tc = main.cal_total_cost(super_child1)
        child2_tc = main.cal_total_cost(super_child2)
        # 자식 pool 만들기
        for _ in range(10):
            tmp_sol = ga.ga_sol(mutation_prob)
            tmp_tc = main.cal_total_cost(tmp_sol)
            # 가장 우수한 자식쌍 유지
            if (child1_tc > tmp_tc) or (child2_tc > tmp_tc):
                if child1_tc > child2_tc:
                    super_child1 = tmp_sol
                    child1_tc = tmp_tc
                else:
                    super_child2 = tmp_sol
                    child2_tc = tmp_tc
        ga.generation_change(super_child1, super_child2)
    sol = (super_child1 if child1_tc < child2_tc else super_child2)
    sol = sol[:1000]
    main.make_csv("tree_solution_2.csv", sol)
    print(main.cal_total_cost(sol))
