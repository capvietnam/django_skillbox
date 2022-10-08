from django import forms
from .models import News, Comment


class NewsForms(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'description', 'news']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'news': forms.Select(attrs={'class': 'form-control'}),
        }
