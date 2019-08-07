from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def cube(request, num):
    # 장고는 str나 int 등 기본자료형은 return 안됨!
    # return num ** 3 불가
    # return HttpResponse(num ** 3) # 이렇게 하면 응답객체가 됨
    r = num ** 3
    context = {'result': r}
    return render(request, 'cube.html', context) # 방법1


def check_int(request, num):
    is_even = num % 2 == 0
    return render(request, 'check_int.html', context={
        'is_even': is_even,
        'num': num,
    })  # 방법2


def pick_lotto(request):
    return render(request, 'pick_lotto.html', context={
        'lucky_numbers': random.sample(range(1, 46), 6),
    })
