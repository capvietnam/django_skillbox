from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, AuthenticationForm, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import *
from .models import Profile


class UserLoginView(LoginView):
    template_name = 'app_users/user-login.html'


class UserLogoutView(LogoutView):
    template_name = 'app_users/user-logout.html'


class PtofileDetail(DetailView):
    """Профиль"""
    model = User
    template_name = 'app_users/user-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ProfileForm'] = ProfileForm
        return context


def UserRegisterView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            description = form.cleaned_data.get('description')
            last_name = form.cleaned_data.get('last_name')
            Profile.objects.create(user=user,
                                   last_name=last_name,
                                   description=description,
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
