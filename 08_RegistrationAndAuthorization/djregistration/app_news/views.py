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
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .permissions import UserRequiredMixin


class HomeNews(ListView):
    """Список всех новостей"""
    model = News
    template_name = 'app_news/news-list.html'
    context_object_name = 'News'
    extra_context = {'title': 'Список объявлений'}

    def get_queryset(self):
        return News.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['News'] = News.objects.all()
        return context


class AddNews(UserRequiredMixin, CreateView):
    """Создание новой новости через сайт"""
    form_class = NewsForms
    template_name = 'app_news/add-news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['User'] = User
        return context


class NewsDetail(UserRequiredMixin, DetailView):
    """Отдельная страница новости"""
    model = News
    template_name = 'app_news/news-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CommentForms'] = CommentForms
        return context

    def post(self, request, pk):
        f = CommentForms(request.POST)
        if f.is_valid():
            if request.user.has_perm('app_users.can_news'):
                new_comment = f.save(commit=False)
                new_comment.news = self.get_object()
                if request.user.is_authenticated:
                    new_comment.user = request.user
                else:
                    new_comment.author += ' аноним'
                f.save()
        return redirect('/news/' + str(pk))


class UpdateNews(UserRequiredMixin, UpdateView):
    """Изменение новости в базе данных"""

    model = News
    template_name = 'app_news/update-view.html'
    fields = ['title', 'description', 'is_published']

    def form_valid(self, form):
        if not request.user.has_perm('app_news.update_news'):
            raise PermissionDenied()

    def get_success_url(self):
        return reverse('news-list')
