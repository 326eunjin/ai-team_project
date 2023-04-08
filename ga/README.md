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
- GA algorithm을 여러번 돌려 최적해에 근사한 값을 찾도록 하는 코드.
- ga_sol.py와 ga_list.py를 import하여 GA algorithm을 돌린다.
- GA algorithm을 돌려 나온 solution의 total distance를 구해가며 최적해를 찾아간다.
- 반복 시행이 끝나면 ga_solution.csv파일을 생성하고 최소 total distance를 출력한다.

-------------------------------------------------------------------------------------------------------
## greedy.py
- ga_sol.py에서 쓴 간선재조합 방식에서는 부모솔루션이 두 개 필요하다.
  하나는 교수님께서 주신 example_solution.csv이고, 다른 하나는 greedy algorithm으로 구한 solution이다.
  이 코드는 greedy algorithm으로 solution을 구하고 greedy_solution.csv파일로 저장하는 역할을 한다.
  (우리가 필요한 건 greedy_solution.csv파일이므로 이 코드는 일회성이다)