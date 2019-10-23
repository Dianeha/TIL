from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm


@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings' : postings,
    })

@login_required
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all() # models.py 에서 related_name='comments'으로 설정해서 그렇다
    if posting.like_users.filter(id=request.user.id).exists():
        is_like = True
    else:
        is_like = False
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
        'comments': comments,
        'is_like': is_like,
    })

@login_required
@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES) # 검증 & 저장 준비
    if form.is_valid(): # 검증!
        posting = form.save(commit=False) # 저장 => posting 객체 return
        posting.user = request.user
        posting.save()
        return redirect(posting) # detail엣 get_absolute_url 생성해둬서 가능
        # 원래는 redirect('sns/posting_detail' posting.id)
    else:
        return redirect('sns:posting_list') # render는 html를 보낼 때

@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.user == posting.user: # 요청보내는 사람과 포스팅 작성자가 다르면 삭제하지 못하도록
        posting.delete()
    return redirect('sns:posting_list')

@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST) # CommentModelForm 은 foms.py 에서 content 값만을 확인
    if form.is_valid(): # content만 값 검증
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 때문에, 저장하는 척만하고 comment를 리턴
        comment.posting = posting # comment.posting_id = posting.id 와 동일
        comment.user = request.user
        comment.save()
    return redirect(posting)

@login_required
@require_POST
def delete_comment(request, posting_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, posting_id=posting_id)
    comment.delete()
    return redirect(comment.posting)

@login_required # 로그인 상태에서만 좋아요 누를 수 있음
@require_POST # DB에 영향을 줌
def toggle_like(request, posting_id):
    user = request.user
    posting = get_object_or_404(Posting, id=posting_id)
    # if user in posting.like_users.all()
    # 좋아요가 100만개면 모든 좋아요 정보 다 불러와서 내가 찾는 좋아요가 있는지 확인 
    # >> 메모리 낭비, 돈낭비
    if posting.like_users.filter(id=user.id).exists():
        posting.like_users.remove(user) # Delete
    else:
        posting.like_users.add(user) # Create
    return redirect(posting)
