print(ord('a'), ord('b'))

# 연습문제2 >> itoa() 구현 정수를 문자로
# data = input('2-3자리 숫자 입력')
# res = [chr(ord(x)) for x in data]
# print(res)

# atoi() 구현
def atoi(str):
    value = 0

    for i in range(len(str)):
        if ord(str[i]) >= ord('0') and ord(str[i]) <= ord('9'):
            digit = ord(str[i]) - ord('0')
        else:
            break

        value = (value * 10) + digit
        # print(value)
    return value

# print(atoi('123'), type(atoi('123')))

# itoa() 구현

def myitoa(x): # 10으로 나눠서 몫, 나머지 이용하는 아이디어

    sr = ''
    while True:
        r = x % 10
        sr = sr + chr(r + ord('0'))
        x = x//10
        if x == 0: break

    s = ''
    for i in range(len(sr)-1, -1, -1):
        s = s + sr[i]

    return s

print(myitoa(123))