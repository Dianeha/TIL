from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')  # /로 route로 길을 뚫어주는데 그러면 templates안에서 index.html 문서를 찾아 서빙할 것이다.
def index():
    return render_template('index.html')


@app.route('/hello/<name>')  # variable routing 
def hello(name):
    return f'Hi, {name}'


@app.route('/pick_lunch/<int:count>')
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '사천탕면',
        '쟁반짜장'
    ]
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 45)
    lucky_numbers = random.sample(numbers, 6)
    return str(lucky_numbers)
# 주소가 /pick_lotto 로 끝나면 아래 명령들을 실행한다
# 이런 고정적인 주소를 '하드코딩'이라고 한다

# # 위와 다르게 <int:num> 변수처럼 처리해서 융통성을 줌
# @app.route('/get_lotto/<int:num>')
# def get_lotto_1():
#     #1회차 로또정보


@app.route('/cube/<int:num>')
def cube(num):
    return str(num ** 3)  # ** 3 > 3제곱(파이썬은 제곱근 지원함)


if __name__ == '__main__':
    app.run(debug=True)
