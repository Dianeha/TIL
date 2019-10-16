from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm

@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings' : postings,
    })

@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all() # models.py 에서 related_name='comments'으로 설정해서 그렇다
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
        'comments': comments,
    })

@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES) # 검증 & 저장 준비
    if form.is_valid(): # 검증!
        posting = form.save() # 저장 => posting 객체 return
        return redirect(posting) # detail엣 get_absolute_url 생성해둬서 가능
        # 원래는 redirect('sns/posting_detail' posting.id)
    else:
        return redirect('sns:posting_list') # render는 html를 보낼 때

@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('sns:posting_list')

@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST) # CommentModelForm 은 foms.py 에서 content 값만을 확인
    if form.is_valid(): # content만 값 검증
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 때문에, 저장하는 척만하고 comment를 리턴
        comment.posting = posting # comment.posting_id = posting.id 와 동일
        comment.save()
    return redirect(posting)

@require_POST
def delete_comment(request, posting_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, posting_id=posting_id)
    comment.delete()
    return redirect(comment.posting)