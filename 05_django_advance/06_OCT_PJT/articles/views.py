from django.shortcuts import render, redirect, get_object_or_404
# User 모델을 가져오는 함수
from django.contrib.auth import get_user_model
# decorator
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm

from django.views.decorators.http import require_GET, require_POST, require_GET, require_http_methods
 
def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    # if article.like_users.filter(id=user.id).exists(): # 성능 고려 코드
    if user in article.like_users.all(): # 시험 통과용 코드 # 이미 좋아요 상태
        article.like_users.remove(user) # 고로 지움
    else:
        article.like_users.add(user)
    return redirect('articles:article_list')

@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles':articles,
    })

@require_GET
def article_detail(request, article_id):
    # get_object_or_404 의 1번 인자: 모델명, 2번 인자: 'id='
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article':article,
    })

# 중요
@login_required # CRD는 모두 @login_required
@require_http_methods(['GET', 'POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user # 혹은 article.user_id = request.user.id
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        form = ArticleForm()
    return render(request, 'articles/form.html', {
        'form':form,
    })

@login_required
@require_http_methods(['GET', 'POST'])
def article_update(request, article_id):
    # Update 추가사항(create 에 비해)
    # 0. article 하나 찾기
    article = get_object_or_404(Article, id=article_id)
    # 1. User 비교하기
    if article.user != request.user:
        return redirect('articles:article_list')
    
    if request.method == 'POST':
        # 2. instance 주기
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # 3. 고치기 (사실 안고쳐도 되긴함)
            article = form.save()
            return redirect('articles:article_detail', article_id)
    else:
        # 4. 또 인스턴스 주기
        form = ArticleForm(instance=article)
    return render(request, 'articles/form.html', {
        'form':form,
    })

@login_required
@require_POST
def article_delete(request, article_id):
    # 주의! user 비교하기
    article = get_object_or_404(Article, id=article_id)
    if article.user == request.user:
        article.delete()
    return redirect('articles:article_list')