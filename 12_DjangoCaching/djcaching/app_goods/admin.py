
from django.contrib import admin
from .models import Shop, Goods


class ShopAdmin(admin.ModelAdmin):
    """Админ панель для модели магазинов"""
    list_display = ('id', 'title', )
    list_display_links = ('id',)


class GoodsAdmin(admin.ModelAdmin):
    """Админ панель для модели товаров"""
    list_display = ('id', 'shop', 'title', 'price', 'description', )
    list_display_links = ('id',)


admin.site.register(Shop, ShopAdmin)
admin.site.register(Goods, GoodsAdmin)
