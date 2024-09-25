from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                # 'class' : 'px-5 mt-5' # Bootstrap
                'class' : 'my-title',
                'placeholder' : '제목을 입력해주세요',
                'maxlength' : 10,
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)