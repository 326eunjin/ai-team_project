import csv
import numpy as np

cities = []

sol = []
visited_cities = set()


def distance(x, y):
    dist = np.linalg.norm(np.array(x) - np.array(y))
    return dist


with open('./2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
    # read TSP city map
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)


def greedy():
    i = 0
    order = 0
    # i가 지금 도시
    # j가 앞으로 갈 도시
    while len(visited_cities) < 1000:
        min = float("inf")
        argmin = 0
        for j in range(len(cities)):  # 전체를 돌면서
            if j in visited_cities:
                continue
            pos_city_1 = [float(cities[j][0]),
                          float(cities[j][1])]
            pos_city_2 = [float(cities[i][0]),
                          float(cities[i][1])]
            dist = distance(pos_city_1, pos_city_2)
            # 거리가 기존의 최소값보다 작고 이미 방문한적이 없는 도시이면
            if min > dist:
                min = dist
                # 최솟값 업데이트 즉, 가장 가까운 도시로 바꿔줌
                argmin = j
                # argmin은 앞으로 갈 도시 중 가장 가까운 도시
        i = argmin
        visited_cities.add(i)
        sol[order] = i
        order += 1

    f = open('greedy_solution.csv', 'w')

    for i in sol:
        f.write(str(i) + '\n')

    return sol


greedy()
