from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=500)
    file = forms.FileField()


class MultiFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

# class AvatarForm(forms.ModelForm):
#     class Meta:
#         model = Avatar
#         fields = ('avatar',)
