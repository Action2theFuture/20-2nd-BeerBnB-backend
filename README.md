## IKEA Clone Project

- 세계 최대의 숙박 공유 서비스 사이트 [에어비앤비](https://www.airbnb.co.kr/) 클론 프로젝트
- [백엔드 github 링크](https://github.com/wecode-bootcamp-korea/20-2nd-BeerBnB-backend)

### 개발 인원 및 기간

- 개발기간 : 2021/5/24 ~ 2030/6/3
- 개발 인원 : 프론트엔드 3명, 백엔드 2명
- 프론트엔드 : [김민정](https://github.com/Alice-in-korea), [김휘성](https://github.com/Heessong), [박준모](https://github.com/junmopark01)
- 백엔드 : [문성호](https://github.com/Room9), [정운산](https://github.com/Action2theFuture)


### 프로젝트 선정이유

- 사용자의 선호도에 따라 구분되는 필터링
- 호스트와 게스트에 따라 달라지는 유동적인 선택
- Request를 method를 다양하게 사용할 수 있는 조건

<br>

## 적용 기술 및 구현 기능

### 적용 기술

> - Front-End : React.js, sass, slick, react-modal
> - Back-End : Python, Django web framework, My SQL, Bcrypt, hmac, hashlib, pyjwt, SMPT, S3, Naver SMS API, Kakao Login API, Googlemap API
> - Common : POSTMAN, Insomnia, RESTful API, Docker, EC2, RDS



### 구현 기능

#### 로그인페이지

- 회원가입 후 이메일인증을 통해 계정활성화
- 네이버 SMS API를 통해 핸드폰 인증 
- 주어진 시간안에 인증이 되지 않으면 재인증
- 카카오 소셜로그인
- 이메일 회원가입


#### 메인페이지

- 검색바, 카테고리 

#### 리스트페이지

- 검색바와 토글을 통한 필터링 
- 주소/가격/인원/환불여부/슈퍼호스트여부/날짜/주종

#### 상세페이지

- 방 상세정보, 편의시설, 예약

#### 에약, 위시리스트

- 예약된 체크인 체크아웃 날짜를 통해 사용할 수 없는 방으로 업데이트
- 사용 불가한 일정은 필터링
- 유저가 원하는 위시리스트 등록

#### 호스트페이지

- 사용자가 게스트에서 호스트로 변경
- 호스트일 경우 방을 등록가능
- 해당 방의 상세정보과 사진 등록

<br>

## Reference

- 이 프로젝트는 [에어비앤비](https://www.airbnb.co.kr/) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
