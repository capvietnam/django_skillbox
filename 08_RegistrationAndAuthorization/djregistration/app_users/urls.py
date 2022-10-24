from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('news/login/', UserLoginView.as_view(), name='user-login'),
    path('news/register/', UserRegisterView, name='user-register'),
    path('news/logout/', UserLogoutView.as_view(), name='user-logout'),
]
