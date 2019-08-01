# 190710 StartCamp - day03



### Lotto 풀이

※ ``print() > 디버깅용이다.`` 사용자에게 값을 전달하는 게 아니고 개발자인 내가 값이 제대로 나오는지 확인하기 위한 용도



![1562894712211](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562894712211.png)

이렇게 하면 결과값을 저장하지 않고 날려보내는 것이다. 나만 확인하는 것이다. 웹앱에서 사용자에게 결과값을 전달하려면

![1562894813365](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562894813365.png)

이렇게 해야 result라는 박스안에 로또 당첨 정보가 저장된다.



◆ 방법1) 

```python
my = [9, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 6]
bonus = 8

match_count = 0
is_bonus = False

for i in my:

    if i == bonus:
        is_bonus = True
        
    for j in real:
        if i == j:
            # match_count = match_count + 1
            match_count += 1

if match_count == 6:
    result = '1등'
elif match_count == 5:
    if is_bonus:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝ㅠ'

print(result)
```



◆ 방법2)

```python
my = [9, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 6]
bonus = 8

match_count = 0

for i in my:
    for j in real:
        if i == j:
            # match_count = match_count + 1
            match_count += 1

if match_count == 6:
    result = '1등'
elif match_count == 5:
    if bonus in my:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝ㅠ'

print(result)
```



◆ 방법3)  set()을 통해 집합개념으로 접근,  교집합의 수를 세는 방법으로 가장 파이썬스러움

```python
my = [9, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 6]
bonus = 8

# [1, 2, 3] => list / {1, 2, 3} => set / (1, 2, 3) => tuple / {'a': 'A'} => dict
match = set(my).intersection(set(real))
match_count = len(match)

if match_count == 6:
    result = '1등'
elif match_count == 5:
    if bonus in my:
        result = '2등'
    else:
        result = '3등'
elif match_count == 4:
    result = '4등'
elif match_count == 3:
    result = '5등'
else:
    result = '꽝ㅠ'

print(result)
```



## chatbot quest 마무리

![1562903111582](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562903111582.png)

1. home화면(student)에 chatbot quest 폴더 새로 만들고 open code with 누름
2. 처음에 감시카메라를 붙여줘야함 

- touch .gitignore을 먼저 한 후에
- git init을 하기 >> 습관들이기

하나의 프로젝트를 새로 만들 때

![1562903199252](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562903199252.png)



내봇이름은 mykindbot

ss2s3Bot : username



- 문자열 자르기

string = '/주식 aapl'

string[0:4] > '/주식 '

string[4:-1] > 'aap'

string[4:] > 'aapl'



string.split(' ') > 문자열을 스페이스바 부분에서 자른다 > 리스트화되어 나온다





127.0.0.1= localhost(내가 나를 부르는 이름)

:5000 (5000번 문 즉, 5000번 port를 열겠다, 다른 컴퓨터의 요청을 들여올 수 있는 문=port )

http://127.0.0.1:5000 = http://localhost:5000

ngrok > 을 통해서 다른 컴퓨터가 들어올 수 있도록 문을 열어둔다



http >  port 80으로 약속

https > port 443





telegram

Postman

ngrok

![image](C:\Users\student\Downloads\image.png)



### Flask 대신 늘 켜져있는 서버 컴퓨터 분양받기

www.pythonanywhere.com 

https://dianeha.pythonanywhere.com/ << 분양받은 컴퓨터

setWebhook >

https://api.telegram.org/bot817133368:AAGC7RmdxokrVwcEOHuU6sMVeavcX_lTN0s/setWebhook?url=https://dianeha.pythonanywhere.com/e532abb1c567e6de90d8a3839ce1f00f3c84bdcf

이렇게 했음



-----------------------------------------------------------------------------------------------------------------------------------------

#### 파이썬 : Requests로 GET∙POST API 요청보내기 - 네이버 파파고 

- 네이버 개발자센터
- https://blog.naver.com/sarang2594/221315881828 여기서 이해해보자



### ※ venv

venv > virtual environment > 가상환경보다는 '독립 가상환경' > 프로젝트별로 필요한 것이 다르므로 독립적으로 관리를 하기 위해서 > 그래서 독립가상관경으로 진행

ex) pip install requests/flask 등을 startcamp라는 폴더(프로젝트)에는 다운받았는데 chatbot quest에는 없다.

- pip install xxx
- pip list > 이걸로 설치된 패키지 확인, 내가 설치하지 않은 패키지들이 있는 이유는 이 패키지가 다른 패키지 위에 만들어졌기 때문 >>  ''거인의 어깨 위에서''라는 말