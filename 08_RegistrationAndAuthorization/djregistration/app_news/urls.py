from django.urls import path
from .views import *
from . import views
from django.urls import *

urlpatterns = [
    path('news/', HomeNews.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
    path('news/add-news/', AddNews.as_view(), name='add-news'),
    path('news/update-news/<int:pk>/', UpdateNews.as_view(), name='update-news'),
]
