# README



## 05/18 

- 기획 및 초기 설정
  - git 
  - notion 
  - tool 결정 
  - 참고 사이트 
- client / server 로 분리 
  - vue / django 
  - vue: router 기능으로 각 카테고리 이동 
  - django: 세부 template 설정 
- server 수정 
  - base.html 및 url 경로 설정



## 05/19

- vue를 통해 api data 가져오기 



## 05/20

- Popular , Now_playing , Detail 생성 
  - page 누적 영화 데이터 가져오기 
  - detail youtube 가져오기 
  - card 형식 정렬 
  - router 기능으로 눌렀을 때 detail 페이지로 



## 5/21

- Article - Comment 관계 설정 및 community 게시판 작성 
  - MovieDetail에 Comment 작성하는 것으로 변경 
  - Movie DB 문제로 인해 Community에 글- 댓글 관계로 재변경 
- Movie DB 저장 성공 

```python
# def seeding - 바로 model 필드에 넣기
# model 안에 movie class - 위에 필드랑 일치하게
# serializer - x
# db에 들어가는지 만 확인
```



## 5/22

- modal 과 carousel이 적용 안됨 (bootstrap, bootstrap vue)
  - 단 card, btn 등 다른 부트스트랩은 잘 적용됨 
- community 게시판 내 ArticleDetail 생성 
  - ArticleList에서 id를 params 로 받아 특정 article data 받기 



## 5/24

- 세부 디자인 수정 
  - notion 참고 
- 추천 알고리즘 재기획 



## 5/25

- 추천 알고리즘 구현 



## 5/26

- 세부 디자인 조정
- create Article 수정 > 날씨 필드 받기 
- 발표 준비 