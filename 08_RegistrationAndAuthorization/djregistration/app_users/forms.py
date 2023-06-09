from django import forms
from .models import Profile
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class AuthenticationForms(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='Город',
                           widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    number = forms.IntegerField(label='Номер телефона',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Mete:
        model = User
        fields = ('username', 'city', 'number', 'verification', 'password', 'password1')


class UserForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'number']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
