from django.urls import path
from .views import *
from . import views
from django.urls import *

urlpatterns = [
    path('user/login/', UserLoginView.as_view(), name='user-login'),
    path('user/register/', UserRegisterView, name='user-register'),
    path('user/logout/', UserLogoutView.as_view(), name='user-logout'),
    path('user/profile/<int:pk>/', PtofileDetail.as_view(), name='user-profile'),
]
