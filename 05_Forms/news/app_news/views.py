from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import News, Comment
from .forms import NewsForms, CommentForms


class HomeNews(ListView):
    model = News
    template_name = 'app_news/news-list.html'
    context_object_name = 'News'
    extra_context = {'title': 'Список объявлений'}

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class AddNews(CreateView):
    form_class = NewsForms
    template_name = 'app_news/add-news.html'


class NewsDetail(DetailView):
    model = News
    template_name = 'app_news/news-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CommentForms'] = CommentForms
        return context

    def post(self, request, pk):
        f = CommentForms(request.POST)
        new_comment = f.save(commit=False)
        new_comment.description = request.POST.get("description")
        new_comment.author = request.POST.get("author")
        new_comment.news = self.model.objects.get(id=pk)
        f.save()
        return redirect('/news/' + str(pk))


class UpdateNews(UpdateView):
    model = News
    template_name = 'app_news/update-view.html'
    fields = ['title', 'description', 'is_published']

    def get_success_url(self):
        return reverse('news-list')
