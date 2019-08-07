# 파일명 및 함수명을 변경하지 마시오.
# def calc(equation):
#     num_list = []
#     for e in equation.split('+'):
#         if e == '':
#             continue
#         elif '-' in e:
#             idx = e.index('-')
#             num_list.append(int(e[idx:]))
#             if idx:
#                 num_list.append(int(e[:idx]))
#         else:
#             num_list.append(int(e))
#     return sum(num_list)


# '+'를 ' +'로 대체, '-'를 ' -'로 대체 하고 split > map(int, number), sum
# 더하기와 빼기만 하는 것은 결국 더하기들
# 파이썬은 +1 도 int로 인식 -1도 int로 인식 >>>> +와 -를 제거할 필요가 없다.
def calc(equation):
    result = equation.replace('+', ' +').replace('-', ' -').split()
    answer = map(int, result)
    return sum(answer)

# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))