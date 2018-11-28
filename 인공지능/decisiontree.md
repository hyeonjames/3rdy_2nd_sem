## Decision tree

- kNN : lazy learning
- DT : eager learning
    - Training Data를 가지고 Function 을 만듬! ( Target function을 생성 )
  
## 트리 표시
- internal node = 속성변수
- branch (가지) =  속성 값
- leaf node = 분류된 결과 값

## Decision Tree
- 널리 사용
- target(뷴류) 변수와 수많은 속성값 들과의 관계에 대한 통찰력을 얻음..?
    - 그냥 한마디로 말해서 수많은 속성값에 대해 분류를 해줌
- Binary decision trees - 그냥 2개의 선택지만 있는경우
- N-way or ternary decision trees - 3개 혹은 4개이상의 선택지가 있는 경우

## Decision Tree Splits
- **같은 성질을 가지는 것들끼리 묶어서 쪼갠다**
- 크고 다양한 집단 => 작고 단순한 집단
- 단일성이 높으면 잘쪼갠것
- 그룹마다 집합의 개수 차이가 적다 = 잘 쪼갠것

## Split Criteria
- Purity : 그룹 내의 단일성의 정도
- 흑이 9, 백이 1개인 집단과 흑이 5, 백이 5개인 집단을 비교했을때 전자가 purity가 높다.
- 쪼개진 집합들의 purity가 제일 크도록 해야함

## Information Gain
- Entropy = Sum(-Pjlog2(Pj)); Pj는 한 집합에서 하나를 꺼냈을 때 j가 나올 확률,
- -log2(Pj)는 j가 나왔을때의 정보의 양이라고 볼 수 있다.
- 그렇다면 Entropy는 한 집합에서 하나의 요소를 꺼냈을때 정보의 양의 기대값이다
- purity가 높을 수록 Entropy는 낮다
- 즉 Gain(S,A) = Entropy(S) - SUM(|Sv|/|S|*Entropy(Sv))
    - Sv 는 잘린 집합
    - S는 원래 집합
- Gain 값이 큰 attribute를 기준으로 나눈다
- depth가 너무 깊게 들어가면 불균형이 생기므로 다시 돌아가는방법을 채택할 수도;

## Gini Purity (Population Diversity)
- Gini = Sum(Pj^2) 으로 한다
- Purity가 크면 Gini값이 크다
- Gain(S,A) = Sum(|Sv|/|S|*Gini(Sv)) - Gini(S)
- Gini(S)가 제일 작아짐

## DT 장점
1. 이해 쉽다
2. 경제학에 적용 가능
3. 많은 종류의 분류 문제와, 예측 문제 해결 가능
4. 선입견이 없음 no prior assumption
5. numerical, cateogrical 속성 처리 가능

## DT의 단점
1. 타겟벨류(결과물) 은 무조건 categorical
2. 하나의 타겟벨류 (결과는 꼭 하나..)
3. 가끔 unstable => Not Optimal
4. 데이터가 숫자면 복잡해진다 => Binary search활용
