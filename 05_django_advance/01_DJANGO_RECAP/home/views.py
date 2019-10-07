from django.shortcuts import render, HttpResponse
import random

def index(request):
    return render(request, 'home/index.html')

def guess(request):
    return render(request, 'home/guess.html')

def answer(request): 
    count = 0
    if request.POST.get('q1') == '1010':
        count += 1
    if request.POST.get('q2') == '토드':
        count += 1
    if request.POST.get('q3') == '재잉':
        count += 1
    
    return render(request, 'home/answer.html', {
        'count': count,
    })
