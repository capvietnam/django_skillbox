from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, View, CreateView
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


class Index(View):
    Comment = Comment()

    def get(self, request, pk):
        return render(request, 'app_news/news-detail.html',
                      {'Comments': Comment.objects.filter(news_id=pk),
                       'News': News.objects.get(pk=pk)}
                      )

    def post(self, request, pk):
        self.Comment.description = request.POST.get("description")
        self.Comment.author = request.POST.get("author")
        self.Comment.news = News.objects.get(id=request.POST.get("news"))
        self.Comment.save()
        return render(request, 'app_news/news-detail.html', {'CommentForms': CommentForms})


class NewsDetail(View):
    News = News()

    def get(self, request, pk):
        return render(request, "app_news/change-news.html", {"News": News})

    def post(self, request, pk):
        News = self.News.objects.get(id=pk)
        News.title = request.POST.get("title")
        News.description = request.POST.get("description")
        News.is_published = request.POST.get("is_published")
        News.save()
        return render(request, 'app_news/change-news.html', {'NewsForms': NewsForms})
