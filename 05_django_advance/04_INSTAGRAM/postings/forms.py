from django import forms
from .models import Posting, Image#, Comment

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('content', )

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file', )
        widgets = {
            'file': forms.FileInput(attrs={'multiple':True})
        } # 여러개의 사진을 업로드할 수 있는 폼 만들어짐

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)