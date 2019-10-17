from django.db import models
from django.urls import reverse
from django.conf import settings # MASTER_APP/settings.py 임포트

"""
$ python manage.py migrate <APP_NAME> zero
$ rm <APP_NAME>/migrations/0*
"""

class Posting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    # pip install pillow 해야지만 ImageField를 쓸 쑤 있다.
    image = models.ImageField(blank=True) # 이미지는 비어있는 값일 수도 있으므로 blank = True를 줬다.
    created_at = models.DateTimeField(auto_now_add=True) # 'auto_now_add' 처음 생성할때만 시간 저장
    updated_at = models.DateTimeField(auto_now=True) # 수정 저장될 때마다 시간 저장
    
    class Meta:
        ordering = ['-created_at', ] # created_at 을 descending 내림차순

    # detail 페이지를 쓸 것이라면 만들어요
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})


    def __str__(self):
        return f'{self.pk}: {self.content[:20]}' # 20글자만 보이도록

class Comment(models.Model):    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # related_name 이 없으면 posting.comment_set / 아래와 같다면 posting.comments.all()
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return f'{self.id}: {self.content[:10]}'