from django.shortcuts import render, redirect, get_object_or_404
# accounts 에서 import할 모든 것들은 django.contrib.auth
from django.contrib.auth import login as auth_login, logout as auth_logout

# User 모델을 가져오는 함수
from django.contrib.auth import get_user_model

# accounts 에서 import 할 Form(UCF, AF)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# decorator
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:article_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login을 하도록 합시다. 인자가 2개!
            auth_login(request, user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/form.html', {
        'form':form
    })
    
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:article_list')
    
    if request.method == 'POST':
        # AuthForm만 유일하게 인자가 2개인 form ★
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 성공 => 성공한 user를 꺼낸다
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:article_list') # request.GET.get('next') or 어려우면 패스한다
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form':form
    })

def logout(request):
    auth_logout(request)
    return redirect('articles:article_list')