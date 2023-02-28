from django.urls import path
from .views import *

urlpatterns = [
    path(r'goods_list/', ListGoods.as_view(), name=r'goods-list'),
    path(r'good-detail/<int:pk>/', GoodsDetail.as_view(), name=r'good-detail'),
]
