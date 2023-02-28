from django import forms
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class AuthenticationForms(AuthenticationForm):
    username = forms.CharField(label=_('Nickname'),
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(UserCreationForm):
    username = forms.CharField(label=_('Nickname'),
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label=_('Surname'),
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label=_('About me'),
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Mete:
        model = User
        fields = ('username', 'last_name', 'description', 'password', 'password1')


class UserForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['last_name', 'description', 'avatar']
