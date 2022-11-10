from django import template
from app_news.models import *

register = template.Library()

def news(user):
    return News.objects.all()

print(news)