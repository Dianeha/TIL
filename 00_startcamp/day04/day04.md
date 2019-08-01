# 190711 startcamp day04





### Github을 이용한 나의 포트폴리오 페이지 작성

1. https://startbootstrap.com/ 에서 포트폴리오 사이트 디자인을 다운받아서 압축을 푼다.
2. 포트폴리오 파일에서 마우스 오른쪽 버튼 클릭 > open with Code를 눌러서 아래와 같은 화면
3. ![1562809026635](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562809026635.png)

4. ![1562809288944](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562809288944.png)

   index.html 파일을 눌러서 뜬 사이트 화면에서 F12 개발자 페이지 들어가기

   => 여기저기 이미지나 text 를 바꿔보면서 어떻게 화면에서 나오는지 확인 후 

   => 마음에 들면 실제 코드로 들어가 검색해서 바꾸면 됨



※ README  작성법도 알아야 한다. (자신의 프로젝트를 설명하는 마크다운 문서)

5. Github이 포트폴리오 사이트 하나 지원해줌

6. Dianeha.github.io 로 생성(유저네임.github.io) >  바꾸고 싶으면 my_portfolio 안에 새로운 양식 또 받아서 생성하고 add . 하고 push하거나 깃헙에서 setting 가장 아래로 가서 다 삭제하고 다시 Dianeha.github.io 생성하면 된다. 

![1562807798866](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562807798866.png)

7. Dianeha.github.io을 url 창에 검색해보면 생성된 것을 볼 수 있다.



https://dianeha.github.io/index.html

https://dianeha.github.io/hidden/hidden.txt

https://dianeha.github.io/css/freelancer.css

> static web

> dinamic web



![1562808308719](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562808308719.png)

url : 어떤 자원이 어디있는지를 보여주는 주소, 탐색기...?

![1562809814324](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562809814324.png)

## html + Flask(웹서버 or 프레임워크)



from flask import Flask, render_template(html 파일을 리턴하기 위해 가져오는 것)



#### < D-day web-app >

![1562810030784](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562810030784.png)

![1562810061201](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562810061201.png)



#### < Box office web-app >

![1562811569101](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562811569101.png)

![1562811584250](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1562811584250.png)

사용자 입력 받아서 처리하는 법 

app.py

```html
@app.route('/receive')
def receive():
    data = request.args.get('msg')
    return render_template('receive.html', data=data)
```



receive.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>수신함</title>
</head>
<body>
    <h1>{{ data }}</h1>
</body>
</html>
```

return render_template('receive.html', data=data) 여기와

{{ data }} 여기





return render_template()

> >  send & receive



#### 암호화



* request.args.get() >> 이렇게 요청하면 주소창에 내가 보낸 데이터(아이디와 비밀번호)가 다 노출된다

result 라우터가 뚫어둔 길에 input_text에 ffffs를 입력했고 font 는 block이다 다 노출

http://127.0.0.1:5000/result?input_text=ffffs&font=block



* request.form.get() >> http://127.0.0.1:5000/receive // 정보가 노출되지 않고 처리된다. (제품을 박스에 넣어서 보내는 느낌)

send.html 에서

```html
<form action="/result" method="POST"
```

app.py 에서

```html
@app.route('/receive', methods=['POST']) <!-- <<<<< 여기 -->
def receive():
    data = request.form.get('msg')
    token = 'pk_63c229409ff14b67a6cc81e38927f1c4'
    stock = Stock(data, token=token).get_quote()
    company_name = stock['companyName']
    lastest_price = stock['iexRealtimePrice']
    return render_template(
        'receive.html',
        c_name=company_name,
        l_price=lastest_price
        )
```



<form action="/receive" method="POST">







※ html <form> 태그 / <a> 태그/ selector/ input태그



<input>

※ 구글크롬 웹스토어 확장 프로그램 설치가능

* json viewer
* Momemtum





