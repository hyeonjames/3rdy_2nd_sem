# Classification - kNN Classifier

## KNN(k Nearest Neighbor) Classifier
- 가장 근접한 k개의 데이터를 찾아서 분류시키는 방법
- instance-based learning , lazy-learning 의 한 종류
    - 새로운 인스턴스가 들어왔을때 분류작업 수행
- 근접한 k개의 데이터의 다수의 값으로 결정
- Euclidean space => Euclidean distance measuring

## How to handle categorial attributes of instances for kNN classification?
- 그냥 numerical value로 변환한다
    - Outlook = {Rain = 0 , Overcast = 1, Sunny = 2}
    - Temperature = { Cool = 0 , Mild = 1, Hot = 2}
    - Humidity = {Normal = 0, High = 1}
    - Wind = {Weak = 0, Strong = 1}
    - (Sunny, Hot,High,Weak) = (2,2,1,0)

## Scaling Attribute Value
- 각각의 차원의 범위가 다르기 때문에 (예로 outlook은 0~2, Humidity는 0~1) , 스케일링을 해줘야 한다
- scaling value X' = (X-평균)/표준편차
- majority voting
## Distance-Weighted NN 알고리즘
- majority voting 할때 가중치를 부여시킴
- 이때의 가중치 => 1/d^2 혹은 그냥 1/d
- 가까이 있는 요소가 끼치는 영향을 크게
- K = 모든 인스턴스의 수이면 모든 인스턴스가 값에 영향을 미친다
    - Shepard's method라고 함
- Voronoi Diagram
- 