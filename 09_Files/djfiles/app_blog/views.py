from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib import messages
from .forms import BlogForms, FileForms
from .models import Blog


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


def BlogDetail(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == "POST":
        blog_form = BlogForms(request.POST, instance=Blog.objects.get(id=pk))
        file_form = FileForms(request.POST, request.FILES, instance=Blog.objects.get(id=pk).files)

        if blog_form.is_valid() and file_form.is_valid():
            blog_form.save()
            file_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='user-profile')
    else:
        blog_form = BlogForms(instance=Blog.objects.get(id=pk))
        file_form = FileForms(instance=Blog.objects.get(id=pk).files)
    return render(request, 'app_blog/add-blog.html', {'blog_form': blog_form, 'file_form': file_form, 'blog': blog})


class AddBlog(CreateView):
    """Создание новой новости через сайт"""
    form_class = BlogForms
    template_name = 'app_blog/add-blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['User'] = User
        return context


# class BlogDetail(DetailView):
#     """Отдельная страница новости"""
#     model = Blog
#     template_name = 'app_blog/blog-detail.html'


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
