from django import forms
from .models import Article, Comment

# forms.Form = > Data 입력/검증(유효성 검사) + HTML 제공 => Model 정보 모름
# forms.modelForm = > Data 입력/검증(유효성 검사) + HTML 제공 => Model 정보 알고있음

class ArticleForm(forms.Form): # forms.Form  모든 컬럼에 대해서 다 작성해야함
    title = forms.CharField(min_length=2, max_length=100)        
    content = forms.CharField()

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
        # fields = '__all__' 와 비교해서
        fields = ('content', ) # id는 검증하지 않고 content만 검증할 것이다.