from django.shortcuts import render
from django.http import HttpResponse


def home_page_list(request, *args, **kwargs):
    return render(request, 'home_page/home_page_list.html', {})


def python_basic_list(request, *args, **kwargs):
    return render(request, 'python_basic/python_basic_list.html', {})


def django_list(request, *args, **kwargs):
    return render(request, 'django/django_list.html', {})


def python_advanced_list(request, *args, **kwargs):
    return render(request, 'python_advanced/python_advanced_list.html', {})


def SQL_list(request, *args, **kwargs):
    return render(request, 'SQL/SQL_list.html', {})


def web_layout_list(request, *args, **kwargs):
    return render(request, 'web_layout/web_layout_list.html', {})
