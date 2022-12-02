from django import forms
from .models import Blog


class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
