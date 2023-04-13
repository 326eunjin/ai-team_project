import csv
import numpy as np
import ga_sol as gl

class main:
    def __init__(self):
    # given cities
        self.cities = []
        # sol1ution
        self.sol1 = [0 for _ in range(1001)]
        self.sol2 = [0 for _ in range(1001)]
        self.optimzation = []

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
            pos_city_1 = [float(self.cities[sol[idx]][0]), float(self.cities[sol[idx]][1])]
            pos_city_2 = [float(self.cities[sol[idx+1]][0]),
                        float(self.cities[sol[idx+1]][1])]

        # distance calculation
            dist = self.distance(pos_city_1, pos_city_2)

        # accumulation
            total_cost += dist
        return total_cost


    # # main function
    # if __name__ == '__main__':
    #     print(cal_total_cost(sol1))
    #     print(cal_total_cost(sol2))
    #     sol = []
    #     ga = gl.Ga_sol(sol1, sol2)
    #     super_child1 = sol1
    #     super_child2 = sol2
    #     for _ in range(2):        # GA algorithm
    #         child1_tc = cal_total_cost(sol1)
    #         child2_tc = cal_total_cost(sol2)
    #         # ga_sol 여러번 돌리기
    #         for _ in range(1000):     # 자식 pool 만들기 (range >= 2)
    #             tmp_sol = ga.ga_sol()
    #             tmp_tc = cal_total_cost(tmp_sol)
    #             if (child1_tc > tmp_tc) | (child2_tc > tmp_tc):          # 가장 우수한 자식쌍 유지
    #                 if child1_tc > child2_tc:
    #                     super_child1 = tmp_sol
    #                     child1_tc = tmp_tc
    #                 else:
    #                     super_child2 = tmp_sol
    #                     child2_tc = tmp_tc
    #         ga.generation_change(super_child1, super_child2)
    #     sol = (super_child1 if child1_tc < child2_tc else super_child2)
    #     make_csv("ga_solution.csv", sol)
    #     print(cal_total_cost(sol))

    def cal_four_points(self, x, y):

        q_1 = []
        q_2 = []
        q_3 = []
        q_4 = []
        tmp = []
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
        tmp = []
        max_2 = 0
        for i in q_2:
            dist = self.distance(i, [x, y])
            if (dist <= max_2):
                max_2 = dist
                tmp = i
        ret.append(tmp)
        tmp = []
        max_3 = 0
        for i in q_3:
            dist = self.distance(i, [x, y])
            if (dist <= max_3):
                max_3 = dist
                tmp = i
        ret.append(tmp)
        tmp = []
        max_4 = 0
        for i in q_4:
            dist = self.distance(i, [x, y])
            if (dist <= max_4):
                max_4 = dist
                tmp = i
        ret.append(tmp)
        ret = [x for x in ret if x]
        return (ret)


    def cal_heuristic(self, index):
        x = float(self.cities[index][0])
        y = float(self.cities[index][1])
        self.point_list = self.cal_four_points(x, y)
        # 1개일때

        # 2개일때

        # 3개일때

        # 4개일때

        return 0


    def make_tree(self):
        # 최적화 경로를 트리를 이용해서 구하는 함수
        ga = gl.Ga_sol(self.sol1, self.sol2)
        adjacency_list = ga.make_adj_list()
        for i in range(1000):
            opt_len = 0
            j = 0
            city = adjacency_list[i]  # 인접도시 리스트
            for j in range(len(city)):
                # if (city not in set(optimzation)):
                # 인접 도시의 인접 도시 문제를 어떻게 해결할 것인가
                tmp = self.cal_heuristic(city[j])+self.cal_total_cost(self.optimzation)
                if (tmp <= opt_len):
                    opt_len = tmp
                    next_city = city[j]  # 그 다음로 갈 도시
            self.optimzation.append(next_city)
        self.optimzation.append(0)  # 원점으로 돌아가야하니깐
        # print(optimzation)


    make_tree()
