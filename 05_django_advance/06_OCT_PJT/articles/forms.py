from django import forms
from .models import Article

# forms / models 든 앞은 s가 붙고, Form / Model (뒤는) 안붙음
# models.Model / form.ModelForm
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', ) # '__all__' 이 아닌 이유는 user를 제외하기 때문, 이 두개만 검증(is_valid)한다