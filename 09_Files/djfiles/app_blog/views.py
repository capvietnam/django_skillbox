from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Blog
from .forms import BlogForms
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# from .permissions import UserRequiredMixin


class HomeBlog(ListView):
    """Список всех новостей"""
    model = Blog
    template_name = 'app_blog/blog-list.html'
    context_object_name = 'Blog'
    extra_context = {'title': 'Список объявлений'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Blogs'] = self.model.objects.all()
        context['Users'] = User.objects.all()
        return context

    def get_queryset(self):
        return Blog.objects.order_by('date_create')


class AddBlog(CreateView):
    """Создание новой новости через сайт"""
    form_class = BlogForms
    template_name = 'app_blog/add-blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['User'] = User
        return context

    def get_success_url(self):
        return reverse('list-blog')

    def post(self, request):
        if request.method == "POST":
            form = BlogForms(request.POST)
            if form.is_valid():
                new_blog = form.save(commit=False)
                new_blog.description = form.cleaned_data.get('description')
                new_blog.user = request.user
                form.save()
                return redirect('/blog/')


class BlogDetail(DetailView):
    """Отдельная страница новости"""
    model = Blog
    template_name = 'app_blog/blog-detail.html'


class UpdateBlog(UpdateView):
    """Изменение новости в базе данных"""

    model = Blog
    template_name = 'app_blog/update-blog.html'
    fields = ['title', 'description']

    def form_valid(self, form):
        if not request.user.has_perm('app_blog.update_blog'):
            raise PermissionDenied()

    def get_success_url(self):
        return reverse('blog-list')
