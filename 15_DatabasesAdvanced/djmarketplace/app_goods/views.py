from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Shop, Goods
from django.contrib.auth.models import User


class ListGoods(ListView):
    """Список всех новостей"""
    model = Goods
    template_name = 'app_goods/goods-list.html'
    context_object_name = 'Shop'
    extra_context = {'title': 'Список товаров'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Goods'] = self.model.objects.all()
        return context


class GoodsDetail(DetailView):
    """Отдельная страница новости"""
    model = Goods
    template_name = 'app_goods/good-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Goods'] = self.model.objects.all()
        return context