from django.shortcuts import render
from .models import News


def news_list(request):
    news = News.objects.all()
    return render(request, 'app_news/news_list.html', {'news': news})
