from django.shortcuts import redirect, render
from .models import House


def contacts(request):
    return render(request, 'app_house/contacts.html')


def about(request):
    return render(request, 'app_house/about.html')


def housing_list(request):
    housing = House.objects.all()
    return render(request, 'app_house/housing_list.html', {'housing': housing})

