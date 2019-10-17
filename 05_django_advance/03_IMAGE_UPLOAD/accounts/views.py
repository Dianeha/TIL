from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


def signup(request): # new_user
    # 사용자가 login한 상태라면 무시하고 포스팅리스트 보여줌
    if request.user.is_authenticated:
        return redirect('sns:posting_list')

    # 사용자가 회원가입할 데이터를 보냈다는 뜻
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('sns:posting_list')
    else: 
        # 사용자가 회원가입 HTML을 달라고 요청
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    # 사용자가 login한 상태라면 무시하고 포스팅리스트 보여줌
    if request.user.is_authenticated:
        return redirect('sns:posting_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # 함수 이름과 겹치지 않도록 import할 때 auth_login 으로 가져옴
            return redirect('sns:posting_list')
            # response = redirect('sns:posting_list') 쿠키 nickname으로 꺼내 쓸 수 있음
            # response.set_cookie(key='nickname', value='idiot', max_age=5)
            # return response

        # 입국신청서 = AuthenticationForm(request, request.POST)
        # if 입국신청서.is_valid():
        #     login(request, 입국신청서.get_user()) 의 사용자
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })

def logout(request):
    auth_logout(request)
    return redirect('sns:posting_list')