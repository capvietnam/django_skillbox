from django.urls import path
from .views import *

urlpatterns = [
    path(r'login/', UserLoginView.as_view(), name=r'user-login'),
    path(r'register/', UserRegisterView, name=r'user-register'),
    path(r'logout/', UserLogoutView.as_view(), name=r'user-logout'),
    path(r'profile/<int:pk>/', ProfileView.as_view(), name=r'user-profile'),
    path(r'update_balance/<int:pk>/', UpdateBalance, name=r'update-balance'),
]
