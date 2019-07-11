# 가져온 로또 번호
import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
response = requests.get(url).text
# print(type(response))
# print(response)

data = json.loads(response)
# print(type(data), data) 
# print(data['bnusNo'])


real_n = []
for i in data:
        print(i)  # 딕셔너리 data 중에 'drwtNo'가 들어간 부분만 추출해서 real_n 리스트에 추가
#     if 'drwtNo' in key:
#         real_n.append(value)

# print(real_n)

# real_n = []
# for i in range(6):
#     real_n.append(data[f'drwtNo{i+1}'])

# print(real_n)
# print(real_n[0])
# print(real_n[1])
# print(real_n[2])
# print(real_n[3])
# print(real_n[4])
# print(real_n[5])
# print(range(6))

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
