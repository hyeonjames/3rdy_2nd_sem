# Uninformed Search
- Uninformed Blind Search
    - Breath-first BFS
    - Depth-first DFS
    - Iterative deepening depth-first
    - uniform cost

## Searching 알고리즘 고려해야 할 점
1. Completeness
    - 해당 함수는 어느 솔루션이던 찾을 수 있는가?
2. Optimality
    - 찾은 솔루션이 언제든지 최적의 솔루션인가?
3. Time complexity
    - b : maximum branching factor of the search tree ; 트리의 차수 ( 자식노드가 가장 많은 것의 자식노드 갯수 )
    - d : 최적의 솔루션에서의 깊이
    - m : 트리의 최대 깊이
4. Space complexity


## BFS
- 너비 우선 탐색
- 기본 룰 : 부모노드로는 가지 않음
- 큐 이용
- Completeness : Y 
- Optimality : Y
- Time complexity : O(b^(d+1)) = O(b^d)
- Space complexity : O(b^(d+1)) = O(b^d)

## DFS
- 깊이 우선 탐색
- 기본 룰 : 현재 path에서 갔던 곳은 가지 않음
- 스택 이용
- Completeness : 루프가 생기는 경우 N
    - 기존 그래프 탐색에서는 기본 룰 때문에 루프가 생기지 않지만 다른 문제에서는 생길 수 있음
- Optimality: N
- Time complexity : O(b^m)
- Space Complexity : O(bm)

## BFS vs DFS
- Time Complexity : 대게는 비슷함
    - many goals, no loops , no infinite paths => DFS가 평균적으로 나음
    - goal이 그렇게 깊지 않은 경우, infinite paths or 많은 loops or 적은 메모리를 차지하는 경우 BFS가 좋음
- Space Complexity : DFS 월등


## DFS with a depth-limit L
- DFS랑 같이 동작하지만 깊이 L초과는 내려가지 않음
- 솔루션이 깊이 L초과에 있다면 incomplete
- infinite paths 문제 해결
- Time Complexity : O(b^l)
- Space Complexity : O(bl)

## Iterative Deepening Search (IDS)
- DFS with a depth limit L의 활용
- L을 점점 키워나가면서 DFS 수행
- Completeness : Y
- Optimality : Y as long as step = 1
- Time Complexity : O(b^d)
    - b + (b+b^2) + (b+b^2+b^3) + ... (b+...b^d) = O(b^d)
    - worst-case는 그다지 차이 안남
- Space Complexity : O(bd)

## Uniform cost search
- Optimality : 모든 경로의 가중치가 양수인 경우만 Y
- 다익스트라의 일종
- 우선순위 큐 이용한다
- Time & Space complexity = O(b^\[C*/ε\])
    - C* =최적의 솔루션에서의 cost
    - floor(C*/ε) = 모든 cost가 거의 같다고 가정할때의 솔루션의 깊이
- 
