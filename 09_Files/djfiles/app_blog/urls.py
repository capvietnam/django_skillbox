from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path(r'', HomeBlog.as_view(), name=r'blog-list'),
    path(r'blog-detail/<int:pk>/', BlogDetail, name=r'blog-detail'),
    path(r'add-blog/', AddBlog.as_view(), name=r'add-blog'),
    path(r'update-blog/<int:pk>/', UpdateBlog.as_view(), name=r'update-blog'),
]
