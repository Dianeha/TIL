my_n = [1, 2, 3, 4, 5, 6]
real_n = [1, 2, 3, 4, 5, 7]
bonus = 6

# my_n 과 real_n 의 숫자 6개가 같으면 1등
# my_n 과 real_n 의 숫자 5개가 같고 하나가 bonus면 2등
# my_n 과 real_n 의 숫자 5개가 같으면 3등
# my_n 과 real_n 의 숫자 4개가 같으면 4등
# my_n 과 real_n 의 숫자 3개가 같으면 5등
# 나머지는 꽝

count = 0
for i in my_n:
    for j in real_n:
        if i == j:
            count = count + 1
# print(count)

bonus_count = 0
for i in my_n:
    if i == bonus:
        bonus_count = bonus_count + 1
# print(bonus_count)

if count == 6:
    print('축하드립니다. 당신은 로또 1등에 당첨되셨습니다!')
elif count == 5:
    if bonus_count == 1:
        print('축하드립니다. 당신은 로또 2등에 당첨되셨습니다!')
    else:
        print('축하드립니다. 당신은 로또 3등에 당첨되셨습니다!')
elif count == 4:
    print('축하드립니다. 당신은 로또 4등에 당첨되셨습니다!')
elif count == 3:
    print('축하드립니다. 당신은 로또 5등에 당첨되셨습니다!')
else:
    print('다음 기회에 ... ')
