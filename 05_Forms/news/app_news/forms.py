from django import forms
from .models import News


class NewsForms(forms.Form):
    title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5
        }))
    date_create = forms.DateField(label='Дата созания', initial='')
    date_update = forms.DateField(label='Дата обновления')
    is_published = forms.BooleanField(label='Опубликованность')


class CommentForms(forms.Form):
    description = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)
    news = forms.ModelChoiceField(queryset=News.objects.all())
