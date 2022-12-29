from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, AuthenticationForm, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView
from .forms import *
from .models import Profile
from django.template.context_processors import request
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.contrib.auth.decorators import login_required




class UserLoginView(LoginView):
    template_name = 'app_users/user-login.html'

    def get_success_url(self):
        return "/blog/"


class UserLogoutView(LogoutView):
    template_name = 'app_users/user-logout.html'

    def get_success_url(self):
        return "/blog/"




@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='user-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'app_users/user-profile.html', {'user_form': user_form, 'profile_form': profile_form})


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
            return redirect('blog-list')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = LoginForm()
    return render(request, 'app_users/user-register.html', {'form': form})
