from django.db import models
from django.urls import reverse

"""
$ python manage.py migrate <APP_NAME> zero
$ rm <APP_NAME>/migrations/0*
"""

class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True) # 이미지는 비어있는 값일 수 도 있다.
    created_at = models.DateTimeField(auto_now_add=True) # 'auto_now_add' 처음 생성할때만 시간 저장
    updated_at = models.DateTimeField(auto_now=True) # 수정 저장될 때마다 시간 저장

    # detail 페이지를 쓸 것이라면 만들어요
    def get_absolute_url(self):
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})

    def __str__(self):
        return f'{self.pk}: {self.content[:20]}' # 20글자만 보이도록