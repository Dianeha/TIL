from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from IPython import embed

from .forms import ArticleModelForm, CommentModelForm, ArticleForm
from .models import Article, Comment

# Create Article with Form
def new_article_with_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article()
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            return redirect(article)
    else:
        form = ArticleForm()
    return render(request, 'board/new.html', {
        'form':form,
    })

# CRUD
@require_http_methods(['GET', 'POST'])
def new_article(request):
    # 요청이 GET/POST 인지 확인한다
    # 만약 POST 라면
    if request.method == "POST":
        # ArticleModeForm의 인스턴스를 생성하고 DATA를 채운다(binding)).
        form = ArticleModelForm(request.POST)
        # embed()
        # binding된 form이 유효한지 체크한다.
        if form.is_valid():
            # 유효하다면 form을 저장한다       
            article = form.save()
            # 저장한 article로 redirect 한다        
            return redirect(article) # return redirect('board:article_detail', article.id), models.py > 에 함수 만들어둠
        else:
            # 유효하지 않은 입력데이터를 담은 HTML과 에러메세리를 사용자에게 보여준다.
            return render(request, 'board/new.html', {
            'form':form
        })

    # GET이라면
    else:
        # 비어있는 form(HTML 생성기)을 만든다.
        form = ArticleModelForm()
        # form과 html을 사용자에게 보여준다
        return render(request, 'board/new.html', {
            'form':form
        })

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # 특정 id에 해당하는 article에 있는 comment를 모두 보여주고 역순으로 정렬해주세요
    comments = article.comment_set.all().order_by('-id') #Comment.objects.filter(article_id=article.id)
    comment_form = CommentModelForm()

    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    })

@require_http_methods(['GET', 'POST'])
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        # form = ArticleModelForm(request.POST) 이렇게 쓰면 새종이에 데이터 쓰는 것이고 instance=article 하면 있는 데이터에 덮어써서 수정하는 것
        form = ArticleModelForm(request.POST, instance=article) # 사용자가 '새로 입력한 데이터'를 미리 만들어둔 case에 넣음
        if form.is_valid():
            article = form.save()
            return redirect(article)
        # else:            
        #     return render(request, 'board/edit.html', {
        #     'form':form
        # })

    # 사용자가 수정하기 위한 html 파일을 요청함/ 있던 데이터를 찾아서 html에 넣어서 보내줌
    else:        
        form = ArticleModelForm(instance=article)
    # 위와 겹치므로 한칸 앞으로 가서 코드 간단히 해줌
    return render(request, 'board/edit.html', {
        'form':form
    })

@require_POST
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('board:article_list')

@require_POST
def new_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    form = CommentModelForm(request.POST)
    # embed()
    if form.is_valid(): # new_article이랑 비교해보기
        comment = form.save(commit=False) # 아직 미완성. forms에서 유효성 검사는 content만 했기 때문
        # 아직 article_id 안들어옴
        comment.article_id = article.id # 여기서 직접 해줌
        comment.save()
    return redirect(article)

@require_POST
def delete_comment(request, article_id, comment_id):
    # import time
    # start = time.time()
    
    # 방법1 안정성 up / 효율 down
    # article = get_object_or_404(Article, id=article_id)
    # comment = get_object_or_404(Comment, id=comment_id)
    # if comment in article.comment_set.all(): # > 여기서 전체 댓글수가 엄청 많으면 지불해야할 비용이 증가
    #     comment.delete()

    # 방법2 가성비 코드 - 안정성 down / 효율 up
    # comment = get_object_or_404(Comment, id=comment_id)
    # comment.delete() # DB에서 삭제
    # end = time.time()
    # print(end - start)

    # 방법3
    comment = get_object_or_404(Comment, id=comment_id, article_id=article_id)
    comment.delete()

    return redirect(comment.article) # 메모리에는 아직 남아있어서 comment.article 가능

