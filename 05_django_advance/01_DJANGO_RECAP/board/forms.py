from django import forms
from .models import Article

# forms.Form = > Data 입력 및 검증
# forms.modelForm = > + HTML 생성까지 해줌

class ArticleModelForm(forms.ModelForm): # forms.ModelForm 를 상속받는 클래스
    # 1. Data 입력 및 검증
    # 2. HTML 을 생성해줌
    title = forms.CharField(min_length=2) # 제목은 최소한 2글자는 써야한다. 는 뜻
    class Meta:
        model = Article
        fields = '__all__'