# README :rose:



### :lion: 프로젝트 개요


- 프로젝트 소개

> 주제 ) 웹 프레임워크를 활용한 평점 기반 커뮤니티 서비스
>
> 내용 ) 영화 주제로 구성된 회원제 커뮤니티 서비스 구현
>
> 팀 이름 ) 평균 나이 25
>
> 일시 ) 2021.5.18~ 2021.5.28



- 프로젝트 개요

> Django REST API 서버 및 프론트엔드 프레임워크(Vue.js) 사용
>
> Popular, Now Playing -> Vue에서 Axios로 영화 데이터 각 60개 수집 
>
> ​	(tmdb 기준 1~3page 분량)
>
> Now Playing 게시판 DB -> Django 에서 영화 데이터 180개 수집



<hr> 

### :lion: 팀원 정보 및 업무 분담

- 팀원 소개

> **김윤서** ( 조장 )
> **김태랑** ( 조원 )



- 업무 분담

> - 대부분 기능 별 업무를 분담한 후 Django - Vue 로 분배
>
> - 주요 담당 기능 
>
>   **김윤서** >  추천 알고리즘 
>   (4점 이상 평점 영화에 대한 영화 추천 및 날씨 필드 입력하여 영화 별 문구 등장)
>
>   **김태랑** > 데이터 수집 후 DB 저장 및 리뷰와 영화 data 연동 작업 
>   
>   (vue와 django를 통한 영화 data 수집 / 커뮤니티 게시판 과의 연동)



<hr> 

### :lion:목표 서비스 구현 및 실제 구현 정도

- 일자별 계획

![image-20210710105330034](README.assets/image-20210710105330034.png)



- 초기 아이디어

> - ##### 목표: 사용자에게 Customize 된 영화 추천 서비스 제공 
>
>     
>
>     - 가입 시 나이 정보를 입력하여 연령대 별 영화 추천 
>                    
>         → 자신이 리뷰를 작성한 영화 중 별점이 4점 이상인 영화들과 유사한 영화를 랜덤으로 추천하는 기능으로 변경 
>
>         
>
>     -  게시할 영화 정보 (대세 컨텐츠) 
>                    
>         →  Popular 기능으로 구현 
>                    
>         →  그 외 최신작으로 tmdb의 latest url을 사용하려고 했으나, 하나의 영화 정보만 담겨와서 실패 (추후 now playing으로 구현)
>
>         
>
>     - 해당 영화의 리뷰가 작성된 네이버 블로그로 가게 하기 
>                    
>         → 디테일 페이지에서 유튜브 예고편과 한줄평 리뷰가 바로 나오도록 개선
>
>         
>
>     - 리뷰 작성 관련 
>                    
>         → 리뷰 게시글 > 영화 디테일로 이동 가능 및 댓글 형식으로 리뷰 제목만 보이게 
>                    
>         → 누르면 리뷰 글로 이동부분은 리뷰 detail이 필요없다고 판단하여 계획 수정 
>                    
>         → 그 외 디테일에서 댓글의 한줄평과 별점이 보이도록 변경
>
>         
>
>     - Event 장르 별 랜덤 영화 픽 
>                    
>         → 사용자에게 custom 된 영화 추천을 위해 평점 4점 이상을 준 영화들 기준으로 영화 추천 
>                    
>         → 그 외 영화 분위기를 날씨 정보로 받아 가장 많이 받은 날씨를 기준으로 영화 detail 페이지에 각각 다른 문구 등장 



- 참고 사이트 디자인 

> 네이버 영화/ Rotten Tomato
>
> - concept: 날씨 (평점에 따라 날씨 아이콘)
>
>   → 아이콘 깨짐으로 인해 날씨 상황 (맑음, 흐림, 천둥번개) 에 따른 영화 분위기를 알려줌



- 초기 프로그램 구조  

> - Django 100% 로 계획
>
>   → data 받아오는 과정에서 vue 사용 으로 전환 (5/18)
>
>   → DB저장에 문제가 있음을 깨닫고 django 로 API 요청을 보내 DB에 추가하여 vue 로 쏴주는 형식으로 변경



<hr>

### :lion:데이터베이스 모델링(ERD)

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/47ea1a56-527e-432a-a15a-c9722d6fba56/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210710T015423Z&X-Amz-Expires=86400&X-Amz-Signature=91a25f4e057975dcf305e030af60f7e4420fa6ff615f9e7420b86a8e15b6babd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<hr>

