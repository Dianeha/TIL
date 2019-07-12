import datetime
import requests
import bs4
from art import *
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


# 숫자 두 개를 받아서 더한 값을 result에 그 결과를 보여줌 input 태그 두개사용
@app.route('/art')
def add():
    return render_template('art.html')


@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
   # print(input_text, font)  # >> 터미널에서 보이기
    result = text2art(input_text, font=font)
    return render_template('result.html', result=result)


@app.route('/')  # 아무 말도 없을 때
def index():
    return render_template('index.html')


@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive')
def receive():
    data = request.args.get('msg')
    token = 'pk_63c229409ff14b67a6cc81e38927f1c4'
    stock = Stock(data, token=token).get_quote()
    company_name = stock['companyName']
    lastest_price = stock['iexRealtimePrice']

    url = 'https://finance.naver.com/marketindex/'
    response = requests.get(url).text
    text = bs4.BeautifulSoup(response, 'html.parser')
    exchange_rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
    wd = exchange_rate.text
    new_wd = wd.replace(",", "")
    wd_rate = float(new_wd)

    return render_template(
        'receive.html',
        c_name=company_name,
        l_price=lastest_price,
        wd_price=round(wd_rate*lastest_price, 2)
        )


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)
    # return f'SSAFY 2기 1학기 종료일까지 {left.days}일 남았습니다.'


@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리 4',
        '기생충',
        '라이온킹'
    ]
    return render_template('boxoffice.html', movies=top_5)


if __name__ == '__main__':
    app.run(debug=True)
