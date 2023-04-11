from django.views.generic import ListView, DetailView
from django.views.generic import ListView, DetailView, View
from .models import Goods
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpRequest
from app_users.models import Profile, Sale
from django.contrib.auth.models import User
from django.db.models import Sum

class ListGoods(ListView):
    """Список всех новостей"""
    model = Goods
    template_name = 'app_goods/goods-list.html'
    context_object_name = 'Shop'
    extra_context = {'title': 'Список товаров'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Goods'] = self.model.objects.select_related('shop').all()
        return context


class GoodsDetail(DetailView):
    """Отдельная страница новости"""
    model = Goods
    template_name = 'app_goods/good-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Goods'] = self.model.objects.defer('id').all()
        return context



def set_cookie_view(request) -> HttpResponse:
    response = HttpResponse('Cookie set')
    response.set_cookie('fizz', "buzz", max_age=3600)
    return response


def get_cookie_view(request) -> HttpResponse:
    value = request.COOKIES.get('fizz', 'default value')
    return HttpResponse(f'Cookie value: {value!r}')


def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    cart = request.session['cart']
    cart[product_id] = 1
    request.session.modified = True
    return redirect('cart_goods')


def cart(request):
    cart = request.session.get('cart', {})
    products = []
    for product_id, quantity in cart.items():
        product = Goods.objects.get(id=product_id)
        products.append({
            'product': product,
            'quantity': quantity
        })
    return render(request, 'app_goods/cart.html', {'products': products})


def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 0))
    if quantity >= 0:
        cart[product_id] = quantity
    request.session.modified = True
    return redirect('cart_goods')

@transaction.atomic()
def place_order(request):
    cart = request.session.get('cart', {})
    products = []
    money_user = request.user.profile.balance
    profile = Profile.objects.get(id=request.user.profile.id)
    sum_cost_goods = 0
    for product_id, quantity in cart.items():
        product = Goods.objects.get(id=product_id)
        sum_cost_goods += product.price * quantity
        products.append({
            'product': product,
            'quantity': quantity
        })
    if money_user >= sum_cost_goods:
        for item in products:
            if item['product'].rest_goods >= item['quantity']:
                item['product'].rest_goods -= item['quantity']
                item['product'].save()
            else:
                return redirect('cart_goods')
        del request.session['cart']
        profile.money_spent += sum_cost_goods
        profile.balance -= sum_cost_goods
        profile.save()
        return redirect('goods-list')
    else:
        return redirect('cart_goods')


def dell_cart(request):
    del request.session['cart']
    return redirect('goods-list')


def top_products(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    sales = Sale.objects.filter(date__range=[start_date, end_date])
    context = sales.values('goods__id', 'goods__title').annotate(total=Sum('quantity')).order_by('-total')
    return render(request, 'app_goods/top_products.html', {'context': context})
