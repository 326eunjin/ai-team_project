# 코드 설명(Code Description)
## greedy.py
- ga_sol.py에서 쓴 간선재조합 방식에서는 부모솔루션이 두 개 필요하다.
  하나는 교수님께서 주신 example_solution.csv이고, 다른 하나는 greedy algorithm으로 구한 solution이다.
  이 코드는 greedy algorithm으로 solution을 구하고 greedy_solution.csv파일로 저장하는 역할을 한다.
  (우리가 필요한 건 greedy_solution.csv파일이므로 이 코드는 일회성이다)
-----------------------------------------------------------------------
## TSP_eval.py
- 다른 부분은 교수님께서 올려주신 그대로되, csv reader상의 인코딩 문제로 34줄에 encoding='utf-8-sig' 부분을 추가
- numpy 모듈이 별도로 설치돼있어야 실행 할 수 있고, 아래 명령어를 통해 설치
>	sudo apt-get update

>   sudo apt-get install python-pip

>   pip install numpy
    
