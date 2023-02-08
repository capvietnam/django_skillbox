from django.urls import path
from .views import *

urlpatterns = [
    path(r'shop_list/', ListShop.as_view(), name=r'shop-list'),
]