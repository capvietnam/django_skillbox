from django.urls import path
from .views import *

urlpatterns = [
    path(r'goods_list/', ListGoods.as_view(), name=r'goods-list'),
    path(r'good-detail/<int:pk>/', GoodsDetail.as_view(), name=r'good-detail'),
    path('cart/', cart, name='cart_goods'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path("cookie/get/", get_cookie_view, name='get-cookie'),
    path("cookie/set/", set_cookie_view, name='set-cookie'),
    path('update-cart/<int:product_id>/', update_cart, name='update_cart'),
    path('place-order/', place_order, name='Buy'),
    path('dell-cart/', dell_cart, name='dell-cart'),
    path('top-products/', top_products, name='top-products'),
]
