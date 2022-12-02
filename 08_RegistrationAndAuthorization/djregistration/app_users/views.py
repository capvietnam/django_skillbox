from django.contrib.auth import authenticate, login
from .forms import ProfileForm
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm

News = apps.get_model('app_news', 'News')


class PtofileDetail(DetailView):
    """Профиль"""
    model = User
    template_name = 'app_users/user-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ProfileForm'] = ProfileForm
        return context


class UserLoginView(LoginView):
    """Аутификация пользоваетлей"""
    template_name = 'app_users/user-login.html'


def UserRegisterView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            number = form.cleaned_data.get('number')
            Profile.objects.create(user=user,
                                   city=city,
                                   number=number
                                   )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('news-list')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = LoginForm()
    return render(request, 'app_users/user-register.html', {'form': form})


class UserLogoutView(LogoutView):
    template_name = 'app_users/user-logout.html'
