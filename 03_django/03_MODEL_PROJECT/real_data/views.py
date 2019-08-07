from django.shortcuts import render
from real_data.models import HotIssue
import requests
from bs4 import BeautifulSoup

def index(n):
    url = 'https://datalab.naver.com/keyword/realtimeList.naver'
    headers = {'user-agent': ':)'}
    res = requests.get(url, headers=headers).text
    soup = BeautifulSoup(res, 'html.parser')

    time_sel = '#content > div > div.section_serch_area > div > div.time_indo > a.time_box._time_trigger > span.time_txt._title_hms'
    date_sel = '#content > div > div.section_serch_area > div > div.date_indo > a.date_box._date_trigger > span.date_txt._title_ymd'
    rank_sel = f'#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child({n}) > a > em'
    keyword_sel = f'#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child({n}) > a > span'

    time = soup.select_one(time_sel).text
    date = soup.select_one(date_sel).text
    rank = soup.select_one(rank_sel).text
    keyword = soup.select_one(keyword_sel).text
    return {'time': time, 'date': date, 'rank': rank, 'keyword': keyword}
    # #content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child(2) > a > span

    for i in range(1, 21):
        HotIssue.objects.create(
            time=get_hot_issue(i).get('time'),
            date=get_hot_issue(i).get('date'),
            rank=get_hot_issue(i).get('rank'),
            keyword=get_hot_issue(i).get('keyword'),
        )
