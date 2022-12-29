from django import forms
from .models import Blog, File


class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class FileForms(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = File
        fields = ['file_field']
