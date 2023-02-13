from django import forms
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class AuthenticationForms(AuthenticationForm):
    """
    Форма аутентификации пользователя
    """
    username = forms.CharField(label=_('Nickname'),
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label=_('Password'),
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(UserCreationForm):
    """
    Форма входа пользователя
    """
    username = forms.CharField(label=_('Nickname'),
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Mete:
        model = User
        fields = ('username', 'password', 'password1')


class UserForm(forms.Form):
    """
    Форма пользователя
    """
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

