# Constraint Satisfaction Problems
1. Constraitn Satisfaction problems
2. Backtracking search for CSPs
3. Local search for CSPs


## CSPs
- 일반적인 탐색 문제 : state is a black box - 어떤 자료구조이던지 다 됨 ( successor function, heuristic function, goal test 가 있다는 하에 )
- CSP :
    - state 는 변수들 Xi와 도메인 Di에 있는 값들에 의해 정해진다
    - goal test : 제약조건의 집합을 만족하는 값들의 조합?
    - 아 모르겠고 그냥 제약조건이 있다

## CSPs의 종류
1. 분리된 변수들
    - 유한한 도메인
        - n개의 변수, 도메인 크기 d라고 할때 O(d^n) 의 복잡도
        - e.g Boolean csps 
    - 무한한 도메인
        - integers, strings, etc
        - e.g job scheduleing
        - need a constraint language e.g. StartJob1 + 5 <= StartJob3
2. 연속된 변수들
    - 범위가 있는 변수들
    - Hubble Space Telescope 관찰을 위한 시작 및 종료 시간
## 제약조건의 종류
1. Unary - 제약조건이 하나의 변수만 연관된 경우
    - e.g., SA != green
2. Binary - 제약조건이 둘의 변수가 연관된 경우
    - e.g., SA != WA
3. Higher-order - 제약조건이 세개 혹은 그 이상의 변수와 연관된 경우
    - e.g., cryptarithmetric column constraints
        - TWO + TWO = FOUR 에서 각 알파벳은 0~9까지 숫자중 하나

## 실생활의 CSPs
1. Assignment problems - 누가 어떤 강의를 가르칠건가?
2. Timetabling problems - 어떤 강의가 언제 어디서 일어나는가?
3. Transportation scheduling - 어떤 차가 언제 어느 도로에 쓰이는가
4. Factory scheduling - 어떤 일이 어디서 어떤 부분이 수행되는가

## Standard search formulation for CSP
- 상태는 할당된 변수에 의해 정의된다
- Initial state : {}
- Successor function : 할당되지 않은 변수에 제약조건에 위반하지 않는 하나의 변수를 할당 -> 할당할 수 있는 변수가 없으면 실패!
- Goal test : 변수들이 다 할당 되었고 제약조건이 위반되지 않는가?

## Overall Complexity for CSP
- 모든 솔루션은 n depth에 n 개의 변수에 나타난다
    - use depth-first search
- Path는 무관하므로 complete-state formulation 사용할 수 있다
- b = (n-l)d at depth l, 따라서 n!*(d^n) 개의 리프노드들

## Backtracking search
- 변수 할당 교류가능( WA = red then NT = green 이라는 조건은 NT = green then WA = red랑 같다) ; commutative
- 한 노드당 하나의 변수만을 고려해도 된다
- DFS for CSPs with single-variable assignments = backtracking 검색
- n ~= 25 정도의 n-queens 문제 풀수 있음

- Improving backtracking efficiency
    - 어떤 변수가 다음에 할당되는게 좋은가?
        - Most constrained variable : 가장 옵션이 없는 변수를 먼저 할당
        - Most constraining variable : 가장 다른 변수에 영향을 많이 주는 변수를 할당
        - Least constraining variable : 가장 다른 변수에 영향을 적게 주는 변수를 할당
    - 노드에서 어떤 순서로 시도해야 하는가?
    - 실패를 어떻게 일찍 탐지할 수 있을까
        - Forward checking : dead-end를 미리 탐지한다
        - 각 변수마다 legal values (가능한 모든 값들)을 계속 추적한다
            - legal values가 아예 없는 변수가 하나라도 존재한다면 실패
    - 문제의 조건을 이용해 이득을 볼 수 있지는 않을까
## Local Search for CSPs
- Hill-climbing
- CSPs 적용을 위해서는
    - 제약조건에 위반하는 states도 허용
    - operators reassign variable values
- Variable selection : 랜덤하게 제약조건 위반해도
- min-conflicts heuristic 으로 선택
    - i.e , hill-climb with h(n) = 위반하는 제약조건 수
    - 