from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request): # new_user
    
    # 사용자가 회원가입할 데이터를 보냈다는 뜻
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
    else: 
        # 사용자가 회원가입 HTML을 달라고 요청
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })
def login(request):
    pass

def logout(request):
    pass
