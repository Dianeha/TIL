터미널에서 ctrl + c : 취소 / ctrl + d: exit

# 190710 StartCamp - day03

※ (인터넷으로 연결된) 전세계에 존재하는 ★**data를 가져오는 3가지 방법★** 

* 스크래핑(웹크롤링)
* API 
* 패키지 혹은 모듈 사용



### 1. Quiz(Python practice)

``` python
# 문제) 사용자로부터 words를 입력받아 첫 글자와 마지막 글자를 출력하라.

words = input('입력하세요: ') # 사용자의 입력을 받으면 그것이 숫자든 문자든 다 str(문자열)로 받는다
print(type(words)) # 124d, 하다연, sdfff든 다 string
print(words[0], words[-1])
# words[0]처럼 쓰는 것은 리스트에서 쓰는 방법 아닌가요?
# >> string도 리스트처럼 메모리에 저장됨 > 리스트뿐 아니라 문자열도 인덱스 접근이 가능하다.


# 문자열은 리스트로 형변환 가능하다
my_list = list('123456')
print(type(my_list)) # 리스트로 형변환 확인
print(my_list[0], my_list[-1])

```

* 기억할 점
  * 입력메세지는 input(여기에다 쓴다) > words = input('입력하세요: ')
  * 사용자의 입력 > 다 자료형 string으로 받음
  * 문자열도 인덱스 접근이 가능
  * 문자열: 리스트로 형변환 가능



```python
# 첫 글자와 마지막 글자를 출력
import random

length = random.choice(range(1, 100))
numbers = list(range(length))

print(numbers[length-1])
print(numbers[-1])  # list[-1]은 리스트의 뒤에서 첫번째 요소를 지칭
print(numbers[-2])
# list화 하려면 numbers = list(range(length)) 이런 식으로 해야한다. 
```



```python
# 문제) 자연수 n을 입력받고, 1부터 n까지 출력

n = input('원하시는 자연수를 입력해주세요: ')
n = int(n) #문자열을 숫자형으로 형변환

for i in range(n):
    print(i + 1, end=' ')

```

* 기억할 점

  * range() 함수의 결과는 **반복가능(iterable)**하기 때문에 **for문을 사용해 (리스트처럼) 출력가능**

  * **range(start, stop)**

    **range(1, 11)**은 **1, 2, 3, 4, 5, 6, 7, 8, 9, 10** 숫자 생성

    start - 시작숫자, stop-1까지 생성됨

  * **range(stop)**

    **range(10)**은 **0, 1, 2, 3, 4, 5, 6, 7, 8, 9** 숫자 생성

    

```python
# 문제) fizz buzz => 3의 배수에서 fizz, 5의 배수에서 buzz, 15의 배수 fizzbuzz 출력
n = int(input('원하시는 숫자를 입력하세요: '))

for num in range(1, n + 1):
    if num % 15 == 0:
        print('fizzbuzz', end=' ')
    elif num % 3 == 0:
        print('fizz', end=' ')
    elif num % 5 == 0:
        print('buzz', end=' ')
    else:
        print(num, end=' ')

```



### Lotto API

```python
# ================= 로또 번호 api로 가져오기 ================= 


import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
response = requests.get(url).text
# print(type(response))
# print(response)

data = json.loads(response)
# print(type(data), data) 
# print(data['bnusNo'])

# 딕셔너리 data 중에 'drwtNo'가 들어간 부분만 추출해서 real_n 리스트에 추가
real_n = []
for key, value in data.items():
    if 'drwtNo' in key:
        real_n.append(value)

print(real_n)

# real_n = []
# for i in range(6):
#     real_n.append(data[f'drwtNo{i+1}'])

# {
#     "totSellamnt": 81961886000,      # 총판매금액
#     "returnValue": "success",        # 성공적으로 응답
#     "drwNoDate": "2019-07-06",       # 추첨일
#     "firstWinamnt": 2240409000,      # 1등금액
#     "drwtNo6": 39,                   # no6
#     "drwtNo4": 34,                   # no4
#     "firstPrzwnerCo": 9,             # 1등 당첨자수
#     "drwtNo5": 37,                   # no5
#     "bnusNo": 12,                    # bonus no
#     "firstAccumamnt": 20163681000,   # 이번회차 누적금
#     "drwNo": 866,                    # 회차
#     "drwtNo2": 15,                   # no2
#     "drwtNo3": 29,                   # no3
#     "drwtNo1": 9                     # no1
# }
```



※ **JSON**

* JSON은 데이타를 교환하는 한 포맷
* 특히 API를 이용해 외부에 데이터를 전달할때 보통 json 형태가 사용되는데, python 에서 json 형태와 가장 유사한 자료형이 바로 딕셔너리
* 위 예시의 경우 api를 이용한 json 포맷의 데이터(lotto 번호 관련)를 받아왔으므로,  json.loads 를 사용해 json 을 dictionary 형태로 변환



### 딕셔너리(라벨지가 붙어있는 박스들의 모임)

* 딕셔너리는 기본적으로 for문을 돌리면 key 값만 출력됨

  ```python
  for i in data:
          print(i)
  ```

  bnusNo
  firstAccumamnt
  drwNo
  drwtNo2
  drwtNo3
  drwtNo1...

* key, value 같이 꺼내려면 딕셔너리.items() 사용

```python
for key, value in data.items():
    print(key, value)
```

bnusNo 12
firstAccumamnt 20163681000
drwNo 866
drwtNo2 15
drwtNo3 29
drwtNo1 9 ...







## Client & Server

```python
# 1번) flask 필통에서 Flask와 render_template 라는 두 가지 연필과 펜을 꺼내 사용하겠다는 의미
from flask import Flask, render_template

# 2번) flask는 너무 큰 필통이기 때문에 import flask로 필통을 책상위에 꺼내는 것은 바보같은 짓
# flask의 경우 필요한 것만 불러와 쓰는 것이 현명


# -----------------------------------------------------
# 비슷한 예로
import random
random.choice([1, 2, 3, 4, 5])

from random import choice
choice([1, 2, 3, 4, 5])
# 의 차이
```

### app.py

- route는 '노선', '길'

- ★사용자 입력 받는 법★도 3가지 

  - input() 사용 (클릭 아니면 입력창)
  - variable routing
  - url 직접변경

  ```python
  @app.route('/')  
  # /로 route로 길을 뚫어주는데 그러면 templates안에서 index.html 문서를 찾아 서빙하겠다는 뜻
  def index():
      return render_template('index.html')
  
  @app.route('/pick_lotto')
  def pick_lotto():
      numbers = range(1, 45)
      lucky_numbers = random.sample(numbers, 6)
      return str(lucky_numbers)
  # 주소가 /pick_lotto 로 끝나면 아래 명령들을 실행한다
  # 이런 고정적인 주소를 '하드코딩'이라고 한다
  
  # 위와 다르게 <name> 변수처럼 처리해서 융통성을 줌
  @app.route('/hello/<name>')  # variable routing 
  def hello(name):
      return f'Hi, {name}'
  ```

  * 기억할 것 - 변화하는 값을 쓰는 형식

  return f'Hi, {name}'

  혹은

  format() 함수 사용

  ex) print'제 나이는 {age}살이고, 제 몸무게는 {weight}kg입니다.'.format(age=19, weigh=64.2)







### Python의 프레임워크

프레임워크란?

![1562742764907](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562742764907.png)

Flask와 Django가 주요 프레임워크