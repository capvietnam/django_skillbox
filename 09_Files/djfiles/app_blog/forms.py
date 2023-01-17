from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['description', ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class BlogFormFull(BlogForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(BlogForm.Meta):
        fields = BlogForm.Meta.fields + ['images', ]


class UploadBlogForm(forms.Form):
    file = forms.FileField()
