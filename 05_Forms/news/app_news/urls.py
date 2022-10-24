from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('/', HomeNews.as_view(), name='news-list'),
    path('/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
    path('/add-news/', AddNews.as_view(), name='add-news'),
    path('/update-news/<int:pk>/', UpdateNews.as_view(), name='update-news'),
]
