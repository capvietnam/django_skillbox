from django import forms
from .models import Goods
from app_users.models import Profile
from django.contrib.auth.models import User


class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['rest_goods', ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['balance', ]
