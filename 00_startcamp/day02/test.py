import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from datetime import datetime

today = datetime.today().strftime('%Y%m%d')

writer = csv.writer(open('movie50.csv', 'w', encoding='utf-8', newline=''))
writer.writerow(['MovieCd', 'movieName', 'movieNameE', 'filmRatings', 'pubDate', 'runtime', 'genre', 'director', 'userRating', 'audience', 'poster_url', 'description'])
# 영화         대표코드(네이버),영화명(국문),영화명(영문), 관람등급,      개봉연도,   상영시간,   장르,      감독,     실관람객평점, '누적관람객',  포스터,     '줄거리'

# 최근상영영화 중 평점 높은 50개
url = f'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date={today}'
headers = {'User-Agent': ':)'} # 딕셔너리(키, 밸류)

response = requests.get(url, headers=headers).text
text = BeautifulSoup(response, 'html.parser')
rows = text.select('.tit5')

for row in rows:
    
    # 1. 영화코드 가져오기 >> 네이버 영화 상세 페이지로 가서 다 긁어올 것임
    target = str(row.select_one('div > a'))
    temp = target[37:43]
    if temp[-1] == '\"':
        temp = temp[:-1]
    MovieCd = int(temp)
    print(MovieCd)

    # 영화 상세 페이지로 이동
    url2 = f'https://movie.naver.com/movie/bi/mi/basic.nhn?code={MovieCd}'
    res = requests.get(url2, headers=headers).text
    text = BeautifulSoup(res, 'html.parser')
    url2 = f'https://movie.naver.com/movie/bi/mi/basic.nhn?code={MovieCd}'
    
    # 2. movieName(영화명-국문)
    movieName = text.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a:nth-child(1)').text
    print(movieName)

    # 3. movieNameE(영화명-영문) / pubDate(개봉연도)
    e = text.select_one('#content > div.article > div.mv_info_area > div.mv_info > strong').text
    movieNameE = e.split(',')[0]
    pubDate = e.split(',')[1][1:]
    print(movieNameE)

    # 4. filmRatings(관람등급)
    filmRatings = text.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p > a').text
    print(filmRatings)

    # 5. runtime(상영시간)
    runtime = text.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)').text[:-1]
    print(runtime)

    # 6. genre(장르)
    # 장르가 2개인 경우는 추후에 보완하도록 하자! 없으면 None 이 나오기 때문에 있을 때만 genre_id에 추가하면 됨. pjt10에서처럼 json 파일에 [1, 5] 이런 식으로....?
    # genreId2 = str(text.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a:nth-child(2)'))
    genre = str(text.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a'))[46:48]
    if genre[-1] == '\"':
        genre = genre[:-1]
    genre = int(genre)
    print(genre)
    
    # 7. director(감독)
    director = text.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a').text
    print(director)

    # 8. userRating
    userRating = float(text.select_one('#actualPointPersentBasic > div > span > span').text[7:11])
    print(userRating)

    # 9. audience
    # what = text.select_one('')
    # print(what)

    # 10. poster_url(포스터)
    tempUrl = urlopen(f"https://movie.naver.com/movie/bi/mi/photoViewPopup.nhn?movieCode={MovieCd}")
    tempRes = BeautifulSoup(tempUrl, 'html.parser')
    poster_url = tempRes.find('img', id="targetImage").get('src')
    # print(poster_url)

    # 11. drscription
    what = text.find('p', class_='con_tx')
    c = text.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div.story_area > p')
    print(c)
    # print(movieName, '|' , genre, '|', poster_url)
    # writer.writerow([MovieCd, movieName, genre, poster_url])
    break
    