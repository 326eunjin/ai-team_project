# 코드 설명(Code Description)

## ga_list.py

- 도시간의 인접리스트(adjacency list)를 구하는 make_adj_list() 메소드가 포함된 코드. 이 인접리스트는 간선재조합에 쓰인다.
- example_solution.csv와 greedy_solution.csv의 각 솔루션을 부모솔루션으로서 리스트로 받아온다.
  이 때의 리스트는 index가 순서, value가 도시를 의미한다. (다른 코드에서의 솔루션은 index가 도시, value가 순서이다)
- 이렇게 받은 두 리스트에서 각 도시별 인접한 도시를 뽑아 인접리스트로 저장한다.

## ga_sol.py

- GA algorithm 중 간선 재조합 방식을 사용한 ga_sol() 메소드가 포함된 코드.
- 도시의 인접리스트(adjacency list)를 인자로 받아 인접리스트상에서 갈 수 있는 후보 도시를 랜덤으로 골라 나아간다.
- 인접리스트상에 간적 없는 인접 도시가 없는 경우 인접 도시의 인접도시를 탐색한다.

## main.py

## tree.py

tree를 만들고 휴리스틱 이용해서 최적의 해를 찾아가는 함수
