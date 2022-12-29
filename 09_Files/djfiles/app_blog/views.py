from _csv import reader
from decimal import Decimal

from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib import messages
from .forms import BlogForm, BlogFormFull, UploadBlogForm
from .models import Blog, Images
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
# from .permissions import UserRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse


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


class BlogDetail(DetailView):
    """Отдельная страница новости"""
    model = Blog
    template_name = 'app_blog/blog-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Images.objects.all()
        return context

@login_required
def AddBlog(request):

    if request.method == "POST":
        # images will be in request.FILES
        form = BlogFormFull(request.POST or None, request.FILES or None)
        images = request.FILES.getlist('images')
        if form.is_valid():
            user = request.user
            description = form.cleaned_data['description']
            blog_obj = Blog.objects.create(user=user,
                                           description=description,)  # create will create as well as save too in db.
            for image in images:
                Images.objects.create(blog=blog_obj, image=image)
            return render(request, 'app_blog/add-blog.html', {})
        else:
            return render(request, 'g/add-blog.html', {})
    else:
        return render(request, 'app_blog/add-blog.html', {})


# class BlogDetail(DetailView):
#     """Отдельная страница новости"""
#     model = Blog
#     template_name = 'app_blog/blog-detail.html'

@login_required
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

@login_required
def upload_blog(request):
    if request.method == "POST":
        upload_blog_form = UploadBlogForm(request.POST, request.FILES)
        if upload_blog_form.is_valid():
            blog_file = upload_blog_form.cleaned_data['file'].read()
            blog_str = blog_file.decode('utf-8').split('\n')
            csv_reader = reader(blog_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                Blog.objects.filter(description=row[0].update(date_create=Decimal(row[1])))
            return HttpResponse(content='Блоги успешно обновлены', status=200)
    else:
        upload_blog_form = UploadBlogForm()

    context = {'form': upload_blog_form}
    return render(request, 'app_blog/upload-blog-file.html', context=context)
