from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class AuthenticationForms(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(UserCreationForm):
    username = forms.CharField(label='Никнейм',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='О себе',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Mete:
        model = User
        fields = ('username', 'last_name', 'description', 'password', 'password1')


class UserForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['last_name', ]
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
