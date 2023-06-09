import random

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import *
from .models import Purchase
from django.views.generic import DetailView
from app_goods.models import Goods
from django.core.cache import cache
from .func import get_random_good, get_good_prise


class UserLoginView(LoginView):
    """
    View регистрации пользователя
    """
    template_name = 'app_users/user-login.html'

    def get_success_url(self):
        return "/goods/shop_list/"


class UserLogoutView(LogoutView):
    """
    View выхода пользователя
    """
    template_name = 'app_users/user-logout.html'

    def get_success_url(self):
        return "/goods/shop_list/"


class Profile(DetailView):
    """
    View профиля пользователя
    """
    template_name = 'app_users/profile-detail.html'
    model = User
    context_object_name = 'User'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        good_id = random.randint(1, len(Goods.objects.all()))
        usarname = self.request.user.username

        random_good_cache_key = 'random_good:{}'.format(usarname)
        good_prise_cache_key = 'good_prise:{}'.format(usarname)

        promotion_good = cache.get(random_good_cache_key)
        promotion_prise = cache.get(good_prise_cache_key)

        if not promotion_good:
            promotion_good = get_random_good(good_id)
            cache.set(random_good_cache_key, promotion_good, 60 * 60)

        if not promotion_good:
            promotion_prise = get_good_prise(good_id)
            cache.set(random_good_cache_key, promotion_good, 60 * 60)


        context['random_good'] = promotion_good
        context['good_prise'] = promotion_prise
        context['Purchase_history'] = Purchase.objects.filter(user=self.request.user)
        return context


def UserRegisterView(request):
    """
    View регистрации пользователя
    """
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('shop-list')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = LoginForm()
    return render(request, 'app_users/user-register.html', {'form': form})