### :lion:필수 기능에 대한 설명

1. #### 정보 제공

- TMDB 사이트를 이용하여 인기작, 현재 상영작 영화 정보 제공 (별점. 제목)
- 영화 클릭 시 Detail 페이지로 이동 
- 구성 : 포스터, 유튜브 예고편, 제목/장르/연도/러닝타임/별점/ 줄거리, 리뷰 별 댓글 및 문구 등장 



2. #### 추천 기능

   ##### < 영화 무드를 날씨로 알려주자! >

- 한줄평을 작성할 때 받는 필드는 영화제목 / 오늘 / 한줄평 / 별점 

  - `오늘` 이란 사용자가 영화에 대해 느끼는 감정, 분위기를 맑음 / 흐림 / 천둥번개 중 선택

- 특정영화 Detail Page에서 가장 많은 사람이 선택한 날씨별로 문구가 등장 
  
  - 특정 영화에 기록된 리뷰의 [맑음, 흐림, 천둥번개]를 각각 count 해서 max count를 가진 날씨 별 상이한 문구가 등장하게 설정 
  
  - ( ex 맑음이 제일 많을 시 : 화창한 날 보기 좋은 영화 
  
     	  흐림이 제일 많을 시: 흐리고 울적한 날에 딱 맞는 영화
  
    천둥번개가 제일 많을 시 :  천둥 번개처럼 긴장감있는 영화 )
  
  
  
  ##### < 리뷰 평점 별 영화를 추천해주자! >
  
- 마이 페이지에서 4점 이상 평점을 매긴 영화들의 similar 영화들을 한 리스트에 담은 후 그 중 5개 랜덤픽으로 하단에 게시 

  + 버튼을 누를 때 마다 다른 영화가 추천되며 영화를 누르면 해당 영화 detail로 이동



3. #### 커뮤니티 기능 

- 한줄평: 현재 상영작 리뷰 확인 및 새 글 작성 
  영화 별 별점순으로 나열하여 리뷰 평이 높은 영화부터 리뷰 확인 가능 

- 마이페이지: 로그인한 이용자가 작성한 게시글 게시 
  영화 별 별점순으로 나열하여 사용자가 시청한 영화 중 높은 별점 순 확인 가능
  하단에는 위의 추천 알고리즘을 이용한 영화 랜덤 추천! 
  - 자신이 쓴 글만 삭제 가능 



4. #### 세부 기능 

- 로그인 / 회원 가입 
  로그인 오류 시 회원 가입 페이지로 이동 

+ Django admin site를 통해 관리자 유저 crud 가능 



<hr> 

### :lion: 느낀점

> 김윤서
>
> - **기간에 대한 압박감**으로 인해 프로젝트 초기에 기획 및 프로젝트 구성에 많은 시간을 사용하지 못한게 제일 아쉬웠다... 
>
>   - Django로 데이터를 받아와서 Vue로 넘겨줘야 DB에 저장된다는 점 등 
>
> - 개발은 정말 **오류 넘어 오류** 라는 말이 어울린다는 생각이 들 정도로 정말 많은 오류를 고치고 그것을 고치면 또 다른 오류가 반복되는 .... 딜레마에서 스트레스를 많이 받았다. 
>
>   - 앞서 언급한 문제로 인해 모든 데이터들을 컴포넌트간 전송 시키는 과정이 어려워졌다. 
>
> - 하지만 특정 컨셉을 **기획**하고 그것을 **직접 알고리즘으로 구현**해내는 과정에서 django, vue를 활용해볼 수 있었고 그 동안 알고리즘 문제를 풀이한 경험에서 많은 도움을 느꼈다. 
>
>   - ex) Django views.py 함수를 이용한 정제된 데이터 추출 / 
>
>     Vue javascript 문법을 이용한 날씨 별 문구 등장 및 영화 추천 
>
> - 또한, 개발과 관련된 오류를 잡고 디자인 구성짜는거에 굉장한 시간을 투자하여 정말 힘들었지만.. 교수님의 피드백으로 인해 더 완성도 높은 사이트를 제작할 수 있었다. 
>
>   - d-flex, align 등 이용을 다시 공부해보게 되었다. 
>
> - 너무 애정과 시간을 쏟아본 첫 프로젝트라서 굉장히 구구절절 느낀점이 되었지만....
>
>   ```python
>   이번 프로젝트에서 배운 점을 향후 진행할 2학기 프로젝트에서 어떻게 적용해야 할지 많은 고민을 하게 된 경험인 것 같다! 
>   ```



