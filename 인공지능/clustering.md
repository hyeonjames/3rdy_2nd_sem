# Clustering
- 학습 데이터가 없는 상태에서 비슷한 것끼리 묶는 것이다
- unsupervised learning
    - 학습데이터 X
- IR( Information retrieval )시스템에서 유용
- e.g. document 카테고리 분류
- "car"를 검색엔진에서 검색했을 때 "automobile"이라는 단어가 있는 문서도 같이 나옴 ) 같은 클러스터에 분류 됬기에
- 기본 클러스터 가설 : 같은 클러스터에 있는 요소들은 비슷하게 행동
    - 기본적인 처리 : 모든 문서를 클러스터링
    - IR 시스템에서 검색 수행시 query에 맞는 document D를 찾으면, D와 같은 클러스터에 있는 것들도 같이 검색됨
## 