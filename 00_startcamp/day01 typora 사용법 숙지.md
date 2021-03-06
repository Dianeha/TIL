# 190708 StartCamp - day1

## 컴퓨터 프로그래밍 언어

### 컴퓨터

컴퓨터란 계산(compute)기다.

### 프로그래밍

명령어의 집합. 컴퓨터에게 일을 시키는 것

### 언어



## Python 변수

(사전강의) 정수형(int) 변수, 문자열(str) 변수, 리스트(list) 변수

- 변수의 자료형 확인 > type()으로 한다
- 변수명 > 문자 숫자 _ 사용, 숫자로 시작 불가, 대소문자 구분/ 파이썬 예약어 사용불가

## Python 기초 문법 3형식

1. 저장(숫자, 문자"", 참/거짓 형식의 정보를 저장 가능)

   * 저장하는법 / 불러오는법 / 출력값

   * 변수(박스1개) dust=40/dust/40

   * 리스트(박스 여러개)★ dusts=[40,50,60]/dust[0]/40

   * 딕셔너리(견출지를 붙인 박스) - key와 value로 이루어짐

     dusts={"영등포구":40, "강남구":50}/dusts["영등포구"]/40

2. 조건(if) - 참/거짓 형식의 정보를 사용함

3. 반복(while/for) 

   1. while True: >> 조건이 True일 때까지 반복 / 종료조건이 필요
   2. for i(무엇을 써도 상관없다)  in 리스트 이름 : >> 리스트 전체를 출력 / 종료조건 불필요



## Python 함수

파이썬 함수에는 내장 함수와 외장 함수가 있다.

★괄호()가 붙으면 함수이다★로 일단 기억하기



- 내장함수 - 책상 위에 있어서 바로 쓸 수 있는 것들
  * `print()` : 출력하는 함수 
  * `list()` : 리스트를 생성하는 함수
  * `range()` : 범위를 생성하는 함수
  
-  외장함수 - 일단 함수다발이 포함된 코드를 불러와야 쓸 수 있음(서랍안에서 꺼내는 행위-import)
  
  - `random` : 랜덤 관련 함수들의 묶음
  
  - `random.choice()` random이라는 외장함수 다발에서 choice라는 함수 하나 꺼낸 것
  
    : 리스트에서 1개 무작위 선택
  
  - `random.sample(p, n)`   random이라는 외장함수 다발에서 sample라는 함수 하나 꺼낸 것
  
    : 모집단에서 n개의 요소를 무작위 비복원추출



### 로또 번호 추첨하기

```python
import random

numbers = list(range(1,46))
lucky_numbers = random.sample(numbers, 6)
print(lucky_numbers)
```





*하고 스페이스바 > 번호가 없는 리스트 생성

1. 하고 스페이스바 하면 자동으로 번호가 있는 1.2.3.생성

2. `` 1번 옆에있는 백틱으로 묶어주면 코드 표시 가능 >> 구별하기 쉽다.

3. ``` 3개쓰면 코드 블록 만들수 있음.
   ​``` 3개를 쓰면 코드 블록을 만들 수 있음
   ```



#### 오늘 설치 프로그램 목록

git bash 2.22.0-64-bit > https://git-scm.com/ > 우측에 모니터 화면에 Lastest source Release 2.22.0 Download 2.22.0 for windows
python 3.7.3 > all release > 3.7.3 > [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe) 다운로드

- vscode > 설치할때 체크박스 5개 나오면 그 중에 2,3,5 체크 > 

	1. 왼쪽에서 확장 누르고 'Korean 랭귀지 팩'이랑 Python 마이크로소프트에서 지원하는 별표붙은 것 설치
 	2. ctrl+백틱 > F1 누르고 > ter치면 > 기본쉘선택 > 깃배쉬 선택

3. F1 누르고 Python selector interpretor 누르면 3.7.3 선택 > 하단 좌측에  ![1563162468750](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1563162468750.png)

4. 휴지통으로 끄고 ctrl+백틱
5. 그 화면에서 python -V 해서 엔터쳐서 버전 정보 확인

typora



#### 기타

안드로이드 앱) 자바 > 코틀린
ios 앱) 자바 > 스위프트
넘어가는 추세



#### 인터페이스는 '접점'이고 '약속'이다

< 사용자 인터페이스(접점) >
ex) 사용자와 아마존(배송 서비스)을 이어주는 접점: 컴퓨터, 스마트폰, 챗봇(최근에 추가된 신기술)



< API(Application Programming Interface) >
다른 시스템 간의 커뮤니케이션 방식
ex) 배달의 민족에서 페이스북을 통해 로그인 가능하게 하고싶을 때 > 배달의 민족이 facebook에 정보제공요청

요청과 응답 과정, 페이스북이 구체적인 요청방식을 제공, 그것을 지켜서 배달의민족이 요청하면 페이스북이 정보를 제공해줌

즉, 웹에서의 커뮤니케이션 방식: 요청과 응답으로 이루어짐