> 김태랑 
>
> - 마지막 관통 프로젝트답게 할 게 많았다.  
> - API 요청을 하는 것부터가 문제였다. django 사용을 안 하고 vue로만 받아와서 페이지를 구성하려던 계획이 명세서를 받고 잘못됐음을 깨달았다.  
> - 그때라도 바꿨어야 하는데 이틀간 한 것이 아까워 vue에서 받은 것을 포기하지 못했고 django에서 새로 받아와 다른 페이지를 구성했다.  
> - 여기서부터 조금씩 문제가 생겼다. 기존에 vue로 작성한 페이지와 model을 연결할 방법이 없었다.  
> - 유저와 연결할 수도 없었으며 django에서 불러온 영화들 그리고 한줄평도 모든 게 다 안됐다. 이때라도 포기하고 엎었어야 하는데 오기가 생겨서 그대로 진행하기로 했다.  
> - 하나하나 잘못된 부분을 고쳐가며 억지로 데이터들을 받고 사용하는 과정에서 많이 불편하고 힘들었지만, 문제들을 해결하며 많이 배웠다. 또 해결했을 때의 뿌듯함이 지겨운 프로젝트를 계속 진행하게 해주는 원동력이 되어줬다.  
> - 어찌어찌 해결들이 됐지만, 코드가 너무 지저분했다. 다음부터는 잘못된 것을 깨달았을 때 고쳐야겠다.  
> - 이번 프로젝트를 진행하며 시작할 때 어떻게 홈페이지를 구성할 것인가에 대한 논의를 잘 마무리하지 못하고 진행했다. 그러다 보니 꾸미고 기능을 추가하고 배치하는 데 문제가 많았다.  
> - 앞으로 프로젝트를 새로 진행한다면 구상에 더 많은 시간을 써야겠다. 



### :lion: 완성작!

Git : https://github.com/ssw02238/FinalPjt 

Notion : https://www.notion.so/SSAFY-b944695aeeb24cb5a9825674d6519e92



< Popular / Now playing >

![image-20210710110244202](README.assets/image-20210710110244202.png)

![image-20210710110220279](README.assets/image-20210710110220279.png)



< Movie Detail >

- 줄거리와 예고편이 모두 존재할 때

![image-20210710111803143](README.assets/image-20210710111803143.png)

- 줄거리와 예고편이 모두 존재하지 않을 때

![image-20210710111858483](README.assets/image-20210710111858483.png)

- 영화 리뷰가 존재할 경우

![image-20210710112006473](README.assets/image-20210710112006473.png)



- 한줄평 커뮤니티

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/faf3be80-bd92-4591-af78-5382d3187d8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210710T022043Z&X-Amz-Expires=86400&X-Amz-Signature=dd2b05a1d98839ad213260c45725d6cbb1da78a7b0b8e7626536d8f4b298b48f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- 새글 작성

![image-20210710110357934](README.assets/image-20210710110357934.png)



- My  page (하단 추천 영화는 사이트 비율에 따른 grid 구성)

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8df46386-c6e3-4b66-bc2e-d91d64daf716/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210710T022108Z&X-Amz-Expires=86400&X-Amz-Signature=fe1b64de5cb1fac5aea2e12851be6ddce4f34248d834985b64f1af6355d08c66&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<Login / Signup>

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F92db7b5d-b704-4f44-8722-e363faa233ab%2FUntitled.png?table=block&id=ae140fbc-91ce-4572-9601-796ef0830be2&spaceId=2756e829-79dc-4b12-a2b0-aa9dae95f129&width=3200&userId=a644f926-4a5c-4321-b640-09d595179e74&cache=v2)

![img](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/93d8541e-45d4-4776-b608-cfd3bb4e363e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210710T020738Z&X-Amz-Expires=86400&X-Amz-Signature=355f0796fe98403c4b649fad8b73b42d387e8ba60661dae78944a2cb34db98d6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

