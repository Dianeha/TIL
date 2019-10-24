from django.db import models
from django.conf import settings # 1. 만약 시험에서 import 되어 있다면,
from django.contrib.auth import get_user_model # 2. 아무것도 import 안되어 있다면 << 그냥 이걸 외운다 
# // 유저 관련된 것은 거의 django.contrib.auth에 있다
User = get_user_model()

# 여기는 줄 것
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 내(Article입장)가 뭐라고 접근할지 = ...related_name=남(User))이 나를 뭐라고 부를지
    like_users = models.ManyToManyField(User, related_name='like_articles')
