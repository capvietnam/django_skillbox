from django.shortcuts import render
from django.views.generic import ListView
from .models import Shop, Goods
from django.contrib.auth.models import User


class ListShop(ListView):
    """Список всех новостей"""
    model = Shop
    template_name = 'app_goods/shop-list.html'
    context_object_name = 'Shop'
    extra_context = {'title': 'Список магазинов'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Shop'] = self.model.objects.all()
        return context
