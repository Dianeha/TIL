# Views 최고 중간 관리자.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다.'

@app.route('/dict/<string:word>')
def my_dict(word):
    d = {
        'apple': '사과',
        'banana': '바나나'
    }

    if word in d:
        return f'{word}은(는) {d[word]}!'
    else:
        return f'{word}은(는) 나만의 단어장에 없는 단어입니다!'

if __name__ == '__main__':
    app.run(debug=True)