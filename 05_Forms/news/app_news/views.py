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

        # model = News
        # context_object_name = 'News'
        # template_name = 'app_news/news-detail.html'
        #
        #
        # def get_context_data(self, *, object_list=None, **kwargs):
        #     context = super(Index, self).get_context_data(**kwargs)
        #     context['title'] = self.model.objects.get(pk=self.kwargs['pk'])
        #     context['CommentForms'] = CommentForms
        #     context['Comments'] = Comment
        #     return context
