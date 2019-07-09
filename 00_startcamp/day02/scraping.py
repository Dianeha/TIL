import requests
import bs4

# response라는 박스안에 네이버 소스코드 문자열 넣음
url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text
# BeautifulSoup에 response를 넣었다 빼서 text에 넣음
text = bs4.BeautifulSoup(response, 'html.parser')
# 네이버 금융 시세 코드들 중에서 특정부분만 빼내서 kospi 박스에 넣음
exchange_rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(exchange_rate.text)
