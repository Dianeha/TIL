from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest

from .forms import PostingForm, ImageForm, CommentForm
from .models import Posting, Comment, HashTag


@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment_form = CommentForm()
    is_like = posting.like_users.filter(id=request.user.id).exists()

    return render(request, 'postings/posting_detail.html', {
        'posting': posting,
        'comment_form':comment_form, # 작성용 폼을 보여주기 위해
        'is_like':is_like,
    })

@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'postings/posting_list.html', {
        'postings': postings,
    })

@login_required
@require_http_methods(['GET', 'POST'])
def create_posting(request):
    images = request.FILES.getlist('file')
    if request.method == 'POST':
        posting_form = PostingForm(request.POST)
        if posting_form.is_valid() and len(images) <= 5: 
            posting = posting_form.save(commit=False)
            posting.author = request.user
            posting.save()

            # Hashtag 부분            
            words = posting.content.split()
            for word in words:
                if word[0] == '#':
                    tag = HashTag.objects.get_or_create(content=word) # get_or_create의 return은 list이다
                    posting.hashtags.add(tag[0])

            for image in images:
                request.FILES['file'] = image
                image_form = ImageForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.posting = posting
                    image.save()
            return redirect(posting)
    else:
        posting_form = PostingForm()
        image_form = ImageForm()
    return render(request, 'postings/posting_form.html', {
        'posting_form': posting_form,
        'image_form': image_form,
    })
            

@login_required
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):    
    posting = get_object_or_404(Posting, id=posting_id)
    if posting.author == request.user:
        if request.method == 'POST':
            form = PostingForm(request.POST, instance=posting)
            if form.is_valid():
                posting = form.save()
                return redirect(posting)
        else:
            form = PostingForm(instance=posting)
    else:
        return redirect(posting)
    return render(request, 'postings/posting_form.html', {
        'posting_form': form,
    })

@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('postings:posting_list')

@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.posting = posting
        comment.save()
    return redirect(posting)

@login_required
@require_POST
def toggle_like(request, posting_id):
    if request.is_ajax:
        posting = get_object_or_404(Posting, id=posting_id)
        user = request.user

        # user가 좋아요 버튼을 눌렀다면
        if posting.like_users.filter(id=user.id).exists():
            posting.like_users.remove(user)
            liked = False
        else:
            posting.like_users.add(user)
            liked = True
        
        context = {'liked': liked, 'posting_id': posting.id, 'user_id': user.id}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest