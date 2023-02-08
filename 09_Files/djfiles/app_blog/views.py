
from _csv import reader
from decimal import Decimal
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import BlogFormFull, UploadBlogForm
from .models import Blog, Images
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


class HomeBlog(ListView):
    """Список всех новостей"""
    model = Blog
    template_name = 'app_blog/blog-list.html'
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
        # images will be in request.F
        # ILES
        form = BlogFormFull(request.POST or None, request.FILES or None)
        images = request.FILES.getlist('images')
        if form.is_valid():
            user = request.user
            description = form.cleaned_data['description']
            blog_obj = Blog.objects.create(user=user,
                                           description=description, )  # create will create as well as save too in db.
            for image in images:
                Images.objects.create(blog=blog_obj, image=image)
            return render(request, 'app_blog/add-blog.html', {})
        else:
            return render(request, 'app_blog/add-blog.html', {})
    else:
        return render(request, 'app_blog/add-blog.html', {})


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
