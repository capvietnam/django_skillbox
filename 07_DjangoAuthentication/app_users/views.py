from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import News, Comment
from .forms import NewsForms, CommentForms
from django.contrib.auth.models import User


class HomeNews(ListView):
    """Список всех новостей"""
    model = News
    template_name = 'app_news/news-list.html'
    context_object_name = 'News'
    extra_context = {'title': 'Список объявлений'}

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class AddNews(CreateView):
    """Создание новой новости через сайт"""
    form_class = NewsForms
    template_name = 'app_news/add-news.html'


class NewsDetail(DetailView):
    """Отдельная страница новости"""
    model = News
    template_name = 'app_news/news-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CommentForms'] = CommentForms
        return context

    def post(self, request, pk):
        # f = CommentForms(request.POST)
        # if f.is_valid():
        #     new_comment = f.save(commit=False)
        #     new_comment.news = self.get_object()
        #     if request.user.is_authenticated:
        #         new_comment.user.username = request.user.username
        #     f.save()
        f = CommentForms(request.POST)
        if f.is_valid():
            new_comment = f.save(commit=False)
            new_comment.news = self.get_object()
            if request.user.is_authenticated:
                new_comment.user = request.user
            else:
                new_comment.author += ' аноним'
            f.save()
        return redirect('/news/' + str(pk))


class UpdateNews(UpdateView):
    """Изменение новости в базе данных"""
    model = News
    template_name = 'app_news/update-view.html'
    fields = ['title', 'description', 'is_published']

    def get_success_url(self):
        return reverse('news-list')


class UserLoginView(LoginView):
    """Аутификация пользоваетлей"""
    template_name = 'app_news/user-login.html'


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
    return render(request, 'app_news/user-register.html', {'form': form})


class UserLogoutView(LogoutView):
    template_name = 'app_news/user-logout.html'

#
# def user_logout(request):
#     """Выход пользователей из системы"""
#     logout(request)
#     return HttpResponse(
#         "Вы успешно вышли" + "<p></p><a class='nav-link' href={% /news/ %}>Все объявления</a>")
