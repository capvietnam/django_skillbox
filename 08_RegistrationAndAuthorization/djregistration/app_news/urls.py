from django.urls import path
from .views import *
from . import views
from django.urls import *

urlpatterns = [
    path(r'', HomeNews.as_view(), name=r'news-list'),
    path(r'tags/<int:pk>/', NewsDetailTags.as_view(), name=r'news-detail-tag'),
    path(r'date/<int:pk>/', NewsDetailDate.as_view(), name=r'news-detail-date'),
    path(r'<int:pk>/', NewsDetail.as_view(), name=r'news-detail'),
    path(r'add-news/', AddNews.as_view(), name=r'add-news'),
    path(r'update-news/<int:pk>/', UpdateNews.as_view(), name=r'update-news'),
]
