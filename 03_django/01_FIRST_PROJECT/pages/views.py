from django.shortcuts import render, HttpResponse
import json

def index(request):
    return HttpResponse('Hi django! :D')

def about(request):
    me = {
        'name': 'Diane',
        'role': 'Student',
        'email': 'fdsa@gmail.com'
    }
    return HttpResponse(json.dumps(me))

# HTML을 내보내고 싶다.
def portfolio(request):
    
    return render(request, 'portfolio.html')

# pages/help/ => help() view 함수 실행 => help.html(내용무관)
def help(request):
    
    return render(request, 'help.html')