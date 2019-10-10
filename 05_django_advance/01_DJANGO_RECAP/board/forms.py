from django import forms
from .models import Article, Comment

# forms.Form = > Data 입력 및 검증(유효성 검사)
# forms.modelForm = > + HTML 생성까지 해줌

class ArticleModelForm(forms.ModelForm): # forms.ModelForm 를 상속받는 클래스
    # 1. Data 입력 및 검증
    # 2. HTML 을 생성해줌
    title = forms.CharField(min_length=2, max_length=100) # 제목은 최소한 2글자는 써야한다. 는 뜻
    class Meta: # meta : 데이터에 대한 데이터 (사진, 사진 찍힌 시간, 위치, 사진의 크기 등)
        # 지금은 위 클래스에 대한 정보
        model = Article
        fields = '__all__'

class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model = Comment
        fields = '__all__'