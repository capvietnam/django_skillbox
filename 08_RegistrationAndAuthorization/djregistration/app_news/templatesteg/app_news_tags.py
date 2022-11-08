from django import template
from app_news.models import *


register = template.Library()

def news():
    return News.objects.all()

print(news)