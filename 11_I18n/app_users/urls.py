from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path(r'login/', UserLoginView.as_view(), name=r'user-login'),
    path(r'register/', UserRegisterView, name=r'user-register'),
    path(r'logout/', UserLogoutView.as_view(), name=r'user-logout'),
    path(r'profile/', views.profile, name=r'user-profile'),
]