from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from IPython import embed

from .forms import ArticleModelForm
from .models import Article

# CRUD
@require_http_methods(['GET', 'POST'])
def new(request):
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
            return redirect(article) # return redirect('board:detail', article.id), models.py > 에 함수 만들어둠
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

def list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'board/detail.html', {
        'article': article,
    })

@require_http_methods(['GET', 'POST'])
def edit(request, id):
    article = get_object_or_404(Article, id=id)
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
def delete(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    return redirect('board:list')
