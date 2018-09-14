# Informed/Heuristic Search

Informed Search 란, uninformed search( BFS, DFS, IDS ) 등과는 달리 성능을 향상시키기 위해 주어진 정보를 활용하는 서치이다.

- Heuristic : 완벽하지 않은, 검증 X, 항상 참X, 불확실,증명 가능X 하지만 그럴싸한 정보
- Heuristic Search : h(n) 으로 정의하고, h(n)은 도달 점 까지의 거리를 대략적으로 측정한 값이라고 본다.

# Greedy best-first search
- Greey best-first search는 Greedy search에서 h(n)을 사용하여 돌린 서치
- Optimal 보장이 안됨
- Completeness : 그래프 전체를 돌지 않는 이상 보장 안됨
- Time : O(b^m)  m = maximum depth of search space
- Space : O(b^m)

# A*search
- 쉽게 말해서 Uniformed Cost search 에서 h(n)을 사용하여 돌린 서치이다
- h'(n)은 실제 값( 알 수 없음)으로 가정 할 때 , 0<=h(n)<=h'(n) 을 만족 하면 Optimality 가 보장이 된다.
- h(n)값이 h'(n)값과 비슷하면 비슷 할 수록 더 효율적이다.
- h(n) 값이 0 이면 Uniformed cost search랑 똑같다
- A* search [구현](./a_star.py)