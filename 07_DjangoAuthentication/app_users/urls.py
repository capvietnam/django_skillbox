from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('news/', HomeNews.as_view(), name='news-list'),
    path('news/login/', UserLoginView.as_view(), name='user-login'),
    path('news/register/', UserRegisterView, name='user-register'),
    # path('news/logout/', user_logout, name='user-logout'),
    path('news/logout/', UserLogoutView.as_view(), name='user-logout'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news-detail'),
    path('news/add-news/', AddNews.as_view(), name='add-news'),
    path('news/update-news/<int:pk>/', UpdateNews.as_view(), name='update-news'),
]
