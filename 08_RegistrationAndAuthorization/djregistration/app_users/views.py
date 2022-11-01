# from .forms import
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Profile

News = apps.get_model('app_news', 'News')


class HomeNews(ListView):
    """Список всех новостей"""
    model = News
    template_name = 'app_news/news-list.html'
    context_object_name = 'News'
    extra_context = {'title': 'Список объявлений'}

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class PtofileDetail(DetailView):
    """Профиль"""
    model = Profile
    template_name = 'app_users/user-profile.html'


class UserLoginView(LoginView):
    """Аутификация пользоваетлей"""
    template_name = 'app_users/user-login.html'


def UserRegisterView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('user-login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'app_users/user-register.html', {'form': form})


class UserLogoutView(LogoutView):
    template_name = 'app_users/user-logout.html'
