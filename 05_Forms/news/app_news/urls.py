from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('news/', HomeNews.as_view(), name='news-list'),
    path('news/<int:pk>/', Index.as_view(), name='news-detail'),
    path('news/add-news/', AddNews.as_view(), name='add-news'),
    path('news/change-news/<int:pk>/', NewsDetail.as_view(), name='change-news'),
]
