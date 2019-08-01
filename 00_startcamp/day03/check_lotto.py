my_n = [1, 2, 3, 4, 5, 6]
real_n = [1, 2, 3, 4, 5, 7]
bonus = 6

# my_n 과 real_n 의 숫자 6개가 같으면 1등
# my_n 과 real_n 의 숫자 5개가 같고 하나가 bonus면 2등
# my_n 과 real_n 의 숫자 5개가 같으면 3등
# my_n 과 real_n 의 숫자 4개가 같으면 4등
# my_n 과 real_n 의 숫자 3개가 같으면 5등
# 나머지는 꽝


# is_bonus = False
# if bonus in my_n:
#         is_bonus = True

count = 0
for i in my_n:
    for j in real_n:
        if i == j:
            # count = count + 1
            count += 1
            break

# 나의 방법
# bonus_count = 0
# for i in my_n:
#     if i == bonus:
#         bonus_count += 1
# print(bonus_count)

if count == 6:
    result = '1등'
elif count == 5:
    if bonus in my_n:
        result = '2등'
    else:
        result = '3등'
elif count == 4:
    result = '4등'
elif count == 3:
    result = '5등'
else:
    result = '꽝'

print(result)
