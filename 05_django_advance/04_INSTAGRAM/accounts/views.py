from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth import login as auth_login, logout as auth_logout

# 회원가입용 Form, 인증(로그인)용 From
from .forms import CustomAuthenticationForm, CustomUserCreationForm

# 현재 프로젝트에서 사용할 USer 모델을 return 하는 함수
from django.contrib.auth import get_user_model
User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('postings/posting_list')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('postings/posting_list.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form
    })

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('postings/posting_list.html')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form
    })

def logout(request):
    auth_logout(request)
    return redirect('postings/posting_list.html')

@require_GET
def user_page(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/user_page.html', {
        'user_info':user_info,
    })

# @require_POST
def follow(request, user_id):
    fan = request.user
    star = get_object_or_404(User, id=user_id)

    if fan != star:
        if star.fans.filter(id=fan.id).exists():
            star.fans.remove(fan)
        else:
            star.fans.add(fan)
    return redirect(star)
