# Project #1
## 유전 알고리즘의 최적화 기법을 활용한 TSP문제 최적화
-  ❖Traveling Salesman Problem 문제의 해를 유전 알고리즘을 이용하여 구함 
-  ❖제안한 유전 알고리즘 기법의 설명 및 실험적 결과 보고
-  ❖해 공간의 부분, 계층, 혹은 전체를 트리 구조로 구성하여 최적화 탐색 기법에 활용함 
-  ❖완전 무작위 (heuristic, brute force search) 탐색과 제안한 탐색의 차별성을 설명함
# 코드 설명(Code Description)
## greedy.py
- ga_sol.py에서 쓴 간선재조합 방식에서는 부모솔루션이 두 개 필요하다.
- 하나는 교수님께서 주신 example_solution.csv이고, 다른 하나는 greedy algorithm으로 구한 solution으로 하기로 했다.
- 이 코드는 greedy algorithm으로 solution을 구하고 greedy_solution.csv파일로 저장하는 역할을 한다.
- (우리가 필요한 건 greedy_solution.csv파일뿐이므로 이 코드는 일회성이다)
## TSP_eval.py
- 다른 부분은 교수님께서 올려주신 그대로되, csv reader상의 인코딩 문제로 34줄에 encoding='utf-8-sig' 부분을 추가
- numpy 모듈이 별도로 설치돼있어야 실행 할 수 있고, 아래 명령어를 통해 설치
>	sudo apt-get update

>   sudo apt-get install python-pip

>   pip install numpy
    
# Project #2
## 인공신경망을 화용한 영상 분류 (classification) 모델 학습
-  ❖Traveling Salesman Problem 문제의 해를 유전 알고리즘을 이용하여 구함 
-  ❖제안한 유전 알고리즘 기법의 설명 및 실험적 결과 보고
-  ❖해 공간의 부분, 계층, 혹은 전체를 트리 구조로 구성하여 최적화 탐색 기법에 활용함 
-  ❖완전 무작위 (heuristic, brute force search) 탐색과 제안한 탐색의 차별성을 설명함
