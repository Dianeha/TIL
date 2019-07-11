# words = input('입력하세요: ')  # 사용자의 입력을 받으면 그것이 숫자든 문자든 다 str(문자열)로 받는다 
# print(type(words))  # 124d, 하다연, sdfff든 다 str
# # words 의 첫 글자와 마지막 글자를 출력하라.
# print(words[0], words[-1])
# # 이렇게 쓰는 것은 리스트에서 쓰는 방법 아닌가요? string도 리스트처럼 메모리에 저장 > 리스트뿐 아니라 문자열도 인덱스 접근이 가능하다.



# # 문자열은 리스트로 형변환 가능하다
# my_list = list('123456')
# print(type(my_list))
# print(my_list[0], my_list[-1])


# 첫 글자와 마지막 글자를 출력
import random

length = random.choice(range(1, 100))
numbers = list(range(length))

print(numbers[length-1])
print(numbers[-1])  # list[-1]은 리스트의 뒤에서 첫번째 요소를 지칭
print(numbers[-2])
# # range() 함수는 list 생성함수는 아니지만 range()는 for문으로 돌려서 리스트처럼 출력 가능 
# list화 하려면 numbers = list(range(length)) 이런 식으로 해야한다. 




# <자연수 n을 입력받고, 1부터 n까지 출력하라>

n = input('원하시는 자연수를 입력해주세요: ')
# print(type(n))
n = int(n)

# print(type(n))
# print(n)
# for number in numbers:
#     print(number)

for i in range(n):
    print(i + 1, end=' ')






# <짝수/홀수를 구분하자> 2 => '짝' 출력
number = int(input('원하시는 숫자를 입력하세요: '))

if number % 2 == 0:
    print('짝!')
else:
    print('홀!')

numbers = range(4, 9)

for num in numbers:
    print(num)





# <fizz buzz => 3의 배수에서 fizz, 5의 배수에서 buzz, 15의 배수 fizzbuzz 출력>
n = int(input('원하시는 숫자를 입력하세요: '))

for num in range(1, n + 1):
    if num % 15 == 0:
        print('fizzbuzz', end=' ')
    elif num % 3 == 0:
        print('fizz', end=' ')
    elif num % 5 == 0:
        print('buzz', end=' ')
    else:
        print(num, end=' ')
