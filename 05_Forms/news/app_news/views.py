from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import News, Comment
from .forms import NewsForms, CommentForms


class HomeNews(ListView):
    model = News
    template_name = 'app_news/news-list.html'
    context_object_name = 'News'
    extra_context = {'title': 'Список объявлений'}


class Index(DetailView):
    model = News
    context_object_name = 'News'
    template_name = 'app_news/news-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['title'] = self.model.objects.get(pk=self.kwargs['pk'])
        return context


class AddNews(View):
    def get(self, request):
        return render(request, 'app_news/add-news.html', {'News': News})

    def post(self, request):
        text = 'рекламное объявление успешно создано'
        form = NewsForms()
        return render(request, 'app_news/add-news.html', {'text': text, 'form': form})
