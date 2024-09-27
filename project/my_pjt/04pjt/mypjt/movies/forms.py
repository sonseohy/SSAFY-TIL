from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control'}),
        }