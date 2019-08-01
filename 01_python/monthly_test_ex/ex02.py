# 파일명 및 함수명을 변경하지 마시오.
def calc(equation):
    num_list = []
    for e in equation.split('+'):
        if e == '':
            continue
        elif '-' in e:
            idx = e.index('-')
            num_list.append(int(e[idx:]))
            if idx:
                num_list.append(int(e[:idx]))
        else:
            num_list.append(int(e))
    return sum(num_list)


# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    print(calc('123+2-124'))
    print(calc('-12+12-7979+9191'))
    print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))