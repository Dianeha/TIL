from django.shortcuts import render, redirect
from .models import Article # 내 위치에 있는 models에서 Article을 가져오겠다

# Create your views here.
def index(request):
    return render(request, 'board/index.html')

def list(request):
    articles = Article.objects.all() # [<A1>, <A2>, <A3>,...] 
    return render(request, 'board/list.html', {
        'articles': articles,
    })

def detail(request, id):
    article = Article.objects.get(id=id) # <A_id> 하나의 객체
    return render(request, 'board/detail.html', {
        'article': article,
    })

def new(request):
    return render(request, 'board/new.html')

def create(request):
    # INSERT INTO board_article (title, content) 
    # VALUES (request.POST.get('title'), request.POST.get('content'))
    # 이것의 python식 표현이 아래와 같다
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    print(article.id, article.title, article.content)
    return redirect('board:detail', article.id)