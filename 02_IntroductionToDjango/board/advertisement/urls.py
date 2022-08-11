from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page_list, name='home_page_list'),
    path("python_basic", views.python_basic_list, name='python_basic_list'),
    path("django", views.django_list, name='django_list'),
    path("python_advanced", views.python_advanced_list, name='python_advanced_list'),
    path("SQL", views.SQL_list, name='SQL_list'),
    path("web_layout", views.web_layout_list, name='web_layout_list'),

]