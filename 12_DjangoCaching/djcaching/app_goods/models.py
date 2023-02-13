from django.db import models
from django.utils.translation import gettext_lazy as _


class Shop(models.Model):
    """Модель магазина всех товаров"""
    title = models.CharField(max_length=500, verbose_name=_('title'))

    class Meta:
        verbose_name = _('shop')
        verbose_name_plural = _('shops')
        ordering = ['title']

    def __str__(self):
        return self.title


class Goods(models.Model):
    """Модель всех товаров"""
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='goods', verbose_name=_('shop'))
    title = models.CharField(max_length=500, verbose_name=_('title'))
    price = models.PositiveIntegerField(blank=True, verbose_name=_('price'))
    description = models.CharField(max_length=500, verbose_name=_('description'))

    class Meta:
        verbose_name = _('goods')
        verbose_name_plural = _('goods')
        ordering = ['title', 'price', 'description', 'shop']

    def __str__(self):
        return self.title
