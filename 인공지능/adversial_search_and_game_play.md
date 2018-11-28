# Adversial Search and Game-playing

## Search vs Games
- search (no adversary 적이 없는 경우)
    - 솔루션 : 골을 찾거나 골을 향한 경로를 찾는 행위
    - 일부의 휴리스틱 기술로 최적의 솔루션을 찾을 수 있다
    - Evaulation function = 시작지점부터 골 지점까지 cost 값
    - 예 : path finding, 8-puzzle
- Games - 적이 있는 경우
    - 나 : 나의 이익을 극대화 하는 것이 목표.
    - 상대방 : 나의 이익을 극소화 하는 것이 목표
    - 솔루션 : 상대방에게 주어진 가능한의 모든 응답에대한 반응을 구체화하는 전략
    - 대부분의 경우 시간 문제 때문에 근사값에 가까운 답만 얻음
    - Utility function - 게임이 얼마나 나에게 유리하게 돌아가고 있는지
    - 예 : chess, checkers, Otehllo, Go

## Typical assumptions

- 두 게임 플레이어는 서로에게 적대적
- Utility values = 얼마나 나에게 유리한가
- Utility value는 서로 반대된다
    - 한 플레이어의 utility value가 상승 -> 다른 플레이어의 utility value 감소
- 게임이론용어:
    - Deterministic : 어떠한 행위의 결과는 예측가능하다
    - turn-taking : 서로 적대시 하는 두명의 플레이어가 있다
    - zero-sum games : 한 플레이어가 체스를 + 1로 이기면, 상대편 플레이어는 -1로 지는 것이다. 즉 합이 0이되야함
    - perfect information : 모든 게임의 상태를 관찰 가능


## Game Setup

- 두명의 플레이어 존재 (MAX and MIN)
- MAX가 먼저 시작하고 게임이 끝날때 까지 턴이 반복됨
- Games as search : 4개의 구성요소
    - Initial state : e.g. board configuration of chess 체스의 초기 구성
    - Successor function : 현재 게임상태에서 가능한 모든 행위
    - Terminal test : 게임이 끝났는가?
    - Utility function : 게임이 얼마나 유리하게 돌아가고 있는지 숫자로 나타낸 함수
- MAX는 이때 수많은 서치트리로 다음 행위를 결정하게 됨..
  

## 트리의 사이즈
- b = 가지수 branching factor
- d = 플레이어의 가능한 모든 행위 수
- Search tree : O(b^d)
- In Chess
    - b ~ 35
    - d ~ 100
        - search tree ~ 10^154 너무 큼
        - 이걸 다 검색하는 건 시간이 너무 듬
- 게임 플레이는 **정해진 시간** 내에 **최적화된 솔루션**을 찾아야함


## Minimax 전략
- 항상 optimal하게 움직이는 MIN에 대하여 MAX의 optimal한 전략을 찾음
- 가정 : 두 플레이어는 항상 optimal하게 움직인다고 가정한다 -> infallible player
- 나와 상대방의 가능한 모든 경우의 수를 탐색함
    - MAX 턴의 경우 : 모든 가능한 경로에서 Utility 값이 가장 큰 값을 올린다
    - MIN 턴의 경우 : 모든 가능한 경로에서 Utility 값이 가장 작은 값을 올린다 (infallible player이므로)
    - Utility 값은 MAX의 utility값을 의미한다.
- 이 전략은 최악의 시나리오에서의 Utility value값을 최대화한다.
- 이 전략은 MIN이 꼭 optimal하게 움직이지 않더라도 작동한다
- Time Complexity : O(b^d)
- Space Complexity : O(bd)
## 멀티플레이어의 경우
- utility 가 벡터가 됨. 
- A,B,C플레이어의 경우 (UtilityForA,UtilityForB,UtilityForC)
- 각 턴마다 해당 플레이어의 Utility값이 MAX가 되는 행위 선택
- 특별한 경우 : 동맹을 맺는 경우
    - 예로 A,B,C에서 B,C가 동맹을 맺는 경우
    - 이 경우는 B,C턴에서 UtilityForB나 UtilityForC가 MAX가 되는 행위로 선택하는 방법이 있음


## 알파-베타 Pruning
- Minimax 전략에서 쓸모 없는 탐색을 없애기 위해 **가지치기**를 한다
- 예로 MIN턴에서 첫번째 자식노드에 3값이 나오고, 두번째 자식노드의 자식노드 값중 2값이 나왔다 가정할때 두번째 자식노드의 나머지 자식노드들은 탐색할 필요가 없다. (무얼하던 2보다 작은 값을 선택할 것이고, 이는 3값 보다 작기때문에 선택될 수가 없음)
- 당연히 Worst-Case 같은 경우 그냥 Minimax 알고리즘과 동일하게 O(b^d)
- Best-Case : O(b^(d/2)) = O(sqrt(b)^d)
- 실 상황에서는 worst보다는 best-case에 가깝다
- 체스같은 경우 b ~ 35 정도인데 best-case로 가면 b ~ 6정도가 된다
- 알파 : 현재까지 나온 MAX의 DFS path에서 가장 큰 값
- 베타 : 현재까지 나온 MIN의 DFS path에서 가장 작은 값


## Utility (Evaulation) Functions
- A Utility function:
    - 현재 상태가 얼마나 나한테 유리한가
    - Othello = 백의 개수 - 흑의 개수
    - Chess = 백의 가중치 합 - 흑의 가중치 합
        - 체스 말의 종류에 따라 점수(가중치)를 매김
    - 전형적으로 \[-infinity, infinity\] 혹은 \[-1,1\] 
    - 